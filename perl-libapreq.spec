%include	/usr/lib/rpm/macros.perl
%define		pnam	libapreq
%define		pdir	libapreq
Summary:	Generic Apache Request Library
Summary(pl):	Standardowa biblioteka zapytañ Apache
Summary(pt_BR):	Biblioteca de requisiçoes do Apache
Name:		perl-libapreq
Version:	1.3
Release:	1
License:	Apache Software License 1.1
Group:		Development/Languages/Perl
Source0:	http://www.apache.org/dist/httpd/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	b40854e91a6210a3af47ffffef9a875e
URL:		http://httpd.apache.org/apreq/
BuildRequires:	apache1-mod_perl >= 1.26-5
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# remember about libapreq.spec when incrementing version

%description
This package contains modules for manipulating client request data via
the Apache API with Perl.

%description -l pl
Ten pakiet zawiera modu³y, s³u¿±ce do manipulowania danymi z zapytañ
klientów HTTP danymi poprzez API Apache przy u¿yciu Perla.

%description -l pt_BR
Este pacote contém módulos para a manipulação de requisições de
cliente através da API do Apache em Perl.

%prep
%setup -q -n %{pnam}-%{version}

%build
echo "/home/services/httpd" | perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -af eg/perl/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS README ToDo
%{perl_vendorarch}/Apache/*.pm

%dir %{perl_vendorarch}/auto/Apache/Cookie
%dir %{perl_vendorarch}/auto/Apache/Request
%{perl_vendorarch}/auto/Apache/Cookie/Cookie.bs
%{perl_vendorarch}/auto/Apache/Request/Request.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Cookie/Cookie.so
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Request/Request.so

%dir %{perl_vendorarch}/auto/libapreq
%{perl_vendorarch}/auto/libapreq/extralibs.ld
%attr(755,root,root) %{perl_vendorarch}/auto/libapreq/libapreq.a
%{perl_vendorarch}/auto/libapreq/include

%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/Apache*
%{_mandir}/man3/libapreq*
