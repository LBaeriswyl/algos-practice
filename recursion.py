# A couple of basic functions and mathematical operations, implemented via recursion.

# Recursively compute a factorial, where x is not negative
def recursive_factorial(x):
  if x == 1:
    return 1
  if x <= 0:
    return 0
  else:
    return x * recursive_factorial(x-1)

# Recursively add all items in a list
def recursive_sum(list):
  if len(list) == 0:
    return 0
  else:
    return list[0] + recursive_sum(list[1:])

# Recursively count how many items in a list
def recursive_len(list):
  if len(list) == 0:
    return 0
  else:
    return 1 + recursive_len(list[1:])

# Recusively find the max in a list
def recursive_max(list):
  if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
  sub_max = recursive_max(list[1:])
  return list[0] if list[0] > sub_max else sub_max




test_list = [0,3,0,5,7]
print(recursive_factorial(3))
print(recursive_sum(test_list))
print(recursive_len(test_list))
print(recursive_max(test_list))