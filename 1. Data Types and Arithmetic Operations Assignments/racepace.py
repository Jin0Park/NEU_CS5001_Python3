"""

Jin Young Park
CS5001 Fall 2021
HW1 racepace.py
The program calculates statistics about a race time with runner's distance and finish time.

Test cases
10km, 1 hours, 20 minutes => 6.21 miles, 12:53 pace, 4.66 MPH
15km, 5 hours, 00 minutes => 9.32 miles, 32:12 pace, 1.86 MPH
5km, 1 hours, 10 minutes => 3.11 miles, 22:32 pace, 2.66 MPH

"""

# User enters the distance in km, hours and minutes of final time.
number_of_km = int(input("How many kilometers did you run? "))
number_of_hours = int(input("What was the finish time? Enter hours: "))
number_of_minutes = int(input("Enter minutes: "))

# Converts the distance in km to miles.
number_of_miles = number_of_km / 1.61
# Convert the finish time to minutes.
total_minutes = (number_of_hours * 60 + number_of_minutes)

# Calculates the average pace per mile.
pace_raw = total_minutes / number_of_miles
# Take the integer place from the pace calculation to the value for minutes in pace.
pace_minutes = int(pace_raw)
# Converts the decimal places of the pace calculation to the value for seconds in pace.
pace_seconds = int(round((pace_raw - pace_minutes) * 60 / 100, 2) * 100)
# Using Python's built-in str function to print out the pace per mile output.
pace = str(pace_minutes) + ":" + str(pace_seconds)

# Calculates the average speed in miles per hour.
mph = number_of_miles / total_minutes * 60

# Output statement for the program: number of miles, average pace per mile, average speed in mph. 
# Round distance and mph to 2 decimal points.
print(round(number_of_miles, 2), "miles,", pace, "pace,", round(mph, 2), "MPH")