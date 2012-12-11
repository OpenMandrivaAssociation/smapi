%define name    smapi
%define version 2.4.0
%define preversion rc5
%define rel 5
%define release 0.%{preversion}.%{rel}

%define major 2.4
%define libname %mklibname %name %major

Summary:	MsgAPI for the Husky-Packages
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source0:		%{name}-%{major}-%{preversion}.tar.bz2
Patch0:		smapi-20021015-main.patch
Patch1:		smapi-Makefile.diff
patch2:		smapi-2.4-rc5.huskymap.patch
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
#% patch0 -p1
%patch1 -p1
%patch2 -p1 -b .huskymak

%build
%make OPTCFLAGS="$RPM_OPT_FLAGS -fPIC -s -c"

%install
install -d $RPM_BUILD_ROOT%{_includedir}/smapi/                                                                
%make INCDIR=$RPM_BUILD_ROOT%{_includedir} LIBDIR=$RPM_BUILD_ROOT%{_libdir} install
install -m 644 cvsdate.h $RPM_BUILD_ROOT%{_includedir}/smapi/

chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so*

%files -n %libname
%defattr(-,root,root)
%doc BEOS.TXT BUGS COPYING ChangeLog HISTORY INSTALL LICENSE TODO VERSION file_id.diz readme.txt
%{_libdir}/libsmapi.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_includedir}/smapi
%{_libdir}/*.so
%{_libdir}/libsmapi.a





%changelog
* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.0-0.rc5.5mdv2009.0
+ Revision: 260821
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.0-0.rc5.4mdv2009.0
+ Revision: 252636
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.4.0-0.rc5.2mdv2008.1
+ Revision: 136503
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4.0-0.rc5.2mdv2007.0
+ Revision: 106738
- fix provides

* Sun Jul 16 2006 Olivier Thauvin <nanardon@mandriva.org> 2.4.0-0.rc5.1mdv2007.0
+ Revision: 41308
- 2.4 rc5
- 2.4 rc5
- Import smapi

* Sun Jan 30 2005 Sylvie Terjan <erinmargault@mandrake.org> 2.4.0rc2-2mdk
- birthday rebuild

