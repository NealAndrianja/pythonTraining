# Step 1: Create a list of numbers
numbers = [1, 2, 3, 4, 5]
# Step 2: Loop through each number in the list
for number in numbers:
    print("Current number:", number)

for i in range(7):
    for j in range(6):
        print(f"- the value of j is {j}")
        if j == 4 :
            break
    print(f"------------ {i}")

for i in range(1, 8,2):
    print(i)
