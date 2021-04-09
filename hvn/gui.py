from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
import __init__ as hvn

# ----------------------------------------------- #

# get all the available options
classes = hvn.get_classes()
races = hvn.get_races()
professions = hvn.get_professions()
genders = {"male", "female"}


# this class holds all the values that the program needs to display
class baseGen:
    power_score = 0
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


class baseOpt:
    pw_score = 0
    race = ""
    gender = ""
    profession = ""
    char_class = ""


# creating dropdowns for the options menu
race_dropdown = DropDown()
gender_dropdown = DropDown()
char_class_dropdown = DropDown()
pw_score_dropdown = DropDown()
profession_dropdown = DropDown()

# The buttons that will open the dropdown
race_widget = Button(text='Race', size_hint=(None, None),
                     size=(200, 50), pos_hint=({'x': .4, 'y': .6}))
gender_widget = Button(text='Gender', size_hint=(None, None),
                       size=(200, 50), pos_hint=({'x': .4, 'y': .5}))
char_class_widget = Button(text='Class', size_hint=(None, None),
                           size=(200, 50), pos_hint=({'x': .4, 'y': .4}))
pw_score_widget = Button(text='Power Score', size_hint=(None, None),
                         size=(200, 50), pos_hint=({'x': .4, 'y': .7}))
profession_widget = Button(text='Professions', size_hint=(None, None),
                           size=(200, 50), pos_hint=({'x': .4, 'y': .3}))

# creating labels for all of the options
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

for prof in professions:
    btn = Button(text=prof, size_hint_y=None, height=50)
    btn.bind(on_release=lambda btn: profession_dropdown.select(btn.text))
    profession_dropdown.add_widget(btn)

profession_widget.bind(on_release=profession_dropdown.open)


# get the values from the dropdown
def pw_btn(instance, value):
    data = value.split()
    baseOpt.pw_score = int(data[2])


def rc_btn(instance, value):
    baseOpt.race = value


def gn_btn(instance, value):
    baseOpt.gender = value


def cl_btn(instance, value):
    baseOpt.char_class = value


def pr_btn(instance, value):
    baseOpt.profession = value


# bind the dropdowns to call functions to get all the values
pw_score_dropdown.bind(on_select=lambda instance, x:
                       setattr(pw_score_widget, 'text', x))
pw_score_dropdown.bind(on_select=pw_btn)
race_dropdown.bind(on_select=lambda instance, x:
                   setattr(race_widget, 'text', x))
race_dropdown.bind(on_select=rc_btn)
gender_dropdown.bind(on_select=lambda instance, x:
                     setattr(gender_widget, 'text', x))
gender_dropdown.bind(on_select=gn_btn)
char_class_dropdown.bind(on_select=lambda instance, x:
                         setattr(char_class_widget, 'text', x))
char_class_dropdown.bind(on_select=cl_btn)
profession_dropdown.bind(on_select=lambda instance, x:
                         setattr(profession_widget, 'text', x))
profession_dropdown.bind(on_select=pr_btn)


# generating all the options that is required to be displayed.
# It takes options as opt that calls weather or not options have been selected
def gen(opt):
    if opt == "none":
        base_class()
    else:
        if baseOpt.pw_score == 0:
            baseGen.power_score = hvn.generate_power_score()
        else:
            baseGen.power_score = baseOpt.pw_score
        if baseOpt.race == "":
            baseGen.race = hvn.generate_race()
        else:
            baseGen.race = baseOpt.race
        if baseOpt.gender == "":
            baseGen.gender = hvn.generate_gender()
        else:
            baseGen.gender = baseOpt.gender
        if baseOpt.profession == "":
            baseGen.profession = hvn.generate_profession(baseGen.power_score)
        else:
            baseGen.profession = baseOpt.profession
        if baseOpt.char_class == "":
            baseGen.char_class = hvn.generate_class()
        else:
            baseGen.char_class = baseOpt.char_class

    name = hvn.generate_full_name(baseGen.race, baseGen.gender)
    baseGen.level = hvn.generate_level(baseGen.power_score)
    baseGen.abiliity_score = hvn.generate_ability_scores(baseGen.race,
                                                         baseGen.char_class)
    baseGen.saves = hvn.generate_saves(baseGen.level, baseGen.char_class,
                                       baseGen.abiliity_score[1])
    baseGen.skills = hvn.generate_skills(baseGen.level, baseGen.char_class,
                                         baseGen.abiliity_score[1])
    baseGen.name = name[0] + ' ' + name[1]

    # this is really dumb way to reset class
    baseOpt.pw_score = 0
    baseOpt.race = ""
    baseOpt.gender = ""
    baseOpt.char_class = ""
    baseOpt.profession = ""


# clear the data from class will be used for when the options are setup
def base_class():
    # this is a bad way to reset it, but for now it works
    baseGen.power_score = hvn.generate_power_score()
    baseGen.race = hvn.generate_race()
    baseGen.gender = hvn.generate_gender()
    baseGen.profession = hvn.generate_profession(baseGen.power_score)
    baseGen.char_class = hvn.generate_class()


# class for the first screen
class HVNLayout(Screen):
    def genBtn(self):
        gen("none")

    def optBtn(self):
        pass


# class for the options screen
class HVNOption(Screen):
    # this __init__ displays all of the option buttons
    def __init__(self, **kwargs):
        super(HVNOption, self).__init__(**kwargs)
        self.add_widget(pw_score_widget)
        self.add_widget(race_widget)
        self.add_widget(gender_widget)
        self.add_widget(char_class_widget)
        self.add_widget(profession_widget)

    def genBtn(self):
        gen("with_opt")

    def optBtn(self):
        pass


# class for the generated data page
class HVNGenerate(Screen):
    # display all of the result data
    def __init__(self, **kwargs):
        super(HVNGenerate, self).__init__(**kwargs)
        rc_label = Label(text=baseGen.race,
                         pos_hint=({'x': 0, 'y': 0.4}))
        lv_label = Label(text=str(baseGen.level),
                         pos_hint=({'x': 0, 'y': 0.35}))
        gn_label = Label(text=baseGen.gender,
                         pos_hint=({'x': 0, 'y': 0.3}))
        pr_label = Label(text=baseGen.profession,
                         pos_hint=({'x': 0, 'y': 0.25}))
        nm_label = Label(text=baseGen.name,
                         pos_hint=({'x': 0, 'y': 0.2}))
        cl_label = Label(text=baseGen.char_class,
                         pos_hint=({'x': 0, 'y': 0.15}))

        self.add_widget(rc_label)
        self.add_widget(lv_label)
        self.add_widget(gn_label)
        self.add_widget(pr_label)
        self.add_widget(nm_label)
        self.add_widget(cl_label)

    def genBtn(self):
        self.clear_widgets()
        self.__init__()
        gen("none")

    def optBtn(self):
        pass


# this is the main app that manages all the windows
class HVNApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HVNLayout(name='layout'))
        sm.add_widget(HVNGenerate(name='generate'))
        sm.add_widget(HVNOption(name='option'))

        return sm


if __name__ == '__main__':
    HVNApp().run()
