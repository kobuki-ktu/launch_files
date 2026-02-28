import os

import ament_index_python.packages
import launch
import launch_ros.actions

import yaml


def generate_launch_description():
    share_dir = ament_index_python.packages.get_package_share_directory('cmd_vel_mux')
    params_file = '/home/pi/launch/kobuki/velocity_mux/cmd_vel_mux_params.yaml'
    with open(params_file, 'r') as f:
        params = yaml.safe_load(f)['cmd_vel_mux']['ros__parameters']

    cmd_vel_mux_node = launch_ros.actions.Node(
        package='cmd_vel_mux',
        executable='cmd_vel_mux_node',
        output='both',
        parameters=[params]
    )

    return launch.LaunchDescription([cmd_vel_mux_node])
