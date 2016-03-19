Name:		run-parts
Version:	4.4
Release:	11
Epoch:		1
Summary:	Run scripts or programs in a directory
License:	GPLv2+
Group:		System/Configuration/Other
Url:		http://svn.mandriva.com/svn/soft/run-parts/trunk
Source0:	http://ftp.de.debian.org/debian/pool/main/d/debianutils/debianutils_%{version}.tar.gz
Patch0:		run-parts-4.4-blacklist-rpm-files.patch
Patch1:		run-parts-4.4-allow-dots-in-filenames.patch
Conflicts:	setup < 2.7.11-2

%description
run-parts runs a number of scripts or programs found in a single direc-
tory.  Filenames should consist entirely of upper and lower
case letters, digits,  underscores,  and  hyphens. Subdirectories  of
directory and files with other names will be silently ignored.

%prep
%setup -q -n debianutils-%{version}
%patch0 -p1
%patch1 -p1

%build
%serverbuild_hardened
%configure
%make run-parts

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man8
install -d -m 755 %{buildroot}%{_mandir}/fr/man8

install -m 755 run-parts  %{buildroot}%{_bindir}
install -m 644 run-parts.8  %{buildroot}%{_mandir}/man8

for l in po4a/*/run-parts.8; do
    install -D -m644  ${l} %{buildroot}%{_mandir}/${l:5:2}/man8/run-parts.8
done

%find_lang %{name} --with-man

%files -f %{name}.lang
%doc debian/changelog debian/copyright
%{_bindir}/run-parts
%{_mandir}/man8/run-parts.8*
