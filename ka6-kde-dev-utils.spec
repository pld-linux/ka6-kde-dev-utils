#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kde-dev-utils
Summary:	Kde dev utils
Name:		ka6-%{kaname}
Version:	24.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	5a55199d047f7d03669bf22a8f1c43e8
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kparts-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small utilities for developers using KDE/Qt libs/frameworks.

%description -l pl.UTF-8
Małe programy użytkowe dla programistów używających bibliotek KDE/Qt.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpartloader
%attr(755,root,root) %{_bindir}/kuiviewer
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/parts/kuiviewerpart.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/quithumbnail.so
%{_desktopdir}/org.kde.kuiviewer.desktop
%{_iconsdir}/hicolor/128x128/apps/kuiviewer.png
%{_iconsdir}/hicolor/16x16/apps/kuiviewer.png
%{_iconsdir}/hicolor/32x32/apps/kuiviewer.png
%{_iconsdir}/hicolor/48x48/apps/kuiviewer.png
%{_iconsdir}/hicolor/64x64/apps/kuiviewer.png
%{_iconsdir}/hicolor/scalable/apps/kuiviewer.svg
%{_datadir}/metainfo/org.kde.kuiviewer.metainfo.xml
%{_datadir}/metainfo/org.kde.kuiviewerpart.metainfo.xml
