import sys
import csv

def writeLine(name, value):
   return "(" + name + " " + value + ")\n"

def writeDate(name, date):
   line = ""
   yearEndLoc = date.find('-')
   monthEndLoc = date[yearEndLoc + 1: ].find('-')
   line += writeLine(name + "-year", date[:yearEndLoc])
   line += writeLine(name + "-month", date[yearEndLoc + 1: yearEndLoc + monthEndLoc + 1])
   return line

def writeProcedureCode(number, value):
   if(not value == "NA"):
      return writeLine("claim-procedure-code-" + str(number), "*" + str(value))
   return writeLine("claim-procedure-code-" + str(number), "*"+ str(-1))

def writeDiagnosisCode(number, value):
   if(not value == "NA"):
      return writeLine("claim-diagnosis-code-" + str(number), "*" + str(value))
   return writeLine("claim-diagnosis-code-" + str(number), "*" + str(-1))

def writeInpatientData():
   inpatient_file = open("inpatient_facts.clp", "x")
   with open(sys.argv[1]) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
         if(line_count == 0):
            line_count += 1
            continue
         line = "(inpatient-data\n"
         line += writeLine("bene-ID", row[0])
         line += writeLine("claim-ID", row[1])
         line += writeDate("claim-start", row[2])
         line += writeDate("claim-end", row[3])
         line += "(provider-ID " + row[4] + ")\n"
         providerSet.add(row[4])
         line += "(insurance-amount-reimbursed " + row[5] + ")\n"
         line += "(attending-physician " + row[6] + ")\n"
         line += "(operating-physician " + row[7] + ")\n"
         line += "(other-physician " + row[8] + ")\n"
         line += writeDate("admission", row[9])
         line += "(claim-admit-diagnosis-code *" + row[10] + ")\n"
         if(row[11] == "NA"):
            line += "(deductible-amount-paid -1)\n"
         else:
            line += "(deductible-amount-paid " + row[11] + ")\n"
         line += writeDate("discharge", row[12])
         line += writeLine("diagnosis-group-code", "*" + str(row[13]))
         line += writeDiagnosisCode(1, row[14])
         line += writeDiagnosisCode(2, row[15])
         line += writeDiagnosisCode(3, row[16])
         line += writeDiagnosisCode(4, row[17])
         line += writeDiagnosisCode(5, row[18])
         line += writeDiagnosisCode(6, row[19])
         line += writeDiagnosisCode(7, row[20])
         line += writeDiagnosisCode(8, row[21])
         line += writeDiagnosisCode(9, row[22])
         line += writeDiagnosisCode(10, row[23])
         line += writeProcedureCode(1, row[24])
         line += writeProcedureCode(2, row[25])
         line += writeProcedureCode(3, row[26])
         line += writeProcedureCode(4, row[27])
         line += writeProcedureCode(5, row[28])
         line += writeProcedureCode(6, row[29])
         line += ")\n\n"
         inpatient_file.write(line)
   inpatient_file.write("\n)\n")
   inpatient_file.close()

def writeOutpatientData():
   inpatient_file = open("outpatient_facts.clp", "x")
   with open(sys.argv[2]) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
         if(line_count == 0):
            line_count += 1
            continue
         line = "(outpatient-data\n"
         line += writeLine("bene-ID", row[0])
         line += writeLine("claim-ID", row[1])
         line += writeDate("claim-start", row[2])
         line += writeDate("claim-end", row[3])
         line += "(provider-ID " + row[4] + ")\n"
         providerSet.add(row[4])
         line += "(insurance-amount-reimbursed " + row[5] + ")\n"
         line += "(attending-physician " + row[6] + ")\n"
         line += "(operating-physician " + row[7] + ")\n"
         line += "(other-physician " + row[8] + ")\n"
         line += writeDiagnosisCode(1, row[9])
         line += writeDiagnosisCode(2, row[10])
         line += writeDiagnosisCode(3, row[11])
         line += writeDiagnosisCode(4, row[12])
         line += writeDiagnosisCode(5, row[13])
         line += writeDiagnosisCode(6, row[14])
         line += writeDiagnosisCode(7, row[15])
         line += writeDiagnosisCode(8, row[16])
         line += writeDiagnosisCode(9, row[17])
         line += writeDiagnosisCode(10, row[18])
         line += writeProcedureCode(1, row[19])
         line += writeProcedureCode(2, row[20])
         line += writeProcedureCode(3, row[21])
         line += writeProcedureCode(4, row[22])
         line += writeProcedureCode(5, row[23])
         line += writeProcedureCode(6, row[24])
         line += writeLine("claim-admit-diagnosis-code", str(row[25]))
         if(row[26] == "" and not 'V' in row[26]):
            line += "(deductible-amount-paid *-1)\n"
         else:
            line += "(deductible-amount-paid *" + row[26] + ")\n"

         line += ")\n\n"
         inpatient_file.write(line)
   inpatient_file.write("\n)\n")
   inpatient_file.close()

def writeProviderInfo(provSet):
   provider_file = open("provider_facts.clp", "x")
   for provider in provSet:
         line = "(provider-data\n"
         line += writeLine("provider-ID", str(provider))
         line += writeLine("num-fraud-claims", str(0))
         line += writeLine("fraud-detected", str("FALSE"))
         line += ")\n\n"
         provider_file.write(line)
   provider_file.write("\n)\n")
   provider_file.close()
      

providerSet = set()
writeInpatientData()
writeOutpatientData()
writeProviderInfo(providerSet)
