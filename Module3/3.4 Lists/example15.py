my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(my_list)

# Reverse the list in place
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)