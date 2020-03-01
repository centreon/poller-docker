#!/bin/env python3

version="20.04"
git_ref="master"

print('''
pkgname="clib"
pkgver="''' + version + '''"
pkgrel=0
pkgdesc="centreon clib library"
url="https://github.com/centreon/centreon-clib"
arch="all"
license="Apache 2"
depends=""
makedepends="cmake ninja g++"
install=""
subpackages="$pkgname-dev"
source="https://github.com/centreon/centreon-clib/archive/'''+ git_ref + '''.tar.gz"
builddir="$srcdir/"

build() {
    cd "$builddir"/centreon-clib-master
    mkdir build && cd build
    cmake -GNinja -DWITH_PREFIX="$pkgdir" ..
    ninja
}

check() {
        # Replace with proper check command(s)
        :
}

package() {
        cd "$builddir"/centreon-clib-master
        cd build
        ninja install
}

''')