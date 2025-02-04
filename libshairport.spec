%global checkout 20121218git16395d8
Name:           libshairport
Version:        1.2.1
Release:        19.%{checkout}%{?dist}
Summary:        Emulates an AirPort Express
Group:          System Environment/Libraries

License:        MIT
URL:            https://github.com/amejia1/libshairport
Source0:        %{name}-%{version}.%{checkout}.tar.gz
# The source for this package was pulled from upstream's vcs.  Invoke the
# following script while in your SOURCES directory to generate the tarball:
#  sh libshairport-generate-tarball-gz.sh
Source1:        libshairport-generate-tarball-gz.sh
# This patch remove unnecessary libssl link, it has been proposed to upstream (https://github.com/amejia1/libshairport/pull/3)
Patch0:         libshairport-remove-libssl-link.patch

BuildRequires:  libao-devel
BuildRequires:  openssl-devel
BuildRequires:  autoconf automake libtool

%description
This program emulates an AirPort Express for the purpose of
streaming music from iTunes and compatible iPods. It implements
a server for the Apple RAOP protocol. ShairPort does not support
AirPlay v2 (video and photo streaming). It supports multiple
simultaneous streams, if your audio output chain
(as detected by libao) does so.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libao-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}.%{checkout}
%patch -P0


%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc LICENSE README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libshairport.pc


%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-19.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-18.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-17.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-16.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-15.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.2.1-14.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-13.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-12.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-11.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-10.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-9.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-8.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.1-7.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.2.1-6.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.1-5.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.2.1-4.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.2.1-3.20121218git16395d8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Dec 30 2012 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.1-2.20121218git16395d8
- Modified specfile to meet review requirements

* Tue Dec 18 2012 Lorenzo Dalrio <lorenzo.dalrio@gmail.com> - 1.2.1-1.20121218git16395d8
- Initial release

