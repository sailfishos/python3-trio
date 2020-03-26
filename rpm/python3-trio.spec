# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-trio
Summary:    Trio is a friendly Python library for async concurrency and I/O
Version:    0.13.0
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/pyfuse3/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
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
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/trio
%{python3_sitearch}/trio-*.egg-info
