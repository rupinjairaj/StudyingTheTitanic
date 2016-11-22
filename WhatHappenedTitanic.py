#!usr/bin/python

import pandas as pd
# pylab is an alias for matplotlib.pylab; contains the matplotlib.pyplot
import pylab as plt
import numpy as np

df = pd.read_csv('Data/titanic data.csv')

print df['Pclass'].isnull().value_counts()

print df['Survived'].isnull().value_counts()

''' Which passenger class has the maximum number of survivors '''
print "1) Passenger class with maximum number of survivors"

# Passengers survived in each class
survivors = df['Survived'].groupby(df['Pclass']).agg(sum)
print survivors

# Total passengers in each class
total_passengers = df.groupby('Pclass')['PassengerId'].count()
# Percentage of survivors in each class
survivor_percentage = survivors / total_passengers

print survivor_percentage

# Plotting the total number of survivors
fig = plt.figure()
ax = fig.add_subplot(111)
rect = ax.bar(survivors.index.values.tolist(),
		survivors, color = 'blue', width = 0.5)
ax.set_ylabel('No. of survivors')
ax.set_title('Total number of survivors based on class')
xTickMarks = survivors.index.values.tolist()
ax.set_xticks(survivors.index.values.tolist())
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize = 20)
plt.show()

# plotting the percentage of survivors in each class
fig = plt.figure()
ax = fig.add_subplot(111)
rect = ax.bar(survivor_percentage.index.values.tolist(),
		survivor_percentage, color = 'blue', width = 0.5)
ax.set_ylabel('Survivor Percentage')
ax.set_title('Percentage of survivors based on class')
xTickMarks = survivors.index.values.tolist()
ax.set_xticks(survivors.index.values.tolist())
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize = 20)
plt.show()

''' What is the distribution of survivors based on gender among the various classes '''
print "2) Distribution of survivors based on gender among the various classes"

print df['Sex'].isnull().value_counts()

male_survivors = df[df['Sex'] == 'male'].groupby('Pclass')['Survived'].agg(sum)
print "male survivors"