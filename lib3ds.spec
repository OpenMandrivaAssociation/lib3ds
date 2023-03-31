%define api	1
%define major	3
%define libname	%mklibname 3ds %{api} %{major}
%define devname	%mklibname 3ds -d

Name:		lib3ds
Version:	1.3.0
Release:	21
Summary:	3D Studio file format library
Group:		Development/C
License:	LGPLv2+
URL:		http://lib3ds.sourceforge.net
Source:		http://downloads.sourceforge.net/lib3ds/lib3ds-%{version}.zip
# Extracted from Debian's lib3ds_1.3.0-1.diff.gz
Patch0:		lib3ds-1.3.0-lib3ds-file.h.diff
# Address https://bugzilla.redhat.com/show_bug.cgi?id=633475
Patch1:		lib3ds-1.3.0-lib3ds-mesh.c.diff
Patch2:		lib3ds-1.2.0-pkgconfig.diff
Patch3:		lib3ds-1.3.0-automake-1.13.patch

%description
lib3ds is a free ANSI-C library for working with the popular "3ds" 3D model
format.

Supported platforms include GNU (autoconf, automake, libtool, make, GCC) on
Unix and Cygwin, and MS Visual C++ 6.0. lib3ds loads and saves Atmosphere
settings, Background settings, Shadow map settings, Viewport setting,
Materials, Cameras, Lights, Meshes, Hierarchy, Animation keyframes. It also
contains useful matrix, vector and quaternion mathematics tools. lib3ds
usually integrates well with OpenGL. In addition, some diagnostic and
conversion tools are included.

%package -n %{libname}
Summary:	3D Studio file format library
Group:		System/Libraries
Obsoletes:	%{name} < 1.3.0-16

%description -n %{libname}
lib3ds is a free ANSI-C library for working with the popular "3ds" 3D model
format.

%package tools
Summary:	3D Studio file format library
Group:		Graphical desktop/Other

%description tools
Some tools to process 3ds files.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{name}-devel < 1.3.0-16
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -vfi
%configure  --disable-static
%make_build

sed -e 's,@prefix@,%{_prefix},' \
  -e 's,@exec_prefix@,%{_exec_prefix},' \
  -e 's,@libdir@,%{_libdir},' \
  -e 's,@includedir@,%{_includedir},' \
  -e 's,@VERSION@,%{version},' \
  lib3ds.pc.in > lib3ds.pc

%install
%make_install

# pkgconfig file
install -Dpm 0644 lib3ds.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}
%{_libdir}/%{name}-%{api}.so.%{major}.*

%files tools
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/3dsdump
%{_mandir}/man1/3dsdump.1*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/lib3ds-config
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/lib3ds.pc
%{_mandir}/man1/lib3ds-config.1*
%{_includedir}/lib3ds/
%{_datadir}/aclocal/*
