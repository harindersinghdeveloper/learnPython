import csv

data = open('example.csv', 'w', newline='')
writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(["name","price"])
writer.writerow(["harry",10000])
writer.writerow(["anuj",20000])
writer.writerows([["gaurav",30000],["tej",40000],["yaman",10000]])
data.close()

data_one = open('example.csv', 'r')
csv_data = csv.reader(data_one)
data_lines=list(csv_data)
print(len(data_lines))
for l in data_lines:
    print(l)