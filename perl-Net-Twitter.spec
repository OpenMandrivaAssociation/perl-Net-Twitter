%define upstream_name    Net-Twitter
%define upstream_version 3.17001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A definition of the TwitterVision API as a Moose role
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(Data::Visitor::Callback)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::Strptime)
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(JSON::Any)
BuildRequires:	perl(JSON::XS)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Exporter)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(MooseX::MultiInitArg)
BuildRequires:	perl(Net::Netrc)
BuildRequires:	perl(Net::OAuth)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
The micro-blogging service the http://identi.ca manpage provides a Twitter
compatible API. This module simply creates an instance of 'Net::Twitter'
with the 'identica' option set.

See the Net::Twitter manpage for full documentation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.170.10-2mdv2011.0
+ Revision: 657456
- rebuild for updated spec-helper

* Tue Apr 05 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.170.10-1
+ Revision: 650587
- add a BR on MooseX::Role::Parameterized
- new upstream version 3.17001

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 3.17000

* Wed Mar 30 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.160.0-1
+ Revision: 649003
- add a br on Test::Fatal
- new version

* Tue Mar 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 3.150.0-1
+ Revision: 641142
- update to 3.15000

* Tue Feb 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.140.30-1
+ Revision: 636795
- update to new version 3.14003

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.140.20-1mdv2011.0
+ Revision: 596737
- adding missing buildrequires
- update to 3.14002

  + Sandro Cazzaniga <kharec@mandriva.org>
    - new upstream version

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 3.130.80-1mdv2011.0
+ Revision: 573799
- update to 3.13008

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.130.70-1mdv2011.0
+ Revision: 552477
- update to 3.13007

* Tue Apr 27 2010 Jérôme Quelin <jquelin@mandriva.org> 3.120.0-1mdv2010.1
+ Revision: 539483
- adding missing buildrequires:
- import perl-Net-Twitter


* Mon Apr 26 2010 cpan2dist 3.12000-1mdv
- initial mdv release, generated with cpan2dist
