Summary:	Generic shell script compiler
Name:		shc
Version:	3.7
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.datsi.fi.upm.es/~frosal/sources/%{name}-%{version}.tgz
# Source0-md5:	49e4054ad39371ea84f7be46cf8d9701
URL:		http://www.datsi.fi.upm.es/~frosal/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic shell script compiler. Shc takes a script, which is
specified on the command line and produces C source code. The
generated source code is then compiled and linked to produce a
stripped binary executable. Use with care.

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
