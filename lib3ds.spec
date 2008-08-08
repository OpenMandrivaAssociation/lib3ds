%define major 3
%define libname %mklibname 3ds %{major}
%define develname %mklibname 3ds -d

Summary:	The 3D Studio file format library
Name:		lib3ds
Version:	1.3.0
Release:	%mkrel 3
#Patch0:		lib3ds-1.2.0-fix-underquoted-calls.patch
License:	GPLv2+
Group:		System/Libraries
URL:		http://lib3ds.sourceforge.net/
Source0:	http://downloads.sourceforge.net/lib3ds/%{name}-%{version}.zip
BuildRequires:	MesaGLU-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for handling
3DS files It's main goal is to simplify the creation of 3DS import and
export filters.

This project is not related in any form to Autodesk. The library is
based on unofficial information about the 3DS format found on the web.

%package -n %{libname}
Summary:	The 3D Studio file format library
Group:		System/Libraries
Obsoletes:	lib3ds < 1.3.0-2
Provides:	lib3ds

%description -n %{libname}
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for handling
3DS files It's main goal is to simplify the creation of 3DS import and
export filters.

This project is not related in any form to Autodesk. The library is
based on unofficial information about the 3DS format found on the web.

%package -n %{develname}
Summary:	Development files and headers for %{name}
Group:          Development/C
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	lib3ds-devel < 1.3.0-2

%description -n	%{develname}
Development files and headers for %{name}.

%prep
%setup -q
#%patch0 -p1 -b .underquoted

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
#multiarch
%multiarch_binaries %{buildroot}%{_bindir}/lib3ds-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/%{name}.la
%{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/*
%defattr(755,root,root,755)
%{_bindir}/3ds*
%{_bindir}/lib3ds-config
%multiarch %{multiarch_bindir}/lib3ds-config
