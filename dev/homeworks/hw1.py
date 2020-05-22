#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:13:14 2020

@author: abhijit
"""

#%% preamble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%% gapminder data
gapminder = pd.read_csv('data/gapminder.tsv', sep='\t')

gapminder[:5]
gapminder.head(5)

new_gm = gapminder[['country','gdpPercap','lifeExp']]

canada = gapminder.query('country=="Canada"')
canada = gapminder[gapminder['country']=='Canada']
canada = gapminder.groupby('country').get_group('Canada')

mtcars = pd.read_csv('data/mtcars.csv')
mtcars['kml'] = mtcars['mpg'] * 1.6/3.8

#%% survey data
from glob import glob
fnames = glob('data/survey*.csv')

visited, person, site, survey = [pd.read_csv(f) for f in fnames]
d1 = pd.merge(survey, visited, how='inner', left_on = 'taken', right_on = 'ident')
d2 = pd.merge(survey, person, how = 'outer', left_on = 'person', right_on = 'ident')

#%% weather data
weather = pd.read_csv('data/weather.csv')

## I will melt the data so tha tthe days become a column and their corresponding
## temperatures become a column. Then I'll pivot so that the values of element become column headers

d1 = pd.melt(weather, id_vars = ['id','year','month','element'],
    var_name = 'days', value_name = 'temp')

# Now we need to pivot the temperature data so that the max and min temperatures
# occupy different columns

d2 = d1.pivot_table(index = ['id','year','month','days'], columns = 'element',
    values = 'temp').reset_index()
    
# Last piece is to make the days column numeric so that we can work with it.

d2['days'] = d2.days.str.replace('d','').astype('int')

d2.info()

## We could also convert the year, month and day data into a `datetime` object.

d2['dates'] = pd.to_datetime(d2[['year','month','days']])

d2.info()

## We can also plot these temperatures.

plot_data = d2[['tmin','tmax']]; plot_data.index = d2.dates
plot_data.sort_index(inplace=True)


#%% plots
sns.set_style('whitegrid',{'font.family':'Times New Roman'})
g = sns.relplot(data = plot_data, kind = 'line', dashes=False)

g.set(title='Temperatures over one year')
g.set_ylabels('Temperature (C)')
g.set_xlabels('')
g.set_xticklabels(rotation = 30, ha='left')
g._legend.set_title('Temperature')
new_labels = ['Minimum','Maximum']
for t,l in zip(g._legend.texts, new_labels): t.set_text(l)


#%% Alternative

import datetime
g = sns.relplot(data = plot_data, kind = 'scatter')

g.set(xlim = (datetime.date(2010,1,1),datetime.date(2010,12,31)))
g.set(title='Temperatures over one year')
g.set_ylabels('Temperature (C)')
g._legend.set_title('Temperature')
new_labels = ['Minimum','Maximum']
for t,l in zip(g._legend.texts, new_labels): t.set_text(l)

g.fig.autofmt_xdate()

#%% Matplotlib

import datetime
d2 = d2.sort_values(by='dates')
fig, ax = plt.subplots()
ax.plot(d2.dates, d2.tmin, 'blue', label = 'Minimum')
ax.plot(d2.dates, d2.tmax, 'orange', label = 'Maximum')

ax.set(xlim = (datetime.date(2010,1,1), datetime.date(2010,12,31)))
ax.set_title('Temperatures over one year')
ax.set_ylabel('Temperature (C)')
ax.set_xlabel('')
ax.legend(title = 'Temperature', loc=(.85,.85))
fig.autofmt_xdate()

