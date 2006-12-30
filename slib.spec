Summary:	Scheme library
Summary(pl):	Biblioteka Scheme
Name:		slib
Version:	3a4
Release:	1
License:	GPL
Group:		Development/Languages/Scheme
Source0:	ftp://ftp-swiss.ai.mit.edu/pub/scm/%{name}%{version}.tar.gz
# Source0-md5:	87bc0b62370c0bf8a510a2acf6868eb9
Patch0:		%{name}-info.patch
URL:		http://www-swiss.ai.mit.edu/~jaffer/SLIB.html
BuildRequires:	texinfo
Requires(post):	/usr/bin/guile
Requires:	guile >= 5:1.8
Requires:	guile < 5:1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLIB is a portable scheme library meant to provide compatibility and
utility functions for all standard scheme implementations. Slib
conforms to Revised^5 Report on the Algorithmic Language Scheme and
the IEEE P1178 specification.

%description -l pl
SLIB jest przenośną biblioteką scheme mającą zapewnić kompatybilność i
funkcje użytkowe dla wszystkich implementacji scheme. SLIB jest zgodne
ze specyfikacją Revised^5 Report on the Algorithmic Language Scheme
oraz IEEE P1178.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_datadir}/guile/slib,%{_bindir},%{_mandir}/man1}
install *.scm $RPM_BUILD_ROOT%{_datadir}/guile/slib
sed -e 's,/usr/lib/slib/,%{_datadir}/guile/slib/,' guile.init > $RPM_BUILD_ROOT%{_datadir}/guile/slib/guile.init
cat > $RPM_BUILD_ROOT%{_bindir}/slib <<EOF
#!/bin/sh
SCHEME_LIBRARY_PATH=%{_datadir}/guile/slib/
EOF
cat slib.sh >>$RPM_BUILD_ROOT%{_bindir}/slib
install slib.1 $RPM_BUILD_ROOT%{_mandir}/man1
install slib.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

# note: using "(use-modules (ice-9 slib))" in -c here fails
%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
umask 022
rm -f %{_datadir}/guile/slibcat
/usr/bin/guile -l %{_datadir}/guile/slib/guile.init -c "(require 'new-catalog)"

%preun
if [ "$1" = "0" ]; then
	rm -f %{_datadir}/guile/1.8/slibcat
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog FAQ README *.init
%attr(755,root,root) %{_bindir}/slib
%{_datadir}/guile/slib
%{_mandir}/man1/slib.1*
%{_infodir}/slib.info*
