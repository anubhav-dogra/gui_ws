#!/usr/bin/env python3
import rospy
import roslaunch
from kivymd.uix.snackbar import Snackbar

def callback(button):
    text = button.text if button.text else "delete"
    Snackbar(text=text).open()


def launch_robot(self):
    global robot
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/iiwa_ros/iiwa_gazebo/launch/iiwa_gazebo.launch",'model:=iiwa14']
    roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]
    robot = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    robot.start()
    rospy.loginfo("robot started")
    # return(robot)

def launch_camera(self, *args):
    global camera
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/cam_viz.launch"]
    roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]
    camera = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    camera.start()
    rospy.loginfo("camera started")
    # return(camera)

def launch_detection(self):
    global markers
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/detection.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    markers = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    markers.start()
    rospy.loginfo("marker started")
    # return(markers)

def launch_wrench(self):
    global wrenches
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/wrench_info.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    wrenches = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    wrenches.start()
    rospy.loginfo("Wrench info ON")
    # return(robot)

def kill_robot(self, *args):
        robot.shutdown()

def kill_camera(self, *args):
        camera.shutdown()

def kill_marker(self, *args):
        markers.shutdown()

def kill_wrench(self, *args):
        wrenches.shutdown()


