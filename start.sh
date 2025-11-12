#!/bin/bash

#tmux new -d -s dualshock ros2 launch teleop_twist_joy teleop-launch.py joy_config:=ps5 stamped:=true
tmux new -d -s dualshock bash -ilc 'ros2 launch /home/pi/ros2_ws_roomba/launch/teleop-launch.py'
tmux new -d -s rplidar bash -ilc 'ros2 launch /home/pi/ros2_ws/launch/rplidar.launch.py'
tmux new -d -s lidar_odom bash -ilc 'cd ~/ros2_ws && source install/setup.bash && ros2 launch /home/pi/ros2_ws/launch/rf2o_laser_odometry.launch.py'

tmux new -d -s slamtoolbox bash -ilc 'cd ~/ros2_ws && ros2 launch launch/slam.launch.py'

#tmux new -d -s camera bash -ilc 'ros2 run v4l2_camera v4l2_camera_node --ros-args -p output_encoding:=yuv422_yuy2 -p qos_overrides./image_raw.publisher.reliability:=best_effort'


tmux new -d -s nav2 bash -ilc 'cd ~/ros2_ws && ros2 launch nav2_bringup navigation_launch.py params_file:=config/nav2_params.yaml'

sleep 20
tmux new -d -s roomba docker run --rm -it \
	--name roomba \
	--device=/dev/ttyROOMBA \
	--device=/dev/ttyRPLidar \
	-v ~/ros2_ws_roomba:/root/ros2_ws_roomba \
	adalava/ros-roomba \
	/root/ros2_ws_roomba/start_roomba.sh

