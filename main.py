from kivymd.app import MDApp
from kivy.uix.widget import Widget


class FitnessWindow(Widget):
    pass


class FitnessApp(MDApp):
    def build(self):
        return FitnessWindow()


FitnessApp().run()
