Summary:	Tool for making audio CD from MP3s
Summary(pl.UTF-8):	Narzędzie do tworzenia płyt audio z plików MP3
Name:		lars
Version:	0.98
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://65.108.58.129/programs/%{name}-%{version}.tar.gz
# Source0-md5:	57ba20949c8ecf98154e059d3384f3b5
URL:		http://lars.naken.cc/
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Lars helps you mass-produce audio CDs from MP3s.

%description -l pl.UTF-8
Lars pomaga w tworzeniu płyt audio CD z plików MP3.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install lars $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lars
