start_hour = float(input("Enter the starting hour: "))
start_minute = float(input("Enter the starting minute: "))
time_passed = float(input("Enter the time passed: "))

total_minutes = (start_hour*60) + start_minute + time_passed
total_hours = total_minutes // 60
hour=total_hours
total_minutes = total_minutes % 60
total_hours = hour % 24

print(int(total_hours), ":", int(total_minutes), sep="")
