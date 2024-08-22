FROM nginx:1.19.0-alpine
RUN mkdir /app


EXPOSE 80/tcp 443/tcp

RUN apk upgrade && \
    apk add --no-cache esh curl openssl && \
    curl https://get.acme.sh | sh && \
    ln -s  /root/.acme.sh/acme.sh  /usr/local/bin/acme.sh

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
WORKDIR /app