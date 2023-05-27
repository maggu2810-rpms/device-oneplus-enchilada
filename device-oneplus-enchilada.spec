Name:           device-oneplus-enchilada
Version:        0.0.0
Release:        3%{?dist}
Summary:        --

License:        --

Requires:       pd-mapper
Requires:       tqftpserv
Requires:       rmtfs
Requires:       qbootctl
Requires:       op6-fedora-pmos
Requires:       kpartx

%description
--


%build
cat > INFO <<EOF
--
EOF

echo 'KERNEL=="sda17", SUBSYSTEM=="block", ACTION=="add",    RUN+="/usr/sbin/kpartx -a -n /dev/$name"' >  sda17-subpartitions.rules
echo 'KERNEL=="sda17", SUBSYSTEM=="block", ACTION=="change", RUN+="/usr/sbin/kpartx -u -n /dev/$name"' >> sda17-subpartitions.rules
echo 'KERNEL=="sda17", SUBSYSTEM=="block", ACTION=="remove", RUN+="/usr/sbin/kpartx -d -n /dev/$name"' >> sda17-subpartitions.rules



%install
mkdir -p %{buildroot}/usr/share/%{name}
install -m 0644 INFO %{buildroot}/usr/share/%{name}/INFO
mkdir -p %{buildroot}/usr/lib/udev/rules.d/
install -m 0644 sda17-subpartitions.rules %{buildroot}/usr/lib/udev/rules.d/66-sda17-subpartitions.rules


%files
/usr/share/%{name}/INFO
/usr/lib/udev/rules.d/66-sda17-subpartitions.rules


%changelog
* Sat May 27 2023 Markus Rathgeb <maggu2810@gmail.com>
- add kpartx udev rule

* Mon May 22 2023 Markus Rathgeb <maggu2810@gmail.com>
- Initial RPM
