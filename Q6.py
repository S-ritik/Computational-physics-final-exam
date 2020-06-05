# Q6 - To solve 2 coupled odes

import numpy as np
import scipy.integrate as  si
import matplotlib.pyplot as plt

def f(x,y):        # Callable function to give right hand side of odes 
    return [32*y[0]+66*y[1]+2*x/3+2/3,-66*y[0]-133*y[1]-1*x/3-1/3]

# To solve the ode 
sol=si.solve_ivp(f,[0,0.5],[1/3,1/3])
x=sol.t
y1=sol.y[0,:]
y2=sol.y[1,:]

# To plot the solution
plt.plot(x,y1,'r',label="Soluton of y1")
plt.plot(x,y2,'c',label="Solution of y2")
plt.xlabel("Value of x")
plt.ylabel("Value of function")
plt.title("Plot of Q6 showing solution of odes")
plt.legend()
plt.show()
