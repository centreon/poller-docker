FROM alpine AS engine
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
WORKDIR /code

ENV VERSION=20.04
ENV PKG_LIB=./clib-${VERSION}-r0.apk
ENV PKG_DEV=./clib-dev-${VERSION}-r0.apk
ENV GIT_VERSION=master

RUN apk --update add git cmake g++ ninja
COPY  $PKG_LIB ./.
COPY   $PKG_DEV ./.
RUN apk --update --allow-untrusted add $PKG_LIB $PKG_DEV
RUN git clone https://github.com/centreon/centreon-engine -b $GIT_VERSION && \
 cd centreon-engine && mkdir build && cd build && cmake -GNinja .. && ninja
