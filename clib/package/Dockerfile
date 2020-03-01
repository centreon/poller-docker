FROM alpine
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
WORKDIR /code
ENV GIT_VERSION=master
RUN cd centreon-clib/build && cmake -GNinja -DWITH_TESTING=ON .. && ninja && ninja test
