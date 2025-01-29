fruits = ["banana", "apple", "mango"]


fruits.append("orange")

fruits.remove("banana")
del fruits[1]

fruits.insert(1, "cherry")

print(fruits)

#Dictionnaries
my_dict = {'a': 2, 'b': 3, 'c': 4}

for key, value in my_dict.items():
    print(value)

#Sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 & set2)