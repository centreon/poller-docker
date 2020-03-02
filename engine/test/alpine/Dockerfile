FROM engine-20.04:alpine
LABEL maintainer Sylvestre Gallon <sgallon@centreon.com>
WORKDIR /code
ENV GIT_VERSION=master
RUN apk add tzdata && cp /usr/share/zoneinfo/Europe/Paris /etc/localtime && echo "Europe/Paris" > /etc/timezone
RUN cd centreon-engine/build && cmake -GNinja -DWITH_TESTING=ON .. && ninja && ./tests/ut
