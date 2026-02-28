ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link laser &

cleanup() {
    jobs -p | xargs -r kill
    exit 0
}

trap cleanup SIGINT

wait
