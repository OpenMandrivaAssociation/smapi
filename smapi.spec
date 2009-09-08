%define name    smapi
%define version 2.4.0
%define preversion rc5
%define rel %mkrel 6
%define release 0.%{preversion}.%{rel}

%define major 2.4
%define libname %mklibname %name %major

Summary:	MsgAPI for the Husky-Packages
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source:		%{name}-%{major}-%{preversion}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Patch0:		smapi-20021015-main.patch
Patch1:		smapi-Makefile.diff
URL:		http://sourceforge.net/projects/husky/
BuildRequires:	huskybse

%description
smapi is a modified message api for *.MSG, SQUISH (C) and JAM-Messagebase
formats. It is required for all other Husky-Software.

%package -n %libname
Summary:        MsgAPI for the Husky-Packages
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n %libname
smapi is a modified message api for *.MSG, SQUISH (C) and JAM-Messagebase
formats. It is required for all other Husky-Software.

%package -n %libname-devel
Summary: MsgAPI for the Husky-Packages, development files
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
smapi is a modified message api for *.MSG, SQUISH (C) and JAM-Messagebase
formats. It is required for all other Husky-Software.

This Package holds the Development files. Only needed if you want to compile
other Husky-Packages.

%prep
%setup -q -n %name
%patch0 -p1
%patch1 -p1

%build
%make OPTCFLAGS="$RPM_OPT_FLAGS -fPIC -s -c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/smapi/                                                                
%make INCDIR=$RPM_BUILD_ROOT%{_includedir} LIBDIR=$RPM_BUILD_ROOT%{_libdir} install
install -m 644 cvsdate.h $RPM_BUILD_ROOT%{_includedir}/smapi/

chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%doc BEOS.TXT BUGS COPYING ChangeLog HISTORY INSTALL LICENSE TODO VERSION file_id.diz readme.txt
%{_libdir}/libsmapi.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_includedir}/smapi
%{_libdir}/*.so
%{_libdir}/libsmapi.a



