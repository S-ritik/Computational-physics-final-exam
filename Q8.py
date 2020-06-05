# Q8 - To solve the boundary value problem

import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt

def solext(x):     # Analytical solution at x
    return (np.exp(2)*(np.exp(4)-1)**-1*(np.exp(2*x)-np.exp(-2*x))+x)

def f(x,y):        # Callable function to give right hand side of odes 
    return np.array([y[1],4*(y[0]-x)])

def bc(ya, yb):
    return np.array([ya[0], yb[0]-2])

x=np.linspace(0,1,100)
y_a = np.zeros((2, x.size))
y_b = np.zeros((2, x.size))

# To solve the ode 
sol=si.solve_bvp(f, bc, x, y_a)
y=sol.sol(x)[0]
yexact=np.zeros(len(x))
for i in range(len(x)):
    yexact[i]=solext(x[i])

# To plot the solution
plt.plot(x,y,'r',label="Numerical soluton of y",lw='5')
plt.plot(x,yexact,'c',label="Analytical solution of y")
plt.xlabel("Value of x")
plt.ylabel("Value of function")
plt.title("Plot of Q8 showing solution of ode")
plt.legend()
plt.show()

yerror=np.divide(y-yexact,yexact)*100
print("x                 yerror")
for i in range(len(x)):
    print(x[i],yerror[i])
