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
        return Background()

    #def build(self):
    #    clearbtn = Button(text='generate')
    #    return clearbtn 


if __name__ == '__main__':
    Hvn_Gui().run()
