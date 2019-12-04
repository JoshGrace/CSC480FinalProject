(open "outputfraudfount.txt" writeFile "w")

; flags reimbursements larger than 5 thousand dollars
(defrule excessive-reimbursement
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(insurance-amount-reimbursed ?amtReimb)
	)
	=>
	(if (> ?amtReimb 5000)
		then
		(assert (potential-fraud 
			(provider-ID ?pId) 
			(bene-ID ?bId) 
			(marked FALSE)
			)
		)
	)
)

(defrule similar-physicians
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(attending-physician ?aPhys)
	(other-physician ?oPhys)
	)
	(test (and (neq ?oPhys NULL) (eq ?aPhys ?oPhys)))
	=>
	(assert (potential-fraud (provider-ID ?pId) (bene-ID ?bId) (marked FALSE)))
)

; Creating a template with a provider-ID and bene-ID should generate unique facts.
; So we can just add all the flags at the end.
(defrule add-flags
	?pFraudData <- (potential-fraud
	(provider-ID ?pId)
	(bene-ID ?bId)
	(marked FALSE)
	)
	?pData <- (provider-data
	(provider-ID ?pId)
	(num-fraud-claims ?nClaims)
	)
	=>
	(modify ?pData (num-fraud-claims (+ ?nClaims 1)))
	(modify ?pFraudData (marked TRUE))
)

; Outputs all the fraudulent providers that have flags over a certain number.
(defrule flag-providers
	(provider-data
	(provider-ID ?pId)
	(num-fraud-claims ?nClaims)
	)
	=>
	(if (> ?nClaims 25)
		then
		(printout writeFile "FRAUD-DETECTED: " ?pId crlf)
	)
)
(close)
