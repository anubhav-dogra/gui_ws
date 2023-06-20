# ! / usr / bin / env python3
import roslaunch
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.snackbar.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from items.divide_layout import DivideLayout
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
        menu_items = [
            {
                "viewclass": "OneLinelistItem",
                "text": "Open",
                "height": dp(56)
                "on_release": lambda x = "Open":self.menu_callback(x)

            },
            {
                "viewclass": "OneLinelistItem",
                "text": "Save",
                "height": dp(56)
                "on_release": lambda x = "Save":self.menu_callback(x)
            }
        ]
        self.menu=MDDropdownMenu(
            items=menu_items,
            width_mult=4
        )

        toolbar=MDToolbar(title="GUI_Created_with_DSL")
        toolbar.left_action_items = [["menu", lambda x:self.open_menu(x)]]

        layout.add_widget(toolbar)
        button_layout1 = GridLayout(cols=3)
        button_layout1.add_widget(MoveTo())
        button_layout1.add_widget(ViaPoint())
        button_layout1.add_widget(Open())
        button_layout1.add_widget(Close())
        button_layout1.add_widget(Test_iiwa())
        