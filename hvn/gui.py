from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import __init__ as hvn


classes = hvn.get_classes()
races = hvn.get_races()
genders = {"Male", "Female"}


class baseGen:
    power_score = -1
    race = ""
    gender = ""
    profession = ""
    char_class = ""
    profession = ""
    level = 0
    name = ""
    saves = {}
    skills = {}
    abiliity_score = {}


race_dropdown = DropDown()
gender_dropdown = DropDown()
char_class_dropdown = DropDown()
pw_score_dropdown = DropDown()
race_widget = Button(text='Race', size_hint=(None, None),
                     size=(200, 50), pos_hint=({'x': .4, 'y': .7}))
gender_widget = Button(text='Gender', size_hint=(None, None),
                       size=(200, 50), pos_hint=({'x': .4, 'y': .6}))
char_class_widget = Button(text='Class', size_hint=(None, None),
                           size=(200, 50), pos_hint=({'x': .4, 'y': .5}))
pw_score_widget = Button(text='Power Score', size_hint=(None, None),
                         size=(200, 50), pos_hint=({'x': .4, 'y': .8}))

for index in range(3, 19):
    btn = Button(text='Power Score %d' % index, size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: pw_score_dropdown.select(btn.text))
    pw_score_dropdown.add_widget(btn)


pw_score_widget.bind(on_release=pw_score_dropdown.open)

for race in races:
    btn = Button(text=race, size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: race_dropdown.select(btn.text))
    race_dropdown.add_widget(btn)

race_widget.bind(on_release=race_dropdown.open)


for gender in genders:
    btn = Button(text=gender, size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: gender_dropdown.select(btn.text))
    gender_dropdown.add_widget(btn)

gender_widget.bind(on_release=gender_dropdown.open)

for char_class in classes:
    btn = Button(text=char_class, size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: char_class_dropdown.select(btn.text))
    char_class_dropdown.add_widget(btn)

char_class_widget.bind(on_release=char_class_dropdown.open)


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
    baseGen.abiliity_score = hvn.generate_ability_scores(baseGen.race,
                                                         baseGen.char_class)
    baseGen.saves = hvn.generate_saves(baseGen.level, baseGen.char_class,
                                       baseGen.abiliity_score[1])
    baseGen.skills = hvn.generate_skills(baseGen.level, baseGen.char_class,
                                         baseGen.abiliity_score[1])

    # this is a bad way to reset it, but for now it works
    baseGen.power_score = -1
    baseGen.race = ""
    baseGen.gender = ""
    baseGen.profession = ""
    baseGen.char_class = ""
    baseGen.profession = ""
    baseGen.level = 0
    baseGen.name = ""
    baseGen.saves = {}
    baseGen.skills = {}
    baseGen.abiliity_score = {}


class HVNLayout(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        pass


class HVNOption(Screen):
    def __init__(self, **kwargs):
        super(HVNOption, self).__init__(**kwargs)
        self.add_widget(pw_score_widget)
        self.add_widget(race_widget)
        self.add_widget(gender_widget)
        self.add_widget(char_class_widget)

    def genBtn(self):
        gen()

    def optBtn(self):
        pass

    def abScore(self):
        pass

    def profession(self):
        baseGen.profession = self.profession.text
        print(baseGen.profession)


class HVNGenerate(Screen):
    def genBtn(self):
        gen()

    def optBtn(self):
        pass


class HVNApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HVNLayout(name='layout'))
        sm.add_widget(HVNGenerate(name='generate'))
        sm.add_widget(HVNOption(name='option'))

        return sm


if __name__ == '__main__':
    HVNApp().run()
