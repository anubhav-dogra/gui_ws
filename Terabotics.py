import rospy
import roslaunch
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int8
from std_msgs.msg import Bool

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class TeraboticsApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('/home/terabotics/gui_ws/asset/terabotics.kv')
        # can add more 
        # self.screen = Builder.load_file('/home/terabotics/gui_ws/src/asset/simple_gui2.kv')

    def build(self):
        # self.theme_cls.theme_style="Dark"
        # self.theme_cls.primary_palette="Orange"

        return self.screen

    def home_position(self,*args):
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

    def switch_detection(self,switchObject,switchValue):
        if (switchValue):
            uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
            roslaunch.configure_logging(uuid)
            cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/one_in_all.launch"]
            # roslaunch_args = cli_args[1:]
            roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
            self.markers = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
            self.markers.start()
            rospy.loginfo("Marker Detection/Pose Estimation// Transformation all ok")
            # self.text = "Detecting Now"
            # return(markers)
        else:
            self.markers.shutdown()
        return(self.markers)
        
    def launch_detection(self,*args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/one_in_all.launch"]
        # roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
        self.markers = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.markers.start()
        rospy.loginfo("Marker Detection/Pose Estimation// Transformation all ok")
        # self.text = "Detecting Now"
        # return(markers)
        return(self.markers)

    def launch_wrench(self,*args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/get_wrench_sim.launch"]
        # roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
        self.wrenches = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.wrenches.start()
        rospy.loginfo("Wrench info ON")
        # tip_forces=True
        return(self.wrenches)

    def send_target_pose(self,*args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/send_target_pose.launch"]
        # roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
        self.target_pose = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.target_pose.start()
        rospy.loginfo("RObot in Motion")
        return(self.target_pose)

    def init_robot_motion(self,*args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/init_robot_motion.launch"]
        # roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
        self.move_ = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.move_.start()
        rospy.loginfo("Robot Ready to Send Target")
        self.text = "Robot Ready to Send Target"
        return(self.move_)

    def force_controller(self,*args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/force_controller.launch"]
        # roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0])]
        self.force_ = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.force_.start()
        rospy.loginfo("FORCE controller ACTIVE")
        # self.text = "Robot Ready to Send Target"
        return(self.force_)
  
    def kill_marker(self, *args):
            self.markers.shutdown()
            self.background_color = (1,0,0,1)

    def kill_wrench(self, *args):
            self.wrenches.shutdown()
            self.background_color = (1,0,0,1)

    def stop_target_pose(self, *args):
            self.target_pose.shutdown()
            self.background_color = (1,0,0,1)

    def stop_robot_motion(self, *args):
            self.move_.shutdown()
            self.background_color = (1,0,0,1)

    def kill_force(self, *args):
            self.force_.shutdown()
            self.background_color = (1,0,0,1)
        

if __name__ == '__main__':
    # rospy.init_node("terabotics_app", anonymous=True)
    # pub  = rospy.Publisher('/button', Bool, queue_size=1) 
    # slider_pub  = rospy.Publisher('/slider', Int8, queue_size=1) 
    TeraboticsApp().run()
 