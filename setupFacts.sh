#!/bin/bash
rm beneficiaries_facts.clp
rm inpatient_facts.clp
rm outpatient_facts.clp
rm provider_facts.clp
python3 csvBeneficiaryToClipsFacts.py
python3 csvToClipsFacts.py healthcare-provider-fraud-detection-analysis/Train_Inpatientdata-1542865627584.csv healthcare-provider-fraud-detection-analysis/Train_Outpatientdata-1542865627584.csv
