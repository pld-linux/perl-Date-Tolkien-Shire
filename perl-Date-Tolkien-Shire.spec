%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Tolkien-Shire
Summary:	Date::Tolkien::Shire perl module
Summary(pl):	Modu³ perla Date::Tolkien::Shire
Name:		perl-Date-Tolkien-Shire
Version:	1.01
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an object-oriented module to convert dates into the Shire
Calender as presented in the Lord of the Rings by J. R. R. Tolkien. It
includes converting epoch time to the Shire Calendar (you can also get
epoch time back), comparison operators, and a method to print a
formatted string containing that does something to the effect of on
this date in history -- pulling events from the Lord of the Rings.

%description -l pl
To jest obiektowo zorientowany modu³ do konwertowania dat na kalendarz
Shire, jaki zosta³ przedstawiony we "W³adcy pier¶cieni" J. R. R.
Tolkiena. Zawiera konwersjê czasu w formacie epoch na kalendarz Shire
(i z powrotem), operatory porównañ oraz metodê do wypisywania
sformatowanego ci±gu zawieraj±cego to, co zdarzy³o siê w tym czasie -
zdarzenia z "W³adcy pier¶cieni".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
