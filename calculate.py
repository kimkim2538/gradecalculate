import csv

def setup(): 
    sumgrade = []
    sumweight = []
    csv = open('Transcriptonlyscore.csv', 'r')
    data = csv.readline()
    for i in data:
        line_data = i.strip().split(",")
        sumweight.append(line_data[1])
        sumgrade.append(line_data[2])
    csv.close()
    print(sumgrade)



setup()
