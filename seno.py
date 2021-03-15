import numpy as np 
import matplotlib.pyplot as plt

pi = 3.1416
x=np.arange(0,2*pi,0.1)
y=np.sin(x)  
plt.plot(x,y)
plt.show()
