"A Generate module"
def generate_recipe(version, git_ref, work_path):
    output = open(work_path + '/clib-package.alpine', 'w+')
    print('pkgname="clib"', file=output)
    print('pkgver="' + version + '"', file=output)
    print('pkgrel=0', file=output)
    print('pkgdesc="centreon clib library"', file=output)
    print('url="https://github.com/centreon/centreon-clib"', file=output)
    print('arch="all"', file=output)
    print('license="Apache 2"', file=output)
    print('depends=""', file=output)
    print('makedepends="cmake ninja g++"', file=output)
    print('install=""', file=output)
    print('subpackages="$pkgname-dev"', file=output)
    print('source="https://github.com/centreon/centreon-clib/archive/'+ git_ref + '.tar.gz"', file=output)
    print('''builddir="$srcdir/"

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
''', file=output)