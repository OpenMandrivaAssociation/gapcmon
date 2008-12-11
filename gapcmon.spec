# spec taken from upstream - thanks. AdamW 2007/07

Summary:	Utility for monitoring the operation of UPSs controlled by apcupsd
Name:		gapcmon
Version:	0.8.6
Release:	%{mkrel 1}
License:	GPLv2+
Group:		Monitoring
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Fixes up the .desktop file - it's too broken to use 
# desktop-file-install. AdamW 2007/07
Patch0:		gapcmon-0.8.5-desktop.patch
URL:		http://gapcmon.sourceforge.net/
BuildRequires:	imagemagick
BuildRequires:	gtk2-devel
BuildRequires:	libGConf2-devel
Requires:	apcupsd
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
gapcmon monitors and displays the status of UPSs under the management 
of apcupsd. 

%prep
%setup -q
%patch0 -p1 -b .desktop

%build
%configure2_5x --disable-maintainer-mode
%make

%install
rm -rf %{buildroot}
%makeinstall

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

