Summary:    Run scripts or programs in a directory
Name:       run-parts
Version:    3.2.1
Release:    %mkrel 1
License:    GPLv2+
Group:      System/Configuration/Other
Url:        http://svn.mandriva.com/svn/soft/run-parts/trunk
Source:     %{name}-%{version}.tar.gz
Conflicts:  setup < 2.7.11-2
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
run-parts runs a number of scripts or programs found in a single direc-
tory.  Filenames should consist entirely of upper and lower
case letters, digits,  underscores,  and  hyphens. Subdirectories  of
directory and files with other names will be silently ignored.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/run-parts
%{_mandir}/man8/*8*
%lang(cs) %_mandir/cs/man8/*8*
%lang(et) %_mandir/et/man8/*8*
%lang(eu) %_mandir/eu/man8/*8*
%lang(fr) %_mandir/fr/man8/*8*
%lang(it) %_mandir/it/man8/*8*
%lang(nl) %_mandir/nl/man8/*8*
%lang(uk) %_mandir/uk/man8/*8*
