my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

# Output: []
# Explanation: The slice my_list[-1:1] starts at index -1 (which is the last element, 2) and goes up to index 1 (which is the second element, 8). Since the start index is greater than the end index, the result is an empty list.