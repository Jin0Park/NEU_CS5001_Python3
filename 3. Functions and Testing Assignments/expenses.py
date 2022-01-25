"""

Jin Young Park
CS5001 Fall 2021
HW3 expenses.py
The program calculates business trip driving expenses.
Contains four functions: calculate_mileage, get_reimbursement_amount,
                         get_actual_mileage_rate, get_actual_trip_cost.

Test cases:
1)
MILEAGE REIMBURSEMENT CALCULATOR
 Options:
 1 - Calculate reimbursement amount from odometer readings
 2 - Calculate reimbursement amount from miles traveled
 3 - Calculate the actual cost of your trip
Enter your choice (1, 2, or 3): 1
Enter your starting odometer reading: 1000
Enter your ending odometer reading: 1010
You will be reimbursed $5.75

2)
MILEAGE REIMBURSEMENT CALCULATOR
 Options:
 1 - Calculate reimbursement amount from odometer readings
 2 - Calculate reimbursement amount from miles traveled
 3 - Calculate the actual cost of your trip
Enter your choice (1, 2, or 3): 2
Enter the number of miles traveled: 10
You will be reimbursed $5.75

3)
MILEAGE REIMBURSEMENT CALCULATOR
 Options:
 1 - Calculate reimbursement amount from odometer readings
 2 - Calculate reimbursement amount from miles traveled
 3 - Calculate the actual cost of your trip
Enter your choice (1, 2, or 3): 3
Enter your starting odometer reading: 1000
Enter your ending odometer reading: 1010
Enter your car's MPG: 36
Enter the fuel price per gallon: 3.09
Your trip cost $0.86

4)
MILEAGE REIMBURSEMENT CALCULATOR
 Options:
 1 - Calculate reimbursement amount from odometer readings
 2 - Calculate reimbursement amount from miles traveled
 3 - Calculate the actual cost of your trip
Enter your choice (1, 2, or 3): 4
Not a valid choice

"""


def main():
    print("“MILEAGE REIMBURSEMENT CALCULATOR\n",
          "Options:\n",
          "1 - Calculate reimbursement amount from odometer readings\n",
          "2 - Calculate reimbursement amount from miles traveled\n",
          "3 - Calculate the actual cost of your trip")
    answer = int(input("Enter your choice (1, 2, or 3): "))
    if answer == 1:
        start = float(input("Enter your starting odometer reading: "))
        end = float(input("Enter your ending odometer reading: "))
        mileage = float(calculate_mileage(start, end))
        get_reimbursement_amount(mileage)
    elif answer == 2:
        mileage = float(input("Enter the number of miles traveled: "))
        get_reimbursement_amount(mileage)
    elif answer == 3:
        start = float(input("Enter your starting odometer reading: "))
        end = float(input("Enter your ending odometer reading: "))
        mpg = float(input("Enter your car's MPG: "))
        fuel_price = float(input("Enter the fuel price per gallon: "))
        get_actual_trip_cost(start, end, mpg, fuel_price)
    else:
        print("Not a valid choice")


def calculate_mileage(start, end):
    """
        Function -- calculate_mileage
            Calculates miles driven using the start and end odometer values.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
                number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
                number greater than 0 and greater than the start value.
        Returns:
            The miles driven, a number. If either parameter is invalid (e.g.
            either parameter is negative or end is less than start), return 0.
    """
    # Invalid case
    if start < 0 or end < 0 or start > end:
        return 0
    # Valid case. Mileage could be calculated by subtracting start odometer
    # value by end odometer value.
    else:
        mileage = end - start
        return mileage


def get_reimbursement_amount(mileage):
    """
        Function -- get_reimbursement_amount
            Calculates the amount in dollars that the employee should be
            reimbursed based on their mileage and the standard rate per mile.
            The standard rate for 2020 is 57.5 cents per mile.
        Parameters:
            mileage -- The number of miles driven.
        Returns:
            The amount the employee should be reimbursed in dollars, a float
            rounded to 2 decimal places.
    """
    # Employee gets reimbursed is standard rate per mile times their mileage.
    reimbursement = mileage * 0.575
    print("You will be reimbursed ${:.2f}".format(reimbursement))
    return reimbursement


def get_actual_mileage_rate(mpg, fuel_price):
    """
        Function -- get_actual_mileage_rate
            Calculates the actual trip cost per mile in dollars based on the
            car's MPG and the fuel price.
        Parameters:
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel cost in dollars per gallon, a non-negative
            float.
        Returns:
            The actual cost per mile in dollars, a float rounded to 4 decimal
            places. If supplied arguments are invalid, returns 0.0
    """
    # Invalid case
    if mpg < 0 or fuel_price <= 0:
        return 0.0
    # Valid case. Mileage rate is calculated by dividing fuel cost by
    # car's miles per gallon.
    else:
        actual_mileage_rate = round(fuel_price / mpg, 4)
        return actual_mileage_rate


def get_actual_trip_cost(start, end, mpg, fuel_price):
    """
        Function -- get_actual_trip_cost
            Calculates the cost of a trip in dollars based on the miles driven,
            the MPG of the car, and the fuel price per gallon.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
                number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
                number greater than 0 and greater than the start value.
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel price per gallon, a non-negative float.
        Returns:
            The cost of the drive in dollars, a float rounded to 2 decimal
            places. If any of the supplied arguments are invalid, returns 0.0
    """
    # Invalid case
    if start < 0 or end < 0 or end < start or mpg < 0 or fuel_price <= 0:
        trip_cost = 0.0
    # Valid case. Call get_actual_mileage_rate function to calculate
    # the mileage rate and use the returned value to calculate the trip cost.
    else:
        mileage = end - start
        mileage_rate = get_actual_mileage_rate(mpg, fuel_price)
        trip_cost = round(mileage * mileage_rate, 2)
    print("Your trip cost ${:.2f}".format(trip_cost))
    return trip_cost


if __name__ == "__main__":
    main()
