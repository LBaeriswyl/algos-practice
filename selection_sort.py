# Sort array of numbers from largest to smallest
# Time complexity of O(n^2)

def find_largest(list):
  largest = list[0]
  largest_index = 0

  for i in range(1, len(list)):
    if list[i] > largest:
      largest = list[i]
      largest_index = i
  return largest_index

def selection_sort(list):
  new_list = []
  
  for i in range(len(list)):
    largest = find_largest(list)
    new_list.append(list.pop(largest))
  return new_list

test_list = [4, 3, 15, 46, 2, 0, 67]
print(selection_sort(test_list))