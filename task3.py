import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

data= pd.read_csv('C:\\Users\\Vasudev\\Downloads\\householdtask3.csv')

a=data.head(10)
print(a)

# scatter plot with year againest own
plt.scatter(data['year'],data['own'])

# Adding title to the plot
print(plt.title('Scatter plot'))

# setting the x and y label
print(plt.xlabel('year'))
print(plt.ylabel('own'))

# showing the chart
print(plt.show())

# line chart with year againest own
print(plt.plot(data['year']))
print(plt.plot(data['own']))

# Adding title to the plot
print(plt.title('Line chart'))

# setting the x and y label
print(plt.xlabel('year'))
print(plt.ylabel('own'))

print(plt.show())

# Bar chart or bar plot 
print(plt.bar(data['year'],data['own']))

# Adding title to the plot
print(plt.title('Bar chart'))

# setting the x and y label
print(plt.xlabel('year'))
print(plt.ylabel('own'))

print(plt.show())

# histogram
print(plt.hist(data['income']))
print(plt.title('Histogram'))
print(plt.show())