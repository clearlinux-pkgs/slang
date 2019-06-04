Name     : slang
Version  : 2.3.2
Release  : 21
URL      : https://www.jedsoft.org/slang/
Source0  : https://www.jedsoft.org/releases/%{name}/%{name}-%{version}.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: slang-bin
BuildRequires : glibc-utils
BuildRequires : libpng-dev
BuildRequires : readline-dev
BuildRequires : ncurses-dev
BuildRequires : onig-dev
BuildRequires : pcre-dev
BuildRequires : zlib-dev
Patch1: stateless.patch

%description
New features and upgrade information for version 2 are described in
the appendices of doc/text/slang.txt and doc/text/cslang.txt.  If you
upgrading from version 1, then you should read these appendices.

%package bin
Summary: bin components for the slang package.
Group: Binaries

%description bin
bin components for the slang package.


%package dev
Summary: dev components for the slang package.
Group: Development

%description dev
dev components for the slang package.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build
%configure --with-readline=gnu
make V=1 %{?_smp_mflags} -j1

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make runtests

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/libslang*.so.2*

%files bin
%defattr(-,root,root,-)
%doc %{_docdir}/slsh
%{_bindir}/slsh
%{_libdir}/slang
%{_mandir}/man1/slsh.1*
%{_datadir}/slsh

%files dev
%defattr(-,root,root,-)
%doc %{_docdir}/slang
%{_libdir}/libslang*.so
%{_libdir}/pkgconfig/slang.pc
%{_includedir}/sl*.h

