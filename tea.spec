Summary:	Powerful text editor
Summary(pl):	Edytor tekstu o du¿ych mo¿liwo¶ciach
Name:		tea
Version:	4.0
Release:	1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://tea.linux.kiev.ua/%{name}.tar.bz2
# Source0-md5:	b874966f4d3910aeacaaabea7154078a
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://tea.linux.kiev.ua/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TEA is a very small, but powerful text editor with many unique
features.

%description -l pl
TEA to bardzo ma³y edytor tekstu o du¿ych mo¿liwo¶ciach, posiadaj±cy
wiele wyj±tkowych cech.

%prep
%setup -q
%patch0 -p1

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

install %{name}_icon_v2.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO doc/*
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
