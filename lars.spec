Summary:	Tool for making audio CD from mp3s
Summary(pl):	Narzêdzie do tworzenia p³yt audio z plików mp3
Name:		lars
Version:	0.98
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://65.108.58.129/programs/%{name}-%{version}.tar.gz
# Source0-md5:	57ba20949c8ecf98154e059d3384f3b5
URL:		http://lars.naken.cc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+-devel


%description
Lars helps you mass-produce audio CDs from MP3s.

%description -l pl
Lars pomoga w tworzeniu p³yt audio CD z plików mp3.

%prep
%setup -q

%build
%{__make} CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install lars $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lars
