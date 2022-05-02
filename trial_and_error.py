import pandas as pd
import helper_functions

logger_df = helper_functions.get_logger()
values = logger_df['activity'].value_counts()

print(values)
print("\n Activity  ",values.idxmin())
