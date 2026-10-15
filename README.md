# Agri-Logistix

## Project Overview
Agri-Logistix is a ROS 2 and Gazebo simulation prototype for monitoring the transport of perishable goods.

## Features
- Simulated cargo temperature and humidity readings
- Cargo door status monitoring
- Simulated battery monitoring
- Alerts for high temperature, low battery and an open door
- Gazebo vehicle simulation with movement commands

## Technologies
- ROS 2 Lyrical
- Gazebo Sim
- Python
- Ubuntu on WSL2

## Build
Run these commands from the workspace:

    source /opt/ros/lyrical/setup.bash
    cd ~/agri_logistix_ws
    colcon build --packages-select agri_logistix_sim --symlink-install
    source install/setup.bash

## Run Sensors and Alerts

    source /opt/ros/lyrical/setup.bash
    source ~/agri_logistix_ws/install/setup.bash
    ros2 launch agri_logistix_sim agri_logistix.launch.py

Press Ctrl+C to stop the nodes.

## Run Gazebo

    source /opt/ros/lyrical/setup.bash
    ros2 launch ros_gz_sim gz_sim.launch.py gz_args:="-r empty.sdf"

In another terminal, spawn the vehicle:

    ros2 run ros_gz_sim create -world empty -file /opt/ros/lyrical/share/ros_gz_sim_demos/models/vehicle/model.sdf -name agri_vehicle -x 0 -y 0 -z 0.5

## Limitations
Sensor values are simulated. Physical sensors, GPS tracking, a live dashboard and hardware integration are not yet implemented.

## Project Status
This is an academic prototype demonstrating simulated cargo monitoring, alerts and a movable Gazebo vehicle.
