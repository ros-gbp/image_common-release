Name:           ros-jade-camera-info-manager
Version:        1.11.6
Release:        0%{?dist}
Summary:        ROS camera_info_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/camera_info_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-camera-calibration-parsers
Requires:       ros-jade-image-transport
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslib
Requires:       ros-jade-sensor-msgs
BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-jade-camera-calibration-parsers
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-image-transport
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sensor-msgs

%description
This package provides a C++ interface for camera calibration information. It
provides CameraInfo, and handles SetCameraInfo service requests, saving and
restoring the camera calibration data.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Jul 16 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.6-0
- Autogenerated by Bloom

* Thu May 14 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.5-0
- Autogenerated by Bloom

* Thu Jan 01 2015 Jack O'Quin <jack.oquin@gmail.com> - 1.11.4-0
- Autogenerated by Bloom

