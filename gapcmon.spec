# spec taken from upstream - thanks. AdamW 2007/07

%define name	gapcmon
%define version	0.8.5
%define release	%mkrel 1

Summary: Utility for monitoring the operation of UPSs controlled by apcupsd
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Source: http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Fixes up the .desktop file - it's too broken to use 
# desktop-file-install. AdamW 2007/07
Patch0:	gapcmon-0.8.5-desktop.patch
URL: http://gapcmon.sourceforge.net/
BuildRequires: ImageMagick
BuildRequires: gtk2-devel
BuildRequires: libGConf2-devel
Requires: apcupsd
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
gapcmon monitors and displays the status of UPSs under the management 
of apcupsd. 

%prep
%setup -q
%patch0 -p1 -b .desktop

%build
%configure --disable-maintainer-mode
%make

%install
rm -rf %{buildroot}
%makeinstall

# fd.o icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
cp %{buildroot}%{_datadir}/pixmaps/apcupsd.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{buildroot}%{_datadir}/pixmaps/apcupsd.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -scale 48 %{buildroot}%{_datadir}/pixmaps/apcupsd.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc README AUTHORS NEWS INSTALL ChangeLog
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

