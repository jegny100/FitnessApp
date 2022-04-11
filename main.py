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
    dialogErrorRequired = None
    date = datetime.today().strftime('%Y-%m-%d')
    chosen_activity = "Choose an activity"
    logger_capsule = {"activity": None, "date": date, "duration": None, "repetition": None, "weight": None}

    def build(self):
        self.theme_cls.primary_palette = "Teal"

        # generate basic activity collection if not existent
        if not os.path.isfile('./activity_collection.csv'):
            activity_collection_df = pd.DataFrame(columns=["activity", "buddy", "duration", "repetition", "weight"])
            activity_row = {'activity': 'Liegestütze', 'buddy': "", 'duration': 0, 'repetition': 1, 'weight': 0}
            activity_collection_df = activity_collection_df.append(activity_row, ignore_index=True)
            activity_collection_df.to_csv('activity_collection.csv')
        self.get_activity_collection()

        return Builder.load_string(main_kivy.KV)

    """ LOGGER FUNCTIONS  """

    # ACTIVITY COLLECTION FUNCTIONS

    # get the most current activity collection
    def get_activity_collection(self):
        activity_collection_df = pd.read_csv('activity_collection.csv', index_col="Unnamed: 0")
        return activity_collection_df

    def check_collection_required(self):
        if self.chosen_activity_check():
            # check which activity was chosen
            activity_collection_df = pd.read_csv('activity_collection_backup.csv', index_col="Unnamed: 0")
            activity_collection_df.set_index('activity', inplace=True)
            activity_collection_df = activity_collection_df.T
            test = activity_collection_df[FitnessApp.chosen_activity] == 1
            required = activity_collection_df.loc[test].index[0]
            print("required ", required)
            print("self logger :", self.logger_capsule[required])
            if self.logger_capsule[required] == "":
                print("False")
                return False
            else:
                print("True")
                return True

    # error message, if required input is missing
    def error_required_dialog(self):
        if not self.dialogErrorRequired:
            self.dialogErrorRequired = MDDialog(
                title="Missing Required Info",
                text="Please fill out the correct information for your chosen activity",
                buttons=[MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.confirm_error_required_dialog)
                         ],
            )
        self.dialogErrorRequired.open()

    def confirm_error_required_dialog(self, obj):
        self.dialogErrorRequired.dismiss()


    # ACTIVITY LOGGER FUNCTIONS

    # creates choose-an-activity-dialog
    def show_activities_dialog(self):
        if not self.dialogActivity:
            activity_collection_df = self.get_activity_collection()
            self.items = [ItemConfirm(text=X) for X in activity_collection_df["activity"].to_list()]
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

    # confirming the choose-an-activity-dialog and handling chosen activity
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

    # saves the chosen date of date picker
    def on_save(self, instance, value, date_range):
        self.root.ids.logger_date.text = str(value)
        self.logger_capsule["date"] = str(value)

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialogActivity box button is clicked."""

    # GET INPUT
    def get_logger(self, duration, repetition, weight):

        self.logger_capsule["duration"] = duration
        self.logger_capsule["repetition"] = repetition
        self.logger_capsule["weight"] = weight

    # Save logger and reset
    def save_logger(self):
        self.logger_save_to_csv()
        self.empty_logger()
        self.root.ids.screen_manager.current = "homescreen"

    # checks if an activity is chosen, otherwise throws an error message
    def chosen_activity_check(self):
        if FitnessApp.chosen_activity == "Choose an activity":
            return False
        else:
            return True

    # error message, if trying to log without an activity
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
