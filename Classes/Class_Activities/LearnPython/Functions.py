# this activity, you will write a function to compute the arithmetic mean (average) for a list of numbers.

num_list = []
sum = 0
For i = 1 to 8:
  num = input("Enter number: ")
  num_list.append(num)

def num_list_average(nums):
  for num in nums:
    sum = sum + num
  avg = sum/len(nums)
  return avg
calc_avg = num_list_average(num_list)
print(calc_avg)


