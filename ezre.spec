Name: nextract-xiso       
Version: 1.0
Summary: Create, modify, and extract Xbox/Xbox 360 XISOs.
Release: 1
License: CUSTOM
URL: https://github.com/alex-free/extract-xiso       
Packager: Alex Free
Group: Unspecified

%description
Create, modify, and extract Xbox/Xbox 360 XISOs.

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/nxiso %{buildroot}/usr/bin/

%files
/usr/bin/nxiso
