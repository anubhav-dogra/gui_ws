# ! / usr / bin / env python3
import roslaunch
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.snackbar.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
# from items.divide_layout import DivideLayout
# from items.command_buttons import *
# from items.reference_buttons import *
# from items.programming_buttons import *
# from items.robot_program import RobotItem , RobotProgram


class MyApp(MDApp):
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
        root = BoxLayout(orientation='vertical', spacing=2)
        layout = DivideLayout(2, orientation='horizontal')
    
