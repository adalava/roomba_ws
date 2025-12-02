from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    return LaunchDescription([
       Node(
            name='rplidar_composition',
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB1',
                'serial_baudrate': 115200,  # A1 / A2
                # 'serial_baudrate': 256000, # A3
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
            }],
        ),
#        Node(
#            package='tf2_ros',
#            executable='static_transform_publisher',
#            output='screen',
#            arguments=["0", "-0.06", "0.15", "0", "0", "0", "base_link", "laser"]
#            ),
#        Node(
#            package='tf2_ros',
#            executable='static_transform_publisher',
#            output='screen',
#            arguments=["0", "0", "0", "0", "0", "0", "base_footprint", "base_link"])


    ])
