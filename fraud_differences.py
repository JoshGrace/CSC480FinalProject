import os
import csv
import numpy as np

BeneID = 0
Provider = 4
InscClaimAmtReimbursed = 5
train_outpatient_path = '\\healthcare-provider-fraud-detection-analysis\\Train_Outpatientdata-1542865627584.csv'

def amt_reimbursed():
   fraud_providers = {}
   fraud_bene = {}
   non_fraud_providers = {}
   non_fraud_bene = {}

   with open('has_fraud.txt') as f:
      csv_reader = csv.reader(f, delimiter=',')
      for row in csv_reader:
         fraud_providers[row[BeneID]] = []
      f.close()

   with open(os.getcwd() + '\\healthcare-provider-fraud-detection-analysis\\Train_Outpatientdata-1542865627584.csv') as f:
      csv_reader = csv.reader(f, delimiter=',')
      line_count = 0
      for row in csv_reader:
         if line_count == 0:
            line_count += 1
         else:
            if row[Provider] in fraud_providers:
               if row[BeneID] not in fraud_bene:
                  fraud_bene[row[BeneID]] = 0
               fraud_bene[row[BeneID]] += int(row[InscClaimAmtReimbursed])
               fraud_providers[row[Provider]].append(row[BeneID])
            else:
               if row[BeneID] not in non_fraud_bene:
                  non_fraud_bene[row[BeneID]] = 0
               non_fraud_bene[row[BeneID]] += (int(row[InscClaimAmtReimbursed]))
               if row[4] not in non_fraud_providers:
                  non_fraud_providers[row[Provider]] = []
               non_fraud_providers[row[Provider]].append(row[BeneID])

   sum = 0
   for key in fraud_bene.keys():
      sum += fraud_bene[key]
   sum2 = 0
   for key in non_fraud_bene.keys():
      sum2 += non_fraud_bene[key]
   print('avg reimbursement for fraudulent beneficiaries', sum / len(fraud_bene.keys()))
   print('avg reimbursement for non fraudulent beneficiaries', sum2 / len(non_fraud_bene.keys()))

# potential fraud cases
# multiple claims in one day by the same provider and/or the same beneficiary
# a beneficiary claiming something that doesn't match a provider code and vice cersa
# a beneficiary claiming somethign with the physician that doesn't exist
# filing the same claim on the same day
# doesn't have an attending physician present
# flag procedure codes
# flag if you all different types of physicians are the same
# the same attending and operating gets flagged

"""
Returns a dictionary containing a set of keys as providers and a list as the beneficiaries of that provider
:filename: string, use either has_fraud.txt or no_fraud.txt 
"""
def get_providers(file_name):
   providers = {}
   try:
      with open(file_name) as f:
         csv_reader = csv.reader(f, delimiter=',')
         for row in csv_reader:
            providers[row[0]] = []
         f.close()
   except FileNotFoundError:
      print('Couldn\'t find {}!'.format(file_name))
   try:
      with open(os.getcwd() + train_outpatient_path) as f:
         csv_reader = csv.reader(f, delimiter=',')
         line_count = 0
         for row in csv_reader:
            if line_count == 0:
               line_count += 1
            else:
               if row[Provider] in providers:
                  providers[row[Provider]].append(row[BeneID])
         f.close()   
         return providers
   except FileNotFoundError:
      print("Couldn't find {}".format(os.getcwd() + train_outpatient_path))

def get_ins_reimb_percentile():
   fraud_providers = get_providers('has_fraud.txt')
   no_fraud_providers = get_providers('no_fraud.txt')
   fraud_ins_reimb_vals = []
   fraud_p80 = 0
   fraud_p99 = 0
   try:
      with open(os.getcwd() + train_outpatient_path) as f:
         csv_reader = csv.reader(f, delimiter=',')
         line_count = 0
         for row in csv_reader:
            if line_count == 0:
               line_count += 1
            else:
               if row[Provider] in fraud_providers:
                  fraud_ins_reimb_vals.append(int(row[InscClaimAmtReimbursed]))
         f.close()
      percentile_list = np.array(fraud_ins_reimb_vals)
      p80 = np.percentile(percentile_list, 80)
      p90 = np.percentile(percentile_list, 90)
      p99 = np.percentile(percentile_list, 99.99)
      with open(os.getcwd() + train_outpatient_path) as f:
         csv_reader = csv.reader(f, delimiter=',')
         line_count = 0
         for row in csv_reader:
            if line_count == 0:
               line_count += 1
            else:
               if int(row[InscClaimAmtReimbursed]) > p99 and row[Provider] in fraud_providers:
                  fraud_p99 += 1
      print(fraud_p99 / len(fraud_ins_reimb_vals))
   except FileNotFoundError:
      print('Error opening file!')

get_ins_reimb_percentile()