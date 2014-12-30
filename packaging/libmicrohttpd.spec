Summary:        Embeded HTTP server library
Name:           libmicrohttpd
Version:        0.9.39
Release:        1
License:        LGPL v2.1+
Group:          Libraries
Source0:        http://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
Patch0:         %{name}-link.patch
URL:            http://www.gnu.org/software/libmicrohttpd/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libcurl-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  texinfo
#BuildRoot:     %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.

%package devel
Summary:        Header files to develop libmicrohttpd applications
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files to develop libmicrohttpd applications.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
    --disable-static \
    --enable-curl \
    --enable-https \
    --enable-largefile \
    --enable-messages \
    --with-pic 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post   devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
#%{_bindir}/microspdy2http
%{_libdir}/libmicrohttpd.so.10
%{_libdir}/libmicrospdy.so.0
%{_libdir}/libmicrohttpd.so.*.*.*
%{_libdir}/libmicrospdy.so.*.*.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*.h
%{_infodir}/libmicrohttpd*.info*
%{_mandir}/man3/libmicrohttpd.3*
%{_libdir}/pkgconfig/*.pc

