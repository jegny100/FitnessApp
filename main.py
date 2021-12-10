from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

import main_kivy

Window.size = (350, 600)


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FitnessApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"

        return Builder.load_string(main_kivy.KV)


FitnessApp().run()
