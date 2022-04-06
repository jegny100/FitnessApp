import pandas as pd
import numpy as np

activity_collection_df = pd.read_csv('activity_collection_backup.csv', index_col="Unnamed: 0")
print(activity_collection_df)
row = activity_collection_df.loc[activity_collection_df['activity'] == "Glute Bridge"].columns[np.where(row.values[0])[-1][-1]]
print(row, "\n")
#print(row.columns[np.where(row.values[0])[-1][-1]])
#print(row.columns)
#print(activity_collection_df.columns[row[0]])
#print(row[row == 1].index)
#print(row.iloc[])
activity_collection_df_test = activity_collection_df.copy()
activity_collection_df_test.set_index('activity', inplace=True)
activity_collection_df_test = activity_collection_df_test.T
#print(activity_collection_df_test.loc[activity_collection_df_test['Glute Bridge'] == 1].index)
