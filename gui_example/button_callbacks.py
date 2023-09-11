#!/usr/bin/env python3
import rospy
import roslaunch
from geometry_msgs.msg import PoseStamped
from kivymd.uix.snackbar import Snackbar
global tip_forces
tip_forces = False

def callback(button):
    text = button.text if button.text else "delete"
    Snackbar(text=text).open()     

def home_position(self):
    rospy.init_node("home_pose", anonymous=True)
    pub_home_pose =rospy.Publisher("/cartesian_trajectory_generator/new_goal", PoseStamped, queue_size=1 )
    home_pose = PoseStamped()
    home_pose.header.frame_id= "world"
    home_pose.header.stamp=rospy.Time.now()
    home_pose.pose.position.x= -0.62
    home_pose.pose.position.y= 0
    home_pose.pose.position.z= 0.2
    home_pose.pose.orientation.x = 0.7
    home_pose.pose.orientation.y = 0.7
    home_pose.pose.orientation.z = 0
    home_pose.pose.orientation.w = 0
    pub_home_pose.publish(home_pose)

def signal_on(self):
    if markers.start() == True:
        self.background_color = (0,1,0,1)  
    else:
        self.background_color = (1,0,0,1) 

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
    # self.background_color = (0,1,0,1)
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/one_in_all.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    markers = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    markers.start()
    rospy.loginfo("Marker Detection/Pose Estimation// Transformation all ok")
    # self.text = "Detecting Now"
    # return(markers)

def launch_wrench(self):
    global wrenches, tip_forces
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/get_wrench_sim.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    wrenches = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    wrenches.start()
    rospy.loginfo("Wrench info ON")
    tip_forces=True
    # return(robot)

def send_target_pose(self):
    global target_pose
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/send_target_pose.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    target_pose = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    target_pose.start()
    rospy.loginfo("RObot in Motion")
    # return(robot)

def init_robot_motion(self):
    global move_
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/init_robot_motion.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    move_ = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    move_.start()
    rospy.loginfo("Robot Ready to Send Target")
    self.text = "Robot Ready to Send Target"
    # return(robot)

def force_controller(self):
    global force_
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/force_controller.launch"]
    # roslaunch_args = cli_args[1:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
    force_ = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
    if tip_forces==True:
        force_.start()
        rospy.loginfo("FORCE controller ACTIVE")
    else:
         rospy.loginfo("NOPE TIP FORCES ARNT ACTIVE")
    # self.text = "Robot Ready to Send Target"
    # return(robot)
  
def kill_robot(self, *args):
        robot.shutdown()
        self.background_color = (1,0,0,1)

def kill_camera(self, *args):
        camera.shutdown()
        self.background_color = (1,0,0,1)

def kill_marker(self, *args):
        markers.shutdown()
        self.background_color = (1,0,0,1)

def kill_wrench(self, *args):
        wrenches.shutdown()
        self.background_color = (1,0,0,1)

def stop_target_pose(self, *args):
        target_pose.shutdown()
        self.background_color = (1,0,0,1)

def stop_robot_motion(self, *args):
        move_.shutdown()
        self.background_color = (1,0,0,1)

def kill_force(self, *args):
        force_.shutdown()
        self.background_color = (1,0,0,1)


