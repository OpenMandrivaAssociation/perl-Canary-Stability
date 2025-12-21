%define upstream_name Canary-Stability

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    2013
Release:    1

Summary:    Canary to check perl compatibility for schmorp's modules
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/pod/Canary::Stability
Source0:    https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch:  noarch

%description
This module is used by Schmorp's modules during configuration stage to
test the installed perl for compatibility with his modules.

It's not, at this stage, meant as a tool for other module authors,
although in principle nothing prevents them from subscribing to the same
ideas.

See the Makefile.PL in Coro or AnyEvent for usage examples.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc COPYING Changes META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
