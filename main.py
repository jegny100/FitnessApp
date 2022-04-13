from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.picker import MDDatePicker
from datetime import datetime
import os
import re
import pandas as pd
import main_kivy
import helper_functions


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


# Dialog Choice Confirmation (Single Choice) specific for buddy system
class BuddyConfirm(OneLineAvatarIconListItem):
    divider = None

    # checks an item in a list with a check icon
    def set_buddy(self, instance_check):
        instance_check.active = not instance_check.active
        check_list = instance_check.get_widgets(instance_check.group)
        self.check_list = check_list
        # ensures single choice
        for check in check_list:
            if check != instance_check:
                check.active = False
        if instance_check.active:
            FitnessApp.chosen_buddy = self.text
        else:
            FitnessApp.chosen_buddy = "plus"
        print("CHOSEN BUDDY :", FitnessApp.chosen_buddy)
        FitnessApp.check_list = check_list


class FitnessApp(MDApp):
    dialogBuddy = None
    dialogActivity = None
    dialogError = None
    dialogErrorRequired = None
    dialogErrorNewActivity = None
    date = datetime.today().strftime('%Y-%m-%d')
    chosen_buddy = 'plus'
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
        helper_functions.get_activity_collection()

        return Builder.load_string(main_kivy.KV)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' ACTIVITY COLLECTION FUNCTIONS '''

    # handle new activity
    # by switching screens and saving new data to activity_collection.csv
    def add_activity_to_collection(self, activity_name, duration, repetition, weight):
        empty_name = re.search("\w", activity_name)
        # check whether the returned activity_name is not empty and unique in activity_collection.csv
        if empty_name is not None:
            if activity_name not in helper_functions.get_activity_collection()["activity"].unique():
                print("df ",helper_functions.get_activity_collection()["activity"])
                print(activity_name)
                id_name = True
            else:
                id_name = False
        else:
            id_name = False
        print("id_name ", id_name)
        if ((duration + repetition + weight) == 1) & (FitnessApp.chosen_buddy != "plus") & id_name:
            self.root.ids.screen_manager.transition.direction = 'right'
            self.root.ids.screen_manager.current = "activity_collection"
            row = {'activity': activity_name, 'buddy': FitnessApp.chosen_buddy, 'duration': duration,
                   'repetition': repetition, 'weight': weight}
        else:
            self.error_new_activity()
        # TODO check for distinct names in csv collection as primary key
        # TODO save to csv

    # check for name, buddy & exactly one measurement
    def check_new_activity(self):
        pass

    # error message if data is missing
    def error_new_activity(self):
        if not self.dialogErrorNewActivity:
            self.dialogErrorNewActivity = MDDialog(
                title="Incorrect Data",
                text="Please choose a buddy, a unique name and exactly one required measurement",
                buttons=[MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.confirm_error_new_activity)
                         ],
            )
        self.dialogErrorNewActivity.open()

    def confirm_error_new_activity(self, obj):
        self.dialogErrorNewActivity.dismiss()

    # show Buddy list as dialog window
    def show_buddy_dialog(self):
        if not self.dialogBuddy:
            buddys_df = helper_functions.get_buddys()
            self.items = [BuddyConfirm(text=X) for X in buddys_df["buddy"].to_list()]
            self.dialogBuddy = MDDialog(
                title="Choose your buddy",
                type="confirmation",
                items=self.items,
                buttons=[MDFlatButton(text="CANCEL",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.cancel_buddy_dialog),
                         MDFlatButton(text="OK",
                                      text_color=self.theme_cls.primary_color,
                                      on_release=self.confirm_buddy_dialog)
                         ],
            )
        self.dialogBuddy.open()

    def cancel_buddy_dialog(self, obj):
        FitnessApp.chosen_buddy = "plus"
        self.root.ids.buddy.icon = "plus"
        self.empty_checkbox()
        self.dialogBuddy.dismiss()

    # confirm dialog and show picture of the chosen buddy
    def confirm_buddy_dialog(self, obj):
        if FitnessApp.chosen_buddy != "plus":
            buddy_df = helper_functions.get_buddys()
            row = buddy_df.loc[buddy_df['buddy'] == FitnessApp.chosen_buddy]
            source = "images/" + str(row["source"][0])
            self.root.ids.buddy.icon = source
            self.dialogBuddy.dismiss()
        else:
            self.root.ids.buddy.icon = "plus"
            self.dialogBuddy.dismiss()

    # checks the requirement of the chosen activity
    def check_collection_required(self):
        if self.chosen_activity_check():
            # check which activity was chosen
            activity_collection_df = pd.read_csv('activity_collection.csv', index_col="Unnamed: 0")
            activity_collection_df.set_index('activity', inplace=True)
            activity_collection_df = activity_collection_df.T
            tmp = activity_collection_df[FitnessApp.chosen_activity] == 1
            required = activity_collection_df.loc[tmp].index[0]
            # specific case of duration measurement
            if required == "duration":
                for i in self.logger_capsule[required]:
                    if i != "" or None:
                        return True
                return False
            # any simple unit of measurement
            if self.logger_capsule[required] == "":
                return False
            else:
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

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' ACTIVITY LOGGER FUNCTIONS '''

    # creates choose-an-activity-dialog
    def show_activities_dialog(self):
        if not self.dialogActivity:
            activity_collection_df = helper_functions.get_activity_collection()
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
    def on_save(self, _instance, value, _date_range):
        self.root.ids.logger_date.text = str(value)
        self.logger_capsule["date"] = str(value)

    def on_cancel(self, instance, value):
        """Events called when the "CANCEL" dialogActivity box button is clicked."""

    # GET INPUT FROM LOGGER
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

    # RESET LOGGER
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


# NOTE: we know it's "buddies" not "buddys"
