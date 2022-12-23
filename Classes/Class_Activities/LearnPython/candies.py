# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]
for candy in candy_list:
    print("[" + str(candy_list.index(candy)) + "] " + candy)

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []
i = 0
while i < allowance:
    choice = int(input("Which candy would you like? (type number) "))
    candy_cart.append(candy_list[choice])
    i = i + 1

# Print out options
print("I brought home with me....")
for candy in candy_cart:
    print(candy)

 