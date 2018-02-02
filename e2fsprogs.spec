#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2F95956950D81A3 (tytso@mit.edu)
#
Name     : e2fsprogs
Version  : 1.43.8
Release  : 51
URL      : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.43.8/e2fsprogs-1.43.8.tar.gz
Source0  : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.43.8/e2fsprogs-1.43.8.tar.gz
Source99 : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.43.8/e2fsprogs-1.43.8.tar.gz.asc
Summary  : Utilities for managing ext2/ext3/ext4 filesystems
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 LGPL-2.1
Requires: e2fsprogs-bin
Requires: e2fsprogs-lib
Requires: e2fsprogs-data
Requires: e2fsprogs-doc
Requires: e2fsprogs-locales
BuildRequires : acl-dev
BuildRequires : acl-dev32
BuildRequires : attr-dev
BuildRequires : attr-dev32
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pbr
BuildRequires : perl(XML::Parser)
BuildRequires : pip
BuildRequires : pkg-config-dev
BuildRequires : procps-ng
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : texinfo
BuildRequires : util-linux-dev
BuildRequires : util-linux-dev32
Patch1: stateless.patch
Patch2: build.patch

%description
The e2fsprogs package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in ext2, ext3,
and ext4 filesystems.  E2fsprogs contains e2fsck (used to repair
filesystem inconsistencies after an unclean shutdown), mke2fs (used to
initialize a partition to contain an empty ext2 filesystem), debugfs
(used to examine the internal structure of a filesystem, to manually
repair a corrupted filesystem or to create test cases for e2fsck),
tune2fs (used to modify filesystem parameters), resize2fs to grow and
shrink unmounted ext2 filesystems, and most of the other core ext2fs
filesystem utilities.

You should install the e2fsprogs package if you are using any ext2,
ext3, or ext4 filesystems (if you're not sure, you probably should
install this package).  You may also need to install it (even if you
don't use ext2/ext3/ext4) for the libuuid and libblkid libraries and
fsck tool that are included here.

%package bin
Summary: bin components for the e2fsprogs package.
Group: Binaries
Requires: e2fsprogs-data

%description bin
bin components for the e2fsprogs package.


%package data
Summary: data components for the e2fsprogs package.
Group: Data

%description data
data components for the e2fsprogs package.


%package dev
Summary: dev components for the e2fsprogs package.
Group: Development
Requires: e2fsprogs-lib
Requires: e2fsprogs-bin
Requires: e2fsprogs-data
Provides: e2fsprogs-devel

%description dev
dev components for the e2fsprogs package.


%package dev32
Summary: dev32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-lib32
Requires: e2fsprogs-bin
Requires: e2fsprogs-data
Requires: e2fsprogs-dev

%description dev32
dev32 components for the e2fsprogs package.


%package doc
Summary: doc components for the e2fsprogs package.
Group: Documentation

%description doc
doc components for the e2fsprogs package.


%package extras
Summary: extras components for the e2fsprogs package.
Group: Default

%description extras
extras components for the e2fsprogs package.


%package lib
Summary: lib components for the e2fsprogs package.
Group: Libraries
Requires: e2fsprogs-data

%description lib
lib components for the e2fsprogs package.


%package lib32
Summary: lib32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-data

%description lib32
lib32 components for the e2fsprogs package.


%package locales
Summary: locales components for the e2fsprogs package.
Group: Default

%description locales
locales components for the e2fsprogs package.


%prep
%setup -q -n e2fsprogs-1.43.8
%patch1 -p1
%patch2 -p1
pushd ..
cp -a e2fsprogs-1.43.8 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514919905
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%reconfigure --disable-static --disable-fsck --disable-libblkid  --disable-uuidd --disable-libuuid --enable-elf-shlibs
make
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --disable-fsck --disable-libblkid  --disable-uuidd --disable-libuuid --enable-elf-shlibs  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1514919905
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang e2fsprogs
## make_install_append content
%make_install install-libs
## make_install_append end

%files
%defattr(-,root,root,-)
%exclude /usr/lib32/e2initrd_helper
/usr/lib64/e2initrd_helper

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/badblocks
%exclude /usr/bin/compile_et
%exclude /usr/bin/debugfs
%exclude /usr/bin/dumpe2fs
%exclude /usr/bin/e2freefrag
%exclude /usr/bin/e2image
%exclude /usr/bin/e2undo
%exclude /usr/bin/e4defrag
%exclude /usr/bin/filefrag
%exclude /usr/bin/logsave
%exclude /usr/bin/mk_cmds
%exclude /usr/bin/mke2fs
%exclude /usr/bin/mkfs.ext2
%exclude /usr/bin/mkfs.ext3
%exclude /usr/bin/mkfs.ext4
/usr/bin/chattr
/usr/bin/e2fsck
/usr/bin/e2label
/usr/bin/e4crypt
/usr/bin/fsck.ext2
/usr/bin/fsck.ext3
/usr/bin/fsck.ext4
/usr/bin/lsattr
/usr/bin/mklost+found
/usr/bin/resize2fs
/usr/bin/tune2fs

%files data
%defattr(-,root,root,-)
%exclude /usr/share/et/et_c.awk
%exclude /usr/share/et/et_h.awk
%exclude /usr/share/ss/ct_c.awk
%exclude /usr/share/ss/ct_c.sed
/usr/share/defaults/e2fsprogs/mke2fs.conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/e2p/e2p.h
/usr/include/et/com_err.h
/usr/include/ext2fs/bitops.h
/usr/include/ext2fs/ext2_err.h
/usr/include/ext2fs/ext2_ext_attr.h
/usr/include/ext2fs/ext2_fs.h
/usr/include/ext2fs/ext2_io.h
/usr/include/ext2fs/ext2_types.h
/usr/include/ext2fs/ext2fs.h
/usr/include/ext2fs/ext3_extents.h
/usr/include/ext2fs/qcow2.h
/usr/include/ext2fs/tdb.h
/usr/include/ss/ss.h
/usr/include/ss/ss_err.h
/usr/lib64/libcom_err.so
/usr/lib64/libe2p.so
/usr/lib64/libext2fs.so
/usr/lib64/libss.so
/usr/lib64/pkgconfig/com_err.pc
/usr/lib64/pkgconfig/e2p.pc
/usr/lib64/pkgconfig/ext2fs.pc
/usr/lib64/pkgconfig/ss.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcom_err.so
/usr/lib32/libe2p.so
/usr/lib32/libext2fs.so
/usr/lib32/libss.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files extras
%defattr(-,root,root,-)
/usr/bin/badblocks
/usr/bin/compile_et
/usr/bin/debugfs
/usr/bin/dumpe2fs
/usr/bin/e2freefrag
/usr/bin/e2image
/usr/bin/e2undo
/usr/bin/e4defrag
/usr/bin/filefrag
/usr/bin/logsave
/usr/bin/mk_cmds
/usr/bin/mke2fs
/usr/bin/mkfs.ext2
/usr/bin/mkfs.ext3
/usr/bin/mkfs.ext4
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcom_err.so.2
/usr/lib64/libcom_err.so.2.1
/usr/lib64/libe2p.so.2
/usr/lib64/libe2p.so.2.3
/usr/lib64/libext2fs.so.2
/usr/lib64/libext2fs.so.2.4
/usr/lib64/libss.so.2
/usr/lib64/libss.so.2.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcom_err.so.2
/usr/lib32/libcom_err.so.2.1
/usr/lib32/libe2p.so.2
/usr/lib32/libe2p.so.2.3
/usr/lib32/libext2fs.so.2
/usr/lib32/libext2fs.so.2.4
/usr/lib32/libss.so.2
/usr/lib32/libss.so.2.0

%files locales -f e2fsprogs.lang
%defattr(-,root,root,-)

