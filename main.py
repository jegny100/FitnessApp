import json
from os import listdir
from os.path import isfile, join

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, OneLineListItem, OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.swiper import MDSwiperItem
from datetime import datetime, timedelta
import os
import re
import ast
import random

from kivymd.uix.tooltip import MDTooltip
from kivymd.utils.fitimage import FitImage

import main_kivy
import pandas as pd
import helper_functions

Window.size = (350, 600)

# Important hex: a4bccd
colors = {
    "Blue": {
        "50": "a4bccd",
        "100": "a4bccd",
        "200": "a4bccd",
        "300": "a4bccd",
        "400": "a4bccd",
        "500": "a4bccd",
        "600": "5191b8",
        "700": "487fa5",
        "800": "426f91",
        "900": "35506d",
        "A100": "b9e1ee",
        "A200": "91cee3",
        "A400": "62acce",
        "A700": "487fa5",
    },
    "Red": {
        "50": "FFEBEE",
        "100": "FFCDD2",
        "200": "EF9A9A",
        "300": "E57373",
        "400": "EF5350",
        "500": "F44336",
        "600": "E53935",
        "700": "D32F2F",
        "800": "C62828",
        "900": "B71C1C",
        "A100": "FF8A80",
        "A200": "FF5252",
        "A400": "FF1744",
        "A700": "D50000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}


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
        FitnessApp.check_list = check_list


class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass


class ListItem(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty()


class FitnessApp(MDApp):
    convo_buddy = ""
    convo_activity = ""
    chat_variables_dict = {}
    convo_id = 0
    convo_list = None
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
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Blue"

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
        self.start_settings()

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' HOMESCREEN FUNCTIONS '''

    # TODO make not random
    # select a random buddy to display on homescreen
    def get_random_buddy_image(self):
        random_image = random.choice([f for f in listdir("images/") if isfile(join("images/", f))])
        return str("images/" + random_image)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' SETTING FUNCTIONS '''

    # save settings to json
    def set_settings(self, logging_encouragement, reminder_start):
        # get setting dict
        with open('settings.json', 'r') as f:
            settings = json.load(f)

        # get updated info
        settings['logging_encouragement'] = logging_encouragement
        settings['reminder_start'] = reminder_start

        # save updatet setting dict
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

    def start_settings(self):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        self.root.ids.setting_logg_encouragement.value = settings['logging_encouragement']
        self.root.ids.setting_start_reminder.active = settings['reminder_start']

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' BUDDY PAGE & CHAT FUNCTIONS '''

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
        self.start_convo("workout")
        self.menu.dismiss()

    # start preparations for a conversation based on the type of chat
    def start_convo(self, chattype):
        chat_df = self.get_convo_csv(chattype)

        if len(chat_df):
            self.get_dict_chat_variables()
            self.fill_conversation_list(chat_df)
            self.convo_id = 0
            self.next_message()
            self.root.ids.screen_manager.transition.direction = "left"
            self.root.ids.screen_manager.current = "convo_page"
        else:
            Snackbar(text="I'm sorry, but I don't know what to say to you yet").open()

    # fill dictionary with relevant variables for blanks in chat messages
    def get_dict_chat_variables(self):
        activity = FitnessApp.convo_activity
        logger_df = helper_functions.get_logger()
        logger_df = logger_df.loc[logger_df["activity"] == activity]

        # if no activity was logged, don't fill the dict
        if logger_df.shape[0] == 0:
            return
        activities_df = helper_functions.get_activity_collection()

        # [workout_name]
        FitnessApp.chat_variables_dict["[workout_name]"] = activity

        # [date_last_logged]
        date_last_logged = logger_df["date"].max()
        FitnessApp.chat_variables_dict["[date_last_logged]"] = date_last_logged

        # [logged_measurement]
        # get relevant measurement
        sub_activities_df = activities_df.set_index('activity').T
        measurement = sub_activities_df.loc[sub_activities_df[activity] == 1].index[0]
        # get measurement for latest activity
        sub_logger_df = logger_df.loc[logger_df["date"] == date_last_logged]
        measurement_value = sub_logger_df[measurement].values[0]
        # special case duration
        if measurement == 'duration':
            measurement_value = ast.literal_eval(measurement_value)
            logged_measurement = ""
            time = ["h", "min", "sec"]
            for i, x in enumerate(measurement_value):
                if x != "":
                    logged_measurement = logged_measurement + x + time[i] + " "
            FitnessApp.chat_variables_dict["[logged_measurement]"] = logged_measurement
        else:
            FitnessApp.chat_variables_dict["[logged_measurement]"] = str(measurement_value) + " " + measurement

        # [instances_last_week]
        instances_last_week = \
            logger_df.loc[pd.to_datetime(logger_df["date"]) > (datetime.today() - timedelta(days=7))].shape[0]
        FitnessApp.chat_variables_dict["[instances_last_week]"] = str(instances_last_week)

        # [difference]
        one_week = logger_df.loc[
            pd.to_datetime(logger_df["date"]) > (datetime.today() - timedelta(days=7))].shape[0]
        two_weeks = logger_df.loc[pd.to_datetime(logger_df["date"]).between(
            datetime.today() - timedelta(days=14), datetime.today() - timedelta(days=7))].shape[0]
        FitnessApp.chat_variables_dict["[difference]"] = str(one_week - two_weeks)

        # [total_logged_instances]
        FitnessApp.chat_variables_dict["[total_logged_instances]"] = str(logger_df.shape[0])

    # replaces variables in chat texts with actual info from chat_variables_dict
    def get_string_variable(self, text_string):
        for key in FitnessApp.chat_variables_dict:
            text_string = text_string.replace(key, FitnessApp.chat_variables_dict[key])
        return text_string

    # choose correct csv file for convo
    def get_convo_csv(self, chattype):
        if chattype == "workout":
            csv_name = FitnessApp.convo_buddy + "_workout_chat.csv"
        elif chattype == "chat":
            csv_name = FitnessApp.convo_buddy + "_chat.csv"
        try:
            buddy_convo_df = pd.read_csv(csv_name)
        except FileNotFoundError:
            return []
        else:
            return buddy_convo_df

    # fill conversation list
    def fill_conversation_list(self, buddy_convo_df):
        logger_df = helper_functions.get_logger()
        # activities_df = helper_functions.get_activity_collection()
        all_buddys_df = helper_functions.get_buddys()
        convo_list = []

        tag = "Intro"
        group = "nan"
        convo_buddy = FitnessApp.convo_buddy
        activity = FitnessApp.convo_activity

        while tag != "nan":
            # filter by tag
            subset_buddy_convo_df = buddy_convo_df.loc[buddy_convo_df["tag"] == tag]

            # filter by friendship
            friendship_lvl = all_buddys_df.loc[all_buddys_df["buddy"] == convo_buddy, "friendship_level"].values[0]
            subset_buddy_convo_df = subset_buddy_convo_df.loc[
                ~(subset_buddy_convo_df["friendship min"] > friendship_lvl)]
            subset_buddy_convo_df = subset_buddy_convo_df.loc[
                ~(subset_buddy_convo_df["friendship max"] < friendship_lvl)]

            # filter by logged any
            subset_logger_df = logger_df.loc[logger_df["activity"] == activity]
            if subset_logger_df.shape[0] > 0:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["logged any"] != 0]
            else:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["logged any"] != 1]

            # filter by logged last week
            subset_logger_df = logger_df.loc[logger_df["activity"] == activity]
            subset_logger_df = subset_logger_df.loc[
                pd.to_datetime(subset_logger_df["date"]) > (datetime.today() - timedelta(days=7))]
            if subset_logger_df.shape[0] > 0:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["logged last week"] != 0]
            else:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["logged last week"] != 1]

            # filter by change
            subset_logger_df = logger_df.loc[logger_df["activity"] == activity]
            # instances of activities for the week before today and the week 2 weeks before today
            one_week_subset_logger_df = subset_logger_df.loc[
                pd.to_datetime(subset_logger_df["date"]) > (datetime.today() - timedelta(days=7))]
            two_weeks_subset_logger_df = subset_logger_df.loc[
                pd.to_datetime(subset_logger_df["date"]).between(datetime.today() - timedelta(days=14),
                                                                 datetime.today() - timedelta(days=7))]

            if one_week_subset_logger_df.shape[0] > two_weeks_subset_logger_df.shape[0]:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[
                    (subset_buddy_convo_df["change"] == 1) | (subset_buddy_convo_df["change"].isnull())]
            if one_week_subset_logger_df.shape[0] == two_weeks_subset_logger_df.shape[0]:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[
                    (subset_buddy_convo_df["change"] == 2) | (subset_buddy_convo_df["change"].isnull())]

            if one_week_subset_logger_df.shape[0] < two_weeks_subset_logger_df.shape[0]:
                subset_buddy_convo_df = subset_buddy_convo_df.loc[
                    (subset_buddy_convo_df["change"] == 3) | (subset_buddy_convo_df["change"].isnull())]

            # filter by group
            subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["rec group"].astype(str) == group]

            # 'error'-message if there is no sentence to choose from since the csv data is corrupted somehow
            if subset_buddy_convo_df.empty:
                convo_list.append(
                    "I'm sorry, I mixed up my sentences. Can we talk about another activity or chat chat a little?")
                break

            # randomly select a suitable successor from the remaining lines
            next_line = subset_buddy_convo_df.loc[random.choice(subset_buddy_convo_df.index)]
            tag = str(next_line["next tag"])
            # add variable to string
            new_chat_line = self.get_string_variable(next_line["Text"])
            convo_list.append(new_chat_line)
            group = str(next_line["set group"])
        FitnessApp.convo_list = convo_list

    # convo: show next message:
    def next_message(self):
        if self.convo_id < len(self.convo_list):
            self.root.ids.convo_chat.text = self.convo_list[self.convo_id]
            self.convo_id += 1

    # handling "back"-button in convo, by either showing the message before or
    #  switching back to the select a chat window
    def last_message(self):
        if self.convo_id > 1:
            self.convo_id -= 1
            self.root.ids.convo_chat.text = self.convo_list[self.convo_id - 1]
        else:
            self.root.ids.screen_manager.transition.direction = "right"
            self.root.ids.screen_manager.current = "buddy_page"

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

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' ACTIVITY COLLECTION FUNCTIONS '''

    # fills the container with activities with pictures in the collection of activities
    def load_activity_collection_list(self):
        self.root.ids.container.clear_widgets()
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

    # show the list of alle current Buddys as a dialog window
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

    # gets the source path of a given buddy
    def get_buddy_path(self, buddy):
        buddy_df = helper_functions.get_buddys()
        source = "images/" + str(buddy_df.loc[buddy_df['buddy'] == buddy, 'source'].values[0])
        return source

    # gets the description of a given buddy
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

    # give buddy feedback depending on setting and activity
    def buddy_feedback_setting(self):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        if settings['logging_encouragement'] == 0:      # never feedback
            self.root.ids.screen_manager.current = "homescreen"
        elif settings['logging_encouragement'] == 1:    # sometimes feedback
            counter = settings["logging_encouragement_counter"]
            if counter < 3:
                counter += 1
                settings["logging_encouragement_counter"] = counter
                self.root.ids.screen_manager.current = "homescreen"
            else:
                settings["logging_encouragement_counter"] = 1
                self.give_feedback()

            with open('settings.json', 'w') as f:
                json.dump(settings, f)

        else:                                           # always feedback
            self.give_feedback()

    # filling feedback screen with text and image
    def give_feedback(self):
        activity_collection_df = helper_functions.get_activity_collection()
        buddys_df = helper_functions.get_buddys()
        buddy = activity_collection_df.loc[activity_collection_df["activity"] == self.logger_capsule["activity"], "buddy"].values[0]
        self.root.ids.buddy_feedback_image.source = self.get_buddy_path(buddy)
        self.root.ids.feedback_buddy_name.text = buddy
        message = buddys_df.loc[buddys_df["buddy"] == buddy, "basic_logg_encouragement"].values[0]
        self.root.ids.buddy_feedback_text.text = message
        self.root.ids.screen_manager.current = "buddy_feedback"

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

    # Save data from logger, give feedback and reset
    def handle_logger(self):
        self.logger_save_to_csv()
        self.buddy_feedback_setting()
        self.empty_logger()

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
        self.increase_friendship_lvl()

    # everytime an activity is logged the friendship level of the corresponding buddy is increased
    def increase_friendship_lvl(self):
        activity = self.logger_capsule["activity"]
        activity_collection_df = helper_functions.get_activity_collection()
        buddys_df = helper_functions.get_buddys()
        buddy = activity_collection_df.loc[activity_collection_df["activity"] == activity, "buddy"].values[0]
        buddys_df.loc[buddys_df["buddy"] == buddy, "friendship_level"] += 1
        buddys_df.to_csv("buddys.csv")

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
