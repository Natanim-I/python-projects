import math


def paint_calc(height, width, cover):
    area = width * height
    no_of_can = math.ceil(area / cover)
    print(f"You'll need {no_of_can} cans of paint.")


test_h = int(input("Enter the height of the board: \n"))
test_w = int(input("Enter the width of the board: \n"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
