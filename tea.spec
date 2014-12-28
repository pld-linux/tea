Summary:	Powerful text editor
Summary(pl.UTF-8):	Edytor tekstu o dużych możliwościach
Name:		tea
Version:	17.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/tea-editor/%{name}-%{version}.tar.bz2
# Source0-md5:	91f06d5ce93543a0b2ab99a97dcfe2d4
Source1:	%{name}.desktop
URL:		http://tea-editor.sourceforge.net/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	gtksourceview-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TEA is a very small, but powerful text editor with many unique
features.

%description -l pl.UTF-8
TEA to bardzo mały edytor tekstu o dużych możliwościach, posiadający
wiele wyjątkowych cech.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pixmaps/%{name}_icon_v2.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tea
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
