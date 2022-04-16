import helper_functions
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

logger_df = helper_functions.get_logger()
activities_df = helper_functions.get_activity_collection()
all_buddys_df = helper_functions.get_buddys()
# print(all_buddys_df)
convo_list = []

convo_buddy, activity = "Red Panda", "Liegestütze"
# convo_buddy, activity = "Red Panda", "test"

csv_name = convo_buddy + "_workout_chat.csv"
buddy_convo_df = pd.read_csv(csv_name)
tag = "Intro"


def get_dict_chat_variables():
    logger_df = helper_functions.get_logger()
    activities_df = helper_functions.get_activity_collection()
    all_buddys_df = helper_functions.get_buddys()


def get_string_variable(text_string):
    # strip string
    # ersetzte [] durch entsprechende variable
    ## if [] ==[] -> [] = variablestring
    ## if [] ==[] -> [] = variablestring
    ## if [] ==[] -> [] = variablestring
    # ...
    # baues string wieder zusammen
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
        pd.to_datetime(subset_logger_df["date"]) <= (datetime.today() - timedelta(days=7))]
    two_weeks_subset_logger_df = subset_logger_df.loc[
        pd.to_datetime(subset_logger_df["date"]) > (datetime.today() - timedelta(days=14))]

    if one_week_subset_logger_df.shape[0] > two_weeks_subset_logger_df.shape[0]:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[(subset_buddy_convo_df["change"] == 1) | (subset_buddy_convo_df["change"].isnull())]
    if one_week_subset_logger_df.shape[0] == two_weeks_subset_logger_df.shape[0]:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[(subset_buddy_convo_df["change"] == 2) | (subset_buddy_convo_df["change"].isnull())]

    if one_week_subset_logger_df.shape[0] < two_weeks_subset_logger_df.shape[0]:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[(subset_buddy_convo_df["change"] == 3) | (subset_buddy_convo_df["change"].isnull())]

    # randomly select a suitable successor from the remaining lines
    next_line = subset_buddy_convo_df.loc[random.choice(subset_buddy_convo_df.index)]
    tag = str(next_line["next tag"])
    # variablen in string einfügen
    new_chat_line = get_string_variable(next_line["Text"])
    convo_list.append(new_chat_line)
    print(next_line["Text"])

# print(convo_list)
# convo_list.append()
