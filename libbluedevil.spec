
%define		qtver	4.7.1

Summary:	Qt-based library to handle all Bluetooth functionality
Summary(pl.UTF-8):	Biblioteka bazuj±ca na Qt obsługująca funkcjonalność Bluetooth
Name:		libbluedevil
Version:	1.8
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	http://media.ereslibre.es/2010/11/%{name}-v%{version}-1.tar.bz2
# Source0-md5:	03c79dd8a6d40e2872fee27c9b81190d
URL:		http://projects.ufocoders.com/projects/libbluedevil
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	dbus-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libbluedevil is a stable Qt-based library written in C++ to handle all
Bluetooth functionality.

%package devel
Summary:	libbluevil - header files and development documentation
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains header files and development documentation for
libbluedevil.

%prep
%setup -q -n %{name}-v%{version}-1

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbluedevil.*

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/bluedevil.pc
%dir %{_includedir}/bluedevil
%{_includedir}/bluedevil/*
