from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
import __init__ as hvn
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
print(Window.size)

# ----------------------------------------------- #

# get all the available options
classes = hvn.get_classes()
races = hvn.get_races()
professions = hvn.get_professions()
genders = {"male", "female"}

#     fields = ["power_score", "level", "race", "gender", "class_name",
#              "first_name", "last_name", "full_name", "profession",
#              "abilities", "modifiers", "saving_throws", "skill_bonuses",
#              "equipment", "armor", "armor_class", "hit_dice", "hit_points",
#              "feature", "treasure"]

option_field = {}

# this is the generator
char = hvn.HVNGenerator()


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
    option_field['power_score'] = int(data[2])


def rc_btn(instance, value):
    option_field['race'] = value


def gn_btn(instance, value):
    option_field['gender'] = value


def cl_btn(instance, value):
    option_field['class_name'] = value


def pr_btn(instance, value):
    option_field['profession'] = value


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
def gen():
    char.set_custom_data(option_field)
    char.generate()
    print(char)
    option_field.clear()


# class for the first screen
class HVNLayout(Screen):
    def genBtn(self):
        gen()

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
        gen()

    def optBtn(self):
        pass


# class for the generated data page
class HVNGenerate(Screen):
    # display all of the result data
    gen()

    def __init__(self, **kwargs):
        super(HVNGenerate, self).__init__(**kwargs)

        stats = f"Stats\nLevel: {char.level}\n"
        stats += f"AC: {char.armor_class}\n"
        stats += f"HP: {char.hit_points}\n"
        stats += f"Hit: Dice {char.hit_dice}\n"

        personal_info = "Generated Personal Information\n"
        personal_info += f"Full Name: {char.first_name} {char.last_name}\n"
        personal_info += f"Gender: {char.gender}\n"
        personal_info += f"Race: {char.race}\n"
        personal_info += f"Class: {char.class_name}\n"
        personal_info += f"Profession: {char.profession}\n"

        save = "Saving Throws\n"
        for ability, score in char.saving_throws.items():
            save += ability + ' ' + str(score) + '\n'

        armor = "Generated Armor statistics\n"
        for ab, score in char.armor.items():
            armor += ab + ' ' + str(score) + '\n'

        skills = "Generated Skills\n"
        for item, score in char.skill_bonuses.items():
            skills += item + ' ' + str(score) + '\n'

        ab = "Abilities\n"
        for ability, score in char.abilities.items():
            ab += ability + ' ' + str(score) + '\n'

        treasure = "Generated Treasures "
        treasure += "High Value NPC\n"
        for tr in char.treasure:
            treasure += tr + '\n'

        on_person_wealth = "Wealth\n"
        for ow, amount in char.person_wealth.items():
            on_person_wealth += ow + ' ' + str(amount) + '\n'

        at_home_wealth = "At Home  Wealth\n"
        for ow, amount in char.home_wealth.items():
            at_home_wealth += ow + ' ' + str(amount) + '\n'

        physical_traits = "Generated Physical traits "
        physical_traits += "for the high valuable NPC(HVN):\n"
        for trait, value in char.physical_traits.items():
            if type(value) is dict:
                for x, v in value.items():
                    if v:
                        physical_traits += f"{x} scarring: {v}\n"
            elif value:
                physical_traits += f"{trait}: {value}\n"

        social_traits = "Social traits:\n"
        if char.social_traits["social"]:
            social_traits += f"social: {char.social_traits['social']}\n"
        if char.social_traits["verbal"]:
            social_traits += f"verbal: {char.social_traits['verbal']}\n"

        pi_label = Label(text=personal_info,
                         pos_hint=({'x': -0.05, 'y': 0.36}))
        with pi_label.canvas:
            Color(1, 1, 1, 0.35)
            Rectangle(pos=(0, 0), size=(800, 600))

        # done
        stat_label = Label(text=stats,
                           pos_hint=({'x': 0.15, 'y': 0.375}))
        # done
        sv_label = Label(text=save,
                         pos_hint=({'x': -0.29, 'y': -0.001}))
        # done
        ar_label = Label(text=armor,
                         pos_hint=({'x': -0.32, 'y': 0.19}))
        # done
        sk_label = Label(text=skills,
                         pos_hint=({'x': 0.37, 'y': 0.16}))
        # done
        ab_label = Label(text=ab,
                         pos_hint=({'x': -0.4, 'y': 0.0}))
        # done
        tr_label = Label(text=treasure,
                         pos_hint=({'x': -0.026, 'y': -0.15}))
        # done
        ow_label = Label(text=on_person_wealth,
                         pos_hint=({'x': -0.4, 'y': -0.17}))
        # done
        aw_label = Label(text=at_home_wealth,
                         pos_hint=({'x': -0.28, 'y': -0.17}))
        # done
        pt_label = Label(text=physical_traits,
                         pos_hint=({'x': 0.045, 'y': 0.12}))
        #
        st_label = Label(text=social_traits,
                         pos_hint=({'x': 0.25, 'y': -0.4}))

        self.add_widget(pi_label)
        self.add_widget(stat_label)
        self.add_widget(sv_label)
        self.add_widget(ar_label)
        self.add_widget(sk_label)
        self.add_widget(ab_label)
        self.add_widget(tr_label)
        self.add_widget(ow_label)
        self.add_widget(aw_label)
        self.add_widget(pt_label)
        self.add_widget(st_label)

    def genBtn(self):
        self.clear_widgets()
        gen()
        self.__init__()

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
