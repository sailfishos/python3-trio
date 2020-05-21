Name:       python3-trio
Summary:    Trio is a friendly Python library for async concurrency and I/O
Version:    0.13.0
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/trio/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-base
Requires:       python3-async-generator >= 1.9
Requires:       python3-attrs >= 19.2.0
Requires:       python3-idna
Requires:       python3-outcome
Requires:       python3-sniffio
Requires:       python3-sortedcontainers

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}/trio

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{python3_sitelib}/trio
%{python3_sitelib}/trio-*.egg-info
%exclude %{python3_sitelib}/trio/tests
%exclude %{python3_sitelib}/trio/testing
%exclude %{python3_sitelib}/trio/_core/tests
