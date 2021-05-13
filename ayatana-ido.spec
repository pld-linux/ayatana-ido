Summary:	Shared functions for Ayatana Indicator Display Objects
Summary(pl.UTF-8):	Funkcje współdzielone dla obiektów wyświetlania wskaźników Ayatana
Name:		ayatana-ido
Version:	0.8.2
Release:	1
License:	LGPL v2.1 or LGPL v3
Group:		Libraries
#Source0Download: https://github.com/AyatanaIndicators/ayatana-ido/releases
Source0:	https://github.com/AyatanaIndicators/ayatana-ido/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f72ce8fb7bdedf80c20d6083fa371e19
URL:		https://github.com/AyatanaIndicators/ayatana-ido
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 1:2.37.0
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gtk+3-devel >= 3.8.2
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	vala
BuildRequires:	which
Requires:	glib2 >= 1:2.37.0
Requires:	gtk+3 >= 3.8.2
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
Requires:	glib2-devel >= 1:2.37.0
Requires:	gtk+3-devel >= 3.8.2

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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

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
%{_datadir}/vala/vapi/AyatanaIdo3-0.4.vapi
