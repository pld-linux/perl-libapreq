%include	/usr/lib/rpm/macros.perl
%define		pnam	libapreq
%define		pdir	libapreq
Summary:	Generic Apache Request Library
Summary(pl):	Standardowa biblioteka zapytañ Apache
Summary(pt_BR):	Biblioteca de requisiçoes do Apache
Name:		perl-libapreq
Version:	1.0
Release:	1
License:	Apache Group
Group:		Development/Languages/Perl
Source0:	http://www.apache.org/dist/httpd/%{pdir}/%{pnam}-%{version}.tar.gz
URL:		http://httpd.apache.org/apreq/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	apache-mod_perl >= 1.26-5
Requires:	apache-mod_perl >= 1.26
Provides:	perl(Apache::Request) = 1.0 perl(Apache::Cookie) = 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains modules for manipulating client request data via
the Apache API with Perl and C.

%description -l pl
Ten pakiet zawiera modu³y, s³u¿±ce do manipulowania z zapytañ klientów
HTTP danymi poprzez API Apache przy u¿yciu Perla i C.

%description -l pt_BR
Este pacote contém módulos para a manipulação de requisições de
cliente através da API do Apache em Perl e C.


%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -f eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/*.pm

%dir %{perl_sitearch}/auto/Apache/Cookie
%{perl_sitearch}/auto/Apache/Cookie/Cookie.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Cookie/Cookie.so
%dir %{perl_sitearch}/auto/Apache/Request
%{perl_sitearch}/auto/Apache/Request/Request.bs
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Request/Request.so

%dir %{perl_sitearch}/auto/libapreq
%{perl_sitearch}/auto/libapreq/extralibs.ld
%attr(755,root,root) %{perl_sitearch}/auto/libapreq/libapreq.a

%{perl_sitearch}/auto/libapreq/include

%doc Changes CREDITS INSTALL LICENSE README ToDo
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
