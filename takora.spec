Name:           takora
Version:        0.1.1
Release:        1%{?dist}
Summary:        Puppet modules for Ceph installation
License:        ASL 2.0

URL:            https://github.com/ceph/takora

#Source0:        https://github.com/ceph/%{name}/archive/%{version}.tar.gz
Source0:       %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
A collection of Puppet modules which are required to install and configure
Ceph via installers using Puppet configuration tool.

%prep
%setup -q

find . -type f -name ".*" -exec rm {} +
rm -f %{name}.spec

%build

%install
install -d -m 0755 %{buildroot}/%{_datadir}/ceph-puppet/modules/
cp -pr $(grep ^mod Puppetfile |cut -d\' -f2) %{buildroot}/%{_datadir}/ceph-puppet/modules/
cp -p Puppetfile %{buildroot}/%{_datadir}/ceph-puppet/

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md CHANGELOG.md
%{_datadir}/ceph-puppet/modules/*
%{_datadir}/ceph-puppet/Puppetfile
