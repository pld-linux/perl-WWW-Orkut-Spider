#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Orkut-Spider
Summary:	WWW::Orkut::Spider - Perl extension for spidering the orkut community
Name:		perl-WWW-Orkut-Spider
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22f998d1a1d8972fda078e21ec5cf870
URL:		http://search.cpan.org/dist/WWW-Orkut-Spider/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-HTML-Parser >= 1
BuildRequires:	perl-WWW-Mechanize >= 0.7
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Orkut::Spider uses WWW:Mechanize to scrape orkut.com. Output is a
simple xml format containing friends, communities and profiles for a
given Orkut UID.

- Access to orkut.com via WWW::Mechanize
- Collects UIDs
- Fetches Profiles/Communities/Friends for a given UID
- Output via simple xml format

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/WWW/Orkut
%{perl_vendorlib}/WWW/Orkut/*.pm
%dir %{perl_vendorlib}/auto/WWW/Orkut
%dir %{perl_vendorlib}/auto/WWW/Orkut/Spider
%{perl_vendorlib}/auto/WWW/Orkut/Spider/autosplit.ix

%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
