%global pypi_name typepy

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        python library for variable type checker/validator/converter at a run time.

License:        MIT
URL:            https://github.com/thombashi/typepy 
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

#test requirements
BuildRequires:  python3-tcolorpy
BuildRequires:  python3-pytz
BuildRequires:  python3-dateutil
%description
python library for variable type checker/validator/converter at a run time.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
 
Requires:  python3-mbstrdecoder >= 1.0.0

%description -n python3-%{pypi_name}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files} 
%license LICENSE
%doc README.rst

%changelog

* Thu Sep 08 2022 Karolina Kula <kkula@redhat.com> - 1.2.0-1
- initial package build

