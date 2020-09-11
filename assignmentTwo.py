import re
import statistics

# Getting user input
print("###This program will give you sum, mean and median ###\n")

userInput = input("Input a string: \n")

# Funtion for sum
def find_sum(str1): 
    return sum(map(int,re.findall('\d+',userInput))) 

# Funtion for mean
def find_mean(str1): 
    return statistics.mean(map(int,re.findall('\d+',userInput))) 

# Funtion for median
def find_median(str1): 
    return statistics.median(map(int,re.findall('\d+',userInput))) 
  
# Printing all data for user
print("Sum: ", find_sum(userInput)) 
print("Mean: ", find_mean(userInput))
print("Median: ", find_median(userInput))
