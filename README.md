# SITL
This is the assigned task for UAV software Engineer Task (SITL). The link to the doc of the task can be found in the link below. The main objective is to perform Software In The Loop (SITL) simulation. Example and steps are shown in the doc, however there are shown using Mission Planer and dronekit.
This repo contains script for SITL using ROS, MAVROS and QGC.

* [LINK](https://docs.google.com/document/d/1pH_aj5hL5RaRzuzeWXZFK4SGmJOqAFgBG_7zk75i9Tk/edit) - Document for the task.

## Prerequisites
In order to run the script, some of the softwares must be installed. These softwares are shown below:

Ubuntu: 16.04, ROS: Kinetic
* [ROS](http://wiki.ros.org/kinetic/Installation/Ubuntu) - Document for ROS installation.

MAVROS: v0.33.0
* [MAVROS](https://github.com/mavlink/mavros/tree/master/mavros#installation) - Document for MAVROS installation.

QGC: v3.5.5
* [QGC](https://docs.qgroundcontrol.com/en/getting_started/download_and_install.html) - Document for QGround Station Installtion.

## Autopilot type and version
- [ ] Ardupilot
- [X] [PX4](https://github.com/PX4/Firmware.git) - Autopilot for SITL.

# Steps
4 terminial is required to run the SITL.
First terminal:
```python
roscore
```
Second terminal:
```
roslaunch mavros px4.launch 
```
Thrid terminal:
```
cd ~/src/Firmware
export PX4_HOME_LAT=2.909368
export PX4_HOME_LON=101.655304
export PX4_HOME_ALT=28.5
make px4_sitl gazebo_solo
```
Fourth terminal:
```
cd ~/SITL/polardrone/src/packages/script
python GNC.py
```

