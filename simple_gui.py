import rospy
import roslaunch
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int8
from std_msgs.msg import Bool

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager

pose_msg = PoseStamped()


class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('/home/terabotics/gui_ws/asset/ros_gui.kv')
        # can add more 
        # self.screen = Builder.load_file('/home/terabotics/gui_ws/src/asset/simple_gui2.kv')


    def build(self):
        # self.theme_cls.theme_style="Dark"
        # self.theme_cls.primary_palette="Orange"
        return self.screen
    
    def launch_robot(self, *args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        cli_args = ["/home/terabotics/stuff_ws/src/iiwa_ros/iiwa_gazebo/launch/iiwa_gazebo.launch",'model:=iiwa14']
        roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]

        self.robot = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.robot.start()
        rospy.loginfo("robot started")
        return(self.robot)

        # self.screen.ids.my_label.text="button pressed"

        # msg=True
        # pub.publish(msg)

    # def slider_func(self, slider_value):
    #     msg = int(slider_value)
    #     slider_pub.publish(msg)

    def launch_camera(self, *args):
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        # cli_args = ["/opt/ros/noetic/share/realsense2_camera/launch/rs_camera.launch",'align_depth:=true', 'filters:=pointcloud']
        cli_args = ["/home/terabotics/stuff_ws/src/tera_iiwa_ros/launch/cam_viz.launch"]
        roslaunch_args = cli_args[1:]
        roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)]
        self.camera = roslaunch.parent.ROSLaunchParent(uuid,roslaunch_file)
        self.camera.start()
        rospy.loginfo("camera started")
        return(self.camera)
    
    
    def kill_robot(self, *args):
        self.robot.shutdown()
    def kill_camera(self, *args):
        self.camera.shutdown()


    def update(x, y, z, xr, yr, zr, wr, tup):
        # self.condition.acquire()
        new_x = x   + tup[0]
        new_y = y   + tup[1]
        new_z = z   + tup[2]
        new_xr = xr + tup[3]
        new_yr = yr + tup[4]
        new_zr = zr + tup[5]
        new_wr = wr + tup[6]
        # Notify publish thread that we have a new message.
        # self.condition.notify()
        # self.condition.release()
        pose_msg.header.frame_id= "world"
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.pose.position.x = new_x
        pose_msg.pose.position.y = new_y
        pose_msg.pose.position.z = new_z
        pose_msg.pose.orientation.x = new_xr
        pose_msg.pose.orientation.y = new_yr
        pose_msg.pose.orientation.z = new_zr
        pose_msg.pose.orientation.w = new_wr

        return pose_msg


if __name__ == '__main__':
    rospy.init_node("simple_gui", anonymous=True)
    # pub  = rospy.Publisher('/button', Bool, queue_size=1) 
    # slider_pub  = rospy.Publisher('/slider', Int8, queue_size=1) 
    TutorialApp().run()
 