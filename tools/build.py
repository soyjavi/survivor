import datetime, glob, hashlib, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'dist')


def frontmatter(text):
    if not text.startswith('---'):
        return {}, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    meta = {}
    for line in parts[1].splitlines():
        m = re.match(r'^(\w+):\s*(.*)$', line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"\'')
    return meta, parts[2]


SW_TEMPLATE = '''const CACHE = 'survivor-%(version)s';
const ASSETS = %(assets)s;

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== self.location.origin) return;
  event.respondWith(
    caches.match(event.request, { ignoreSearch: true }).then((hit) => {
      if (hit) return hit;
      return fetch(event.request).then((response) => {
        if (response.ok) caches.open(CACHE).then((cache) => cache.put(event.request, response.clone()));
        return response;
      });
    }).catch(() => (event.request.mode === 'navigate' ? caches.match('./index.html') : Response.error()))
  );
});
'''


def write_service_worker():
    files = []
    digest = hashlib.sha1()
    for root, dirs, names in os.walk(OUT):
        dirs.sort()
        for name in sorted(names):
            if name in ('sw.js', 'version.json'):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, OUT).replace(os.sep, '/')
            files.append('./' + rel)
            digest.update(rel.encode())
            with open(path, 'rb') as fh:
                digest.update(fh.read())
    files.sort()
    body = SW_TEMPLATE % {
        'version': digest.hexdigest()[:12],
        'assets': json.dumps(['./'] + files, ensure_ascii=False),
    }
    with open(os.path.join(OUT, 'sw.js'), 'w', encoding='utf-8') as fh:
        fh.write(body)


def git(*args):
    try:
        return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ''


def write_version(articles):
    pinned = os.environ.get('SURVIVOR_COMMIT')
    commit = pinned or git('rev-parse', '--short', 'HEAD') or 'uncommitted'
    if not pinned and commit != 'uncommitted' and git('status', '--porcelain'):
        commit += '+'
    info = {'commit': commit, 'articles': articles, 'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}
    with open(os.path.join(OUT, 'version.json'), 'w', encoding='utf-8') as fh:
        json.dump(info, fh)


KEYS = ['id', 'type', 'title', 'description', 'section', 'tags', 'timestamp', 'origin', 'review']


def check_document(path, text):
    sec = os.path.basename(os.path.dirname(path))
    name = os.path.relpath(path, ROOT)
    if not text.startswith('---\n') or '\n---' not in text[4:]:
        return [name + ': missing frontmatter']
    errors = []
    raw = text[4:].split('\n---', 1)[0]
    keys = [m.group(1) for m in (re.match(r'^([a-z_]+):', l) for l in raw.splitlines()) if m]
    if keys != KEYS:
        errors.append('%s: frontmatter keys %s' % (name, keys))
    meta, body = frontmatter(text)
    if not re.fullmatch(re.escape(sec) + r'-\d\d', meta.get('id', '')):
        errors.append('%s: bad id %r' % (name, meta.get('id')))
    if meta.get('section') != sec:
        errors.append('%s: section %r does not match folder' % (name, meta.get('section')))
    if len(re.findall(r'^# .+$', body, re.M)) != 1:
        errors.append(name + ': expected exactly one # title')
    if re.search(r'\]\(#?\)', body):
        errors.append(name + ': empty link target')
    for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', body):
        if not os.path.exists(os.path.join(ROOT, 'assets', sec, os.path.basename(target))):
            errors.append('%s: missing image %s' % (name, target))
    return errors


def validate(items):
    errors = []
    for md in sorted(glob.glob(os.path.join(ROOT, 'documents', '*', '*.md'))):
        errors += check_document(md, open(md, encoding='utf-8').read())
    for field in ('id', 'title'):
        seen = {}
        for item in items:
            seen.setdefault(item[field], []).append(item['href'])
        errors += ['duplicate %s %r: %s' % (field, k, v) for k, v in seen.items() if len(v) > 1]
    return errors


def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    okf = os.path.join(OUT, 'okf')
    items = []
    copied = set()
    for md in sorted(glob.glob(os.path.join(ROOT, 'documents', '*', '*.md'))):
        sec = os.path.basename(os.path.dirname(md))
        rel = os.path.join('okf', sec, os.path.basename(md))
        os.makedirs(os.path.dirname(os.path.join(OUT, rel)), exist_ok=True)
        shutil.copy(md, os.path.join(OUT, rel))
        if sec not in copied:
            copied.add(sec)
            assets = os.path.join(ROOT, 'assets', sec)
            if os.path.isdir(assets):
                shutil.copytree(assets, os.path.join(okf, sec, 'assets'))
        text = open(md, encoding='utf-8').read()
        meta, body = frontmatter(text)
        words = len(re.findall(r'\w+', body))
        images = len(re.findall(r'!\[', body))
        items.append({
            'id': meta.get('id') or hashlib.sha1(rel.encode()).hexdigest()[:10],
            'type': 'web',
            'cat': meta.get('section', sec),
            'book': 'survivor',
            'title': meta.get('title', os.path.basename(md)),
            'description': meta.get('description', ''),
            'tags': [t.strip() for t in meta.get('tags', '').strip('[]').split(',') if t.strip()],
            'origin': meta.get('origin', 'generated'),
            'review': meta.get('review', ''),
            'words': words,
            'readMin': max(1, round(words / 220)),
            'images': images,
            'href': 'reader.html?f=' + rel.replace(os.sep, '/'),
        })
    for name in ['index.html', 'reader.html', 'favicon.svg', 'geist.woff2']:
        src = os.path.join(ROOT, 'web', name)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(OUT, name))
    for d in ['lib']:
        src = os.path.join(ROOT, 'web', d)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(OUT, d))
    for f in glob.glob(os.path.join(ROOT, 'web', '*.woff2')):
        shutil.copy(f, OUT)
    if os.path.isdir(os.path.join(ROOT, 'web', 'icons')):
        shutil.copytree(os.path.join(ROOT, 'web', 'icons'), os.path.join(OUT, 'icons'))
    shutil.copy(os.path.join(ROOT, 'web', 'manifest.webmanifest'), OUT)
    errors = validate(items)
    if errors:
        for e in errors:
            print('error:', e, file=sys.stderr)
        sys.exit(1)
    write_version(len(items))
    with open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8') as fh:
        json.dump(items, fh, ensure_ascii=False)
    write_service_worker()
    print('items', len(items), 'dist', OUT)


if __name__ == '__main__':
    build()
