#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Date
%define		pnam	Tolkien-Shire
Summary:	Date::Tolkien::Shire - convert dates into the Shire Calendar
Summary(pl.UTF-8):	Date::Tolkien::Shire - konwersja dat do kalendarza Śródziemia
Name:		perl-Date-Tolkien-Shire
Version:	1.13
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad5744d66f118305a0a09b52f3e24b27
URL:		http://search.cpan.org/dist/Date-Tolkien-Shire/
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

%description -l pl.UTF-8
To jest obiektowo zorientowany moduł do konwertowania dat na kalendarz
Śródziemia, jaki został przedstawiony we "Władcy pierścieni" J. R. R.
Tolkiena. Zawiera konwersję czasu w formacie epoch na kalendarz
Śródziemia (i z powrotem), operatory porównań oraz metodę do
wypisywania sformatowanego ciągu zawierającego to, co zdarzyło się w
tym czasie - zdarzenia z "Władcy pierścieni".

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
