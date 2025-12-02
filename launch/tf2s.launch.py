import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                arguments=[
                    '--x', '-0.06', '--y', '0.0', '--z', '0.20',
                    '--yaw', '0.0', '--pitch', '0.0', '--roll',
                    '0.0', '--frame-id', 'base_footprint', '--child-frame-id', 'laser']
            ),

#            Node(
#                package='tf2_ros',
#                executable='static_transform_publisher',
#                arguments=[
#                    '--x', '0.0', '--y', '0.0', '--z', '0.0',
#                    '--yaw', '0.0', '--pitch', '0.0', '--roll',
#                    '0.0', '--frame-id', 'base_link', '--child-frame-id', 'base_footprint']
#            ),

#            Node(
#                package='tf2_ros',
#                executable='static_transform_publisher',
#                arguments=[
#                    '--x', '0.11', '--y', '0.0', '--z', '0.12',
#                    '--yaw', '0.0', '--pitch', '0.0', '--roll',
#                    '0.0', '--frame-id', 'base_link', '--child-frame-id', 'camera_link']
#            ),

#            Node(
#                package='tf2_ros',
#                executable='static_transform_publisher',
#                arguments=[
#                    '--x', '0.0', '--y', '0.0', '--z', '0.0',
#                    '--yaw', '0.0', '--pitch', '0.0', '--roll',
#                    '0.0', '--frame-id', 'odom_lidar', '--child-frame-id', 'base_footprint']
#            ),

#            Node(
#                package='tf2_ros',
#                executable='static_transform_publisher',
#                arguments=[
#                    '--x', '0.0', '--y', '0.0', '--z', '0.0',
#                    '--yaw', '0.0', '--pitch', '0.0', '--roll',
#                    '0.0', '--frame-id', 'odom', '--child-frame-id', 'base_footprint']
#            ),


    ])
