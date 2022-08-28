# Implement basic binary search using a while loop
# Find an item in a *sorted* list of numbers and return the index or 0

def binary_search(list, item):
  low = 0
  high = len(list)-1
  
  while low <= high:
    pointer_index = (low + high) // 2
    pointer_item = list[pointer_index]

    if pointer_item == item:
      return pointer_index
    if pointer_item > item:
      high = pointer_index - 1
    else:
      low = pointer_index + 1
  
  return None



test_list = [1,3,5,6,8,9,13,33,34,35,36]
print(binary_search(test_list, 33))