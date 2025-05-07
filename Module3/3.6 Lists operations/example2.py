list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# The output of this code will be [1] because list_2 is a shallow copy of list_1.
# When we modify list_1, it does not affect list_2 since they are two separate lists.
# This is an example of how to create a shallow copy of a list in Python.