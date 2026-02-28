# Launch rplidar
ros2 launch rplidar_ros rplidar.launch.py

cleanup() {
    jobs -p | xargs -r kill
    exit 0
}

trap cleanup SIGINT

wait
