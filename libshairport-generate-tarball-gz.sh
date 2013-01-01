#!/bin/sh

LIBSHAIRPORT_GIT_URL="git://github.com/amejia1/libshairport.git"
LIBSHAIRPORT_GIT_COMMIT="16395d85ea2801cec612b935ba2972bd1a42a6a5"
DATE_RETRIEVED="20121218"
COMMIT_SHORT_FORM="$(echo $LIBSHAIRPORT_GIT_COMMIT | \
                     sed -e 's/^\([[:xdigit:]]\{,7\}\).*/\1/')"
LIBSHAIRPORT_VERSION="1.2.1.${DATE_RETRIEVED}git${COMMIT_SHORT_FORM}"

rm -rf "libshairport-${LIBSHAIRPORT_VERSION}"
git clone "$LIBSHAIRPORT_GIT_URL" "libshairport-${LIBSHAIRPORT_VERSION}"
cd "libshairport-${LIBSHAIRPORT_VERSION}"
git checkout "$LIBSHAIRPORT_GIT_COMMIT"
cd ..

# repack
tar --exclude-vcs -czvf libshairport-$LIBSHAIRPORT_VERSION.tar.gz libshairport-$LIBSHAIRPORT_VERSION
