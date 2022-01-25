"""

Jin Young Park
CS5001 Fall 2021
HW2 shape.py
The program calculates the area of a shape based on information
given by the user.

Test cases:
1)
Select a shape (triangle, square, or rectangle): TriangLE
Enter the width: 7
Enter the height: 7
The area of the triangle is 24.5

2)
Select a shape (triangle, square, or rectangle): RECTANGLE
Enter the width: 4
Enter the height: 0
Invalid height

3)
Select a shape (triangle, square, or rectangle): square
Enter the width: 5
The area of the square is 25.0

"""


def main():
    # User selects a shape among the choices.
    # Converts the input to lowercase.
    shape = input("Select a shape (triangle, square, or rectangle): ")
    shape = shape.lower()

    # If the user's shape is neither triangle nor square nor rectangle
    # print false statement.
    if not(shape == "triangle" or shape == "rectangle" or shape == "square"):
        print("Unknown shape")
    # If statement when the user's shape is one of the three shapes.
    else:
        # Ask for width of the shape.
        width = float(input("Enter the width: "))
        # If the width is equal or lower than 0, it is not a valid shape.
        if width <= 0:
            print("Invalid width")
            return
        # For squares, area is width ** 2. No need to ask for height.
        if shape == "square":
            area = width ** 2
        # If the shape is triangle or rectangle, ask for height.
        else:
            height = float(input("Enter the height: "))
            # If the height is equal or lower than 0,
            # it is not a valid shape.
            if height <= 0:
                print("Invalid height")
                return
            # For rectangles, area is width times height.
            area = width * height
            # For triangles, area is width times height divided by 2.
            if shape == "triangle":
                area = area / 2

        # Output statement.
        print("The area of the", shape, "is", round(area, 2))


if __name__ == "__main__":
    main()
