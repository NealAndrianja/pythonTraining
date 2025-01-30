import csv

def writeData(data):
    with open("contacts.csv", "r") as file:
        reader = csv.reader(file)
        if reader.line_num < 2:
            writeNew(data)
        else:
            appendData(data)



def writeNew(data):
    with open("contacts.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerows([data.values()])

def appendData(data):
    with open("contacts.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data.values()])