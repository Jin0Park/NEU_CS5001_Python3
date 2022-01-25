"""

Jin Young Park
CS5001 Fall 2021
HW2 registration.py
The program tells if a student is fulfilled to register desired course.

Test cases:
1)
Enter a course number: b500
What grade did you get for X101? a
What grade did you get for X102? c
You meet all the prerequisites and have successfully registered for B500

2)
Enter a course number: cs5001
Invalid course number

3)
Enter a course number: x101
You have successfully registered for X101

4)
Enter a course number: b701
What grade did you get for X101? a
What grade did you get for X102? d
You do not meet the prerequisites for B701

"""


def main():
    # User's desired course to register
    course_num = input("Enter a course number: ")
    # Covert the input to the standard version
    course_num = course_num.replace(" ", "")
    course_num = course_num.upper()

    # If the input is X101 or X102, the user can register for the course.
    if course_num == "X101" or course_num == "X102":
        print("You have successfully registered for", course_num)

    # If the input is B500 or B525 or B701, user needs to provide
    # his or her grade for X101 and X102.
    elif course_num == "B500" or course_num == "B525" or course_num == "B701":
        grade_X101 = input("What grade did you get for X101? ")
        grade_X101 = grade_X101.upper()
        grade_X102 = input("What grade did you get for X102? ")
        grade_X102 = grade_X102.upper()
        # If user's grade for X101 is A or B and grade for X102 is A or B or C,
        # user can register for the course. Otherwise, user cannot register.
        if (grade_X101 == "A" or grade_X101 == "B") and \
           (grade_X102 == "A" or grade_X102 == "B" or grade_X102 == "C"):
            print("You meet all the prerequisites and have successfully",
                  "registered for", course_num)
        else:
            print("You do not meet the prerequisites for", course_num)

    # If input is not a valid course number, user should provide a valid one.
    else:
        print("Invalid course number")


if __name__ == "__main__":
    main()
