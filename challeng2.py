#!/usr/bin/python3
# import libraries for random and mean functions
import random
import statistics

# function to get total of rolled numbers
def getTotal(array):
  total = 0
  for num in array:
    total += num

  return total

# function to get average of the rolled numbers
def getAvg(array):
  x = statistics.mean(array)
  return x

# First loop that controls prompting user input for number of rolls
ii = 0

# stores dice rolled 
rollArray = []

while ii < 1:
  num=0
  while num not in range(1, 99, 1):
    try:
      num = int(input('How many dice would you like to roll (1-99)? '))
    except ValueError:
        continue
    print("\n")

  i = 1
  
  # Store current rolls
  rollArrayCur = []
  # second loop to roll dice based on user's input
  while i <= num:
    i += 1
    dice=random.randint(1,6)
    rollArrayCur.append(dice)
    rollArray.append(dice)

  # Print the array, its total and mean values
  print("Rolls list = " ,rollArrayCur)
  print("Total = ", getTotal(rollArray))
  print("Avg = ", str(round(getAvg(rollArray), 2)))
  print("***************************\n")

  # Prompt user to roll again. If input is not 'y' then exit program
  ii += 1
  if input("Roll again?(y/[n]) ") == 'y':
    print("\n")
    ii = 0  
  else:
    # Print the ilifetime summary array, its total and mean values
    print("Rolls list = " ,rollArray)
    print("Total = ", getTotal(rollArray))
    print("Avg = ", str(round(getAvg(rollArray), 2)))
    print("***************************\n")
    print('End')
