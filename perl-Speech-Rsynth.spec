#
# Conditional build:
# _with_tests - perform "make test" (uses auto device, requires /usr/lib/dict/bDict.db)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Speech
%define		pnam	Rsynth
Summary:	Speech::Rsynth Perl module - interface to librsynth speech synthesis library
Summary(pl):	Modu³ perla Speech::Rsynth - interfejs do biblioteki syntezy mowy librsynth
Name:		perl-Speech-Rsynth
Version:	0.03
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	librsynth-devel >= 2.1.4
%{?_with_tests:BuildRequires:	librsynth-dict-beep}
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speech::Rsynth is a Perl OO interface to Bryan Jurish's adaptation of
Nick Ing-Simmons' "rsynth" speech synthesizer package, itself based on
Jon Iles' implementation of a Klatt formant synthesizer. It currently
provides only basic Text-to-Speech (TTS) capabilities, with output to
file(s) of several formats, as well as directly to an audio device.

%description -l pl
Speech::Rsynth to obiektowo zorientowany interfejs Perla do adaptacji
Bryana Jurisha pakietu do syntezy mowy "rsynth" Nicka Ing-Simmonsa,
bazowanej na implementacji Jona Ilesa syntezatora formantów Klatta.
Modu³ aktualnie udostêpnia tylko podstawowe mo¿liwo¶ci zamiany tekstu
na mowê, z wyj¶ciem do pliku(ów) w kilku formatach oraz bezpo¶rednio
na urz±dzenie d¼wiêkowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

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
