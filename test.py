import roslaunch
import rospy

rospy.init_node('test', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
cli_args = ["/home/terabotics/stuff_ws/src/iiwa_ros/iiwa_gazebo/launch/iiwa_gazebo.launch",'model:=iiwa14']
roslaunch_args = cli_args[1:]
roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]

parent = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
parent.start()
rospy.loginfo("started")

rospy.sleep(10)
# 3 seconds later
parent.shutdown()