import numpy as np
import matplotlib.pyplot as plt

k = 1.380649*10**(-23)
tempt = [300,400,500]
vel = np.arange(0,2000,1)
amu = 1.66e-27
mass = 85*amu


def theory(m,T,v):
  a = (m/(2*np.pi*k*T))**(3/2)
  b = 4*np.pi*v**(2)
  x = (m*v**(2))/(2*k*T)
  c = np.exp(-x)
  return a*b*c
  
fig = plt.figure(figsize=(12,9))
ax1=fig.add_subplot()
ax1.plot(vel, theory(mass,tempt[0],vel), label = '16O', color = 'red', linestyle = '--') # plotting for theoretical value
ax1.plot(vel, theory(mass,tempt[1],vel), label = '16O', color = 'blue', linestyle = '--') # plotting for theoretical value
ax1.plot(vel, theory(mass,tempt[2],vel), label = '16O', color = 'green', linestyle = '--') # plotting for theoretical value
ax1.set_xlabel('Velocity')
ax1.set_ylabel('Probablity')
ax1.title.set_text('Simulation of Maxwell-Boltzman Distribution')
ax1.legend()
fig.savefig("TheoryTest.pdf")
