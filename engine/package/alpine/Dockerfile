FROM alpine AS engine-package
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
WORKDIR /engine

ENV VERSION=20.04
ENV PKG_LIB=./clib-${VERSION}-r0.apk
ENV PKG_DEV=./clib-dev-${VERSION}-r0.apk
ENV GIT_VERSION=master

COPY $PKG_LIB ./.
COPY $PKG_DEV ./.
RUN apk --update --allow-untrusted add $PKG_LIB $PKG_DEV

RUN apk --update add alpine-sdk cmake ninja g++

RUN adduser -D centreon-engine && addgroup centreon-engine abuild

COPY engine-package.alpine /engine/APKBUILD
RUN chown -R centreon-engine /engine && su centreon-engine
RUN su - centreon-engine -c "abuild-keygen -a -i"
RUN su - centreon-engine -c "cd /engine && abuild checksum && abuild"
