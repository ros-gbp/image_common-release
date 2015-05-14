Name:           ros-indigo-camera-calibration-parsers
Version:        1.11.5
Release:        0%{?dist}
Summary:        ROS camera_calibration_parsers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-sensor-msgs
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  yaml-cpp-devel

%description
camera_calibration_parsers contains routines for reading and writing camera
calibration parameters.

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
* Thu May 14 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

