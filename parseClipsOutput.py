provideFraud = open("has_fraud.txt", "r")
providerDict = set()
num_correct = 0
detectedFraudDict = set()
total = 0
for line in provideFraud:
   providerDict.add(line)
provideFraud.close()
print()
detectedFraud = open("outputfraudfound.txt", "r")
for line in detectedFraud:
   index = line.index("FRAUD-DETECTED: ")
   offset = len("FRAUD-DETECTED: ")
   if line not in detectedFraudDict and index < len(line) and index >= 0:
      detectedFraudDict.add(line)
      if line[index + offset:] in providerDict:
         # print("PROVIDER FOUND IN HAS_FRAUD: " + line[offset + index: ])
         num_correct += 1
         total += 1
      else:
         # print("PROVIDER FOUND NOT IN HAS_FRAUD: " + line[offset + index: ])
         total += 1
print("provider Dict len: " + str(len(providerDict)))
print("detectedFraudDict " + str(len(detectedFraudDict)))
print("True Positive Percent: {0:.2f}%".format((num_correct/total) * 100))
print("Correct Sample Percent: {0:.2f}%".format((num_correct/len(providerDict)) * 100))
detectedFraud.close()