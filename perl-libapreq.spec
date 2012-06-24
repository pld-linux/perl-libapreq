%include	/usr/lib/rpm/macros.perl
%define		pnam	libapreq
%define		pdir	libapreq
Summary:	Generic Apache Request Library
Summary(pl):	Standardowa biblioteka zapyta� Apache
Summary(pt_BR):	Biblioteca de requisi�oes do Apache
Name:		perl-libapreq
Version:	1.1
Release:	2
License:	Apache Group
Group:		Development/Languages/Perl
Source0:	http://www.apache.org/dist/httpd/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	99471b32f72c43dfd5d2e3078d44c1fc
URL:		http://httpd.apache.org/apreq/
BuildRequires:	apache-mod_perl >= 1.26-5
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# remember about libapreq.spec when incrementing version

%description
This package contains modules for manipulating client request data via
the Apache API with Perl.

%description -l pl
Ten pakiet zawiera modu�y, s�u��ce do manipulowania danymi z zapyta�
klient�w HTTP danymi poprzez API Apache przy u�yciu Perla.

%description -l pt_BR
Este pacote cont�m m�dulos para a manipula��o de requisi��es de
cliente atrav�s da API do Apache em Perl.

%prep
%setup -q -n %{pnam}-%{version}

%build
echo "/home/services/httpd" | perl Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -af eg/perl/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS README ToDo
%{perl_vendorarch}/Apache/*.pm

%dir %{perl_vendorarch}/auto/Apache/Cookie
%{perl_vendorarch}/auto/Apache/Cookie/Cookie.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Cookie/Cookie.so
%dir %{perl_vendorarch}/auto/Apache/Request
%{perl_vendorarch}/auto/Apache/Request/Request.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Request/Request.so

%dir %{perl_vendorarch}/auto/libapreq
%{perl_vendorarch}/auto/libapreq/extralibs.ld
%attr(755,root,root) %{perl_vendorarch}/auto/libapreq/libapreq.a
%{perl_vendorarch}/auto/libapreq/include

%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/Apache*
