"""
Write a python script to assign a grade to a student based on marks obtained as per the criteria men-
tioned in the above table:

marks >= 90 : A
marks >= 70 and marks < 90 : B
marks >= 50 and marks < 70 : C
marks >= 40 and marks < 50 : D
marks < 40 : E
"""


def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70 and marks < 90:
        return "B"
    elif marks >= 50 and marks < 70:
        return "C"
    elif marks >= 40 and marks < 50:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    marks = int(input("Enter the marks: "))
    print("The grade is: ", assign_grade(marks))
