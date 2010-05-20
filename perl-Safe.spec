%define upstream_name    Safe
%define upstream_version 2.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Restrict eval'd code to safe subset of ops
Source0:    http://www.cpan.org/modules/by-module/Safe/%{upstream_name}-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{upstream_name}

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The Safe extension module allows the creation of compartments in which perl
code can be evaluated. Each compartment has

* a new namespace

  The "root" of the namespace (i.e. "main::") is changed to a different
  package and code evaluated in the compartment cannot refer to variables
  outside this namespace, even with run-time glob lookups and other tricks.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*

