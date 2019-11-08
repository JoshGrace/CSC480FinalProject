
(deftemplate provider-data

   (slot provider-ID
   (type SYMBOL)
   (default NIL))

   (slot num-fraud-claims
   (type INTEGER)
   (default 0))

   (slot fraud-detected
   (type SYMBOL)
   (default NIL))

)
