%define modname	Safe
%define modver 2.35

Summary:	Restrict eval'd code to safe subset of ops
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Safe/Safe-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
The Safe extension module allows the creation of compartments in which perl
code can be evaluated. Each compartment has

* a new namespace

  The "root" of the namespace (i.e. "main::") is changed to a different
  package and code evaluated in the compartment cannot refer to variables
  outside this namespace, even with run-time glob lookups and other tricks.

%prep
%setup -qn %{modname}-%{modver} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


