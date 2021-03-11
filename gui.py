from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Background(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    pass

class Hvn_Gui(App):

    def build(self):
        btn = Button(text ="Generate", 
                   font_size ="20sp", 
                   background_color =(1, 1, 1, 1), 
                   color =(1, 1, 1, 1),  
                   size =(32, 32), 
                   size_hint =(.2, .2), 
                   pos =(300, 250))  
        return btn
        #return Background()


if __name__ == '__main__':
    Hvn_Gui().run()
