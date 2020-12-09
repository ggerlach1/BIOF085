#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 08:13:14 2020

@author: abhijit
"""

#Answers to the exersizes done above, there is more than one correct to do many of these 
#this is a good example of efficient code and there are also explinations

#%% preamble
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%% Data transformations
mtcars = pd.read_csv('data/mtcars.csv')
mtcars['kml'] = mtcars['mpg'] * 1.6/3.8




#%% gapminder data - data concatination 
gapminder = pd.read_csv('data/gapminder.tsv', sep='\t')

gapminder[:5]
gapminder.head(5)

new_gm = gapminder[['country','gdpPercap','lifeExp']]

canada = gapminder.query('country=="Canada"')
canada = gapminder[gapminder['country']=='Canada']
canada = gapminder.groupby('country').get_group('Canada')

#%% survey data -data merging 
from glob import glob
fnames = glob('data/survey*.csv')

person, site, survey, visited = [pd.read_csv(f) for f in fnames]

d1 = pd.merge(survey, visited, how='inner', left_on = 'taken', right_on = 'ident')
d2 = pd.merge(survey, person, how = 'outer', left_on = 'person', right_on = 'ident')

#%% weather data - tidy data and reshaping data 
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

#%% Split apply Combine

data = pd.read_csv('data2/gapminder.tsv', sep = '\t')
data

con = data.groupby('continent')['gdpPercap'].agg(np.median)

year = data.groupby('year')['gdpPercap'].agg(np.median)
year


#%%



