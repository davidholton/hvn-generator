from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
# import __init__ as hvn

# baseGen = {'name': "", 'race': "",
#           'gender': "", 'profession': "",
#           'health': "", 'ac': "",
#           'str': "", 'dex': "", 'con': "",
#           'int': "", 'wis': "", 'cha': "",
#           'saves': "", 'skills': "",
#           'features': "", 'attack': "",
#           'treasure': "", 'phys': "",
#           'traits': ""}

def gen():
    print('hello')


def opt():
    print('bye')

class HVNLayout(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt()


class HVNOption(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt()



class HVNGenerate(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt()



class HVNApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HVNLayout(name='layout'))
        sm.add_widget(HVNGenerate(name='generate'))
        sm.add_widget(HVNOption(name='option'))

        # return HVNLayout()
        return sm


if __name__ == '__main__':
    HVNApp().run()
