FROM nginx:1.19.0-alpine
RUN mkdir /app


EXPOSE 80/tcp 443/tcp

RUN apk upgrade && \
    apk add --no-cache esh curl openssl && \
    curl https://get.acme.sh | sh && \
    ln -s  /root/.acme.sh/acme.sh  /usr/local/bin/acme.sh

RUN rm /etc/nginx/conf.d/default.conf
# RUN acme.sh --issue --server letsencrypt -d y0gurtlab.tech -w /var/www/local_static --config-home /acme.sh

# RUN acme.sh --install-cert -d y0gurtlab.tech --config-home /acme.sh --key-file /etc/nginx/certs/key.pem --fullchain-file /etc/nginx/certs/cert.pem --reloadcmd "nginx -s reload"
COPY nginx.conf /etc/nginx/conf.d/
WORKDIR /app