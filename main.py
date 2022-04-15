import random

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, OneLineListItem, OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from datetime import datetime
import os
import re
import pandas as pd
from kivymd.uix.swiper import MDSwiperItem

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


class ListItem(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty()


class FitnessApp(MDApp):
    convo_buddy = ""
    convo_activity = ""
    # buddy_info_capsule = {"name": None, "source": None, }
    dialogBuddy = None
    dialogActivity = None
    dialogError = None
    dialogErrorRequired = None
    dialogErrorNewActivity = None
    date = datetime.today().strftime('%Y-%m-%d')
    chosen_buddy = 'plus'
    chosen_activity = "Choose an activity"
    logger_capsule = {"activity": None, "date": date,
                      "duration": None, "repetition": None,
                      "weight": None}

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

    def on_start(self):
        self.load_activity_collection_list()
        # self.generate_buddys()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    # menu to select the activity to talk about with a buddy
    def callback_activity_menu(self):
        activity_df = helper_functions.get_activity_collection()
        activity_df_filtered = activity_df.loc[activity_df["buddy"] == FitnessApp.convo_buddy, "activity"].values
        menu_items = [{"viewclass": "OneLineListItem", "text": f"{activity}",
                       "height": dp(56),
                       "on_release": lambda x=f"{activity}": self.menu_callback(x)}
                      for activity in activity_df_filtered]
        self.menu = MDDropdownMenu(caller=self.root.ids.workout_convo_btn,
                                   items=menu_items, width_mult=4)
        self.menu.open()

    # handle chosen activity to talk about with a buddy
    def menu_callback(self, text_item):
        FitnessApp.convo_activity = text_item
        self.workout_chat()
        self.root.ids.screen_manager.transition.direction = "left"
        self.root.ids.screen_manager.current = "convo_page"
        self.menu.dismiss()

    def workout_chat(self):
        # fill conversation list
        convo_list = []
        csv_name = FitnessApp.convo_buddy + "_workout_chat.csv"
        logger_df = helper_functions.get_logger()
        activities_df = helper_functions.get_activity_collection()
        buddy_convo_df = pd.read_csv(csv_name)
        tag = "Intro"
        subset_buddy_convo_df = buddy_convo_df.loc[buddy_convo_df["Tag"] == tag]
        subset_buddy_convo_df.loc[random.choice(subset_buddy_convo_df.index)]
        convo_list.append()

    # set info for buddy & convo screens given the chosen buddy (show name, description and image)
    def set_convo_info(self, convo_buddy):
        FitnessApp.convo_buddy = convo_buddy
        # set up for detailed buddy page
        self.root.ids.buddy_page_image_id.source = self.get_buddy_path(convo_buddy)
        self.root.ids.buddy_name.text = convo_buddy
        self.root.ids.buddy_description.text = self.get_buddy_description(convo_buddy)

        # set up for conversation page with buddy
        self.root.ids.convo_buddy_name.text = convo_buddy
        self.root.ids.convo_image_id.source = self.get_buddy_path(convo_buddy)

        # continue in ui
        self.root.ids.screen_manager.current = "buddy_page"

    ''' ACTIVITY COLLECTION FUNCTIONS '''

    # fills the container with activities with pictures in the collection of activities
    def load_activity_collection_list(self):
        for activity, buddy in helper_functions.get_activity_collection()[["activity", "buddy"]].values:
            try:
                source = self.get_buddy_path(buddy)
            except KeyError:
                source = "alert"
            self.root.ids.container.add_widget(ListItem(text=activity, icon=source))

    # handle new activity
    # by switching screens and saving new data to activity_collection.csv
    def add_activity_to_collection(self, activity_name, duration, repetition, weight):
        empty_name = re.search("\w", activity_name)
        # check whether the returned activity_name is not empty and unique in activity_collection.csv
        if empty_name is not None:
            print("empty")
            activity_collection_df = helper_functions.get_activity_collection()
            if activity_name not in activity_collection_df["activity"].unique():
                id_name = True
            else:
                id_name = False
        else:
            id_name = False

        # check for correct data
        if ((duration + repetition + weight) == 1) & (FitnessApp.chosen_buddy != "plus") & id_name:
            self.root.ids.screen_manager.transition.direction = 'right'
            self.root.ids.screen_manager.current = "activity_collection"
            row = {'activity': activity_name, 'buddy': FitnessApp.chosen_buddy, 'duration': duration,
                   'repetition': repetition, 'weight': weight}
            # update to csv
            activity_collection_df = helper_functions.get_activity_collection().append(row, ignore_index=True)
            activity_collection_df.to_csv('activity_collection.csv')
            print(activity_collection_df, "\n")
        else:
            self.error_new_activity()

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

    def get_buddy_path(self, buddy):
        buddy_df = helper_functions.get_buddys()
        source = "images/" + str(buddy_df.loc[buddy_df['buddy'] == buddy, 'source'].values[0])
        return source

    def get_buddy_description(self, buddy):
        buddy_df = helper_functions.get_buddys()
        source = buddy_df.loc[buddy_df['buddy'] == buddy, 'description'].values[0]
        return source

    # confirm dialog and show picture of the chosen buddy
    def confirm_buddy_dialog(self, obj):
        if FitnessApp.chosen_buddy != "plus":
            self.root.ids.buddy.icon = self.get_buddy_path(FitnessApp.chosen_buddy)
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
