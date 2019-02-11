import numpy as np
import random
'''

@Author: Terrell Green

Task: Given a text file of ages, create 5 new sets of 100 ages, and calculate the mean of each set
		The datasets are to be created from random sampling the original data set. Each value of the original can appear
		appear any number of times or none at all in each of the new sets


'''




'''
Implementation: First create new array from extracting data from the txt file while ignoring the first line.
This was done to avoid creation of an invalid type, as the first entry in the 'dataforanalysttask.txt' file would be the string "ages"
not a number. Although dealing with ages, this implementation handles dealing with both ints and doubles

'''
data= np.genfromtxt('dataforanalysttask.txt',skip_header=1)
#print(data)

#create new array with random sampling with replacement
randomdata=[random.choice(data) for _ in data]





for i in randomdata:
    print(i)

#use numpy to calculate mean of randomdata array
print("Calculated Mean is: ", np.mean(randomdata))


