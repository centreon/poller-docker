ARG GIT_VERSION=master
ARG VERSION=20.04
ARG PKG_LIB=/home/centreon/packages/x86_64/clib-${VERSION}-r0.apk
ARG PKG_DEV=/home/centreon/packages/x86_64/clib-dev-${VERSION}-r0.apk

FROM clib-${VERSION}-package:alpine AS engine
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
WORKDIR /code

FROM clib-${VERSION}-package:alpine AS engine-build
ENV LIB_VER=20.04
ENV INST_PKG_LIB=./clib-${LIB_VER}-r0.apk
ENV INST_PKG_DEV=./clib-dev-${LIB_VER}-r0.apk
ENV GIT_VERSION=master
ENV PKG_LIB=/home/centreon/packages/x86_64/clib-$LIB_VER-r0.apk
ENV PKG_DEV=/home/centreon/packages/x86_64/clib-dev-$LIB_VER-r0.apk
WORKDIR /code

RUN apk --update add git cmake g++ ninja
COPY --from=0  $PKG_LIB ./.
COPY --from=0  $PKG_DEV ./.
RUN apk --update --allow-untrusted add $INST_PKG_LIB $INST_PKG_DEV
RUN git clone https://github.com/centreon/centreon-engine -b $GIT_VERSION && \
 cd centreon-engine && mkdir build && cd build && cmake -GNinja .. && ninja
