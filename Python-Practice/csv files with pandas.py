import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import seaborn as sns

filename = 'data.csv'
df = pd.read_csv(filename, header=0) # see if the header is there


## quantitative Exploratory data analysis
df.head()
df.shape
df.info()
#df['Duration'].value_counts()
df.describe()

df.columns.to_list() #converts the column names of the DataFrame ‘df’ into a Python list, providing a convenient way to access and manipulate column names.

#check for missing valuses
df.isnull().sum()

#Checking duplicate Values
df.nunique()

##sql selects 
sqldf('''SELECT distinct Duration from df''', env=None)



## graphical exploratory data analysis
## ploting histogram
sns.set()
pd.DataFrame.hist(df[['Duration']])
plt.xlabel('duration')
plt.ylabel('count')
plt.show()


# bee swarm plot
# Assuming 'df' is your DataFrame
plt.figure(figsize=(10, 8))

# Using Seaborn to create a swarm plot
sns.swarmplot(x="Duration", y="Calories", data=df, palette='viridis')

plt.title('Swarm Plot for Quality and Alcohol')
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()


# Set Seaborn style
sns.set_style("darkgrid")

# Identify numerical columns
numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns

# Plot distribution of each numerical feature
plt.figure(figsize=(14, len(numerical_columns) * 3))
for idx, feature in enumerate(numerical_columns, 1):
    plt.subplot(len(numerical_columns), 2, idx)
    sns.histplot(df[feature], kde=True)
    plt.title(f"{feature} | Skewness: {round(df[feature].skew(), 2)}")

# Adjust layout and show plots
plt.tight_layout()
plt.show()


# Set the color palette
sns.set_palette("Pastel1")

# Assuming 'df' is your DataFrame
plt.figure(figsize=(10, 6))

# Using Seaborn to create a pair plot with the specified color palette
sns.pairplot(df)

plt.suptitle('Pair Plot for DataFrame')
plt.show()
