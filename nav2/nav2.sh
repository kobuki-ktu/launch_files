ros2 launch navigation_launch.py params_file:="/home/pi/launch/nav2/nav2_params.yaml"

cleanup() {
    jobs -p | xargs -r kill
    exit 0
}

trap cleanup SIGINT

wait
