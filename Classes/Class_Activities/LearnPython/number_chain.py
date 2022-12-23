# Number Chain

# In this activity, you will take user input and print out a string of numbers.

## Instructions

# Using a `while` loop, ask the user "How many numbers?", 
# and then print out a chain of numbers in increasing order, from 0 to the user-input number.
def user_input_num_to_count():
    user_num = int(input("How many numbers? "))
    i = 0
    while i <= user_num:
        print(i)
        i = i + 1
    return

user_input_num_to_count()

# After the results have been printed, ask the user if they would like to continue.
continue_que = input("Would you like to continue (y/n?) ")

# If "y" is entered, keep the chain running by inputting a new number 
# and starting a new count from 0 to the new user-input number.
while continue_que == "y":
    user_input_num_to_count()
    continue_que = input("Would you like to continue (y/n?) ")


## Bonus

'''Rather than just displaying numbers starting from 0, 
have the numbers begin at the end of the previous chain.'''
