# Load libraries
import pandas 
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

from pandas import DataFrame
import numpy as numpy



# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)




# shape
print(dataset.shape)

# head
print(dataset.head(80))

# descriptions
print(dataset.describe())

df=dataset

print ("sepal-length mean is",(dataset.loc[:,"sepal-length"].mean()) )
print ("petal-length mean is",(dataset.loc[:,"petal-length"].mean()))
print ("sepal-width mean is",(dataset.loc[:,"sepal-width"].mean()))
print ("petal-width mean is",(dataset.loc[:,"petal-width"].mean()))



# class distribution
print(dataset.groupby('class').size())