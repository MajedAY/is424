maxList = []

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    maxList.append(number)

largest = maxList[0]

for number in maxList:
    if number > largest:
        largest = number

print("The largest number is:", largest)
