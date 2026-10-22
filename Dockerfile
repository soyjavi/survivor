FROM python:3.12-slim AS build
ARG SURVIVOR_COMMIT=
ENV SURVIVOR_COMMIT=$SURVIVOR_COMMIT
WORKDIR /src
COPY . .
RUN python tools/build.py

FROM nginx:alpine
COPY --from=build /src/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
