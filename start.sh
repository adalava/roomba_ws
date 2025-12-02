#!/bin/bash

PWD=$(pwd)

cd ~/roomba_ws

tmux new -d -s roomba \
	bash -ilc 'source install/setup.bash && ros2 launch launch/create_2.launch'

tmux new -d -s roomba_description \
	bash -ilc 'source install/setup.bash && ros2 launch create_description create_2.launch'

#tmux new -d -s dualshock \
#	bash -ilc "ros2 launch launch/teleop-launch.py config_filepath:=${PWD}/config/ps5.config.yaml"

tmux new -d -s rplidar \
	bash -ilc 'ros2 launch launch/rplidar.launch.py'

tmux new -d -s lidar_odom \
	bash -ilc 'source install/setup.bash && ros2 launch launch/rf2o_laser_odometry.launch.py'

tmux new -d -s tf2s \
	bash -ilc 'source install/setup.bash && ros2 launch launch/tf2s.launch.py'

#tmux new -d -s localization \
#	bash -ilc 'ros2 launch launch/ekf.launch.py'

tmux new -d -s slamtoolbox \
	bash -ilc 'ros2 launch launch/slam.launch.py'

#tmux new -d -s camera \
#	bash -ilc 'source install/setup.bash && ros2 launch launch/rs_launch.py config_file:="config/rs_L515.yaml" camera_namespace:="L515" '

tmux new -d -s nav2 \
	bash -ilc 'ros2 launch nav2_bringup navigation_launch.py params_file:=config/nav2_params.yaml'

#tmux new -d -s camera bash -ilc 'ros2 run v4l2_camera v4l2_camera_node --ros-args -p output_encoding:=yuv422_yuy2 -p qos_overrides./image_raw.publisher.reliability:=best_effort'


