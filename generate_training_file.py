import csv
import pandas as pd
import random

random_number_list = []

#3 columns in trining data : title 1, title 2, yes/no
training_set_column_1 = []
training_set_column_2 = []
training_set_column_3 = []

for x in range(300):
  random_number_list.append(random.randint(5,1000))

df = pd.read_csv('processed_data.csv', header = None, sep = ',',skipinitialspace=True)
#denote the number of rows to check top and bottom of a random row
skip_row = 1

#Add similar titles in training data. In general, items that have similar titles occur together in the dataset.
#Thus, we generate random numbers and add neighbours(bottom and top) of the random_number row.
for i in random_number_list:
    for j in range(skip_row):
        training_set_column_1.append(df.iloc[i][1])
        training_set_column_2.append(df.iloc[i-(j+1)][1])
        training_set_column_3.append('Y')

    for j in range(skip_row):
        training_set_column_1.append(df.iloc[i][1])
        training_set_column_2.append(df.iloc[i+(j+1)][1])
        training_set_column_3.append('Y')

#Add disimilar items to training data
for i in random_number_list:
    training_set_column_1.append(df.iloc[i][1])
    training_set_column_2.append(df.iloc[i+random.randint(10,30)][1])
    training_set_column_3.append('N')

#Print training set for product titles
for i in range(len(training_set_column_1)):
    print(training_set_column_1[i] + ' || ' + training_set_column_2[i] + ' || ' + training_set_column_3[i])
