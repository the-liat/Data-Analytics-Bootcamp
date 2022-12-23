'''1. Create a dictionary to store the following information:

* Your name
* Your age
* A list of a few of your hobbies
* A dictionary that includes a few days and the time you typically wake up on those days# '''

info_dict = {"name": "Liat", "age": 40, "hobbies": ["cooking", "exercising", "playing piano"], "wake": {"sunday": 7.5, "monday": 8,"tuesday": 6.5}}
print(f'Your name: {info_dict["name"]}')
print(f'number of hobbies: {len(info_dict["hobbies"])}')
print(f'time you wake up on tuesday: {info_dict["wake"]["tuesday"]}')