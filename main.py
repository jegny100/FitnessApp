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
import os
import pandas as pd
import main_kivy

Window.size = (350, 600)


# Menu class to navigate through screens
class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


# Dialog Choice Confirmation (Single Choice)
class ItemConfirm(OneLineAvatarIconListItem):
    divider = None
    chosen_activity = None

    # checks an item in a list with a check icon
    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False
        ItemConfirm.chosen_activity = self.text


class FitnessApp(MDApp):
    dialog = None
    date = datetime.today().strftime('%Y-%m-%d')
    chosen_activity = "Choose an activity"
    logger_capsule = {"activity": None,
                      "date": date,
                      "duration": None,
                      "repetition": None,
                      "weight": None}

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(main_kivy.KV)

    """ LOGGER FUNCTIONS  """

    # ACTIVITY FUNCTIONS
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
        self.chosen_activity = ItemConfirm.chosen_activity
        self.root.ids.logger_chosen_activity.text = self.chosen_activity
        self.logger_capsule["activity"] = self.chosen_activity
        self.dialog.dismiss()

    # DATE FUNCTIONS
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.date = str(value)
        self.root.ids.logger_date.text = self.date
        self.logger_capsule["date"] = self.date

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialog box button is clicked."""

    # CAPSULE WEIGHT, REPETITION & DURATION
    def get_logger(self, duration, repetition, weight):
        self.logger_capsule["duration"] = duration
        self.logger_capsule["repetition"] = repetition
        self.logger_capsule["weight"] = weight
        if os.path.isfile('./logged_activities.csv'):
            print("existend file")
            df = pd.read_csv('logged_activities.csv', index_col="Unnamed: 0")
        else:
            df = pd.DataFrame(columns=["activity", "date", "duration", "repetition", "weight"])
        df = df.append(self.logger_capsule, ignore_index=True)
        df.to_csv('logged_activities.csv')
        print(df)

    def empty_logger(self):
        self.root.ids.logger_chosen_activity.text = "Choose an activity"
        self.root.ids.logger_date.text = datetime.today().strftime('%Y-%m-%d')
        self.root.ids.logger_duration_hour.text = ""
        self.root.ids.logger_duration_min.text = ""
        self.root.ids.logger_duration_sec.text = ""
        self.root.ids.logger_repetition.text = ""
        self.root.ids.logger_weight.text = ""


FitnessApp().run()
