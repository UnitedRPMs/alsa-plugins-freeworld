Name:           alsa-plugins-freeworld
Version:        1.2.6
Release:        7%{dist}
Summary:        Extra Plug-Ins for ALSA Library
License:        LGPLv2+
Group:          System Environment/Libraries
Url:            http://www.alsa-project.org/
Source:         https://www.alsa-project.org/files/pub/plugins/alsa-plugins-%{version}.tar.bz2

#--------------------------------------------
BuildRequires:  libtool
BuildRequires:  autoconf 
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa) >= 1.2.2
BuildRequires:  pkgconfig(avtp)
BuildRequires:	ffmpeg-devel >= 5.0


%description
This is a meta package installing a few sub-packages for extra plug-ins
for ALSA library.

%package a52
Summary:        A52 Output Plug-In for ALSA Library
License:        LGPLv2+
Group:          System Environment/Libraries

%description a52
This package contains the A52 (aka AC3) output plug-in for ALSA library.


%package lavrate
Summary:        Rate Converter Plug-In for ALSA Library using libavcodec
License:        LGPLv2+
Group:          System Environment/Libraries


%description lavrate
This package contains the sample rate converter plugin for ALSA
library using libavcodec.

%package aaf
Summary:        AVTP Audio Format PCM Plug-In for ALSA Library
License:        LGPLv2+
Group:          System Environment/Libraries

%description aaf
This package contains the AVTP AUdio Format (AAF) I/O plug-in
for ALSA library.

%prep
%autosetup -n alsa-plugins-%{version}

%build
%configure --disable-static \
  --disable-mix \
  --disable-oss \
  --disable-maemo-plugin \
  --disable-jack \
  --disable-pulseaudio \
  --disable-speexdsp \
  --disable-usbstream \
  --disable-arcamav \
  --disable-samplerate \
  --with-speex=no

%make_build

%install
%make_install

# modules don't need *.la files
find %{buildroot} -type f -name "*.la" -delete -print


%files a52
%license COPYING
%doc doc/a52.txt
%{_libdir}/alsa-lib/libasound_module_pcm_a52.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/60-a52-encoder.conf
%{_sysconfdir}/alsa/conf.d/60-a52-encoder.conf

%files lavrate
%license COPYING
%doc doc/lavrate.txt
%{_libdir}/alsa-lib/libasound_module_rate_lavrate.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_fast.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_faster.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_high.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_higher.so
%dir %{_datadir}/alsa/alsa.conf.d
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%{_datadir}/alsa/alsa.conf.d/10-rate-lav.conf
%{_sysconfdir}/alsa/conf.d/10-rate-lav.conf

%files aaf
%license COPYING
%doc doc/aaf.txt
%{_libdir}/alsa-lib/libasound_module_pcm_aaf.so


%changelog

* Fri Feb 11 2022 David Va <davidva AT tuta DOT io> 1.2.6-7 
- Updated to 1.2.6

* Fri May 29 2020 David Va <davidva AT tuta DOT io> 1.2.2-7 
- Initial build
