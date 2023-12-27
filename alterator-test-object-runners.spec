Name: alterator-test-object-runners
Version: 0.0.1
Release: alt1

Summary: Test object runners
License: GPLv2+
Group: Other
URL: https://github.com/mchernigin/alterator-test-object-runners

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
Requires: python3-module-pydbus

%description
Description for alterator-test-object-runners...

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/%name
mkdir -p %buildroot%_datadir/alterator/applications
mkdir -p %buildroot%_sysconfdir/alterator/backends
mkdir -p %buildroot%_datadir/alterator/objects/test-object1
mkdir -p %buildroot%_datadir/alterator/objects/test-object2
mkdir -p %buildroot%_sysconfdir/polkit-1/rules.d

install -v -p -m 644 -D test-object1.backend %buildroot%_sysconfdir/alterator/backends
install -v -p -m 644 -D test-object1.alterator %buildroot%_datadir/alterator/objects/test-object1
install -v -p -m 755 -D test-runner1.py %buildroot%_libexecdir/%name
install -v -p -m 644 -D test-runner1.application %buildroot%_datadir/alterator/applications

install -v -p -m 644 -D test-object2.backend %buildroot%_sysconfdir/alterator/backends
install -v -p -m 644 -D test-object2.alterator %buildroot%_datadir/alterator/objects/test-object2
install -v -p -m 755 -D test-runner2.py %buildroot%_libexecdir/%name
install -v -p -m 644 -D test-runner2.application %buildroot%_datadir/alterator/applications

install -v -p -m 644 -D 49-alterator-test-objects.rules %buildroot%_sysconfdir/polkit-1/rules.d

%files
%dir %_libexecdir/%name
%_libexecdir/%name/*.py

%_datadir/alterator/objects/test-object1/test-object1.alterator
%_sysconfdir/alterator/backends/test-object1.backend
%_datadir/alterator/applications/test-runner1.application

%_datadir/alterator/objects/test-object2/test-object2.alterator
%_sysconfdir/alterator/backends/test-object2.backend
%_datadir/alterator/applications/test-runner2.application

%_sysconfdir/polkit-1/rules.d/49-alterator-test-objects.rules

%changelog
* Wed Dec 05 2023 Michael Chernigin <chernigin@altlinux.org> 0.0.1-alt1
- Initial build
