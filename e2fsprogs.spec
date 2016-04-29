#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : e2fsprogs
Version  : 1.42.13
Release  : 35
URL      : http://downloads.sourceforge.net/e2fsprogs/e2fsprogs-1.42.13.tar.gz
Source0  : http://downloads.sourceforge.net/e2fsprogs/e2fsprogs-1.42.13.tar.gz
Summary  : Utilities for managing ext2/ext3/ext4 filesystems
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 LGPL-2.1
Requires: e2fsprogs-bin
Requires: e2fsprogs-lib
Requires: e2fsprogs-data
Requires: e2fsprogs-doc
Requires: e2fsprogs-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : gettext
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pbr
BuildRequires : perl(XML::Parser)
BuildRequires : pip
BuildRequires : pkg-config-dev
BuildRequires : procps-ng
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : texinfo
BuildRequires : util-linux-dev
Patch1: stateless.patch
Patch2: 0001-Skip-certain-tests-due-to-failure-on-XFS-build-hosts.patch

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


%package locales
Summary: locales components for the e2fsprogs package.
Group: Default

%description locales
locales components for the e2fsprogs package.


%prep
%setup -q -n e2fsprogs-1.42.13
%patch1 -p1
%patch2 -p1

%build
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%reconfigure --disable-static --disable-fsck --disable-libblkid  --disable-uuidd --disable-libuuid --enable-elf-shlibs
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang e2fsprogs
## make_install_append content
%make_install install-libs
## make_install_append end

%files
%defattr(-,root,root,-)
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
%exclude /usr/bin/fsck.ext4dev
%exclude /usr/bin/logsave
%exclude /usr/bin/mk_cmds
%exclude /usr/bin/mke2fs
%exclude /usr/bin/mkfs.ext2
%exclude /usr/bin/mkfs.ext3
%exclude /usr/bin/mkfs.ext4
%exclude /usr/bin/mkfs.ext4dev
/usr/bin/chattr
/usr/bin/e2fsck
/usr/bin/e2label
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

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
/usr/bin/fsck.ext4dev
/usr/bin/logsave
/usr/bin/mk_cmds
/usr/bin/mke2fs
/usr/bin/mkfs.ext2
/usr/bin/mkfs.ext3
/usr/bin/mkfs.ext4
/usr/bin/mkfs.ext4dev
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f e2fsprogs.lang 
%defattr(-,root,root,-)

