negatives = []
zeros = []
positives = []

while True:
    user_input = input("Enter an integer (blank line to stop): ")
    if user_input == "":
        break
    else:
        num = int(user_input)
        if num < 0:
            negatives.append(num)
        elif num == 0:
            zeros.append(num)
        else:
            positives.append(num)

print("Negative numbers: ", end="")
for num in negatives:
    print(num, end=" ")

print("Zeros: ", end="")
for num in zeros:
    print(num, end=" ")

print("Positive numbers: ", end="")
for num in positives:
    print(num, end=" ")