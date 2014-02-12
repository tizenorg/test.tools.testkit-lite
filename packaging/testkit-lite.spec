Summary:        Test runner with a command-line interface
Name:           testkit-lite
Version:        2.3.22
Release:        0
URL:            https://github.com/testkit/testkit-lite
License:        GPL-2.0
Group:          Development/Testing
Source:         %{name}_%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  fdupes
BuildRequires:  python-distribute
BuildRequires:  python-requests
BuildRequires:  python
Requires:       python
Requires:       python-lxml
Requires:       python-requests
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
sed -i '/^#!/d' ./commodule/connector.py
sed -i '/^#!/d' ./commodule/log.py
sed -i '/^#!/d' ./commodule/killall.py
sed -i '/^#!/d' ./commodule/autoexec.py
sed -i '/^#!/d' ./commodule/httprequest.py
sed -i '/^#!/d' ./commodule/str2.py
sed -i '/^#!/d' ./commodule/impl/androidmobile.py
sed -i '/^#!/d' ./commodule/impl/tizenpc.py
sed -i '/^#!/d' ./commodule/impl/localhost.py
sed -i '/^#!/d' ./commodule/impl/tizenmobile.py
sed -i '/^#!/d' ./testkitlite/common/process_killall.py
sed -i '/^#!/d' ./testkitlite/engines/default/runner.py
sed -i '/^#!/d' ./testkitlite/engines/default/worker.py


%build


%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/opt/testkit/lite/testkit-lite_user_guide_for_tct.pdf


%clean
rm -rf %{buildroot}


%post
# Set permissions
chmod ugo+rwx /opt/testkit/lite


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license LICENSE
%{_bindir}/testkit-lite
%{python_sitelib}/testkitlite/*
%{python_sitelib}/commodule/*
%{python_sitelib}/testkit_lite-%{version}-py%{py_ver}.egg-info/*
/opt/testkit/lite/VERSION
