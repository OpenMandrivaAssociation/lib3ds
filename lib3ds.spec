%define major 3
%define libname %mklibname 3ds %{major}
%define develname %mklibname 3ds -d

Summary:	The 3D Studio file format library
Name:		lib3ds
Version:	1.3.0
Release:	6
License:	GPLv2+
Group:		System/Libraries
URL:		http://lib3ds.sourceforge.net/
Source0:		http://downloads.sourceforge.net/lib3ds/%{name}-%{version}.zip
BuildRequires:	pkgconfig(glut)


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


%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std
#multiarch
%multiarch_binaries %{buildroot}%{_bindir}/lib3ds-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -n %{libname}
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/*
%defattr(755,root,root,755)
%{_bindir}/3ds*
%{_bindir}/lib3ds-config
%multiarch %{multiarch_bindir}/lib3ds-config


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-5mdv2011.0
+ Revision: 620064
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2010.0
+ Revision: 429715
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2009.0
+ Revision: 267802
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.0-2mdv2009.0
+ Revision: 195676
- libify the package
- new license policy
- new development library policy
- spec file clean

* Tue Dec 25 2007 Emmanuel Andry <eandry@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 137803
- New version
- drop patch (applied upstream)
- create lib3ds binary package

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 18 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.0-6mdv2007.0
+ Revision: 110447
- compile with -fPIC
- Import lib3ds

* Wed Jan 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.0-5mdk
- fix underquoted calls (P0)

* Fri May 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.0-4mdk
- multiarch

* Sat Aug 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.0-3mdk
- rebuild

