cd kobuki
./kobuki.sh &
cd ..

sleep 3
cd slam
ros2 launch nav2.launch.py &
./tf.sh &
cd ..

sleep 3
cd nav2
./nav2.sh &
cd ..

sleep 3
cd slam
nav2.launch.py &
cd ..

cd teleop
./joystick.sh &
cd ..

cleanup() {
    jobs -p | xargs -r kill
    exit 0
}

trap cleanup SIGINT

wait
