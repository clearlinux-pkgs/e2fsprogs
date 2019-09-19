#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2F95956950D81A3 (tytso@mit.edu)
#
Name     : e2fsprogs
Version  : 1.45.3
Release  : 71
URL      : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.45.3/e2fsprogs-1.45.3.tar.gz
Source0  : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.45.3/e2fsprogs-1.45.3.tar.gz
Source1 : https://sourceforge.net/projects/e2fsprogs/files/e2fsprogs/v1.45.3/e2fsprogs-1.45.3.tar.gz.asc
Summary  : Utilities for managing ext2/ext3/ext4 filesystems
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 LGPL-2.1
Requires: e2fsprogs-bin = %{version}-%{release}
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-lib = %{version}-%{release}
Requires: e2fsprogs-libexec = %{version}-%{release}
Requires: e2fsprogs-license = %{version}-%{release}
Requires: e2fsprogs-locales = %{version}-%{release}
Requires: e2fsprogs-man = %{version}-%{release}
Requires: e2fsprogs-services = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : acl-dev32
BuildRequires : attr-dev
BuildRequires : attr-dev32
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-distutils3
BuildRequires : file-dev
BuildRequires : fuse-dev
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
BuildRequires : perl(XML::Parser)
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(udev)
BuildRequires : procps-ng
BuildRequires : systemd-dev32
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
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-libexec = %{version}-%{release}
Requires: e2fsprogs-license = %{version}-%{release}
Requires: e2fsprogs-services = %{version}-%{release}

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
Requires: e2fsprogs-lib = %{version}-%{release}
Requires: e2fsprogs-bin = %{version}-%{release}
Requires: e2fsprogs-data = %{version}-%{release}
Provides: e2fsprogs-devel = %{version}-%{release}
Requires: e2fsprogs = %{version}-%{release}

%description dev
dev components for the e2fsprogs package.


%package dev32
Summary: dev32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-lib32 = %{version}-%{release}
Requires: e2fsprogs-bin = %{version}-%{release}
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-dev = %{version}-%{release}

%description dev32
dev32 components for the e2fsprogs package.


%package doc
Summary: doc components for the e2fsprogs package.
Group: Documentation
Requires: e2fsprogs-man = %{version}-%{release}

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
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-libexec = %{version}-%{release}
Requires: e2fsprogs-license = %{version}-%{release}

%description lib
lib components for the e2fsprogs package.


%package lib32
Summary: lib32 components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-data = %{version}-%{release}
Requires: e2fsprogs-license = %{version}-%{release}

%description lib32
lib32 components for the e2fsprogs package.


%package libexec
Summary: libexec components for the e2fsprogs package.
Group: Default
Requires: e2fsprogs-license = %{version}-%{release}

%description libexec
libexec components for the e2fsprogs package.


%package license
Summary: license components for the e2fsprogs package.
Group: Default

%description license
license components for the e2fsprogs package.


%package locales
Summary: locales components for the e2fsprogs package.
Group: Default

%description locales
locales components for the e2fsprogs package.


%package man
Summary: man components for the e2fsprogs package.
Group: Default

%description man
man components for the e2fsprogs package.


%package services
Summary: services components for the e2fsprogs package.
Group: Systemd services

%description services
services components for the e2fsprogs package.


%prep
%setup -q -n e2fsprogs-1.45.3
%patch1 -p1
%patch2 -p1
pushd ..
cp -a e2fsprogs-1.45.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568854820
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%reconfigure --disable-static --disable-fsck --disable-libblkid  --disable-uuidd --disable-libuuid --enable-elf-shlibs
make
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure --disable-static --disable-fsck --disable-libblkid  --disable-uuidd --disable-libuuid --enable-elf-shlibs  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check
cd ../build32;
make VERBOSE=1 V=1 check || :

%install
export SOURCE_DATE_EPOCH=1568854820
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/e2fsprogs
cp NOTICE %{buildroot}/usr/share/package-licenses/e2fsprogs/NOTICE
cp debian/copyright %{buildroot}/usr/share/package-licenses/e2fsprogs/debian_copyright
cp ext2ed/COPYRIGHT %{buildroot}/usr/share/package-licenses/e2fsprogs/ext2ed_COPYRIGHT
cp lib/ext2fs/tdb/patches/copyright %{buildroot}/usr/share/package-licenses/e2fsprogs/lib_ext2fs_tdb_patches_copyright
cp lib/uuid/COPYING %{buildroot}/usr/share/package-licenses/e2fsprogs/lib_uuid_COPYING
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
## Remove excluded files
rm -f %{buildroot}/usr/bin/uuidgen
rm -f %{buildroot}/usr/lib32/e2fsprogs/e2scrub_all_cron
rm -f %{buildroot}/usr/lib32/e2fsprogs/e2scrub_fail
rm -f %{buildroot}/usr/lib32/e2initrd_helper
rm -f %{buildroot}/usr/lib64/e2fsprogs/e2scrub_all_cron
rm -f %{buildroot}/usr/share/man/man1/uuidgen.1
## install_append content
%make_install install-libs
mkdir -p %{buildroot}/usr/libexec
mv %{buildroot}/usr/lib64/e2fsprogs/e2scrub_fail %{buildroot}/usr/libexec/
sed -i 's|/usr/lib64/e2fsprogs/|/usr/libexec/|' %{buildroot}/usr/lib/systemd/system/e2scrub_fail@.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/e2initrd_helper

%files bin
%defattr(-,root,root,-)
/usr/bin/chattr
/usr/bin/e2fsck
/usr/bin/e2label
/usr/bin/e2mmpstatus
/usr/bin/e2scrub
/usr/bin/e2scrub_all
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
/usr/share/defaults/e2fsprogs/mke2fs.conf

%files dev
%defattr(-,root,root,-)
/usr/include/com_err.h
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
/usr/include/ext2fs/hashmap.h
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
/usr/share/man/man3/com_err.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcom_err.so
/usr/lib32/libe2p.so
/usr/lib32/libext2fs.so
/usr/lib32/libss.so
/usr/lib32/pkgconfig/32com_err.pc
/usr/lib32/pkgconfig/32e2p.pc
/usr/lib32/pkgconfig/32ext2fs.pc
/usr/lib32/pkgconfig/32ss.pc
/usr/lib32/pkgconfig/com_err.pc
/usr/lib32/pkgconfig/e2p.pc
/usr/lib32/pkgconfig/ext2fs.pc
/usr/lib32/pkgconfig/ss.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

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
/usr/lib/udev/rules.d/96-e2scrub.rules
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

%files libexec
%defattr(-,root,root,-)
/usr/libexec/e2scrub_fail

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/e2fsprogs/NOTICE
/usr/share/package-licenses/e2fsprogs/debian_copyright
/usr/share/package-licenses/e2fsprogs/ext2ed_COPYRIGHT
/usr/share/package-licenses/e2fsprogs/lib_ext2fs_tdb_patches_copyright
/usr/share/package-licenses/e2fsprogs/lib_uuid_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/chattr.1
/usr/share/man/man1/compile_et.1
/usr/share/man/man1/lsattr.1
/usr/share/man/man1/mk_cmds.1
/usr/share/man/man5/e2fsck.conf.5
/usr/share/man/man5/ext2.5
/usr/share/man/man5/ext3.5
/usr/share/man/man5/ext4.5
/usr/share/man/man5/mke2fs.conf.5
/usr/share/man/man8/badblocks.8
/usr/share/man/man8/debugfs.8
/usr/share/man/man8/dumpe2fs.8
/usr/share/man/man8/e2freefrag.8
/usr/share/man/man8/e2fsck.8
/usr/share/man/man8/e2image.8
/usr/share/man/man8/e2label.8
/usr/share/man/man8/e2mmpstatus.8
/usr/share/man/man8/e2scrub.8
/usr/share/man/man8/e2scrub_all.8
/usr/share/man/man8/e2undo.8
/usr/share/man/man8/e4crypt.8
/usr/share/man/man8/e4defrag.8
/usr/share/man/man8/filefrag.8
/usr/share/man/man8/fsck.ext2.8
/usr/share/man/man8/fsck.ext3.8
/usr/share/man/man8/fsck.ext4.8
/usr/share/man/man8/logsave.8
/usr/share/man/man8/mke2fs.8
/usr/share/man/man8/mkfs.ext2.8
/usr/share/man/man8/mkfs.ext3.8
/usr/share/man/man8/mkfs.ext4.8
/usr/share/man/man8/mklost+found.8
/usr/share/man/man8/resize2fs.8
/usr/share/man/man8/tune2fs.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/e2scrub@.service
/usr/lib/systemd/system/e2scrub_all.service
/usr/lib/systemd/system/e2scrub_all.timer
/usr/lib/systemd/system/e2scrub_fail@.service
/usr/lib/systemd/system/e2scrub_reap.service

%files locales -f e2fsprogs.lang
%defattr(-,root,root,-)

