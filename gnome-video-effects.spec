Name:           gnome-video-effects
Version:        0.4.1
Release:        1%{?dist}
Summary:        Collection of GStreamer video effects

Group:          System Environment/Libraries
License:        GPLv2
URL:            http://live.gnome.org/GnomeVideoEffects
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.4/%{name}-%{version}.tar.xz
Buildarch:      noarch

BuildRequires:  intltool

Requires:       frei0r-plugins

%description
A collection of GStreamer effects to be used in different GNOME Modules.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS  COPYING NEWS README
%{_datadir}/pkgconfig/gnome-video-effects.pc
%{_datadir}/gnome-video-effects


%changelog
* Mon Apr 14 2014 Richard Hughes <rhughes@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.0-6
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep  8 2012 Hans de Goede <hdegoede@redhat.com> - 0.4.0-4
- Drop Requires for gstreamer-plugins, as we may be used with both
  gstreamer-0.10 and 1.0. Instead apps using gnome-video-effects should add
  the necessary Requires themselves

* Fri Aug 24 2012 Hans de Goede <hdegoede@redhat.com> - 0.4.0-3
- Add Requires for the gstreamer-plugins used by the effects (related#850505)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Yanko Kaneti <yaneti@declera.com> 0.4.0-1
- Update to 0.4.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 10 2011 Yanko Kaneti <yaneti@declera.com> 0.3.0-1
- Update to 0.3.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Yanko Kaneti <yaneti@declera.com> 0.2.0-1
- Update to 0.2.0. New effects.

* Wed Sep  1 2010 Yanko Kaneti <yaneti@declera.com> 0.1.0-1
- Packaged for review
