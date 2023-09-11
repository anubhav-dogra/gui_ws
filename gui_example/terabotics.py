# ! / usr / bin / env python3
import roslaunch
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
        root = BoxLayout(orientation='vertical', spacing=4)
        layout = DivideLayout(2, orientation='horizontal')
        
        button_layout1 = GridLayout(cols=2)
        # button_layout1.add_widget(Open())
        button_layout1.add_widget(M_Detection())
        button_layout1.add_widget(Kill_Marker())
        button_layout1.add_widget(Get_Wrench())
        button_layout1.add_widget(Kill_Wrench())
        button_layout1.add_widget(Init_Motion())
        button_layout1.add_widget(Kill_Motion())
        button_layout1.add_widget(Send_Target())
        button_layout1.add_widget(Kill_Target())
        button_layout1.add_widget(Force_Controller())
        button_layout1.add_widget(Kill_Force())
        # button_layout1.add_widget(Signal())
        button_layout2 = GridLayout(cols=2)
        button_layout2.add_widget(Home_Pose())
        

        layout.add_widget_to_layout(DivideLayout(1, orientation='vertical'),0)
        left = layout.get_widget(0)
        left.add_widget_to_layout(button_layout1, 0)

        layout.add_widget_to_layout(DivideLayout(2, orientation='vertical'),1)
        right = layout.get_widget(1)
        right.add_widget_to_layout(button_layout2, 0)
        
        # right.add_widget_to_layout(button_layout2, 1)
        # center = layout.get_widget(1)
        # right = layout1.get_widget(1)
        # right.add_widget_to_layout(button_layout2, 0)


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