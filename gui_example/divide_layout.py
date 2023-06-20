# ! / usr / bin / env python3
from kivy.uix.boxlayout import BoxLayout

class DivideLayout(BoxLayout):
    def __init__(self, number_of_parts, **kwargs):
        super().__init__(**kwargs)
        self.widgets =[None]*number_of_parts
        self.number_of_parts=number_of_parts
        self.spacing=2

    def add_widget_to_layout(self, widget, index):
        if(self.number_of_parts>index):
            self.widgets[index]=widget
            self.__update_widgets()
        else:
            raise IndexError('outside_of_range')
        
    def remove_widget_from_layout(self, index):
        self.widgets[index]=None
        self.__update_widgets()

    def __update_widgets(self):
        self.clear_widgets()
        for i in range(0,self.number_of_parts):
            if(self.widgets[i] != None):
                self.add_widget(self.widgets[i])
            else:
                self.add_widget(BoxLayout())
    
    def get_widget(self,index):
        return self.widgets[index]