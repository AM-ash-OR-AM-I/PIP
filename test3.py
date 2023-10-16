side1, side2, side3 = map(
    int, input("Enter the length of three sides of triangle: ").split()
)
assert (
    side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2
), "Sum of any two sides should be greater than the third side"
