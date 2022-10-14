list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
maxInd = 0

Max = list_numbers[0]
for i in range(20):
    if list_numbers[i] > Max:
        Max = list_numbers[i]
        maxInd = i

list_numbers[maxInd] = list_numbers[19]
list_numbers[19] = Max

print(list_numbers)
