# spec taken from upstream - thanks. AdamW 2007/07

Summary:	Utility for monitoring the operation of UPSs controlled by apcupsd
Name:		gapcmon
Version:	0.8.9
Release:	2
License:	GPLv2+
Group:		Monitoring
Source0:	https://sourceforge.net/projects/gapcmon/files/gapcmon/0.8.9/%{name}-%{version}.tar.bz2
# Fixes up the .desktop file - it's too broken to use 
# desktop-file-install. AdamW 2007/07
Patch0:		gapcmon-0.8.5-desktop.patch
Patch1:		gapcmon-0.8.6-fix-str-fmt.patch
URL:		https://gapcmon.sourceforge.net/
BuildRequires:	imagemagick
BuildRequires:	gtk2-devel
BuildRequires:	libGConf2-devel
Requires:	apcupsd

%description
gapcmon monitors and displays the status of UPSs under the management 
of apcupsd. 

%prep
%setup -q
%patch0 -p1 -b .desktop
%patch1 -p0 -b .str

%build
export LDFLAGS="-lX11"
%configure2_5x --disable-maintainer-mode
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# fd.o icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %{buildroot}%{_datadir}/pixmaps/apcupsd.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{buildroot}%{_datadir}/pixmaps/apcupsd.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -scale 48 %{buildroot}%{_datadir}/pixmaps/apcupsd.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc README AUTHORS NEWS INSTALL ChangeLog
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 0.8.6-2mdv2010.1
+ Revision: 508341
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.8.6-1mdv2009.0
+ Revision: 218423
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Mar 01 2008 Adam Williamson <awilliamson@mandriva.org> 0.8.6-1mdv2008.1
+ Revision: 177115
- spec clean
- new release 0.8.6

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Adam Williamson <awilliamson@mandriva.org> 0.8.5-1mdv2008.0
+ Revision: 48428
- buildrequires libGConf2-devel
- Import gapcmon


