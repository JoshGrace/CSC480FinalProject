provideFraud = open("has_fraud.txt", "r")
providerDict = set()
for line in provideFraud:
   providerDict.add(line)
provideFraud.close()
print()
detectedFraud = open("outputfraudfound.txt", "r")
for line in detectedFraud:
   index = line.index("FRAUD-DETECTED: ")
   offset = len("FRAUD-DETECTED: ")
   if index < len(line) and index >= 0:
      if line[index + offset:] in providerDict:
         print("PROVIDER FOUND IN HAS_FRAUD: " + line[offset + index: ])
      else:
         print("PROVIDER FOUND NOT IN HAS_FRAUD: " + line[offset + index: ])
detectedFraud.close()
