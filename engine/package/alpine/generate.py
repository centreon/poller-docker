"A Generate module"
def generate_recipe(version, git_ref, work_path):
    output = open(work_path + '/engine-package.alpine', 'w+')
    print('pkgname="engine"', file=output)
    print('pkgver="' + version + '"', file=output)
    print('pkgrel=0', file=output)
    print('pkgdesc="centreon engine"', file=output)
    print('url="https://github.com/centreon/centreon-engine"', file=output)
    print('arch="all"', file=output)
    print('license="Apache 2"', file=output)
    print('depends="clib"', file=output)
    print('makedepends="cmake ninja g++"', file=output)
    print('install=""', file=output)
    print('subpackages="$pkgname-dev"', file=output)
    print('source="https://github.com/centreon/centreon-engine/archive/'+ git_ref + '.tar.gz"', file=output)
    print('''builddir="$srcdir/"

build() {
    cd "$builddir"/centreon-engine-master
    mkdir build && cd build
    cmake -GNinja -DWITH_PREFIX="$pkgdir" -DWITH_STARTUP_DIR="$pkgdir"/etc/centreon-engine \
        -DWITH_GROUP=centreon-engine -DWITH_USER=centreon-engine ..
    ninja
}

check() {
        # Replace with proper check command(s)
        :
}

package() {
        cd "$builddir"/centreon-engine-master
        cd build
        ninja install
}
''', file=output)