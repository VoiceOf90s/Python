numbers = [2, -93, -2, 8, 0, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
uni_numbers = set(numbers)
numbers[4] = sum(uni_numbers)/len(uni_numbers)
print("Измененный список:",numbers)