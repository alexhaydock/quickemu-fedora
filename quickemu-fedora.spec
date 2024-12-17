## START: Set by rpmautospec
## (rpmautospec version 0.7.3)
## RPMAUTOSPEC: autorelease
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
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