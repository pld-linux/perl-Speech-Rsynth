#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# (uses auto device, requires /usr/lib/dict/bDict.db)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Speech
%define		pnam	Rsynth
Summary:	Speech::Rsynth Perl module - interface to librsynth speech synthesis library
Summary(pl.UTF-8):	Moduł perla Speech::Rsynth - interfejs do biblioteki syntezy mowy librsynth
Name:		perl-Speech-Rsynth
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.ling.uni-potsdam.de/~moocow/projects/spsyn/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5c3e75c4bba2edd6c00a3fac773099ca
BuildRequires:	gdbm-devel
BuildRequires:	librsynth-devel >= 2.2.1
%{?with_tests:BuildRequires:	librsynth-dict-beep}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speech::Rsynth is a Perl OO interface to Bryan Jurish's adaptation of
Nick Ing-Simmons' "rsynth" speech synthesizer package, itself based on
Jon Iles' implementation of a Klatt formant synthesizer. It currently
provides only basic Text-to-Speech (TTS) capabilities, with output to
file(s) of several formats, as well as directly to an audio device.

%description -l pl.UTF-8
Speech::Rsynth to obiektowo zorientowany interfejs Perla do adaptacji
Bryana Jurisha pakietu do syntezy mowy "rsynth" Nicka Ing-Simmonsa,
bazowanej na implementacji Jona Ilesa syntezatora formantów Klatta.
Moduł aktualnie udostępnia tylko podstawowe możliwości zamiany tekstu
na mowę, z wyjściem do pliku(ów) w kilku formatach oraz bezpośrednio
na urządzenie dźwiękowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README util/*
%{perl_vendorarch}/Speech/Rsynth.pm
%dir %{perl_vendorarch}/auto/Speech/Rsynth
%{perl_vendorarch}/auto/Speech/Rsynth/autosplit.ix
%{perl_vendorarch}/auto/Speech/Rsynth/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Speech/Rsynth/*.so
%{_mandir}/man3/*
