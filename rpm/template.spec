%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-cyclonedds
Version:        0.10.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS cyclonedds package

License:        Eclipse Public License 2.0 and Eclipse Distribution License 1.0
URL:            https://projects.eclipse.org/projects/iot.cyclonedds
Source0:        %{name}-%{version}.tar.gz

Requires:       openssl
Requires:       ros-iron-iceoryx-binding-c
Requires:       ros-iron-iceoryx-hoofs
Requires:       ros-iron-iceoryx-posh
Requires:       ros-iron-ros-workspace
BuildRequires:  cmake3
BuildRequires:  openssl-devel
BuildRequires:  ros-iron-iceoryx-binding-c
BuildRequires:  ros-iron-iceoryx-hoofs
BuildRequires:  ros-iron-iceoryx-posh
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Eclipse Cyclone DDS is a very performant and robust open-source DDS
implementation. Cyclone DDS is developed completely in the open as an Eclipse
IoT project.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Fri Nov 08 2024 Eclipse Foundation, Inc. <cyclonedds-dev@eclipse.org> - 0.10.5-1
- Autogenerated by Bloom

* Wed Feb 07 2024 Eclipse Foundation, Inc. <cyclonedds-dev@eclipse.org> - 0.10.4-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Eclipse Foundation, Inc. <cyclonedds-dev@eclipse.org> - 0.10.3-2
- Autogenerated by Bloom

* Thu Apr 06 2023 Eclipse Foundation, Inc. <cyclonedds-dev@eclipse.org> - 0.10.3-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Eclipse Foundation, Inc. <cyclonedds-dev@eclipse.org> - 0.9.1-3
- Autogenerated by Bloom

