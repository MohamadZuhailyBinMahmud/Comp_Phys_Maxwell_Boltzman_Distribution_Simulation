import numpy as np
import matplotlib.pyplot as plt

k = 1.380649*10**(-23)
tempt = 300
vel = np.arange(0,2500,1)
mass16O = 2.6569e-26 #mass of a single atom in kg (not equal to atomic mass unit)
mass4He = 6.6422e-27

def theory(m,T,v):
  a = (m/(2*np.pi*k*T))**(3/2)
  b = 4*np.pi*v**(2)
  x = (m*v**(2))/(2*k*T)
  c = np.exp(-x)
  return a*b*c
  
fig = plt.figure(figsize=(12,9))
ax1=fig.add_subplot()
ax1.plot(vel, theory(mass16O,tempt,vel), label = '16O', color = 'red', linestyle = '--') # plotting for theoretical value
ax1.plot(vel, theory(mass4He,tempt,vel), label = '4He', color = 'blue', linestyle = '--') # plotting for theoretical value
ax1.set_xlabel('Velocity')
ax1.set_ylabel('Probablity')
ax1.title.set_text('Simulation of Maxwell-Boltzman Distribution')
ax1.legend()
plt.show()
