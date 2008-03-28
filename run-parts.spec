Summary:    Run scripts or programs in a directory
Name:       run-parts
Version:    1.15
Release:    %mkrel 1
License:    GPLv2+
Group:      System/Configuration/Other
Url:        http://svn.mandriva.com/svn/soft/run-parts/trunk
Source:     %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}
Conflicts:  setup < 2.7.11-2

%description
run-parts runs a number of scripts or programs found in a single direc-
tory.  Filenames should consist entirely of upper and lower
case letters, digits,  underscores,  and  hyphens. Subdirectories  of
directory and files with other names will be silently ignored.

%prep
%setup -q

%build
%configure
%make CFLAGS="$RPM_OPT_FLAGS"

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
