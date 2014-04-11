# TODO: integration with other Scheme implementations (see Makefile catalogs target)
Summary:	Scheme library
Summary(pl.UTF-8):	Biblioteka Scheme
Name:		slib
Version:	3b4
Release:	1
License:	distributable (BSD and Public Domain parts)
Group:		Development/Languages/Scheme
Source0:	http://groups.csail.mit.edu/mac/ftpdir/scm/%{name}-%{version}.tar.gz
# Source0-md5:	dcada65c4df4209c8f71211095bcef8e
Patch0:		%{name}-info.patch
URL:		http://people.csail.mit.edu/jaffer/SLIB.html
BuildRequires:	texinfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLIB is a portable scheme library meant to provide compatibility and
utility functions for all standard scheme implementations. Slib
conforms to Revised^5 Report on the Algorithmic Language Scheme and
the IEEE P1178 specification.

%description -l pl.UTF-8
SLIB jest przenośną biblioteką scheme mającą zapewnić kompatybilność i
funkcje użytkowe dla wszystkich implementacji scheme. SLIB jest zgodne
ze specyfikacją Revised^5 Report on the Algorithmic Language Scheme
oraz IEEE P1178.

%package -n guile-slib
Summary:	Scheme library for Guile
Summary(pl.UTF-8):	Biblioteka Scheme dla Guile
Group:		Development/Languages/Scheme
Requires(post):	/usr/bin/guile
Requires:	%{name} = %{version}-%{release}
Requires:	guile >= 5:2.0

%description -n guile-slib
SLIB is a portable scheme library meant to provide compatibility and
utility functions for all standard scheme implementations. Slib
conforms to Revised^5 Report on the Algorithmic Language Scheme and
the IEEE P1178 specification.

This package integrates SLIB with Guile implementation.

%description -n guile-slib -l pl.UTF-8
SLIB jest przenośną biblioteką scheme mającą zapewnić kompatybilność i
funkcje użytkowe dla wszystkich implementacji scheme. SLIB jest zgodne
ze specyfikacją Revised^5 Report on the Algorithmic Language Scheme
oraz IEEE P1178.

Ten pakiet integruje SLIB z implementacją Guile.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_datadir}/slib,%{_bindir},%{_mandir}/man1}

cp -p *.scm $RPM_BUILD_ROOT%{_datadir}/slib
cp -p guile.init guile-2.init $RPM_BUILD_ROOT%{_datadir}/slib
# TODO (and possibly other, not present yet in PLD)
#cp -p scheme48.init umbscheme.init $RPM_BUILD_ROOT%{_datadir}/slib

cat > $RPM_BUILD_ROOT%{_bindir}/slib <<EOF
#!/bin/sh
SCHEME_LIBRARY_PATH=%{_datadir}/slib/
EOF
cat slib.sh >>$RPM_BUILD_ROOT%{_bindir}/slib

install slib.1 $RPM_BUILD_ROOT%{_mandir}/man1
install slib.info $RPM_BUILD_ROOT%{_infodir}

install -d $RPM_BUILD_ROOT%{_datadir}/guile/site/2.0
:> $RPM_BUILD_ROOT%{_datadir}/guile/site/2.0/slibcat

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post -n guile-slib
# old (guile < 2) location
rm -f %{_datadir}/guile/site/slibcat
umask 022
/usr/bin/guile -l %{_datadir}/slib/guile.init -c "(use-modules (ice-9 slib)) (require 'new-catalog)" >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE COPYING ChangeLog FAQ README
%attr(755,root,root) %{_bindir}/slib
%dir %{_datadir}/slib
%{_datadir}/slib/*.scm
%{_mandir}/man1/slib.1*
%{_infodir}/slib.info*

%files -n guile-slib
%defattr(644,root,root,755)
%{_datadir}/slib/guile.init
%{_datadir}/slib/guile-2.init
%ghost %{_datadir}/guile/site/2.0/slibcat
