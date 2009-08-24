Summary:    Run scripts or programs in a directory
Name:       run-parts
Version:    3.2.1
Release:    %mkrel 3
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
