FROM alpine AS clib
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
RUN apk --update add git cmake g++ ninja
WORKDIR /code
ENV GIT_VERSION=master
RUN git clone https://github.com/centreon/centreon-clib -b $GIT_VERSION && \
  cd centreon-clib && mkdir build && cd build && cmake -GNinja .. && ninja && ninja install

FROM alpine AS engine-build
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
RUN apk --update add git cmake g++ ninja
WORKDIR /code
COPY --from=clib /usr/local /usr/local
ENV GIT_VERSION=master
RUN git clone https://github.com/centreon/centreon-engine -b $GIT_VERSION && \
  cd centreon-engine && mkdir build && cd build && cmake -GNinja .. && ninja && ninja install

FROM alpine
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
COPY --from=engine-build /usr/local /usr/local
