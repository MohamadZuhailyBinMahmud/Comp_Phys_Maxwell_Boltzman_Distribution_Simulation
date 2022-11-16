import numpy as np
import matplotlib.pyplot as plt
import random
import ROOT

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

#print(theory(mass4He,tempt,vel))

x = int(random.random)
print(x)

