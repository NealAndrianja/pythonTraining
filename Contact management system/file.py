import csv
import os

def writeData(data):
    has_data = False
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            has_data = any(reader)
    except FileNotFoundError:
        has_data = False

    if not has_data:
        writeNew(data)
    else:
        appendData(data)



def writeNew(data):
    with open("contacts.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerows([data.values()])

def appendData(data):
    with open("contacts.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerows([data.values()])

def readData():
    data = []

    if not os.path.exists("contacts.csv"):
        print("file not found")
        return data

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def searchBy(value):
    data = readData()
    matches = [d for d in data if any(value in str(v) for v in d.values())]
    if not matches:
        print("No contact found")
    return matches