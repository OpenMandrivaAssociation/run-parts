Name:       run-parts
Version:    3.2.1
Release:    12
Epoch:      1
Summary:    Run scripts or programs in a directory
License:    GPLv2+
Group:      System/Configuration/Other
Url:        http://svn.mandriva.com/svn/soft/run-parts/trunk
Source:     debianutils_%{version}.tar.gz
Patch0:     run-parts-3.2.1-blacklist-rpm-files.patch
Patch1:     run-parts-3.2.1-allow-dots-in-filenames.patch
Conflicts:  setup < 2.7.11-2
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
run-parts runs a number of scripts or programs found in a single direc-
tory.  Filenames should consist entirely of upper and lower
case letters, digits,  underscores,  and  hyphens. Subdirectories  of
directory and files with other names will be silently ignored.

%prep
%setup -q -n debianutils-%{version}
%patch0 -p 1
%patch1 -p 1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man8
install -d -m 755 %{buildroot}%{_mandir}/fr/man8

install -m 755 run-parts  %{buildroot}%{_bindir}
install -m 644 run-parts.8  %{buildroot}%{_mandir}/man8
install -m 644 po4a/fr/run-parts.8  %{buildroot}%{_mandir}/fr/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc debian/changelog debian/copyright
%{_bindir}/run-parts
%{_mandir}/man8/run-parts.8*
%{_mandir}/fr/man8/run-parts.8*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1:3.2.1-8mdv2011.0
+ Revision: 669463
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.2.1-7mdv2011.0
+ Revision: 607383
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.2.1-6mdv2010.1
+ Revision: 523936
- rebuilt for 2010.1

* Tue Aug 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:3.2.1-5mdv2010.0
+ Revision: 421072
- set epoch, to ease upgrade from inccorrectly versioned previous release

* Tue Aug 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.1-4mdv2010.0
+ Revision: 420852
- fix regexp in allow-dots-in-filenames.patch

* Mon Aug 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.1-3mdv2010.0
+ Revision: 420536
- use debianutils tarball as source, with mandriva modifications as patches
- drop outdated foreign language man pages
- do not allow dot as first character in filenames

* Mon Aug 24 2009 Nicolas Vigier <nvigier@mandriva.com> 3.2.1-2mdv2010.0
+ Revision: 420431
- bump release

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version (fix #52274)

* Mon Jun 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.13-1mdv2010.0
+ Revision: 386122
- new version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.15-3mdv2009.1
+ Revision: 351540
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.15-2mdv2009.0
+ Revision: 225340
- rebuild

* Fri Mar 28 2008 Toshihiro Yamagishi <toshihiro@turbolinux.co.jp> 1.15-1mdv2008.1
+ Revision: 190880
- added localized man pages
- branched out run-parts from setup-2.7.11-1mdv2008.1
- Created package structure for run-parts.

  + Pixel <pixel@mandriva.com>
    - fix conflict (setup 2.7.12 is not out yet)
    - minor fixes

