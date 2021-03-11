from kivy.app import App
from kivy.uix.widget import Widget


class HVNLayout(Widget):
    pass


class HVNApp(App):
    def build(self):
        return HVNLayout()


if __name__ == "__main__":
    HVNApp().run()
