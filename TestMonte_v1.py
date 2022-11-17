import numpy as np
import matplotlib.pyplot as plt
import random

k = 1.380649*10**(-23)
tempt = 300
vel = np.arange(0,2000,1)
mass16O = 2.6569e-26 #mass of a single atom in kg (not equal to atomic mass unit)
mass4He = 6.6422e-27

def theory(m,T,v):
  a = (m/(2*np.pi*k*T))**(3/2)
  b = 4*np.pi*v**(2)
  x = (m*v**(2))/(2*k*T)
  c = np.exp(-x)
  return a*b*c

def monte():
  
  def chance(m,T,v):
    a = (m/(2*np.pi*k*T))**(3/2)
    b = 4*np.pi*v**(2)
    x = (m*v**(2))/(2*k*T)
    c = np.exp(-x)
    x = 1
    
  n = 100
  count = np.zeros(n)
  r = random.random()
  print(r)
   
#print(theory(mass4He,tempt,vel))

x = random.random
print(x)

