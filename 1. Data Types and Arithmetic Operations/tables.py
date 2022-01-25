"""

Jin Young Park
CS5001 Fall 2021
HW1 tables.py
The program runs a robot to assemble a table with a table top, four legs, and eight screws.

Test cases
5 tops, 10 legs, 20 screws => 2 tables assembled. Leftover part: 3 table tops, 2 legs, 4 screws.
20 tops, 50 legs, 100 screws => 12 tables assembled. Leftover part: 8 table tops, 12 legs, 4 screws.
100 tops, 110 legs, 120 screws => 15 tables assembled. Leftover part: 85 table tops, 50 legs, 0 screws.

"""

# User enters the number of table tops, legs, and screws.
number_of_tops = int(input("Number of tops: "))
number_of_legs = int(input("Number of legs: "))
number_of_screws = int(input("Number of screws: "))

# Number of tables can be made out of the table tops, legs, and screws
number_of_tables = min(number_of_tops, number_of_legs // 4, number_of_screws // 8)

# Calculates table tops, legs, screws left after tables were made
remaining_tops = number_of_tops - number_of_tables
remaining_legs = number_of_legs - (number_of_tables * 4)
remaining_screws = number_of_screws - (number_of_tables * 8)

# Output statement for the program: number of tables made and number of leftover parts.
print(number_of_tables, "tables assembled. Leftover part:", remaining_tops,\
      "table tops,", remaining_legs, "legs,", remaining_screws, "screws.")
