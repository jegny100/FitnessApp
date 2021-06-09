from kivy.app import App
from kivy.uix.widget import Widget


class FitnessWindow(Widget):
    pass


class FitnessApp(App):
    def build(self):
        return FitnessWindow()


FitnessApp().run()
