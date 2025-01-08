import tkinter as tk
from tkinter import messagebox
import csv

# do verify with the fact that it will change all of the formatting for the the rows in the selected column for the hard coded format that is for each one
# need to be able to validate the different fields like address and email
# populate the column drop downs and make sure that the email and such are valid
# verify the emails have @ and . e.g. "aaaa@aaa.a" is valid 
# create a function called "proper" that will make the first letter capitalized of every name, including in emails and addresses

read_rows = 0
successful_rows = 0
errors = 0


def verify(file_path, dropdown_options, fields, field_dict):
    print("\n\nVERIFY FUNCTION")
    print("OLD VALUES----------------------")
    for x in field_dict:
        print(x, " : ", field_dict[x])
    #stuff
    print("NEW VALUES----------------------")
    for x in field_dict:
        print(x, " : ", field_dict[x])
    pass

'''

def proper(): # function to properly capitalize names
    header = 
    for 
    # Function for each sort of formatting and verification dependent on the selected field
    
    
    # need to print out each of the functions into 

    # for names, apostrophes 
    pass

def push_errors():
    # push out the error columns into the error button

    pass'''