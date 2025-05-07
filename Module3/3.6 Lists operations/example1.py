list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# The output of this code will be [2] because list_2 is a reference to list_1.
# When we modify list_1, it also affects list_2 since they are the same list in memory.
