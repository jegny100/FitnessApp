import helper_functions
import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

logger_df = helper_functions.get_logger()
activities_df = helper_functions.get_activity_collection()
all_buddys_df = helper_functions.get_buddys()
#print(all_buddys_df)
convo_list = []

convo_buddy, activity = "Red Panda", "Liegestütze"
#convo_buddy, activity = "Red Panda", "test"

csv_name = convo_buddy + "_workout_chat.csv"
buddy_convo_df = pd.read_csv(csv_name)
tag = "Intro"

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
    subset_logger_df = subset_logger_df.loc[pd.to_datetime(subset_logger_df["date"]) > (datetime.today()-timedelta(days=7))]
    if subset_logger_df.shape[0] > 0:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["logged last week"] != 0]
    else:
        subset_buddy_convo_df = subset_buddy_convo_df.loc[subset_buddy_convo_df["logged last week"] != 1]

    # filter by change
    logger_df.loc[logger_df["activity"] == activity]



    # buddy_convo_df.loc[buddy_convo_df["logged last week"] == 1]
    # buddy_convo_df.loc[buddy_convo_df["logged last week"] == 0]

    # randomly select a suitable successor from the remaining lines
    next_line = subset_buddy_convo_df.loc[random.choice(subset_buddy_convo_df.index)]
    tag = str(next_line["next tag"])

    convo_list.append(next_line["Text"])
    print(next_line["Text"])

# print(convo_list)
#convo_list.append()
