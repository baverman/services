FROM alpine:3.7

RUN apk update \
 && apk add collectd collectd-disk \
 && rm /var/cache/apk/*

ENTRYPOINT ["/usr/sbin/collectd"]
