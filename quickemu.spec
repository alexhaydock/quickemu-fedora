## START: Set by rpmautospec
## (rpmautospec version 0.7.3)
## RPMAUTOSPEC: autorelease
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 10;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

Name:           quickemu
Version:        4.9.7
Release:        %{autorelease}
Summary:        Quickly create and run optimised Windows, macOS and Linux virtual machines
License:        MIT

URL:            https://github.com/quickemu-project/quickemu
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Import an upstream fix that solves VMs crashing due to the use of Pipewire on
# Fedora 41 and above
Patch:          https://github.com/quickemu-project/quickemu/pull/1565.patch

# Import an upstream proposed fix which ensures UEFI Secure Boot functions
# as a user would expect (on Fedora and other distributions), by enabling the
# Microsoft UEFI Secure Boot Platform Keys within VMs
Patch:          https://github.com/quickemu-project/quickemu/pull/1579.patch

BuildArch:      noarch

Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       edk2-tools
Requires:       genisoimage
Requires:       grep
Requires:       jq
Requires:       mesa-demos
Requires:       pciutils
Requires:       procps
Requires:       python3
Requires:       qemu
Requires:       sed
Requires:       socat
Requires:       spice-gtk-tools
Requires:       swtpm
Requires:       unzip
Requires:       usbutils
Requires:       util-linux
Requires:       xdg-user-dirs
Requires:       xrandr

%description
Quickly create and run optimised Windows, macOS and Linux virtual machines

%prep
%autosetup -p1

%install
# Install binaries
install -Dm755 chunkcheck %{buildroot}%{_bindir}/chunkcheck
install -Dm755 quickemu %{buildroot}%{_bindir}/quickemu
install -Dm755 quickget %{buildroot}%{_bindir}/quickget
install -Dm755 quickreport %{buildroot}%{_bindir}/quickreport
# Install manpages
install -Dm644 docs/quickemu_conf.5 %{buildroot}%{_mandir}/man1/quickemu_conf.5
install -Dm644 docs/quickemu.1 %{buildroot}%{_mandir}/man1/quickemu.1
install -Dm644 docs/quickget.1 %{buildroot}%{_mandir}/man1/quickget.1

%files
%license LICENSE
%{_bindir}/chunkcheck
%{_bindir}/quickemu
%{_bindir}/quickget
%{_bindir}/quickreport
%{_mandir}/man1/quickemu_conf.5*
%{_mandir}/man1/quickemu.1*
%{_mandir}/man1/quickget.1*

%changelog
* Tue Dec 17 2024 Alex Haydock <alex@alexhaydock.co.uk> - 4.9.7-1
- Initial package import to Fedora
