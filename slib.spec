Summary: 	scheme library
Name:		slib
Version:	2c7
Release:	0
License:	GPL
Group:		Development/Languages/scheme
URL:		http://www-swiss.ai.mit.edu/~jaffer/SLIB.html
Source:		ftp://ftp-swiss.ai.mit.edu/pub/scm/%{name}%{version}.tar.gz
Patch:		slib2c3-texi.patch
Requires:	guile
BuildArchitectures:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
SLIB is a portable scheme library meant to provide compatibility and 
utility functions for all standard scheme implementations. Slib conforms to 
Revised^5 Report on the Algorithmic Language Scheme and the IEEE P1178 
specification.    

%prep
%setup -q -n %{name}
%patch -p1

%build
#make slib.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_infodir},%{_datadir}/guile/slib,etc/profile.d}
cp -p *.scm $RPM_BUILD_ROOT/%{_datadir}/guile/slib
cp -p slib.info* $RPM_BUILD_ROOT/%{_infodir}

gzip -9nf $RPM_BUILD_ROOT/%{_infodir}/*.info*
gzip -9nf ANNOUNCE ChangeLog FAQ README *.init *.pat *.sh 


echo 'SCHEME_LIBRARY_PATH=%{_datadir}/guile/slib/
export SCHEME_LIBRARY_PATH' \
> $RPM_BUILD_ROOT/etc/profile.d/slib.sh
echo 'setenv SCHEME_LIBRARY_PATH %{_datadir}/guile/slib/' \
> $RPM_BUILD_ROOT/etc/profile.d/slib.csh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.gz ChangeLog.gz FAQ.gz README.gz
%doc  *.init.gz *.pat.gz *.sh.gz 
%attr(755, root, root) /etc/profile.d/slib.sh
%attr(755, root, root) /etc/profile.d/slib.csh
%{_infodir}/slib.info*.gz
%{_datadir}/guile/slib
