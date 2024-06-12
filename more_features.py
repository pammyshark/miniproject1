import csv

a = {"task": ["1"], "priority": ["2"], "date": ["3"]}

w = csv.writer(open("output.csv", "w"))
# loop over dictionary keys and values
for key, val in a.items():
    w.writerow([key, val]) #writing by row
