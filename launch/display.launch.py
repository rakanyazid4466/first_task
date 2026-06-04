import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    # 1. Locate our package files in the system
    pkg_description = get_package_share_directory('first_task')
    xacro_file = os.path.join(pkg_description, 'urdf', 'robot.urdf.xacro')
    
    # 2. Process the Xacro file into raw URDF XML text
    robot_description_raw = xacro.process_file(xacro_file).toxml()

    # 3. Configure the robot_state_publisher node
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description_raw,
            'use_sim_time': False
        }]
    )

    # 4. Configure the joint_state_publisher_gui node (adds sliders to rotate your wheels)
    node_joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # 5. Configure RViz2
    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        node_robot_state_publisher,
        node_joint_state_publisher_gui,
        node_rviz
    ])