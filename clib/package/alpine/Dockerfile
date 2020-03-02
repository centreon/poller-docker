FROM alpine AS clib-package
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
RUN apk --update add alpine-sdk cmake ninja g++
WORKDIR /clib
ENV GIT_VERSION=master
RUN adduser -D centreon && addgroup centreon abuild
COPY clib-package.alpine /clib/APKBUILD
RUN chown -R centreon /clib && su centreon
RUN su - centreon -c "abuild-keygen -a -i"
RUN su - centreon -c "cd /clib && abuild checksum && abuild"
