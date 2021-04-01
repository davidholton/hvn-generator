from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
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

dropdown = DropDown()
def gen():
    print('hello')


def opt(self):
    pwScore = Button(text='Power Score', size_hint=(None, None))
    for index in range(10):
        btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
    pwScore.bind(on_release=dropdown.open)
    self.add_widget(pwScore)

    print('bye')
    
class HVNLayout(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt(self)


class HVNOption(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt(self)

    def abScore(self):
        pass


class HVNGenerate(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt(self)



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
