provideFraud = open("has_fraud.txt", "r")
providerDict = set()
num_correct = 0
HAS_FRAUD_LENGTH = 506
NO_FRAUD_LENGTH = 4905
detectedFraudDict = set()
total = 0
for line in provideFraud:
   providerDict.add(line[:line.index('\n')])
provideFraud.close()
detectedFraud = open("./provider_flags.txt", "r")
arr = []
for line in detectedFraud:
   if line not in detectedFraudDict:
      arr.append((int(line.split(" ")[1]),line.split(" ")[0]))
      detectedFraudDict.add(line)
arr.sort(key = lambda tup: tup[0])
max_num_correct = 0
max_total = 0
best_level = -1
best_pos = -1
max_ratio = -1
for i in range(len(arr)):
   num_correct = 0
   total = 0
   for entry in arr[i:]:
      if(entry[1] in providerDict):
         num_correct += 1
      total += 1
      # print(num_correct/total)
   if(.1032 >= (num_correct/total)):
      max_ratio = (num_correct/total) * (num_correct/len(providerDict))
      max_total = total
      max_num_correct = num_correct
      best_pos = i
      best_level = arr[i][0]-1

if(best_level == -1):
   print("Something Went Wrong!")
   exit(-1)
print("Ideal Level: " + str(best_level))
print("True Positive Percent: {0:.2f}%".format((max_num_correct/max_total) * 100))
print("Correct Sample Percent: {0:.2f}%".format((max_num_correct/len(providerDict)) * 100)) 

detectedFraud.close()
