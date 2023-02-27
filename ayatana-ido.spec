Summary:	Shared functions for Ayatana Indicator Display Objects
Summary(pl.UTF-8):	Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana
Name:		ayatana-ido
Version:	0.9.3
Release:	1
License:	LGPL v2.1 or LGPL v3
Group:		Libraries
#Source0Download: https://github.com/AyatanaIndicators/ayatana-ido/releases
Source0:	https://github.com/AyatanaIndicators/ayatana-ido/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	596a1f9a13d5a903bc46d26175bbe6b0
Patch0:		build-type.patch
URL:		https://github.com/AyatanaIndicators/ayatana-ido
BuildRequires:	cmake >= 3.13
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	vala
Requires:	glib2 >= 1:2.58
Requires:	gtk+3 >= 3.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shared functions for Ayatana Indicator Display Objects.

%description -l pl.UTF-8
Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana.

%package devel
Summary:	Development files for ayatana-ido library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki ayatana-ido
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.58
Requires:	gtk+3-devel >= 3.24

%description devel
This package contains the header files for developing applications
that use ayatana-ido library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę ayatana-ido.

%package -n vala-ayatana-ido
Summary:	Vala API for ayatana-ido library
Summary(pl.UTF-8):	API języka Vala do biblioteki ayatana-ido
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.14.0
BuildArch:	noarch

%description -n vala-ayatana-ido
Vala API for ayatana-ido library.

%description -n vala-ayatana-ido -l pl.UTF-8
API języka Vala do biblioteki ayatana-ido.

%prep
%setup -q
%patch0 -p1

%build
%cmake -B build \
	-DENABLE_TESTS:BOOL=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libayatana-ido3-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libayatana-ido3-0.4.so.0
%{_libdir}/girepository-1.0/AyatanaIdo3-0.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libayatana-ido3-0.4.so
%{_includedir}/libayatana-ido3-0.4
%{_datadir}/gir-1.0/AyatanaIdo3-0.4.gir
%{_pkgconfigdir}/libayatana-ido3-0.4.pc

%files -n vala-ayatana-ido
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libayatana-ido3-0.4.vapi
