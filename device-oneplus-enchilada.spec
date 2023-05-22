Name:           device-oneplus-enchilada
Version:        0.0.0
Release:        2%{?dist}
Summary:        --

License:        --

Requires:       pd-mapper
Requires:       tqftpserv
Requires:       rmtfs
Requires:       qbootctl
Requires:       op6-fedora-pmos

%description
--


%build
cat > INFO <<EOF
--
EOF


%install
mkdir -p %{buildroot}/usr/share/%{name}
install -m 0644 INFO %{buildroot}/usr/share/%{name}/INFO


%files
/usr/share/%{name}/INFO


%changelog
* Mon May 22 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial RPM
