pkgname=smms
pkgver=0.0.1
pkgrel=1
provides=(smms)
pkgdesc="a python script for smms pic bed"
arch=('any')
url="https://github.com/chaichunyang/smms.git"
license=('MIT')
depends=('python>=3.6.0' 'python-requests')
source=(
'git+https://github.com/chaichunyang/smms.git'
)
sha256sums=(
    'SKIP'
)

package() {
    install -Dm755 "${srcdir}/smms/smms.py" "${pkgdir}/usr/bin/smms"
}
