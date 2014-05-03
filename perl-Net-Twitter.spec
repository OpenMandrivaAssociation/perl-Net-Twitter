%define upstream_name    Net-Twitter
%define upstream_version 4.01004

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A definition of the TwitterVision API as a Moose role

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
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
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


