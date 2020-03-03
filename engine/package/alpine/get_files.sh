#!/bin/bash
if [ $# -ne 1 ]; then
  echo 'usage: ./get_files.sh docker-name version'
  exit 1;
fi

version=$1
docker="engine-$version-package:alpine"
id=$(docker create $docker)
docker cp $id:/home/centreon-engine/packages/x86_64/engine-$version-r0.apk ../../../packages
docker cp $id:/home/centreon-engine/packages/x86_64/engine-dev-$version-r0.apk ../../../packages
docker rm -v $id
