FROM alpine AS clib
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
RUN apk --update add git cmake g++ ninja
WORKDIR /code
ENV GIT_VERSION=master
RUN git clone https://github.com/centreon/centreon-clib -b $GIT_VERSION && \
  cd centreon-clib && mkdir build && cd build && cmake -GNinja .. && ninja
