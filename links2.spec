#
# Conditional build:
# _without_javascript - don't use javascript interpreter
# _without_graphics - don't use graphics
# _without_svgalib - compile without svgalib graphics driver
# _without_x - compile without X Window System graphics driver
# _without_fb - compile without Linux Framebuffer graphics driver
# _without_pmshell - compile without PMShell graphics driver
# _without_atheos - compile without Atheos graphics driver

%ifnarch %{ix86} alpha
%define _without_svgalib 1
%endif
%define		pre	pre11

Summary:	Lynx-like WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx
Summary(pl):	Podobna do Lynksa przegl�darka WWW
Summary(pt_BR):	O links � um browser para modo texto, similar ao lynx
Summary(ru):	��������� WWW ������� ���� Lynx
Summary(uk):	��������� WWW ������� ���� Lynx
Name:		links2
Version:	2.1%{pre}
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/links/links-%{version}.tar.bz2
# Source0-md5:	d602768af82c3262051cca8f9aa76176
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
Source4:	glinks.desktop
Patch0:		%{name}-links-g_if_glinks.patch
Patch1:		%{name}-ac25x.patch
Patch2:		%{name}-reallyquit.patch
Patch3:		%{name}-img.patch
Patch4:		%{name}-convert-old-bookmarks.patch
Patch5:		%{name}-cookies-save.patch
#Patch6:		%{name}-cookie-parsing.patch
Patch7:		%{name}-config-dirs.patch
Patch8:		%{name}-dump_codepage.patch
Patch9:		%{name}-gzip_fallback.patch
Patch10:	%{name}-js-Date-getTime.patch
#Patch11:	%{name}-js-submit-nodefer.patch
#Patch12:	%{name}-home_etc.patch
Patch13:	http://sven.gimp.org/links-directfb.patch
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	zlib-devel
%if%{!?_without_graphics:1}%{?_without_graphics:0}
%{!?_without_fb:BuildRequires:	DirectFB-devel >= 0.9.17}
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
%{!?_without_javascript:BuildRequires:	flex}
%{!?_without_javascript:BuildRequires:	bison}
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
%{!?_without_x:BuildRequires:	XFree86-devel}
%endif
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Links is a WWW browser, at first look similiar to Lynx, but somehow
different:

- renders tables and frames,
- displays colors as specified in current HTML page,
- uses drop-down menu (like in Midnight Commander),
- can download files in background.

%{!?_without_graphics:This version can work in graphical mode.}
%{!?_without_javascript:This version has support for JavaScript.}

%description -l es
Links es un browser WWW modo texto, similar al Lynx. El links muestra
tablas, hace baja archivos en segundo plano, y usa conexiones HTTP/1.1
keepalive.

%description -l pl
Links jest przegl�dark� WWW, na pierwszy rzut oka podobn� do Lynksa,
ale mimo wszystko inn�:

- renderuje tabelki i ramki,
- wy�wietla kolory zgodnie z definicjami w ogl�danej stronie HTML,
- u�ywa opuszczanego menu (jak w Midnight Commanderze),
- mo�e �ci�ga� pliki w tle.

%{!?_without_graphics:Ta wersja mo�e pracowa� w trybie graficznym.}
%{!?_without_javascript:Ta wersja obs�uguje JavaScript.}

%description -l pt_BR
Links � um browser WWW modo texto, similar ao Lynx. O Links exibe
tabelas, faz baixa arquivos em segundo plano, e usa as conex�es
HTTP/1.1 keepalive.

%description -l ru
Links - ��� ��������� WWW �������, �� ������ ������ ������� �� Lynx,
�� ��������� ������������:

- ���������� ������� � (�����) ������,
- ���������� ����� ��� ������� � HTML ��������,
- ���������� ���������� ���� (��� � Midnight Commander),
- ����� ��������� ����� � ����.

%description -l uk
Links - �� ��������� WWW �������, �� ������ ������ ������ �� Lynx, ���
����� צ�ͦ���� צ� �����:

- צ�������� �����æ �� (���������) ������,
- �����դ ������� �� ������� � HTML ���Ҧ�æ,
- ����������դ �������ަ ���� (�� � Midnight Commander),
- ���� ������������� ����� � ��Φ.

%prep
%setup -q -n links-%{version}
%{!?_without_graphics:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p1
#%patch12 -p1
#%patch13 -p1

%build
rm -f missing
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--program-suffix=2 \
	%{!?_without_graphics:--enable-graphics} \
	%{!?_without_javascript:--enable-javascript} \
	%{?_without_svgalib:--without-svgalib} \
	%{?_without_x:--without-x} \
	%{?_without_fb:--without-fb} \
	%{?_without_pmshell:--without-pmshell} \
	%{?_without_atheos:--without-atheos}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/WWW,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%if%{!?_without_graphics:1}%{?_without_graphics:0}
ln -sf links2 $RPM_BUILD_ROOT%{_bindir}/glinks
echo ".so links2.1" > $RPM_BUILD_ROOT%{_mandir}/man1/glinks.1
echo ".so links2.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/glinks.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links2.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README SITES TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/WWW/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_pixmapsdir}/*
