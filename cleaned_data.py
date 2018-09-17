#JULIAN WAUGH 9/17, script for exploring data and cleaning adta
#from sklearn import linear_model as lm
import numpy as np
import pandas as pd


#import the data
train = pd.read_csv('train.csv')

# clean data
# replace NaN in age with the median age of all other ones (also try dropping those rows later)

train_copy = train
median_age = np.median(train.Age.dropna().values)
median_age = np.around(median_age, decimals = 1)

train_age = train.Age.fillna(median_age)
train.Age = train_age


#now, replace male/ female column with 1 if male, 0 if female

sexes = list(train.Sex.values)

new_sexes = []
for sex in sexes:
    if sex == 'male':
        new_sexes.append(1)
    else:
        new_sexes.append(0)
new_sexes = np.array(new_sexes)
train.Sex = new_sexes

