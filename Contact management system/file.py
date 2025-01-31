import csv

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
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data
