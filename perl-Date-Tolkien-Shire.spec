%include	/usr/lib/rpm/macros.perl
Summary:	Date-Tolkien-Shire perl module
Summary(pl):	Modu³ perla Date-Tolkien-Shire
Name:		perl-Date-Tolkien-Shire
Version:	0.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/Date-Tolkien-Shire-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an object-oriented module to convert dates into the Shire Calender as
presented in the Lord of the Rings by J. R. R. Tolkien.  It includes converting
epoch time to the Shire Calendar (you can also get epoch time back), comparison
operators, and a method to print a formatted string containing that does
something to the effect of on this date in history -- pulling events from the
Lord of the Rings.

%prep
%setup -q -n Date-Tolkien-Shire-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Date/Tolkien/Shire.pm
%{_mandir}/man3/*
