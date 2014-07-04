Summary:        Test runner with a command-line interface
Name:           testkit-lite
Version:        3.1.0
Release:        0
URL:            https://github.com/testkit/testkit-lite
License:        GPL-2.0
Group:          Development/Testing
Source:         %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  fdupes
BuildRequires:  python-distribute
BuildRequires:  python-requests
BuildRequires:  python
Requires:       python
Requires:       python-lxml
Requires:       python-requests
Requires:       testkit-stub
BuildArch:      noarch

%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
testkit-lite is a test runner with command-line interface. It has the following functions
1. Accepts .xml test case descriptor files as input.
2. drives automatic test execution.
3. provide multiple options to meet various test requirements.


%prep
%setup -q
cp %{SOURCE1001} .
# for rpmlint warning: remove shebang from python library
sed -i '/^#!/d' ./testkitlite/commodule/androidmobile.py
sed -i '/^#!/d' ./testkitlite/commodule/localhost.py
sed -i '/^#!/d' ./testkitlite/commodule/tizenivi.py
sed -i '/^#!/d' ./testkitlite/commodule/tizenlocal.py
sed -i '/^#!/d' ./testkitlite/commodule/tizenmobile.py
sed -i '/^#!/d' ./testkitlite/engines/androidunit.py
sed -i '/^#!/d' ./testkitlite/engines/default.py
sed -i '/^#!/d' ./testkitlite/engines/pyunit.py
sed -i '/^#!/d' ./testkitlite/util/autoexec.py
sed -i '/^#!/d' ./testkitlite/util/config.py
sed -i '/^#!/d' ./testkitlite/util/connector.py
sed -i '/^#!/d' ./testkitlite/util/errors.py
sed -i '/^#!/d' ./testkitlite/util/httprequest.py
sed -i '/^#!/d' ./testkitlite/util/killall.py
sed -i '/^#!/d' ./testkitlite/util/log.py
sed -i '/^#!/d' ./testkitlite/util/process.py
sed -i '/^#!/d' ./testkitlite/util/result.py
sed -i '/^#!/d' ./testkitlite/util/session.py
sed -i '/^#!/d' ./testkitlite/util/str2.py


%build


%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d %{buildroot}/%{_datadir}/%{name}
cp -r xsd %{buildroot}/%{_datadir}/%{name}
%fdupes %{buildroot}
pushd %{buildroot}%{python_sitelib}
%py_compile .
popd


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license LICENSE
%config %{_sysconfdir}/dbus-1/system.d/com.intel.testkit.conf
%{_bindir}/testkit-lite
%{_bindir}/testkit-lite-dbus
/opt/testkit/lite/testkit-lite_user_guide.pdf
/opt/testkit/lite/testkit-lite_tutorial.pdf
/opt/testkit/lite/test_definition_schema.pdf
%{python_sitelib}/testkitlite/*
%{python_sitelib}/testkit_lite-%{version}-py%{py_ver}.egg-info/*
%{_datadir}/%{name}
/opt/testkit/lite/VERSION
/opt/testkit/lite/commodule/CONFIG
