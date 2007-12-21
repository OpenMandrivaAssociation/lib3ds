%define	name	lib3ds
%define	version	1.2.0
%define	rel	6
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		lib3ds-1.2.0-fix-underquoted-calls.patch
License:	GPL
Group:		System/Libraries
URL:		http://lib3ds.sourceforge.net/
Summary:	The 3D Studio File Format Library
BuildRequires:	MesaGLU-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for handling
3DS files It's main goal is to simplify the creation of 3DS import and
export filters.

This project is not related in any form to Autodesk. The library is
based on unofficial information about the 3DS format found on the web.

This  program  is  distributed in  the  hope that it will  be useful,  but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
License for more details.

%package -n	%{name}-devel
Summary:        The 3D Studio File Format Library
Group:          Development/C

%description -n	%{name}-devel
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for handling
3DS files It's main goal is to simplify the creation of 3DS import and
export filters.

This project is not related in any form to Autodesk. The library is
based on unofficial information about the 3DS format found on the web.

This  program  is  distributed in  the  hope that it will  be useful,  but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
License for more details.

%prep
%setup -q
%patch0 -p1 -b .underquoted

%build
CFLAGS="%{optflags} -fPIC" %configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
#multiarch
%multiarch_binaries %{buildroot}%{_bindir}/lib3ds-config

%clean
rm -rf %{buildroot}

%files -n %{name}-devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README TODO
%{_libdir}/%{name}.a
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/*
%defattr(755,root,root,755)
%{_bindir}/3ds*
%{_bindir}/lib3ds-config
%multiarch %{multiarch_bindir}/lib3ds-config


