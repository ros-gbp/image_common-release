Name:           ros-melodic-image-transport
Version:        1.11.13
Release:        0%{?dist}
Summary:        ROS image_transport package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/image_transport
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-filters
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-rosconsole
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roslib
Requires:       ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-rosconsole
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-sensor-msgs

%description
image_transport should always be used to subscribe to and publish images. It
provides transparent support for transporting images in low-bandwidth compressed
formats. Examples (provided by separate plugin packages) include JPEG/PNG
compression and Theora streaming video.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Mar 26 2018 Jack O'Quin <jack.oquin@gmail.com> - 1.11.13-0
- Autogenerated by Bloom

