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
mkdir -p %buildroot%_libexecdir/alterator/scripts
mkdir -p %buildroot%_datadir/applications
install -v -p -m 666 -D test-runner1.py %buildroot%_libexecdir/alterator/scripts
install -v -p -m 666 -D test-runner1.desktop %buildroot%_datadir/applications
install -v -p -m 666 -D test-runner2.py %buildroot%_libexecdir/alterator/scripts
install -v -p -m 666 -D test-runner2.desktop %buildroot%_datadir/applications

%files
%_libexecdir/alterator/scripts/*.py
%_datadir/applications/test-runner1.desktop
%_datadir/applications/test-runner2.desktop

%changelog
* Wed Dec 05 2023 Michael Chernigin <chernigin@altlinux.org> 0.0.1-alt1
- Initial build
