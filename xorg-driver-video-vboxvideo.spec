Summary:	X.org video driver for VirtualBox virtual video card
Summary(pl.UTF-8):	Sterownik obrazu X.org dla wirtualnej karty graficznej VirtualBoksa
Name:		xorg-driver-video-vboxvideo
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-vboxvideo-%{version}.tar.xz
# Source0-md5:	35f4a0059f2294edfc5b93866f45a218
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	gcc >= 5:3.2
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.12.901
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.6
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-lib-libpciaccess >= 0.12.901
Requires:	xorg-xserver-server >= 1.6
Provides:	xorg-driver-video
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for VirtualBox virtual video card.

%description -l pl.UTF-8
Sterownik obrazu X.org dla wirtualnej karty graficznej VirtualBoksa.

%prep
%setup -q -n xf86-video-vboxvideo-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/vboxvideo_drv.so
%{_mandir}/man4/vboxvideo.4*
