Name:           ros-indigo-image-common
Version:        1.11.7
Release:        0%{?dist}
Summary:        ROS image_common package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/image_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-camera-calibration-parsers
Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-polled-camera
BuildRequires:  ros-indigo-catkin

%description
Common code for working with images in ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 28 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.7-0
- Autogenerated by Bloom

* Thu Jul 16 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Thu May 14 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

