Summary:	Scheme library
Summary(pl):	Biblioteka Scheme
Name:		slib
Version:	2c9
Release:	4
License:	GPL
Group:		Development/Languages/Scheme
Source0:	ftp://ftp-swiss.ai.mit.edu/pub/scm/%{name}%{version}.zip
Patch0:		%{name}-info.patch
URL:		http://www-swiss.ai.mit.edu/~jaffer/SLIB.html
Requires:	guile
Prereq:		/usr/bin/guile
BuildRequires:	unzip
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
install -d $RPM_BUILD_ROOT/{%{_infodir},%{_datadir}/guile/slib}

install *.scm $RPM_BUILD_ROOT/%{_datadir}/guile/slib

install slib.info* $RPM_BUILD_ROOT/%{_infodir}

gzip -9nf ANNOUNCE ChangeLog FAQ README *.init *.pat *.sh

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
%doc *.gz
%{_infodir}/slib.info*
%{_datadir}/guile/slib
