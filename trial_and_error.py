import ast

import helper_functions
import random
import pandas as pd
from datetime import datetime, timedelta

logger_df = helper_functions.get_logger()
activities_df = helper_functions.get_activity_collection()
all_buddys_df = helper_functions.get_buddys()
# print(all_buddys_df)
convo_list = []

#convo_buddy, activity = "Red Panda", "Liegestütze"
convo_buddy, activity = "Red Panda", "Joggen"
# convo_buddy, activity = "Red Panda", "test"

csv_name = convo_buddy + "_workout_chat.csv"
buddy_convo_df = pd.read_csv(csv_name)
tag = "Intro"

chat_variables_dict = {}


def get_dict_chat_variables():
    logger_df = helper_functions.get_logger()
    logger_df = logger_df.loc[logger_df["activity"] == activity]
    activities_df = helper_functions.get_activity_collection()
    all_buddys_df = helper_functions.get_buddys()

    # [workout_name]
    chat_variables_dict["[workout_name]"] = activity

    # [date_last_logged]
    date_last_logged = logger_df["date"].max()
    chat_variables_dict["[date_last_logged]"] = date_last_logged

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
        chat_variables_dict["[logged_measurement]"] = logged_measurement
    else:
        chat_variables_dict["[logged_measurement]"] = str(measurement_value) + " " + measurement

    # [instances_last_week]
    instances_last_week = logger_df.loc[pd.to_datetime(logger_df["date"]) > (datetime.today() - timedelta(days=7))].shape[0]
    chat_variables_dict["[instances_last_week]"] = str(instances_last_week)

    # [difference]
    one_week = logger_df.loc[
        pd.to_datetime(logger_df["date"]) > (datetime.today() - timedelta(days=7))].shape[0]
    two_weeks = logger_df.loc[pd.to_datetime(logger_df["date"]).between(
            datetime.today() - timedelta(days=14), datetime.today() - timedelta(days=7))].shape[0]
    chat_variables_dict["[difference]"] = str(one_week - two_weeks)

    # [total_logged_instances]
    chat_variables_dict["[total_logged_instances]"] = str(logger_df.shape[0])


get_dict_chat_variables()


# replaces variables in chat texts with actual info from chat_variables_dict
def get_string_variable(text_string):
    for key in chat_variables_dict:
        text_string = text_string.replace(key, chat_variables_dict[key])
    print(text_string)
    return text_string


while tag != 'nan':
    # filter by tag
    subset_buddy_convo_df = buddy_convo_df.loc[buddy_convo_df["tag"] == tag]

    # filter by friendship
    friendship_lvl = all_buddys_df.loc[all_buddys_df["buddy"] == convo_buddy, "friendship_level"].values[0]
    subset_buddy_convo_df = subset_buddy_convo_df.loc[~(subset_buddy_convo_df["friendship min"] > friendship_lvl)]
    subset_buddy_convo_df = subset_buddy_convo_df.loc[~(subset_buddy_convo_df["friendship max"] < friendship_lvl)]

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
        pd.to_datetime(subset_logger_df["date"]).between(datetime.today() - timedelta(days=14), datetime.today() - timedelta(days=7))]

    if one_week_subset_logger_df.shape[0] > two_weeks_subset_logger_df.shape[0]:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[
            (subset_buddy_convo_df["change"] == 1) | (subset_buddy_convo_df["change"].isnull())]
    if one_week_subset_logger_df.shape[0] == two_weeks_subset_logger_df.shape[0]:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[
            (subset_buddy_convo_df["change"] == 2) | (subset_buddy_convo_df["change"].isnull())]

    if one_week_subset_logger_df.shape[0] < two_weeks_subset_logger_df.shape[0]:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[
            (subset_buddy_convo_df["change"] == 3) | (subset_buddy_convo_df["change"].isnull())]

    # randomly select a suitable successor from the remaining lines
    next_line = subset_buddy_convo_df.loc[random.choice(subset_buddy_convo_df.index)]
    tag = str(next_line["next tag"])
    # variablen in string einfügen
    new_chat_line = get_string_variable(next_line["Text"])
    convo_list.append(new_chat_line)

# print(convo_list)
# convo_list.append()
