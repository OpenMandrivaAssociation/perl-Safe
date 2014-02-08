%define upstream_name    Safe
%define upstream_version 2.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Restrict eval'd code to safe subset of ops
Source0:	http://www.cpan.org/modules/by-module/Safe/%{upstream_name}-%{upstream_version}.tar.gz
Url:		http://search.cpan.org/dist/%{upstream_name}

BuildRequires:	perl-devel

BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.290.0-4mdv2012.0
+ Revision: 765637
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.290.0-3
+ Revision: 764150
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.290.0-2
+ Revision: 667307
- mass rebuild

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.290.0-1mdv2011.0
+ Revision: 597197
- update to 2.29

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.270.0-3mdv2011.0
+ Revision: 555310
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Thu May 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.270.0-1mdv2010.1
+ Revision: 545460
- update to 2.27

* Tue Mar 09 2010 Jérôme Quelin <jquelin@mandriva.org> 2.260.0-1mdv2010.1
+ Revision: 517109
- update to 2.26

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.250.0-1mdv2010.1
+ Revision: 515654
- update to 2.25

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 2.240.0-1mdv2010.1
+ Revision: 515358
- update to 2.24

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 2.230.0-1mdv2010.1
+ Revision: 510070
- update to 2.23

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-1mdv2010.1
+ Revision: 504489
- update to 2.22

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 2.210.0-1mdv2010.1
+ Revision: 491623
- update to 2.21

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.200.0-1mdv2010.1
+ Revision: 472367
- update to 2.20

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 2.190.0-1mdv2010.0
+ Revision: 421137
- update to 2.19

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 2.170.0-2mdv2010.0
+ Revision: 400259
- rebuild, without noarch

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.170.0-1mdv2010.0
+ Revision: 392709
- update to 2.17
- using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 2.16-2mdv2010.0
+ Revision: 375905
- rebuild

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.16-1mdv2010.0
+ Revision: 372660
- import perl-Safe


* Wed May 06 2009 cpan2dist 2.16-1mdv
- initial mdv release, generated with cpan2dist

