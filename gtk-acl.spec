Name: 		gtk-acl
Version:	0.1.90
Release:	%mkrel 7
Summary:	A GTK front end to manage ACL permissions on files
Group:		File tools
URL:		http://savannah.nongnu.org/projects/gtk-acl/
Source:		http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
License:	GPL
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Buildrequires:	acl-devel 
Buildrequires:  gtk+-devel
Buildrequires:  libglade2.0-devel

%description
You can :
        - Set write, read and execute attributes to acl and unix files
        permissions
        - Change user and group owner of unix file
        - Add or delete acl users
        - Add or delete acl groups


%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall_std mkinstalldirs=`pwd`/mkinstalldirs
rm -Rf %{buildroot}/%{_prefix}/doc
install -d %{buildroot}/%{_datadir}/konqueror/servicemenus
install -m644 %{SOURCE1} %{buildroot}/%{_datadir}/konqueror/servicemenus

%{find_lang} %{name}

%clean
rm -Rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/konqueror/servicemenus/*
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS README TODO

