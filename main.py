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


# Menu class to navigate through screens
class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


# Dialog Choice Confirmation (Single Choice)
class ItemConfirm(OneLineAvatarIconListItem):
    divider = None
    chosen_activity_item = "itemsDings"

    # checks an item in a list with a check icon
    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False
        ItemConfirm.chosen_activity_item = self.text


class FitnessApp(MDApp):
    dialog = None
    chosen_activity = "Choose an activity"

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
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.cancel_dialog),
                         MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.confirm_dialog)
                         ],
            )
        self.dialog.open()

    def cancel_dialog(self, obj):
        self.dialog.dismiss()

    def confirm_dialog(self, obj):
        self.chosen_activity = ItemConfirm.chosen_activity_item
        self.root.ids.logger_chosen_activity.text = self.chosen_activity
        self.dialog.dismiss()


FitnessApp().run()
