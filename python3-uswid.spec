#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A pure-python library for embedding CoSWID data
Summary(pl.UTF-8):	Czysto pythonowa biblioteka do usadzania danych CoSWID
Name:		python3-uswid
Version:	0.5.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/uswid/
Source0:	https://files.pythonhosted.org/packages/source/u/uswid/uswid-%{version}.tar.gz
# Source0-md5:	e43ff6d49ddcda0c95338d3271694b91
Patch0:		uswid-no-wheel.patch
URL:		https://pypi.org/project/uswid/
# current cbor3 requires python 3.8
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cbor2
BuildRequires:	python3-lxml
BuildRequires:	python3-pefile
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pure-python library for embedding CoSWID data.

%description -l pl.UTF-8
Czysto pythonowa biblioteka do usadzania danych CoSWID.

%package apidocs
Summary:	API documentation for Python uswid module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona uswid
Group:		Documentation

%description apidocs
API documentation for Python uswid module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona uswid.

%prep
%setup -q -n uswid-%{version}
%patch0 -p1

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest uswid/test_uswid.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/uswid
%{py3_sitescriptdir}/uswid
%{py3_sitescriptdir}/uswid-%{version}-py*.egg-info
