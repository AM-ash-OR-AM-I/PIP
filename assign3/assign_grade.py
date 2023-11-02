"""
Write a python script to assign a grade to a student based on marks obtained as per the criteria men-
tioned in the above table:

marks >= 90 : A
marks >= 70 and marks < 90 : B
marks >= 50 and marks < 70 : C
marks >= 40 and marks < 50 : D
marks < 40 : F
"""


def assign_grade(marks):
    for i in range(5):
        if marks >= marks_arr[i]:
            return grades[i]


if __name__ == "__main__":
    marks_arr = [90, 70, 50, 40, 0]
    grades = ["A", "B", "C", "D", "F"]
    marks = int(input("Enter the marks: "))
    print("The grade is: ", assign_grade(marks))
