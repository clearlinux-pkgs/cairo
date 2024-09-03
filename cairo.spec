#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v18
# autospec commit: f35655a
#
Name     : cairo
Version  : 1.18.2
Release  : 103
URL      : https://gitlab.freedesktop.org/cairo/cairo/-/archive/1.18.2/cairo-1.18.2.tar.gz
Source0  : https://gitlab.freedesktop.org/cairo/cairo/-/archive/1.18.2/cairo-1.18.2.tar.gz
Summary  : script surface backend for cairo graphics library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1
Requires: cairo-bin = %{version}-%{release}
Requires: cairo-lib = %{version}-%{release}
Requires: cairo-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gtk+-dev
BuildRequires : libXrender-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : librsvg-dev
BuildRequires : libxcb-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libspectre)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(poppler-glib)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: madvise.patch

%description
This directory provides code that is common to both of cairo's tests
suites:
* The test suite for correctness in test/
* The test suite for performance in perf/

%package bin
Summary: bin components for the cairo package.
Group: Binaries
Requires: cairo-license = %{version}-%{release}

%description bin
bin components for the cairo package.


%package dev
Summary: dev components for the cairo package.
Group: Development
Requires: cairo-lib = %{version}-%{release}
Requires: cairo-bin = %{version}-%{release}
Provides: cairo-devel = %{version}-%{release}
Requires: cairo = %{version}-%{release}

%description dev
dev components for the cairo package.


%package lib
Summary: lib components for the cairo package.
Group: Libraries
Requires: cairo-license = %{version}-%{release}

%description lib
lib components for the cairo package.


%package license
Summary: license components for the cairo package.
Group: Default

%description license
license components for the cairo package.


%prep
%setup -q -n cairo-1.18.2
cd %{_builddir}/cairo-1.18.2
%patch -P 1 -p1
pushd ..
cp -a cairo-1.18.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725380303
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/cairo
cp %{_builddir}/cairo-%{version}/COPYING-LGPL-2.1 %{buildroot}/usr/share/package-licenses/cairo/8088b44375ef05202c0fca4e9e82d47591563609 || :
cp %{_builddir}/cairo-%{version}/COPYING-MPL-1.1 %{buildroot}/usr/share/package-licenses/cairo/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
cp %{_builddir}/cairo-%{version}/perf/COPYING %{buildroot}/usr/share/package-licenses/cairo/2cc384b53d50baa25a960aa83b0ac0edca682fa7 || :
cp %{_builddir}/cairo-%{version}/test/COPYING %{buildroot}/usr/share/package-licenses/cairo/a4233e56493311ffd59845410b6e156f03b07335 || :
cp %{_builddir}/cairo-%{version}/test/pdiff/gpl.txt %{buildroot}/usr/share/package-licenses/cairo/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1 || :
cp %{_builddir}/cairo-%{version}/util/cairo-script/COPYING %{buildroot}/usr/share/package-licenses/cairo/d888f729a340181e37b0b2fb25c2942d5005e6a2 || :
cp %{_builddir}/cairo-%{version}/util/cairo-trace/COPYING %{buildroot}/usr/share/package-licenses/cairo/0315f8fa18770a489890f8448111722aca24b8ec || :
cp %{_builddir}/cairo-%{version}/util/cairo-trace/COPYING-GPL-3 %{buildroot}/usr/share/package-licenses/cairo/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cairo-trace

%files dev
%defattr(-,root,root,-)
/usr/include/cairo/cairo-deprecated.h
/usr/include/cairo/cairo-features.h
/usr/include/cairo/cairo-ft.h
/usr/include/cairo/cairo-gobject.h
/usr/include/cairo/cairo-pdf.h
/usr/include/cairo/cairo-ps.h
/usr/include/cairo/cairo-script-interpreter.h
/usr/include/cairo/cairo-script.h
/usr/include/cairo/cairo-svg.h
/usr/include/cairo/cairo-tee.h
/usr/include/cairo/cairo-version.h
/usr/include/cairo/cairo-xcb.h
/usr/include/cairo/cairo-xlib-xrender.h
/usr/include/cairo/cairo-xlib.h
/usr/include/cairo/cairo.h
/usr/lib64/libcairo-gobject.so
/usr/lib64/libcairo-script-interpreter.so
/usr/lib64/libcairo.so
/usr/lib64/pkgconfig/cairo-fc.pc
/usr/lib64/pkgconfig/cairo-ft.pc
/usr/lib64/pkgconfig/cairo-gobject.pc
/usr/lib64/pkgconfig/cairo-pdf.pc
/usr/lib64/pkgconfig/cairo-png.pc
/usr/lib64/pkgconfig/cairo-ps.pc
/usr/lib64/pkgconfig/cairo-script-interpreter.pc
/usr/lib64/pkgconfig/cairo-script.pc
/usr/lib64/pkgconfig/cairo-svg.pc
/usr/lib64/pkgconfig/cairo-tee.pc
/usr/lib64/pkgconfig/cairo-xcb-shm.pc
/usr/lib64/pkgconfig/cairo-xcb.pc
/usr/lib64/pkgconfig/cairo-xlib-xrender.pc
/usr/lib64/pkgconfig/cairo-xlib.pc
/usr/lib64/pkgconfig/cairo.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/cairo/libcairo-fdr.so
/V3/usr/lib64/cairo/libcairo-trace.so
/V3/usr/lib64/libcairo-gobject.so.2.11802.2
/V3/usr/lib64/libcairo-script-interpreter.so.2.11802.2
/V3/usr/lib64/libcairo.so.2.11802.2
/usr/lib64/cairo/libcairo-fdr.so
/usr/lib64/cairo/libcairo-trace.so
/usr/lib64/libcairo-gobject.so.2
/usr/lib64/libcairo-gobject.so.2.11802.2
/usr/lib64/libcairo-script-interpreter.so.2
/usr/lib64/libcairo-script-interpreter.so.2.11802.2
/usr/lib64/libcairo.so.2
/usr/lib64/libcairo.so.2.11802.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cairo/0315f8fa18770a489890f8448111722aca24b8ec
/usr/share/package-licenses/cairo/2cc384b53d50baa25a960aa83b0ac0edca682fa7
/usr/share/package-licenses/cairo/8088b44375ef05202c0fca4e9e82d47591563609
/usr/share/package-licenses/cairo/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/cairo/9a13113b89f7985efe22a28b8e4ad1ace7f2b5d1
/usr/share/package-licenses/cairo/a4233e56493311ffd59845410b6e156f03b07335
/usr/share/package-licenses/cairo/aba8d76d0af67d57da3c3c321caa59f3d242386b
/usr/share/package-licenses/cairo/d888f729a340181e37b0b2fb25c2942d5005e6a2
