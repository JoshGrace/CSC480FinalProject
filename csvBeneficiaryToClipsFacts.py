import sys
import csv
beneficiary_file = open("beneficiaries_facts.clp", "x")

with open("healthcare-provider-fraud-detection-analysis/Train_Beneficiarydata-1542865627584.csv") as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   line_count = 0
   for row in csv_reader:
      if(line_count == 0):
         line_count += 1
         continue
      line = "(beneficiary \n"
      line += "(bene-ID " + row[0] + ")\n"
      yearEndLoc = row[1].find('-')
      line += "(birth-year " + row[1][:yearEndLoc] + ")\n"
      monthEndLoc = row[1][yearEndLoc + 1: ].find('-')
      line += "(birth-month " + row[1][yearEndLoc + 1: yearEndLoc + monthEndLoc + 1] + ")\n"

      yearEndLoc = row[2].find('-')
      if(not row[2] == "NA"):
         line += "(has-died TRUE)\n"
         line += "(death-year " + row[2][:yearEndLoc] + ")\n"
         monthEndLoc = row[2][yearEndLoc + 2: ].find('-')
         line += "(death-month " + row[2][yearEndLoc + 1: yearEndLoc + monthEndLoc + 1] + ")\n"
      else:
         line += "(has-died FALSE)\n"
         line += "(death-year -1)\n"
         line += "(death-month -1)\n"

      line += "(gender " + row[3] + ")\n"
      line += "(race " + row[4] + ")\n"

      if(row[5] == "Y"):
         line += "(has-renal-disease TRUE)\n"
      else:
         line += "(has-renal-disease FALSE)\n"

      line += "(state " + row[6] + ")\n"
      line += "(country " + row[7] + ")\n"
      line += "(num-months-part-a-cov " + row[8] + ")\n"
      line += "(num-months-part-b-cov " + row[9] + ")\n"

      if(row[10] == "1"):
         line += "(has-chronic-cond-alzheimers TRUE)\n"
      else:
         line += "(has-chronic-cond-alzheimers FALSE)\n"

      if(row[11] == "1"):
         line += "(has-chronic-cond-heart-failure  TRUE)\n"
      else:
         line += "(has-chronic-cond-heart-failure FALSE)\n"

      if(row[12] == "1"):
         line += "(has-chronic-cond-kidney-disease  TRUE)\n"
      else:
         line += "(has-chronic-cond-kidney-disease FALSE)\n"

      if(row[13] == "1"):
         line += "(has-chronic-cond-cancer  TRUE)\n"
      else:
         line += "(has-chronic-cond-cancer FALSE)\n"

      if(row[14] == "1"):
         line += "(has-chronic-cond-pulminary-obstruction TRUE)\n"
      else:
         line += "(has-chronic-cond-pulminary-obstruction FALSE)\n"

      if(row[15] == "1"):
         line += "(has-chronic-cond-depression TRUE)\n"
      else:
         line += "(has-chronic-cond-depression FALSE)\n"

      if(row[16] == "1"):
         line += "(has-chronic-cond-diabetes TRUE)\n"
      else:
         line += "(has-chronic-cond-diabetes FALSE)\n"

      if(row[17] == "1"):
         line += "(has-chronic-cond-ischemic-heart TRUE)\n"
      else:
         line += "(has-chronic-cond-ischemic-heart FALSE)\n"

      if(row[18] == "1"):
         line += "(has-chronic-cond-osteoporasis TRUE)\n"
      else:
         line += "(has-chronic-cond-osteoporasis FALSE)\n"

      if(row[19] == "1"):
         line += "(has-chronic-cond-rheumatoidarthritis TRUE)\n"
      else:
         line += "(has-chronic-cond-rheumatoidarthritis FALSE)\n"

      if(row[20] == "1"):
         line += "(has-chronic-cond-stroke TRUE)\n"
      else:
         line += "(has-chronic-cond-stroke FALSE)\n"

      line += "(inpatient-reimbursment-amount " + row[21] + ")\n"
      line += "(inpatient-deductible-amount " + row[22] + ")\n"
      line += "(outpatient-reimbursment-amount " + row[23] + ")\n"
      line += "(outpatient-deductible-amount " + row[24] + ")\n"
      line += ")\n\n"
      beneficiary_file.write(line)
      

beneficiary_file.write("\n\n")
beneficiary_file.close()
