# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:32:42 2023

@author: Md Monir Hossain
Student ID: 22080904
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_excel('Global_Estimates.xlsx')

print(data.head(5))

# Display summary statistics
print(data.describe())


def stacked_plot(data):
    """
  Create a stacked area chart of Gas, Liquids, and Solids over the Years.

  Args:
      data (pandas DataFrame): The input data containing columns 'Year', 'Gas', 'Liquids', 'Solids'.

  """

    plt.figure(figsize=(10, 6))
    plt.stackplot(data['Year'], data['Gas'], data['Liquids'],
                  data['Solids'], labels=['Gas', 'Liquids', 'Solids'])
    plt.title('Stacked Area Chart of Gas, Liquids, and Solids over the Years')
    plt.xlabel('Year')
    plt.ylabel('Amount')
    plt.legend(loc='upper left')
    plt.show()


def scatter_plot(data):
    """
   Create a scatter plot of Production vs Flaring.

   Args:
       data (pandas DataFrame): The input data containing columns 'Production' and 'Flaring'.

   """

    plt.figure(figsize=(8, 6))
    plt.scatter(data['Production'], data['Flaring'])
    plt.title('Production vs Flaring')
    plt.xlabel('Production')
    plt.ylabel('Flaring')
    plt.show()


def bar_plot(data):
    """
   Create a bar plot showing the sum of Gas, Liquids, and Solids by Year.

   Args:
       data (pandas DataFrame): The input data containing columns 'Year', 'Gas', 'Liquids', 'Solids'.

   """
    # Calculate the sum of Gas, Liquids, and Solids for each row and
    sum_gas_liquids_solids = data[['Gas', 'Liquids', 'Solids']].sum(axis=1)

    plt.figure(figsize=(10, 6))
    plt.bar(data['Year'], sum_gas_liquids_solids)
    plt.title('Sum of Gas, Liquids, and Solids by Year')
    plt.xlabel('Year')
    plt.ylabel('Total Amount')
    plt.show()


# below call 3 types of plot to show
stacked_plot(data)
scatter_plot(data)
bar_plot(data)
