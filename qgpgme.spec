%define major 15
%define libname %mklibname qgpgme
%define devname %mklibname qgpgme -d
%define libname6 %mklibname qgpgmeqt6
%define devname6 %mklibname qgpgmeqt6 -d

Name:		qgpgme
Version:	2.0.0
Release:	1
Source0:	https://gnupg.org/ftp/gcrypt/qgpgme/qgpgme-%{version}.tar.xz
Summary:	Qt bindings to GPGme
URL:		https://gnupg.org/download/index.html
License:	GPL
Group:		System/Libraries
BuildRequires:	pkgconfig(gpgmepp) >= 2.0.0
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt6CorePrivate)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6TestPrivate)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake
BuildSystem:	cmake

%description
Qt bindings to GPGme

%package -n %{libname}
Summary:	Qt 5.x bindings to GPGme
Group:		System/Libraries
# Renamed after 6.0 2025-06-08
%rename	%{mklibname qgpgme 15}

%description -n %{libname}
Qt 5.x bindings to GPGme

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}:
Qt 5.x bindings to GPGme

%package -n %{libname6}
Summary:	Qt 6.x bindings to GPGme
Group:		System/Libraries
# Renamed after 6.0 2025-06-08
%rename	%{mklibname qgpgme 15}

%description -n %{libname6}
Qt 6.x bindings to GPGme

%package -n %{devname6}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname6} = %{EVRD}

%description -n %{devname6}
Development files (Headers etc.) for %{name}:
Qt 6.x bindings to GPGme

%files -n %{libname}
%{_libdir}/libqgpgme.so.%{major}*

%files -n %{devname}
%{_includedir}/qgpgme-qt5
%{_libdir}/cmake/QGpgme
%{_libdir}/libqgpgme.so

%files -n %{libname6}
%{_libdir}/libqgpgmeqt6.so.%{major}*

%files -n %{devname6}
%{_includedir}/qgpgme-qt6
%{_libdir}/cmake/QGpgmeQt6
%{_libdir}/libqgpgmeqt6.so
