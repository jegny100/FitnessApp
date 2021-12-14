from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem

import main_kivy

Window.size = (350, 600)


# Menu class to navigate trough screens
class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


# Dialog Choice Confirmation (Single Choice)
class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class FitnessApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Teal"

        return Builder.load_string(main_kivy.KV)

    def show_activities_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Choose activity",
                type="confirmation",
                items=[ItemConfirm(text="Spazieren"),
                       ItemConfirm(text="Joggen"),
                       ItemConfirm(text="Liegestütze")],
                buttons=[MDFlatButton(text="CANCEL",
                                      text_color=self.theme_cls.primary_color),
                         MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color)
                         ],
            )
        self.dialog.open()


FitnessApp().run()
