# Step 1: Create a list of fruits
fruits = ["apple", "banana", "cherry"]
# Step 2: Access the first item in the list
print("First fruit:", fruits[0])
# Step 3: Add a new item to the list
fruits.append("orange")
print("Fruits after adding orange:", fruits)
# Step 4: Remove an item from the list
fruits.remove("banana")
print("Fruits after removing banana:", fruits)
# Step 5: Loop through each item in the list
for fruit in fruits:
    print("Fruit:", fruit)

    # Step 1: Create a tuple of colors
    colors = ("red", "green", "blue")
    # Step 2: Access the second item in the tuple
    print("Second color:", colors[1])
    # Step 3: Try to change an item in the tuple (This will cause an error)
    # colors[1] = "yellow" # Uncommenting this line will cause an error
    # Step 4: Loop through each item in the tuple
    for color in colors:
        print("Color:", color)
