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

    def show_dialog(self, obj):
        self.dialog = MDDialog(title='Aktivität hinzufügen',
                               text='Test test tesst', size_hint=(0.8, 1),

                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='Save')]
                               )
        self.dialog.open()


    def close_dialog(self, obj):
        self.dialog.dismiss()


FitnessApp().run()
