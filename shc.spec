Summary:	Generic shell script compiler
Summary(pl.UTF-8):	Kompilator prostych skryptów powłoki
Name:		shc
Version:	3.8.7
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://www.datsi.fi.upm.es/~frosal/sources/%{name}-%{version}.tgz
# Source0-md5:	6057436b4f00b2e0dbf5d364263d822e
URL:		http://www.datsi.fi.upm.es/~frosal/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic shell script compiler. Shc takes a script, which is
specified on the command line and produces C source code. The
generated source code is then compiled and linked to produce a
stripped binary executable. Use with care.

%description -l pl.UTF-8
Kompilator prostych skryptów powłoki. Shc bierze skrypt podany w linii
polecenia i tworzy kod źródłowy w C. Następnie wygenerowany kod w C
jest kompilowany i konsolidowany, tworząc binarny program pozbawiony
symboli dla debuggera. Używając go należy zachować ostrożność.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES shc.README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
