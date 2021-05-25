#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-Abstract
Version  : 3.008
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Abstract-3.008.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Abstract-3.008.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libe/libemail-abstract-perl/libemail-abstract-perl_3.008-1.debian.tar.xz
Summary  : 'unified interface to mail representations'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Email-Abstract-license = %{version}-%{release}
Requires: perl-Email-Abstract-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Email::Simple)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Pluggable)

%description
This archive contains the distribution Email-Abstract,
version 3.008:
unified interface to mail representations

%package dev
Summary: dev components for the perl-Email-Abstract package.
Group: Development
Provides: perl-Email-Abstract-devel = %{version}-%{release}
Requires: perl-Email-Abstract = %{version}-%{release}

%description dev
dev components for the perl-Email-Abstract package.


%package license
Summary: license components for the perl-Email-Abstract package.
Group: Default

%description license
license components for the perl-Email-Abstract package.


%package perl
Summary: perl components for the perl-Email-Abstract package.
Group: Default
Requires: perl-Email-Abstract = %{version}-%{release}

%description perl
perl components for the perl-Email-Abstract package.


%prep
%setup -q -n Email-Abstract-3.008
cd %{_builddir}
tar xf %{_sourcedir}/libemail-abstract-perl_3.008-1.debian.tar.xz
cd %{_builddir}/Email-Abstract-3.008
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Email-Abstract-3.008/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Email-Abstract
cp %{_builddir}/Email-Abstract-3.008/LICENSE %{buildroot}/usr/share/package-licenses/perl-Email-Abstract/f64962ea2646981898a121d94ec42de3a591f049
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Email-Abstract/ce1a3d9133bfc81a12f4f9822f2bdaec062009bc
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::Abstract.3
/usr/share/man/man3/Email::Abstract::EmailMIME.3
/usr/share/man/man3/Email::Abstract::EmailSimple.3
/usr/share/man/man3/Email::Abstract::MIMEEntity.3
/usr/share/man/man3/Email::Abstract::MailInternet.3
/usr/share/man/man3/Email::Abstract::MailMessage.3
/usr/share/man/man3/Email::Abstract::Plugin.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Email-Abstract/ce1a3d9133bfc81a12f4f9822f2bdaec062009bc
/usr/share/package-licenses/perl-Email-Abstract/f64962ea2646981898a121d94ec42de3a591f049

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract.pm
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract/EmailMIME.pm
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract/EmailSimple.pm
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract/MIMEEntity.pm
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract/MailInternet.pm
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract/MailMessage.pm
/usr/lib/perl5/vendor_perl/5.34.0/Email/Abstract/Plugin.pm
