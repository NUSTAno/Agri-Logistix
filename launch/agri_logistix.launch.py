from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='agri_logistix_sim',
            executable='cargo_sensor',
            name='cargo_sensor',
            output='screen'
        ),
        Node(
            package='agri_logistix_sim',
            executable='cargo_alerts',
            name='cargo_alerts',
            output='screen'
        ),
    ])
