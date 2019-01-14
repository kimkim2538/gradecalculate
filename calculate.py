import csv

listgrade = []
listweight = []

def setup():
   with open('grade.csv','r') as csvfile:
        #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        spamreader = csv.reader(csvfile)
        for row in spamreader:
           #line_data = row.strip().split(",")
           listgrade.append(row[3])
           listweight.append(row[1])
           #print(','.join(row[1]))
           #print(','.join(row[3]))
           #print(row)
   print (listgrade)
   print (listweight)
   calculate (listweight,listgrade)

def calculate(weight,grade):
   sum_weight = 0
   sum_grade = 0
   for i in range(len(grade)):
       sum_weight += int(weight[i])
       sum_grade += float(weight[i])*float(grade[i])
   print ('%.2f'%(sum_grade/sum_weight))
   
setup()
