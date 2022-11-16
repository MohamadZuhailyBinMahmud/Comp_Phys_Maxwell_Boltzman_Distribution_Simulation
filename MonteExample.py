'''
Name : Mohamad Zuhaily Bin Mahmud
Student ID : U2004495

'''
###############################################################################
#Import Library
###############################################################################
import numpy as np
import matplotlib.pyplot as plt
import random

###############################################################################
#Constant
###############################################################################

t_half = 10 #--------half life
N0 = 1000 #--initial number of atom
t1 = 60 #----total time for x-axis
n_intervals = 60 #----number of interval for x-axis


###############################################################################
#Global variable
###############################################################################

dt = t1 / n_intervals #Calculating the interval between each time division
p_decay = 1 - pow(2,(-dt/t_half)) #Calculating the decay probabilities in a time interval
timebase = np.arange(0, t1, dt) #creating the array of times for use in the analytic solution and scipy

###############################################################################
#Generate monte carlo simulation
###############################################################################

def simulate_monte_carlo(N0, n_intervals):

    ###########################################################################
    '''
    count = counter-type variable that will count number of atom that have not decay
    count_decay = counter-type variable that will count number of atom that have decay
    atoms = create 1000 individual atoms

    '''
    ###########################################################################
    count   = np.zeros((n_intervals)) #creating zero arrays to put the counts into
    count_decay   = np.zeros((n_intervals)) #creating zero arrays to put the counts into
    atoms   = np.ones((N0)) #Creating an array of numbers to represent the atoms in the simulation

    ###########################################################################
    #Nested loop process to count decayed number of atom in each interval
    ###########################################################################
    
    
    for x in range(n_intervals): #for initial x=0, while (x < n_timpoints),loop (increase x by 1 after each loop until condition is met) where x is interval time
        
        '''Counting how many atoms of each type remain in the interval
        in this case x = current time interval eg : interval 1, 2, 3,..., 60'''
        
        count[x]   = (atoms == 1).sum() #(atoms == 1).sum() count how many elements in variable atoms is equal to 1...element = 1 show that is still havent decay
                                               # and set it equal to the xth element in count

        count_decay[x]   = (atoms == 2).sum() #(atoms == 2).sum() count how many elements in variable atoms is equal to 2...element = 2 show that is still have decay
                                               # and set it equal to the xth element in count_decay
        
        
        for y in range(N0): #for intial y=0, while (y < N0),loop (increase y by 1 after each loop until condition is met) where y is individual atom eg : atom 1,2,3...,1000
            
            if atoms[y] == 1: #if individual atom have not decay (element value = 1)..proceed to test
                r = random.random() #generate random probability that the atom will decay or not (from 0 until 1)
                if r < p_decay: #if r <= p_decay atom will decay...since we set the atom that does not decay to 1...atom that decay can be changed into any appropiate number
                    atoms[y] = 2 #in this case change it to 2
                else:
                    atoms[y] = 1 #set to 1 for atom that does not decay


    return count, count_decay

###############################################################################
#Define plot value
###############################################################################

halflife  = timebase/t_half
theory = N0 * pow(2,(-timebase/t_half))
n_count, n_decay  = simulate_monte_carlo(N0, n_intervals) #Calling the Monte Carlo Simulation

###############################################################################
#Plotting
###############################################################################

fig = plt.figure(figsize=(12,9))
ax1=fig.add_subplot()
ax1.plot(halflife, n_count, label = 'Remaining Atom, Monte Carlo', color = 'blue') #plotting for remaining atom
ax1.plot(halflife, n_decay, label = 'Decayed Atom, Monte Carlo', color = 'yellow') #plottoing for decayed atom
ax1.plot(halflife, theory, label = 'Theory', color = 'red', linestyle = '--') # plotting for theoretical value
ax1.set_xlabel('Half Lifes')
ax1.set_ylabel('Number of atoms')
ax1.title.set_text('Mohamad Zuhaily Bin Mahmud,U2004495\nMonte Carlo Simulation of Radioactive Decay')
ax1.legend()
fig.savefig("MonteExample.pdf")