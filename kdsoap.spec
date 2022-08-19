%define libname %mklibname kdsoap
%define lib6name %mklibname kdsoap-qt6
%define slibname %mklibname kdsoap-server
%define slib6name %mklibname kdsoap-server-qt6
%define devname %mklibname -d kdsoap

Name:		kdsoap
Version:	2.0.0
Release:	1
Url:		https://www.kdab.com/products/kd-soap
Source0:	https://github.com/KDAB/KDSoap/releases/download/kdsoap-%{version}/kdsoap-%{version}.tar.gz
Patch0:		kdsoap-2.0.0-fix-qt6-codegen.patch
Group:		System/Libraries
Summary:	Qt based client-side and server-side SOAP component
License:	GPL/AGPL/LGPL
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)

%description
Qt based client-side and server-side SOAP component

%package -n %{libname}
Summary:	Qt based client-side SOAP component
Group:		System/Libraries

%description -n %{libname}
Qt based client-side SOAP component

%package -n %{lib6name}
Summary:	Qt based client-side SOAP component
Group:		System/Libraries

%description -n %{lib6name}
Qt 6 based client-side SOAP component

%package -n %{slibname}
Summary:	Qt based server-side SOAP component
Group:		System/Libraries

%description -n %{slibname}
Qt based server-side SOAP component

%package -n %{slib6name}
Summary:	Qt 6 based server-side SOAP component
Group:		System/Libraries

%description -n %{slib6name}
Qt 6 based server-side SOAP component

%package -n %{devname}
Summary:	Development files for the Qt based client-side and server-side SOAP component
Group:		Development/Qt and KDE
Requires:	%{libname} = %{EVRD}
Requires:	%{slibname} = %{EVRD}
Requires:	%{lib6name} = %{EVRD}
Requires:	%{slib6name} = %{EVRD}

%description -n %{devname}
Development files for the Qt based client-side and server-side SOAP component

%prep
%autosetup -p1
%cmake_kde5

cd ..

export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DKDSoap_QT6:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%ninja_build -C build-qt6

%install
%ninja_install -C build

%ninja_install -C build-qt6

%files -n %{libname}
%{_libdir}/libkdsoap.so.*

%files -n %{lib6name}
%{_libdir}/libkdsoap-qt6.so.*

%files -n %{slibname}
%{_libdir}/libkdsoap-server.so.*

%files -n %{slib6name}
%{_libdir}/libkdsoap-server-qt6.so.*

%files -n %{devname}
%{_bindir}/kdwsdl2cpp
%{_libdir}/*.so
%{_includedir}/KDSoapClient
%{_includedir}/KDSoapServer
%{_libdir}/cmake/KDSoap
%{_libdir}/qt5/mkspecs/modules/qt_KDSoapClient.pri
%{_libdir}/qt5/mkspecs/modules/qt_KDSoapServer.pri
%{_datadir}/mkspecs/features/kdsoap.prf
%doc %{_docdir}/KDSoap
