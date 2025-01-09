import csv

with open("data.txt", "w") as file:
    file.write("hello world\n")
    file.write("This is a sample file\n")
with open("data.txt", "r") as file:
    content = file.read()
    print("File content: ", content)

csvData = [
  ["Name", "Age", "City"],
  ["Alice", 25, "New York"],
  ["Bob", 30, "Los Angeles"],
  ["Charlie", 22, "Chicago"],
  ["Diana", 28, "San Francisco"]
]

with open("data/sample.csv", "w", newline='') as data:
    writer = csv.writer(data)
    writer.writerows(csvData)

with open("data/sample.csv", "r") as data:
    reader = csv.reader(data)
    for row in reader:
        print(row)
