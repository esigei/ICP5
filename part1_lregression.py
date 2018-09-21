
import numpy as np
import matplotlib.pyplot as plt
import pandas
# Reading data from the excel file
exdata=pandas.read_excel('slr04.xls')
#Reading individual values and putting it in on x,y variables
x=exdata['X']
y=exdata['Y']
#f= lambda mx,b: mx+b
m,b = np.polyfit(x,y,deg=1)
f= lambda x: m*x+b
plt.xlabel('national unemployment rate for adult males')
plt.ylabel('national unemployment rate for adult females')
plt.title('Unemployment Rates')
plt.plot(x,f(x),color='r')
plt.scatter(x,y,color='b')
print(m)
print(b)
plt.show()
