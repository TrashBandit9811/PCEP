year = int(input("Enter a year: "))

year_type="Common year"

if year < 1582:
	print("Not within the Gregorian calendar period")
elif year % 4 == 0:
    year_type="Leap year"
elif year % 400 == 0:
    year_type="Leap year"

print(year_type)
	