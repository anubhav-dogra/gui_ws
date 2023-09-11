#!/usr/bin/env python3
from kivy.uix.button import Button 
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRectangleFlatButton
from button_callbacks import *

# class MoveTo(Button):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.background_color = (1,0,1,1)
#         self.text = "Move_to"
#         self.font_size = "24sp"
#         self.bind(on_press=callback)

# class Open(Button):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.background_color = (1,0,1,1)
#         self.text = "Open"
#         self.font_size = "24sp"
#         self.bind(on_press=callback)

# class Close(Button):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.background_color = (1,0,1,1)
#         self.text = "Close"
#         self.font_size = "24sp"
#         self.bind(on_press=callback)
       

class Robot_start(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.95,0.5,0,1)
        self.text = "Launch Robot"
        self.font_size = "24sp"
        self.bind(on_press=launch_robot)

class Cam_start(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.65,0.65,0.65,1)
        self.text = "Launch Cam"
        self.font_size = "24sp"
        self.bind(on_press=launch_camera)

class M_Detection(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0.1,0.7,0,1)
        self.text = "Detect Marker"
        self.font_size = "24sp"
        self.bind(on_press=launch_detection)

class Get_Wrench(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Wrench Info"
        self.font_size = "24sp"
        self.bind(on_press=launch_wrench)

class Send_Target(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Send Target"
        self.font_size = "24sp"
        self.bind(on_press=send_target_pose)

class Init_Motion(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Robot Motion"
        self.font_size = "24sp"
        self.bind(on_press=init_robot_motion)

class Home_Pose(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0,0,0,1)
        self.text = "Home Pose"
        self.font_size = "24sp"
        self.bind(on_press=home_position)

class Force_Controller(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0,0,0,1)
        self.text = "Force Controller"
        self.font_size = "24sp"
        self.bind(on_press=force_controller)


#  #################### Killing Functions ##############
class KillRobot(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Robot"
        self.font_size = "24sp"
        self.bind(on_press=kill_robot)

class KillCam(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Cam"
        self.font_size = "24sp"
        self.bind(on_press=kill_camera)

class Kill_Marker(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Marker"
        self.font_size = "24sp"
        self.bind(on_press=kill_marker)

class Kill_Wrench(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Wrench"
        self.font_size = "24sp"
        self.bind(on_press=kill_wrench)

class Kill_Target(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Target sender"
        self.font_size = "24sp"
        self.bind(on_press=stop_target_pose)

class Kill_Motion(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Robot Motion"
        self.font_size = "24sp"
        self.bind(on_press=stop_robot_motion)

class Kill_Force(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (178.0/255.0,190.0/255.0, 181.0/255.0,1)
        self.text = "Kill Force"
        self.font_size = "24sp"
        self.bind(on_press=kill_force)