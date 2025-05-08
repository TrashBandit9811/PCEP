my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    while my_list.count(i) > 1:
        my_list.remove(i)

print("The list with unique elements only:")
print(my_list)

