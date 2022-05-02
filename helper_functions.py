import pandas as pd


# get the most current activity collection
def get_activity_collection():
    activity_collection_df = pd.read_csv('files/activity_collection.csv', index_col="Unnamed: 0")
    return activity_collection_df


# get the list of buddies/buddys
def get_buddys():
    buddys_df = pd.read_csv('files/buddys.csv', index_col="Unnamed: 0")
    return buddys_df

def get_logger():
    logger_df = pd.read_csv('files/logged_activities.csv', index_col="Unnamed: 0")
    return logger_df


