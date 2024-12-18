## START: Set by rpmautospec
## (rpmautospec version 0.7.3)
## RPMAUTOSPEC: autorelease
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 4;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

Name:        quickemu
Version:     4.9.6
Release:     %autorelease
Summary:     Quickly create and run optimised Windows, macOS and Linux virtual machines

Group:       Applications/Emulators
BuildArch:   noarch
License:     MIT
URL:         https://github.com/quickemu-project/%{name}
Source0:     %{url}/archive/refs/tags/%{version}.tar.gz

# Define upstream SHA256SUM for the .tar.gz matching this release version
#   curl -fsSL https://github.com/quickemu-project/quickemu/archive/refs/tags/4.9.6.tar.gz -o - 2>/dev/null | sha256sum
%define      SHA256SUM0 796a047b0bfabb91eb143e5422ff74f5d2812f47120ed6b34eaf82bbdfe3e2a3

# Based on: https://github.com/quickemu-project/quickemu/wiki/01-Installation#install-requirements-on-fedora
# The `zsync` package is listed under Recommends as it is no longer packaged in mainline Fedora
Requires:    bash
Requires:    coreutils
Requires:    curl
Requires:    edk2-tools
Requires:    genisoimage
Requires:    grep
Requires:    jq
Requires:    mesa-demos
Requires:    pciutils
Requires:    procps
Requires:    python3
Requires:    qemu
Requires:    sed
Requires:    socat
Requires:    spice-gtk-tools
Requires:    swtpm
Requires:    unzip
Requires:    usbutils
Requires:    util-linux
Requires:    xdg-user-dirs
Requires:    xrandr
Recommends:  zsync

%description
Quickly create and run optimised Windows, macOS and Linux virtual machines

%global debug_package %{nil}

%prep
# Validate our checksum
echo "%SHA256SUM0  %SOURCE0" | sha256sum -c -
%setup -q

%install
# Install binaries
install -Dm755 chunkcheck %{buildroot}%{_bindir}/chunkcheck
install -Dm755 quickemu %{buildroot}%{_bindir}/quickemu
install -Dm755 quickget %{buildroot}%{_bindir}/quickget
install -Dm755 quickreport %{buildroot}%{_bindir}/quickreport
# Install manpages
install -Dm644 docs/quickemu_conf.1 %{buildroot}%{_mandir}/man1/quickemu_conf.1
install -Dm644 docs/quickemu.1 %{buildroot}%{_mandir}/man1/quickemu.1
install -Dm644 docs/quickget.1 %{buildroot}%{_mandir}/man1/quickget.1

%files
%license LICENSE
%{_bindir}/quickget
%{_bindir}/quickemu
%{_bindir}/quickreport
%{_bindir}/chunkcheck
%{_mandir}/man1/quickemu.1*
%{_mandir}/man1/quickemu_conf.1*
%{_mandir}/man1/quickget.1*

%changelog
* Wed Dec 18 2024 Alex Haydock <alex@alexhaydock.co.uk> - 4.9.6-4
- Rename spec file to match Fedora Packaging Guidelines

* Tue Dec 17 2024 Alex Haydock <alex@alexhaydock.co.uk> - 4.9.6-3
- Use correct SHA256 checksum to validate upstream package

* Tue Dec 17 2024 Alex Haydock <alex@alexhaydock.co.uk> - 4.9.6-2
- Add SHA256SUM validation for upstream code being pulled from GitHub

* Tue Dec 17 2024 Alex Haydock <alex@alexhaydock.co.uk> - 4.9.6-1
- Initial commit
