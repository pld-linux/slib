Summary:	scheme library
Name:		slib
Version:	2c9
Release:	1
License:	GPL
Group:		Development/Languages/Scheme
Group(de):	Entwicklung/Sprachen/Scheme
Group(pl):	Programowanie/Jêzyki/Scheme
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

%prep
rm -rf %{name}
unzip -qq %{SOURCE0}
cd %{name}
#%patch -p1

%build
cd %{name}

%install
rm -rf $RPM_BUILD_ROOT

cd %{name}
install -d $RPM_BUILD_ROOT/{%{_infodir},%{_datadir}/guile/slib}
cp -p *.scm $RPM_BUILD_ROOT/%{_datadir}/guile/slib

install slib.info* $RPM_BUILD_ROOT/%{_infodir}

gzip -9nf ANNOUNCE ChangeLog FAQ README *.init *.pat *.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fix_info_dir
/usr/bin/guile -c "(use-modules (ice-9 slib)) (require 'new-catalog ) "

%preun
if [ "$1" = "0" ]; then
	rm -f %{_datadir}/guile/slibcat
fi

%postun
%fix_info_dir

%files
%defattr(644,root,root,755)
%doc %{name}/ANNOUNCE.gz %{name}/ChangeLog.gz %{name}/FAQ.gz %{name}/README.gz
%doc %{name}/*.init.gz %{name}/*.pat.gz %{name}/*.sh.gz 
%{_infodir}/slib.info*
%{_datadir}/guile/slib
