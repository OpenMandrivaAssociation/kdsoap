%define libname %mklibname kdsoap 1
%define devname %mklibname -d kdsoap

Name:		kdsoap
Version:	1.9.0
Release:	1
Url:		https://www.kdab.com/products/kd-soap
Source0:	https://github.com/KDAB/KDSoap/archive/kdsoap-%{version}.tar.gz
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

%description
Qt based client-side and server-side SOAP component

%package -n %{libname}
Summary:	Qt based client-side and server-side SOAP component
Group:		System/Libraries
Provides:	%{mklibname kdsoap-server 1} = %{EVRD}

%description -n %{libname}
Qt based client-side and server-side SOAP component

%package -n %{devname}
Summary:	Development files for the Qt based client-side and server-side SOAP component
Group:		Development/Qt and KDE
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for the Qt based client-side and server-side SOAP component

%prep
%autosetup -p1 -n KDSoap-kdsoap-1.9.0
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{devname}
%{_bindir}/kdwsdl2cpp
%{_libdir}/*.so
%{_includedir}/KDSoapClient
%{_includedir}/KDSoapServer
%{_libdir}/cmake/KDSoap
%{_datadir}/mkspecs/features/kdsoap.prf
%doc %{_docdir}/KDSoap
