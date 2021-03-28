import kivy

from kivy.app import App
from kivy.uix.widget import Widget 
import __init__ as hvn

#baseGen = {'name': "", 'race': "",
#           'gender': "", 'profession': "",
#           'health': "", 'ac': "",
#           'str': "", 'dex': "", 'con': "",
#           'int': "", 'wis': "", 'cha': "",
#           'saves': "", 'skills': "",
#           'features': "", 'attack': "",
#           'treasure': "", 'phys': "",
#           'traits': ""}


class HVNLayout(Widget): 
    def optBtn(self):
       print("hello") 

    def genBtn(self):
        print("Bye")
  
class HVNApp(App):
    def build(self):
        return HVNLayout() 


  
if __name__ == '__main__':
    HVNApp().run()
