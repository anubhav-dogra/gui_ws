#!/usr/bin/env python
# import roslaunch
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.snackbar.snackbar import Snackbar
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivymd.uix import label
from kivymd.uix.list import OneLineListItem
from divide_layout import DivideLayout
from command_buttons import *
# from reference_buttons import *
# from items.programming_buttons import *
from robot_program import RobotItem , RobotProgram


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_menu(self,button):
        self.menu.caller = button
        self.menu.open()

    def open_robot_menu(self, button):
        self.robot_menu.caller = button
        self.robot_menu.open()
    
    def menu_callback(self, text_item):
        self.menu.dismiss()
        Snackbar(text=text_item).open()

    def build(self):
        root = BoxLayout(orientation='vertical', spacing=1)
        layout = DivideLayout(1, orientation='horizontal')
        # menu_items = [
        #             {
        #                 "viewclass": "OneLinelistItem",
        #                 "text": "Open",
        #                 "height": dp(56),
        #                 "on_release": lambda x = "Open":self.menu_callback(x)

        #             },
        #             {
        #                 "viewclass": "OneLinelistItem",
        #                 "text": "Save",
        #                 "height": dp(56),
        #                 "on_release": lambda x = "Save":self.menu_callback(x)
        #             }
        # ]

        # self.menu=MDDropdownMenu(
        #     items=menu_items,
        #     width_mult=4
        # )

        # toolbar=MDTopAppBar(title="GUI")
        # toolbar.left_action_items = [["menu", lambda x:self.open_menu(x)]]

        # layout.add_widget(toolbar)
        # section1 = BoxLayout(orientation='horizontal',spacing=2)
        # layout.add_widget(section1)
        button_layout1 = GridLayout(cols=2)
        button_layout1.add_widget(Robot_start_sim())
        button_layout1.add_widget(KillRobotSim())
        button_layout1.add_widget(Robot_start())
        button_layout1.add_widget(KillRobot())
        button_layout1.add_widget(Cam_start())
        button_layout1.add_widget(KillCam())
        # button_layout1.add_widget(Open())
        # button_layout2 = GridLayout(cols=2)
        # button_layout2.add_widget(M_Detection())
        # button_layout2.add_widget(Kill_Marker())
        # button_layout2.add_widget(Get_Wrench())
        # button_layout2.add_widget(Kill_Wrench())
        

        layout.add_widget_to_layout(DivideLayout(1, orientation='vertical'),0)
        left = layout.get_widget(0)
        left.add_widget_to_layout(button_layout1, 0)
        # left.add_widget_to_layout(button_layout2, 1)
        # center = layout.get_widget(1)
        # right = layout.get_widget(2)


        # robot_program = RobotProgram("Robot")
        # for i in range(5):
        #     robot_program.add_item(RobotItem(
        #         robot_program, text=f"command_{i}"
        #     ))
        # layout.add_widget_to_layout(robot_program, 1)
        # root.add_widget(toolbar)
        root.add_widget(layout)
        return root


MainApp().run()