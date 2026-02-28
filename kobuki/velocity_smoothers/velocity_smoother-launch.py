# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Open Source Robotics Foundation, Inc.
#
# Software License Agreement (BSD License 2.0)
#   https://raw.githubusercontent.com/kobuki-base/velocity_smoother/license/LICENSE

"""Launch the velocity smoother node with default configuration."""

import os

import ament_index_python.packages
import launch
import launch_ros.actions

import yaml


def generate_launch_description():
    params_file_keyop = '/home/pi/launch/kobuki/velocity_smoothers/keyop_velocity_smoother_params.yaml'
    with open(params_file_keyop, 'r') as f:
        params = yaml.safe_load(f)['kobuki_velocity_smoother']['ros__parameters']
    velocity_smoother_node_keyop = launch_ros.actions.Node(
        package='kobuki_velocity_smoother',
        remappings=[
            ('/kobuki_velocity_smoother_keyop/input', '/cmd_vel_raw/keyop'),
            ('/kobuki_velocity_smoother_keyop/smoothed', '/cmd_vel_mux/keyop'),
            ('/kobuki_velocity_smoother_keyop/feedback/cmd_vel', '/cmd_vel'),
            ('/kobuki_velocity_smoother_keyop/feedback/odometry', '/odom'),
        ],
        executable='velocity_smoother',
        name='kobuki_velocity_smoother_keyop',
        output='both',
        parameters=[params])


    params_file_navigation = '/home/pi/launch/kobuki/velocity_smoothers/navigation_velocity_smoother_params.yaml'
    with open(params_file_navigation, 'r') as f:
        params = yaml.safe_load(f)['kobuki_velocity_smoother']['ros__parameters']
    velocity_smoother_node_navigation = launch_ros.actions.Node(
        package='kobuki_velocity_smoother',
        remappings=[
            ('/kobuki_velocity_smoother_navigation/input', '/cmd_vel_raw/navigation'),
            ('/kobuki_velocity_smoother_navigation/smoothed', '/cmd_vel_mux/navigation'),
            ('/kobuki_velocity_smoother_navigation/feedback/cmd_vel', '/cmd_vel'),
            ('/kobuki_velocity_smoother_navigation/feedback/odometry', '/odom'),
        ],
        executable='velocity_smoother',
        name='kobuki_velocity_smoother_navigation',
        output='both',
        parameters=[params])


    params_file_joystick = '/home/pi/launch/kobuki/velocity_smoothers/joystick_velocity_smoother_params.yaml'
    with open(params_file_navigation, 'r') as f:
        params = yaml.safe_load(f)['kobuki_velocity_smoother']['ros__parameters']
    velocity_smoother_node_joystick= launch_ros.actions.Node(
        package='kobuki_velocity_smoother',
        remappings=[
            ('/kobuki_velocity_smoother_joystick/input', '/cmd_vel_raw/joystick'),
            ('/kobuki_velocity_smoother_joystick/smoothed', '/cmd_vel_mux/joystick'),
            ('/kobuki_velocity_smoother_joystick/feedback/cmd_vel', '/cmd_vel'),
            ('/kobuki_velocity_smoother_joystick/feedback/odometry', '/odom'),
        ],
        executable='velocity_smoother',
        name='kobuki_velocity_smoother_joystick',
        output='both',
        parameters=[params])

    return launch.LaunchDescription([velocity_smoother_node_keyop, velocity_smoother_node_navigation, velocity_smoother_node_joystick])
