"""
Created on Mon Jan  3 11:34:54 2022

@author: Connor
"""

import pandas as pd

df = pd.read_csv("file.csv", sep = ",")

# User inputs what category of search they wish to perform
choice = input("1 - First Name\n2 - Last Name\n3 - Date of Birth\nChoose the field in which you would like to filter: ")

# Lack of switch statements in python, will use elif because of small scope 
if choice == '1': # user chose first name

  filterBy = input("Please enter First Name you wish to filter by: ") 
  if df[df["first_name"] == filterBy].empty: # check for no result
      print("\nNo results found for First Name: " + filterBy + ", please try again")
  else:
      print (df[df["first_name"] == filterBy]) # if result exists, print
  
elif choice == '2': # user chose last name
  filterBy = input("Please enter Last Name you wish to filter by: ")
  if df[df["last_name"] == filterBy].empty: # check for no result
      print("\nNo results found for Last Name: " + filterBy + ", please try again")
  else:
      print (df[df["last_name"] == filterBy]) # if result exists, print
  
elif choice == '3': # user chose dob
  filterBy = input("Please enter Date of Birth you wish to filter using this format YYYYMMDD: ")
  if df[df["dob"] == filterBy].empty: # check for no result
      print("\nNo results found for DOB: " + filterBy + ", please check your formatting and try again")
  else:
      print (df[df["dob"] == int(filterBy)]) # if result exists, print
else:
  #user chose incorrectly
  print ("\nIncorrect input, please try again using the options listed above")
    
