from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import __init__ as hvn


class baseGen:
    power_score = -1
    race = ""
    gender = ""
    profession = ""
    char_class = ""
    profession = ""
    level = 0
    name = ""


class optGen:
    power_score = -1
    race = ""
    gender = ""
    profession = "" 
    charClass = ""  
    profession = ""

dropdown = DropDown()
pwScore = Button(text='Power Score', size_hint=(None, None))

# this function really needs to be refactored, but for now it works
def gen():
    if baseGen.power_score == -1:
        baseGen.power_score = hvn.generate_power_score()
    if baseGen.race == "":
        baseGen.race = hvn.generate_race()
    if baseGen.gender == "":
        baseGen.gender = hvn.generate_gender()
    if baseGen.profession == "":
        baseGen.profession = hvn.generate_profession(baseGen.power_score)
    if baseGen.char_class == "":
        baseGen.char_class = hvn.generate_class()

    baseGen.name = hvn.generate_full_name(baseGen.race, baseGen.gender)
    baseGen.level = hvn.generate_level(baseGen.power_score)

    #this is a bad way to reset it, but for now it works
    baseGen.power_score = -1
    baseGen.race = ""
    baseGen.gender = ""
    baseGen.profession = ""
    baseGen.char_class = ""
    baseGen.profession = ""
    baseGen.level = 0
    baseGen.name = ""


def opt(self):
    for index in range(10):
        btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)

    pwScore.bind(on_release=dropdown.open)


class HVNLayout(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        opt(self)


class HVNOption(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        pass

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

        return sm


if __name__ == '__main__':
    HVNApp().run()
