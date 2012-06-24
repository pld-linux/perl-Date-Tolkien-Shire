#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Tolkien-Shire
Summary:	Date::Tolkien::Shire - convert dates into the Shire Calendar
Summary(pl):	Date::Tolkien::Shire - konwersja dat do kalendarza �r�dziemia
Name:		perl-Date-Tolkien-Shire
Version:	1.12
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b05bd57758a858354c95a563a1d58ce5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
To jest obiektowo zorientowany modu� do konwertowania dat na kalendarz
�r�dziemia, jaki zosta� przedstawiony we "W�adcy pier�cieni" J. R. R.
Tolkiena. Zawiera konwersj� czasu w formacie epoch na kalendarz
�r�dziemia (i z powrotem), operatory por�wna� oraz metod� do
wypisywania sformatowanego ci�gu zawieraj�cego to, co zdarzy�o si� w
tym czasie - zdarzenia z "W�adcy pier�cieni".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%dir %{perl_vendorlib}/Date/Tolkien
%{perl_vendorlib}/Date/Tolkien/Shire.pm
%{_mandir}/man3/*
