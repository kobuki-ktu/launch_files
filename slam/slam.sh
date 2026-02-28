ros2 launch slam_toolbox online_sync_launch.py &

cleanup() {
    jobs -p | xargs -r kill
    exit 0
}

trap cleanup SIGINT

wait
