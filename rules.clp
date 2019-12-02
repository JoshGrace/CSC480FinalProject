(open "outputfraudfound.txt" writeFile "w")
; Marks as possible fraud if the reimbursement is larger than 50 thousand.
(defrule large-reimbursement
	(inpatient-data
	(bene-ID ?b)
	(provider-ID ?pId)
	(insurance-amount-reimbursed ?amtReimb)
	)
	=>
	(if (> ?amtReimb 50000)
		then
		(printout writeFile "FRAUD-DETECTED " ?pId crlf)
		(assert (potential-fraud ?pId))
	)
)

; Marks as possible fraud if the attending physican and the other physician are the same.
(defrule similar-physicians
	(inpatient-data
	(bene-ID ?b)
	(provider-ID ?pId)
	(attending-physician ?aPhys)
	(other-physician ?othPhys)
	)
	=>
	(if (and (neq ?othPhys NULL) (eq ?aPhys ?othPhys))
	then
	(assert (potential-fraud (provider-ID ?pId) (bene-ID ?b)))
	)
)
(defrule add-claims
	(potential-fraud
	(provider-ID ?pId)
	)
	=>
	(find-all-facts 
	((?provider provider-data))
	(+ ?provider:num-fraud-claims 1)
	)
)
(close)
