(deftemplate inpatient-data
   (slot bene-ID
   (type SYMBOL)
   (default NULL))

   (slot claim-ID
   (type SYMBOL)
   (default NULL))

   (slot claim-start-year
   (type INTEGER)
   (default 0))

   (slot claim-start-month
   (type INTEGER)
   (default 0))

   (slot claim-end-year
   (type INTEGER)
   (default 0))

   (slot claim-end-month
   (type INTEGER)
   (default 0))

   (slot provider-ID
   (type SYMBOL)
   (default NULL))

   (slot insurance-amount-reimbursed
   (type INTEGER)
   (default 0))

   (slot attending-physician
   (type SYMBOL)
   (default NULL))

   (slot operating-physician
   (type SYMBOL)
   (default NULL))

   (slot other-physician
   (type SYMBOL)
   (default NULL))

   (slot admission-year
   (type INTEGER)
   (default 0))

   (slot admission-month
   (type INTEGER)
   (default 0))

   (slot claim-admit-diagnosis-code
   (type SYMBOL)
   (default NIL))

   (slot deductible-amount-paid
   (type INTEGER)
   (default 0))

   (slot discharge-year
   (type INTEGER)
   (default 0))

   (slot discharge-month
   (type INTEGER)
   (default 0))

   (slot diagnosis-group-code
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-1
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-2
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-3
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-4
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-5
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-6
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-7
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-8
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-9
   (type SYMBOL)
   (default NIL))

   (slot claim-diagnosis-code-10
   (type SYMBOL)
   (default NIL))

   (slot claim-procedure-code-1
   (type SYMBOL)
   (default NIL))

   (slot claim-procedure-code-2
   (type SYMBOL)
   (default NIL))

   (slot claim-procedure-code-3
   (type SYMBOL)
   (default NIL))

   (slot claim-procedure-code-4
   (type SYMBOL)
   (default NIL))

   (slot claim-procedure-code-5
   (type SYMBOL)
   (default NIL))

   (slot claim-procedure-code-6
   (type SYMBOL)
   (default NIL))

)
