# TODO
# - put headers and .a to -devel
%define		pnam	libapreq
Summary:	Generic Apache Request Library
Summary(pl.UTF-8):	Standardowa biblioteka zapytań Apache
Summary(pt_BR.UTF-8):	Biblioteca de requisiçoes do Apache
Name:		perl-libapreq
Version:	1.33
Release:	4
License:	Apache v1.1
Group:		Development/Languages/Perl
Source0:	http://www.apache.org/dist/httpd/libapreq/%{pnam}-%{version}.tar.gz
# Source0-md5:	8ac4296342e637c6faa731dcf9087685
Patch0:		libapreq-modperl2.patch
URL:		http://httpd.apache.org/apreq/
BuildRequires:	perl-Apache-Test >= 1.27-2.3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-mod_perl1-devel >= 1.26-5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildConflicts:	apache-mod_perl < 1:2.0.2-10
Requires:	perl-mod_perl1 >= 1.26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# remember about libapreq.spec when incrementing version

%description
This package contains modules for manipulating client request data via
the Apache API with Perl.

%description -l pl.UTF-8
Ten pakiet zawiera moduły, służące do manipulowania danymi z zapytań
klientów HTTP danymi poprzez API Apache przy użyciu Perla.

%description -l pt_BR.UTF-8
Este pacote contém módulos para a manipulação de requisições de
cliente através da API do Apache em Perl.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -af eg/perl/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/libapreq/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/libapreq.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS README ToDo
%{perl_vendorarch}/Apache/*.pm

%dir %{perl_vendorarch}/auto/Apache/Cookie
%dir %{perl_vendorarch}/auto/Apache/Request
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Cookie/Cookie.so
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Request/Request.so

%dir %{perl_vendorarch}/auto/libapreq
%{perl_vendorarch}/auto/libapreq/extralibs.ld
%attr(755,root,root) %{perl_vendorarch}/auto/libapreq/libapreq.a
%{perl_vendorarch}/auto/libapreq/include

%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/Apache*
%{_mandir}/man3/libapreq*
