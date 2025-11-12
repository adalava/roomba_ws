from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():  
#    remappings = [
#          ('/myRobot/cmd_vel', '/cmd_vel')]
    
    return LaunchDescription([
        #Node(
        #    package='tf2_ros',
        #    executable='static_transform_publisher',
        #    arguments=[
        #        '--x', '0.06', '--y', '0.0', '--z', '0.16',
        #        '--yaw', '0.0', '--pitch', '0.0', '--roll',
        #        '0.0', '--frame-id', 'base_footprint', '--child-frame-id', 'laser']
        #    ),
        #Node(
        #    package='robot_localization',
        #    executable='ekf_node',
        #    name='ekf_filter_node',
        #    output='screen',
        #    parameters=['config/ekf.yaml'],
        #   ),        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('slam_toolbox'),
                    'launch',
                    'online_sync_launch.py'
                ])
            ]),
            launch_arguments={
                'slam_params_file': '/home/pi/ros2_ws/config/mapper_params_online_async.yaml'
            }.items()
        )
    ])
