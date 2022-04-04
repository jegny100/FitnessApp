from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
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

    # checks an item in a list with a check icon
    def set_icon(self, instance_check):
        instance_check.active = not instance_check.active
        check_list = instance_check.get_widgets(instance_check.group)
        self.check_list = check_list
        # ensures single choice
        for check in check_list:
            if check != instance_check:
                check.active = False
        if instance_check.active:
            FitnessApp.chosen_activity = self.text
        else:
            FitnessApp.chosen_activity = "Choose an activity"
        FitnessApp.check_list = check_list


class FitnessApp(MDApp):
    dialogActivity = None
    dialogError = None
    date = datetime.today().strftime('%Y-%m-%d')
    chosen_activity = "Choose an activity"
    logger_capsule = {"activity": None,
                      "date": date,
                      "duration": None,
                      "repetition": None,
                      "weight": None}

    def build(self):
        self.theme_cls.primary_palette = "Teal"

        # check if activity_collection.csv is existent
        if os.path.isfile('./activity_collection.csv'):
            activity_collection_df = pd.read_csv('activity_collection.csv', index_col="Unnamed: 0")
        else:
            activity_collection_df = pd.DataFrame(columns=["activity", "buddy", "duration", "repetition", "weight"])
            activity_collection_df.to_csv('activity_collection.csv')
            print(activity_collection_df)

        return Builder.load_string(main_kivy.KV)

    """ LOGGER FUNCTIONS  """

    # ACTIVITY COLLECTION FUNCTIONS

    def get_activity_collection(self):
        print(self.activity_collection_df[1])


    # ACTIVITY LOGGER FUNCTIONS
    def show_activities_dialog(self):
        if not self.dialogActivity:
            self.items = [ItemConfirm(text="Spazieren"),
                          ItemConfirm(text="Joggen"),
                          ItemConfirm(text="Liegestütze")]
            self.dialogActivity = MDDialog(
                title="Choose activity",
                type="confirmation",
                items=self.items,
                buttons=[MDFlatButton(text="CANCEL",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.cancel_activity_dialog),
                         MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.confirm_activity_dialog)
                         ],
            )
        self.dialogActivity.open()

    def cancel_activity_dialog(self, obj):
        self.dialogActivity.dismiss()

    def confirm_activity_dialog(self, obj):
        self.root.ids.logger_chosen_activity.text = FitnessApp.chosen_activity
        if self.chosen_activity != "Choose an activity":
            self.logger_capsule["activity"] = FitnessApp.chosen_activity
        else:
            self.logger_capsule["activity"] = ""

        self.dialogActivity.dismiss()

    # DATE FUNCTIONS
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.root.ids.logger_date.text = str(value)
        self.logger_capsule["date"] = str(value)

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialogActivity box button is clicked."""

    # GET INPUT, SAVE TO CSV, RESET LOGGER
    def handle_logger(self, duration, repetition, weight):
        self.root.ids.screen_manager.current = "homescreen"
        self.logger_capsule["duration"] = duration
        self.logger_capsule["repetition"] = repetition
        self.logger_capsule["weight"] = weight
        self.logger_save_to_csv()
        self.empty_logger()

    # checks if an activity is chosen, otherwise throws an error message
    def chosen_activity_check(self):
        if FitnessApp.chosen_activity == "Choose an activity":
            return False
        else:
            return True

    def error_activity_dialog(self):
        if not self.dialogError:
            self.dialogError = MDDialog(
                title="Missing Activity",
                text="Please choose an activity to log your training session",
                buttons=[MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.confirm_error_activity_dialog)
                         ],
            )
        self.dialogError.open()

    def confirm_error_activity_dialog(self, obj):
        self.dialogError.dismiss()

    # save data to df and csv
    def logger_save_to_csv(self):
        if os.path.isfile('./logged_activities.csv'):
            logged_activities_df = pd.read_csv('logged_activities.csv', index_col="Unnamed: 0")
        else:
            logged_activities_df = pd.DataFrame(columns=["activity", "date", "duration", "repetition", "weight"])
        logged_activities_df = logged_activities_df.append(self.logger_capsule, ignore_index=True)
        logged_activities_df.to_csv('logged_activities.csv')
        print(logged_activities_df, "\n")

    # reset all variables of the logger
    def empty_logger(self):
        self.root.ids.logger_chosen_activity.text = "Choose an activity"
        FitnessApp.chosen_activity = "Choose an activity"
        self.logger_capsule["activity"] = None
        self.empty_checkbox()
        self.root.ids.logger_date.text = datetime.today().strftime('%Y-%m-%d')
        self.root.ids.logger_duration_hour.text = ""
        self.root.ids.logger_duration_min.text = ""
        self.root.ids.logger_duration_sec.text = ""
        self.root.ids.logger_repetition.text = ""
        self.root.ids.logger_weight.text = ""

    # uncheck activities in "show_activities_dialog"
    def empty_checkbox(self):
        try:
            for item in self.check_list:
                item.active = False
        except:
            pass


FitnessApp().run()
