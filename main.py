from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.picker import MDDatePicker
from datetime import datetime

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
    date = datetime.today().strftime('%Y-%m-%d')
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

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        """Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        """
        self.date = str(value)
        self.root.ids.logger_date.text = self.date

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''


FitnessApp().run()
