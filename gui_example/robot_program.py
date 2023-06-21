# ! / usr / bin / env python3
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button.button import MDIconButton
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.card.card import MDCardSwipeFrontBox , MDCardSwipeLayerBox
from kivymd.uix.list.list import OneLineListItem
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList
from button_callbacks import callback

class RobotProgram(BoxLayout):
    def __init__(self, title, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = '10dp'
        self.toolbar = MDTopAppBar(
            elevation=10,
            title=title,
            md_bg_color = (1,0,1,1)
        )

        self.scrollview = ScrollView(scroll_timeout=100)
        self.md_list = MDList(padding=0)
        self.scrollview.add_widget(self.md_list)
        self.add_widget(self.toolbar)
        self.add_widget(self.scrollview)

    def add_item(self, item):
        self.md_list.add_widget(item)

    def remove_item(self, item):
        self.md_list.remove_widget(item)



class RobotItem(MDCardSwipe):
    def __init__(self, robot_program, text, **kwargs):
        super().__init__(**kwargs)
        
        self.robot_program = robot_program
        self.layer_box = MDCardSwipeLayerBox(padding="8dp")
        self.delete_icon = MDIconButton(
            icon="trash-can",
            pos_hint={'center_y': .5},
            on_release= callback
        )
        self.layer_box.add_widget(self.delete_icon)
        self.front_box = MDCardSwipeFrontBox()
        self.content=OneLineListItem(
            text=text,
            _no_ripple_effect = True
        )

        self.front_box.add_widget(self.content)

        self.size_hint_y=None
        self.height=self.content.height

        self.add_widget(self.layer_box)
        self.add_widget(self.front_box)