# --------------
# Code starts here

#### Data 1
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import skew
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder

# Load the data
df = pd.read_csv(path)
print(df.info())

# Overview of the data
print(df.describe())
import warnings
warnings.filterwarnings("ignore")

# Histogram showing distribution of car prices
sns.distplot(df['price'], kde=True, rug=True)

# Countplot of the make column
plt.figure()
sns.countplot(y='make', data=df)

# Jointplot showing relationship between 'horsepower' and 'price' of the car
plt.figure(figsize = (10,10))
sns.jointplot('horsepower','price', data=df, kind='reg')

# Correlation heat map
plt.figure(figsize = (11,11))
sns.heatmap(data=df.corr(), cmap="YlGnBu")

# boxplot that shows the variability of each 'body-style' with respect to the 'price'
plt.figure(figsize=(12,8))
sns.boxplot(x="body-style", y="price", data=df)

#### Data 2

# Load the data
df = pd.read_csv(path2)
print(df.shape)
print(df.columns)

# Impute missing values with mean
df = df.replace("?", "NaN")
print(df.head(5))

mean_imputer = Imputer(missing_values = "NaN", strategy='mean')
df[['normalized-losses']] = mean_imputer.fit_transform(df[['normalized-losses']])
df[['horsepower']] = mean_imputer.fit_transform(df[['horsepower']])

# Skewness of numeric features
numeric_columns = df._get_numeric_data().columns
for i in numeric_columns:
    if skew(df[i]) > 1:
        df[i] = np.sqrt(df[i])

# Label encode 
categorical_cols = df.select_dtypes(include='object').columns
#print(categorical_cols)

encoder = LabelEncoder()
for i in categorical_cols:
    df[i] = encoder.fit_transform(df[i])

print(df[categorical_cols].head(n=5))


#Combine the 'height' and 'width' to make a new feature 'area' of the frame of the car
df['area'] = df['height'] * df['width']
print(df['area'][:5])

# Code ends here


