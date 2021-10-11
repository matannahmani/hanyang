
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#IMPORT SEABORN
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print("Setup Complete")

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv('data.csv')

#define data
ratingcount = df["Rating of Online Class experience"].value_counts()
# print(ratingcount) # print the results
data = [413,387, 230, 98, 30]
labels = ['Very poor', 'Poor', 'Average', 'Good', 'Excellent']
# Time Spent count
count = df["Time spent on Online Class"].value_counts()
print("Time spent on Online classes (RESULTS)")
print(count) # print the results

#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:5]

#create pie chart
sns.catplot(x="Rating of Online Class experience",y="Time spent on Online Class", kind="violin" ,order=['Very poor', 'Poor', 'Average', 'Good', 'Excellent'] , data=df) # shows the plot chart
# plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')  # shows pie chart regarding Rating count
plt.show() # display images please choose one graph at a time!