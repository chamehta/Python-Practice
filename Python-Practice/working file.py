import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import seaborn as sns

filename1 = 'attempts.csv'
filename2 = 'tests.csv'
df_attempt = pd.read_csv(filename1, header=0) # see if the header is there
df_test = pd.read_csv(filename2, header=0) 

## quantitative Exploratory data analysis
df_attempt.head()
df_test.head()
df_attempt.shape
df_test.shape

df_attempt.columns.to_list()
df_test.columns.to_list()

df_attempt.info()
df_test.info()


sqldf('''SELECT  distinct test_id from df_test''', env=None)
sqldf('''SELECT  count(attempt_id)*0.001 from df_attempt
      ''', env=None)


combine_df = pd.merge(df_attempt, df_test, how= "left", on="test_id")
combine_df.head()
combine_df.info()
combine_df.columns.to_list()

sqldf('''SELECT attempt_id, test_title from combine_df
      ''', env=None)