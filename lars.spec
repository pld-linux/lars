Summary:	Tool for making audio CD from mp3s
Summary(pl):	Narz�dzie do tworzenia p�yt audio z plik�w mp3
Name:		lars
Version:	0.90
Release:	1
License:	GPL
Group:		Applications
Source0:	http://65.108.58.129/programs/%{name}-%{version}.tar.gz
URL:		http://lars.naken.cc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+-devel

%define         _prefix         /usr/X11R6
%define         _mandir         %{_prefix}/man

%description
Lars helps you mass-produce audio CDs from MP3s.

%description -l pl
Lars pomoga w tworzeniu p�yt audio CD z plik�w mp3.

%prep
%setup -q

%build
%{__make} CC=%{__cc}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install lars	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lars
