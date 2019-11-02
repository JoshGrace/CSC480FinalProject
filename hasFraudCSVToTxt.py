

import sys
import csv
f_has_fraud = open("has_fraud.txt", "x")
f_no_fraud = open("no_fraud.txt", "x")

with open(sys.argv[1]) as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   line_count = 0
   for row in csv_reader:
      if(row[1] == "Yes"):
         f_has_fraud.write(row[0] + '\n')
      else:
         f_no_fraud.write(row[0] + '\n')
f_has_fraud.close()
f_no_fraud.close()
