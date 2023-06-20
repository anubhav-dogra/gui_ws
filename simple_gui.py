import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Bool
from kivymd.app import MDApp
from kivy.lang import Builder


class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.screen = Builder.load_file('/home/terabotics/gui_ws/src/asset/ros_gui.kv')
        # can add more 
        self.screen = Builder.load_file('/home/terabotics/gui_ws/src/asset/simple_gui2.kv')


    def build(self):
        return self.screen
    
    # def my_function(self, *args):
    #     print("button_press")

    #     self.screen.ids.my_label.text="button pressed"

    #     msg=True
    #     pub.publish(msg)

    # def slider_func(self, slider_value):
    #     msg = int(slider_value)
    #     slider_pub.publish(msg)


if __name__ == '__main__':
    rospy.init_node("simple_gui", anonymous=True)
    # pub  = rospy.Publisher('/button', Bool, queue_size=1) 
    # slider_pub  = rospy.Publisher('/slider', Int8, queue_size=1) 
    TutorialApp().run()
 