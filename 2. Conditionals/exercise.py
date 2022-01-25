"""

Jin Young Park
CS5001 Fall 2021
HW2 exercise.py
The program creates an exercise plan
based on the day of the week and the weather.

Test cases:
1)
What day is it? th
Is it a holiday? y
Is it raining? n
What is the temperature? 70
Hike for 45 minutes

2)
What day is it? w
Is it a holiday? n
Is it raining? n
What is the temperature? 50
Run for 45 minutes

3)
What day is it? sa
Is it a holiday? n
Is it raining? y
What is the temperature? 20
Swim for 30 minutes

4)
What day is it? su
Is it a holiday? n
Is it raining? n
What is the temperature? 50
Take a rest day

"""


def main():
    # Ask for what day it is and capitalize the first letter
    # to meet the standard form.
    day = input("What day is it? ")
    day = day.capitalize()

    # Determine whether it is running day or hiking day or rest day
    if day == "M" or day == "W" or day == "F":
        exercise = "Run"
    elif day == "Sa":
        exercise = "Hike"
    elif day == "Tu" or day == "Th" or "Su":
        exercise = "Rest"
    else:
        exercise = "invalid"

    # Ask if it is a holiday
    holiday = input("Is it a holiday? ")
    holiday = holiday.lower()
    if exercise == "invalid":
        exercise
    else:
        # If it is a holiday, exercise type is Hiking.
        if holiday == "y" or holiday == "yes":
            exercise = "Hike"
        elif holiday == "n" or holiday == "no":
            exercise
        else:
            exercise = "invalid"

    # Ask if it is raining.
    raining = input("Is it raining? ")
    raining = raining.lower()
    if exercise == "invalid":
        exercise
    else:
        # If it is raining, exercise type is Swimming.
        if raining == "y" or raining == "yes":
            exercise = "Swim"
        elif raining == "n" or raining == "no":
            exercise
        else:
            exercise = "invalid"

    # Ask for temperature.
    temp = float(input("What is the temperature? "))
    # If temp is lower than 35 or higher than 75,
    # limit the duration of exercise to 30 min.
    if temp < 35 or temp > 75:
        workout_time = 30
    # If temp is in between 35 and 75,
    # the duration of exercise is 45 min.
    elif temp > 35 and temp < 75:
        workout_time = 45

    # Output statement
    if exercise == "invalid":
        print("Swim for 35 minutes")
    elif exercise == "Rest":
        print("Take a rest day")
    else:
        print(exercise, "for", workout_time, "minutes")


if __name__ == "__main__":
    main()
