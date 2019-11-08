(deftemplate beneficiary
   (slot bene-ID
   (type SYMBOL)
   (default NULL))

   (slot birth-year
   (type INTEGER)
   (default 0))

   (slot birth-month
   (type INTEGER)
   (default 0))
   
   (slot has-died
   (type SYMBOL)
   (default NIL))
   
   (slot death-year
   (type INTEGER)
   (default 0))

   (slot death-month
   (type INTEGER)
   (default 0))

   (slot gender
   (type INTEGER)
   (default 0))

   (slot race
   (type INTEGER)
   (default 0))

   (slot has-renal-disease
   (type SYMBOL)
   (default NULL))

   (slot state
   (type INTEGER)
   (default 0))

   (slot country
   (type INTEGER)
   (default 0))

   (slot num-months-part-a-cov
   (type INTEGER)
   (default 0))

   (slot num-months-part-b-cov
   (type INTEGER)
   (default 0))

   (slot has-chronic-cond-alzheimers
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-heart-failure
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-kidney-disease
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-cancer
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-pulminary-obstruction
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-depression
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-diabetes
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-ischemic-heart
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-osteoporasis
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-rheumatoidarthritis
   (type SYMBOL)
   (default NULL))

   (slot has-chronic-cond-stroke
   (type SYMBOL)
   (default NULL))

   (slot inpatient-reimbursment-amount
   (type INTEGER)
   (default 0))

   (slot inpatient-deductible-amount
   (type INTEGER)
   (default 0))

   (slot outpatient-reimbursment-amount
   (type INTEGER)
   (default 0))

   (slot outpatient-deductible-amount
   (type INTEGER)
   (default 0))

)
