%include	/usr/lib/rpm/macros.perl
Summary:	libapreq perl module
Summary(pl):	Modu³ perla libapreq
Name:		perl-libapreq
Version:	0.33
Release:	1
License:	Apache Group
Group:		Development/Languages/Perl
Source0:	http://www.apache.org/dist/httpd/libapreq-%{version}.tar.gz
URL:		http://httpd.apache.org/apreq/
BuildRequires:	perl >= 5.6
BuildRequires:	apache-mod_perl
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains modules for manipulating client request data via
the Apache API with Perl and C.

%description -l pl
Ten pakiet zawiera modu³y do manipulowania danymi z zapytañ klientów
poprzez API Apache'a.

%prep
%setup -q -n libapreq-%{version}

%build
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes LICENSE README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Apache/*
%dir %{perl_sitearch}/auto/Apache/Cookie
%{perl_sitearch}/auto/Apache/Cookie/Cookie.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Cookie/Cookie.so
%dir %{perl_sitearch}/auto/Apache/Request
%{perl_sitearch}/auto/Apache/Request/Request.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Request/Request.so

%{_mandir}/man3/*

%dir %{perl_sitearch}/auto/libapreq
%{perl_sitearch}/auto/libapreq/include
%{perl_sitearch}/auto/libapreq/.packlist
%{perl_sitearch}/auto/libapreq/extralibs.ld
%attr(755,root,root) %{perl_sitearch}/auto/libapreq/libapreq.a
%{perl_sitearch}/libapreq.pod
