Name:           ros-indigo-rapid-pbd
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS rapid_pbd package

Group:          Development/Libraries
License:        MIT
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-depthcloud-encoder
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mongodb-store
Requires:       ros-indigo-moveit-core
Requires:       ros-indigo-moveit-goal-builder
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-moveit-ros-planning
Requires:       ros-indigo-moveit-ros-planning-interface
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-pr2-controllers-msgs
Requires:       ros-indigo-pr2-mechanism-msgs
Requires:       ros-indigo-rapid-pbd-msgs
Requires:       ros-indigo-robot-controllers-msgs
Requires:       ros-indigo-robot-markers
Requires:       ros-indigo-ros-web-video
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-shape-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-surface-perception
Requires:       ros-indigo-tf
Requires:       ros-indigo-trajectory-msgs
Requires:       ros-indigo-transform-graph
Requires:       ros-indigo-urdf
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mongodb-store
BuildRequires:  ros-indigo-moveit-core
BuildRequires:  ros-indigo-moveit-goal-builder
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-moveit-ros-planning
BuildRequires:  ros-indigo-moveit-ros-planning-interface
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-pr2-controllers-msgs
BuildRequires:  ros-indigo-pr2-mechanism-msgs
BuildRequires:  ros-indigo-rapid-pbd-msgs
BuildRequires:  ros-indigo-robot-controllers-msgs
BuildRequires:  ros-indigo-robot-markers
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-shape-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-surface-perception
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-transform-graph
BuildRequires:  ros-indigo-urdf
BuildRequires:  ros-indigo-visualization-msgs

%description
Programming by demonstration for 1 or 2 arm robots

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Mon Sep 11 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.3-0
- Autogenerated by Bloom

* Mon Sep 11 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.2-0
- Autogenerated by Bloom

