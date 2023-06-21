#!/usr/bin/env python3
from kivy.uix.button import Button 
from button_callbacks import *

class MoveTo(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Move_to"
        self.font_size = "20sp"
        self.bind(on_press=callback)

class Open(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Open"
        self.font_size = "20sp"
        self.bind(on_press=callback)

class Close(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Close"
        self.font_size = "20sp"
        self.bind(on_press=callback)

class Robot_start(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Launch Robot"
        self.font_size = "20sp"
        self.bind(on_press=launch_robot)

class Cam_start(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,1,1)
        self.text = "Launch Cam"
        self.font_size = "20sp"
        self.bind(on_press=launch_camera)

class KillRobot(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,0,1)
        self.text = "Kill Robot"
        self.font_size = "20sp"
        self.bind(on_press=kill_robot)

class KillCam(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (1,0,0,1)
        self.text = "Kill Cam"
        self.font_size = "20sp"
        self.bind(on_press=kill_camera)