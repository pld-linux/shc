Summary:	Generic shell script compiler
Summary(pl):	Kompilator prostych skryptów pow³oki
Name:		shc
Version:	3.8.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.datsi.fi.upm.es/~frosal/sources/%{name}-%{version}.tgz
# Source0-md5:	b2cb72065f1bfab5a4c5d36c1f40770f
URL:		http://www.datsi.fi.upm.es/~frosal/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic shell script compiler. Shc takes a script, which is
specified on the command line and produces C source code. The
generated source code is then compiled and linked to produce a
stripped binary executable. Use with care.

%description -l pl
Kompilator prostych skryptów pow³oki. Shc bierze skrypt podany w linii
polecenia i tworzy kod ¼ród³owy w C. Nastêpnie wygenerowany kod w C
jest kompilowany i konsolidowany, tworz±c binarny program pozbawiony
symboli dla debuggera. U¿ywaj±c go nale¿y zachowaæ ostro¿no¶æ.

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
