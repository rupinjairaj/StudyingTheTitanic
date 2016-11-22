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
print "Total survivors grouped by class {0}".format(survivors)

# Total passengers in each class
total_passengers = df.groupby('Pclass')['PassengerId'].count()
# Percentage of survivors in each class
survivor_percentage = survivors / total_passengers

print "Percentage of survivors in each class {0}".format(survivor_percentage)

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

# male passengers survived in each class
male_survivors = df[df['Sex'] == 'male'].groupby('Pclass')['Survived'].agg(sum)
print "Total male survivor count in each class{0}".format(male_survivors)

# total male grouped by class
male_total_passengers = df[df['Sex'] == 'male'].groupby('Pclass')['PassengerId'].count()
print "Total male passengers in each class {0}".format(male_total_passengers)

male_survivor_percentage = male_survivors / male_total_passengers
print "Percentage of male survivors in each class {0}".format(male_survivor_percentage)

# female passenger survived in each class
female_survivors = df[df['Sex'] == 'female'].groupby('Pclass')['Survived'].agg(sum)
print "Female survivors count in each class{0}".format(female_survivors)

# total female passenger count grouped by class 
female_total_passengers = df[df['Sex'] == 'female'].groupby('Pclass')['PassengerId'].count()
print "Female survivors in each class {0}".format(female_total_passengers)

# percentage of female survivors grouped by class
female_survivor_percentage = female_survivors / female_total_passengers
print "Percentage of female survivors in each class {0}".format(female_survivor_percentage)

# plotting the gender based count of passengers who survived
fig = plt.figure()
ax = fig.add_subplot(111);
index = np.arange(male_survivors.count())
bar_width = 0.35
rect1 = ax.bar(index, male_survivors, bar_width, color = 'blue', label = 'Men')
rect2 = ax.bar(index+bar_width, female_survivors, bar_width, color = 'green', label = 'Women')
ax.set_ylabel('Survivor Numbers')
ax.set_title('Male and Female survivor count based on class')
xTickMarks = male_survivors.index.values.tolist()
ax.set_xticks(index + bar_width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize = 20)
plt.legend()
plt.tight_layout()
plt.show()

# Plotting the percentage of survivors 
fig = plt.figure()
ax = fig.add_subplot(111)
index = np.arange(male_survivor_percentage.count())
bar_width = 0.35
rect1 = ax.bar(index, male_survivor_percentage, bar_width, color = 'blue', label = 'Men')
rect2 = ax.bar(index + bar_width, female_survivor_percentage, bar_width, color = 'green', label = 'Women')
ax.set_ylabel('Survivor Percentage')
ax.set_title('Percentage of Male and Female survivors based on class')
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize = 20)
plt.legend()
plt.tight_layout()
plt.show() 