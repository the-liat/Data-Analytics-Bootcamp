# House of Pies

"""In this activity, you will build an order form that displays a list of pies and then prompts users to make a selection. The form will continue to prompt for selections until the user decides to end the process.

## Instructions

* Create an order form that displays a list of pies to the user in the following way:


```
Welcome to the House of Pies! Here are our pies:

---------------------------------------------------------------------
(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
```

* Then, prompt the user to enter the number for the pie they would like to order.

* Immediately follow up their order with `Great! We'll have that <PIE NAME> right out for you`, and then ask if they would like to make another order. If so, repeat the process.

* Once the user is done purchasing pies, print the total number of pies ordered.

## Bonus

* Modify the application so that at the conclusion of the transaction, the user's purchases are listed out, with the total pie count broken by _each_ pie. For example:

```
You purchased:
0 Pecan
0 Apple Crisp
0 Bean
2 Banoffee
0 Black Bun
0 Blueberry
0 Buko
0 Burek
0 Tamale
1 Steak
"""

# The list of pies to print to the screen
pies_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee",  "Black Bun","Blueberry", "Buko", "Burek",  "Tamale, Steak"]
print("Welcome to the House of Pies! Here are our pies:")
print("-" * 100)
for pie in pies_list:
    pie_num = pies_list.index(pie) + 1
    print("[" + str(pie_num) + "] " + pie)

# user pie choices
pie_choice = int(input("Enter the number for the pie you would like to order: "))
print("Great! We'll have that " + str(pie_choice) + " right out for you")
pie_cart = [pies_list[pie_choice-1]]
# The list used to store all of the candies selected inside of
while more_pie == 'y':
    pie_cart.append(pies_list[pie_choice-1])
    more_pie = int(input("Would you like to make another order? type (y)es or (n)o. "))
    pie_choice = int(input("Enter the number for the pie you would like to order: "))
    
    

# Print out options
print("I brought home with me....")
for pie in pies_cart:
    print(pie)
