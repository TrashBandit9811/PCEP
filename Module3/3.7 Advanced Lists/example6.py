temps = [[0.0 for h in range(24)] for d in range(31)]

# The list is filled with some values

total = 0.0

for day in temps:
    total +=day[11]
# Day is a list of 24 elements, so day[11] is the temperature at 11:00

average = total / 31

print("Average temperature at 11:00 is", average)

highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

