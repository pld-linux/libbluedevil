
%define		qtver	4.6.3

Summary:	Qt-based library to handle all Bluetooth functionality
Summary(pl.UTF-8):	Biblioteka bazuj±ca na Qt obsługująca funkcjonalność Bluetooth
Name:		libbluedevil
Version:	1.7
Release:	0.git.1
License:	GPL
Group:		X11/Libraries
# get via: git clone git://projects.ufocoders.com/libbluedevil
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	fc89a1a6de7801417a837073b9fb306d
URL:		http://projects.ufocoders.com/projects/libbluedevil
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
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
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
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
