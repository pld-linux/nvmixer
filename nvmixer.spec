Summary:	nForce mixer utility
Summary(pl):	Narzêdzie do miksera nForce
Name:		nvmixer
# see bottom of README
Version:	0290
Release:	1
License:	nVidia
Group:		Applications/Sound
Source0:	ftp://download.nvidia.com/linux/nforce/nvmixer/%{name}.tgz
# Source0-md5:	38ac39d298b2dbdc46c660af77e6fe47
Patch0:		%{name}-libm.patch
BuildRequires:	qt-devel
Requires:	kernel-misc(nforce)
# there aren't any kernel modules for other archs
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nForce mixer utility.

%description -l pl
Narzêdzie do miksera nForce.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I." \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -I%{_includedir}/qt" \
	MOC="%{_bindir}/moc"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}

%{__make} install \
	INSTROOT=$RPM_BUILD_ROOT \
	MOC="%{_bindir}/moc"

# strip install information
sed '1,3d;s,/bin,%{_sbindir},' MixerRegistry/ReadMe > ReadMe.nvmix-reg
install MixerRegistry/nvmix-reg $RPM_BUILD_ROOT%{_sbindir}
install MixerRegistry/nvmixrc $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE ReadMe.nvmix-reg
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
