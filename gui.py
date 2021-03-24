from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

baseGen = {'name': "", 'race': "", \
        'gender': "", 'profession': "", \
        'health': "", 'ac': "", \
        'str': "", 'dex': "", 'con': "", \
        'int': "", 'wis': "", 'cha': "", \
        'saves': "", 'skills': "", \
        'features': "", 'attack': "", \
        'treasure': "", 'phys': "", \
        'traits': ""}

class HVNLayout(FloatLayout):
    pass

class HVNApp(App):
    def build(self):
        parent = Widget()
        genButt = Button(text="Generate", size= (200, 100))
        optButt = Button(text="Options", pos=(Window.width - 100, Window.height - 100))
        background = HVNLayout()
        background.size = Window.size
        genButt.bind(on_release=self.generate)
        optButt.bind(on_release=self.genOptions)
        parent.add_widget(background)
        parent.add_widget(genButt)
        parent.add_widget(optButt)
        return parent


    def generate(self, obj):
        generation()

    def genOptions(self, obj):
        optionGeneration()
    

def generation():
    print(baseGen.values())

def optionGeneration():
    pass

if __name__ == "__main__":
    HVNApp().run()
