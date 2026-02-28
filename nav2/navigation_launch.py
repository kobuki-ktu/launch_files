import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Path Setup
    # Change 'nav2_bringup' to your own package name if this file is in your workspace
    bringup_dir = get_package_share_directory('nav2_bringup')
    
    # 2. Launch Configurations
    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')
    autostart = LaunchConfiguration('autostart')

    # 3. Nodes to manage via Lifecycle (The 'Soldier' list)
    # MUST match the 'name' of the nodes launched below
    lifecycle_nodes = [
        'controller_server', 
        'smoother_server', 
        'planner_server', 
        'behavior_server', 
        'bt_navigator', 
        'waypoint_follower'
    ]

    # 4. Standard Remappings
    remappings = [('/tf', 'tf'), ('/tf_static', 'tf_static')]

    return LaunchDescription([
        # Set logging to unbuffered to see errors immediately
        SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'),

        DeclareLaunchArgument('use_sim_time', default_value='false'),
        DeclareLaunchArgument('autostart', default_value='true'),
        DeclareLaunchArgument('params_file', 
            default_value=os.path.join(bringup_dir, 'params', 'nav2_params.yaml')),

        # Controller Server
        Node(
            package='nav2_controller',
            executable='controller_server',
            output='screen',
            parameters=[params_file, {'use_sim_time': use_sim_time}],
            remappings=remappings + [('cmd_vel', 'cmd_vel_raw/navigation')]
        ),

        # Smoother Server (The one causing the previous hang)
        Node(
            package='nav2_smoother',
            executable='smoother_server',
            name='smoother_server',
            output='screen',
            parameters=[params_file, {'use_sim_time': use_sim_time}],
            remappings=remappings
        ),

        # Planner Server
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[params_file, {'use_sim_time': use_sim_time}],
            remappings=remappings
        ),

        # Behavior Tree Navigator
        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[params_file, {'use_sim_time': use_sim_time}],
            remappings=remappings
        ),

        # Behavior Server (Spin, Backup, etc.)
        Node(
            package='nav2_behaviors',
            executable='behavior_server',
            name='behavior_server',
            output='screen',
            parameters=[params_file, {'use_sim_time': use_sim_time}],
            remappings=remappings + [('cmd_vel', 'cmd_vel_raw/navigation')]
        ),

        # Waypoint Follower
        Node(
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            name='waypoint_follower',
            output='screen',
            parameters=[params_file, {'use_sim_time': use_sim_time}],
            remappings=remappings
        ),

        # Lifecycle Manager
        # It won't finish starting until ALL nodes in 'lifecycle_nodes' are running
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time,
                         'autostart': autostart,
                         'node_names': lifecycle_nodes}]
        ),
    ])
