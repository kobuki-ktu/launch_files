ros2 launch kobuki_node kobuki_node-launch.py &
ros2 launch velocity_mux/cmd_vel_mux-launch.py &
ros2 launch velocity_smoothers/velocity_smoother-launch.py &
# ros2 launch kobuki_safety_controller safety_controller-launch.py &

cleanup() {
    jobs -p | xargs -r kill
    exit 0
}

trap cleanup SIGINT

wait
