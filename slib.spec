Summary:	Scheme library
Summary(pl):	Biblioteka Scheme
Name:		slib
Version:	3a1
Release:	2
License:	GPL
Group:		Development/Languages/Scheme
Source0:	ftp://ftp-swiss.ai.mit.edu/pub/scm/%{name}%{version}.tar.gz
# Source0-md5:	dc1aa0ffb9e2414223ceefc315f6baf9
Patch0:		%{name}-info.patch
URL:		http://www-swiss.ai.mit.edu/~jaffer/SLIB.html
BuildRequires:	texinfo
Requires(post):	/usr/bin/guile
Requires:	guile
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SLIB is a portable scheme library meant to provide compatibility and
utility functions for all standard scheme implementations. Slib
conforms to Revised^5 Report on the Algorithmic Language Scheme and
the IEEE P1178 specification.

%description -l pl
SLIB jest przeno¶n± bibliotek± scheme maj±c± zapewniæ kompatybilno¶æ i
funkcje u¿ytkowe dla wszystkich implementacji scheme. SLIB jest zgodne
ze specyfikacj± Revised^5 Report on the Algorithmic Language Scheme
oraz IEEE P1178.

%prep
%setup -q -n %{name}
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_datadir}/guile/slib}
install *.scm $RPM_BUILD_ROOT%{_datadir}/guile/slib
install slib.info $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/usr/bin/guile -c "(use-modules (ice-9 slib)) (require 'new-catalog ) "
chmod 644 %{_datadir}/guile/slibcat

%preun
if [ "$1" = "0" ]; then
	rm -f %{_datadir}/guile/slibcat
fi

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog FAQ README *.init *.sh
%{_datadir}/guile/slib
%{_infodir}/slib.info*
