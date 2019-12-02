(open "outputfraudfound.txt" writeFile "w")
; Marks as possible fraud if the reimbursement is larger than 50 thousand.
(defrule large-reimbursement
	(outpatient-data
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
	(outpatient-data
	(bene-ID ?b)
	(provider-ID ?pId)
	(attending-physician ?aPhys)
	(other-physician ?othPhys)
	)
	=>
	(if (and (neq ?othPhys NULL) (eq ?aPhys ?othPhys))
	then
	(assert (potential-fraud (potential-fraud ?pId))
	)
)

(defrule add-claims
	(declare (salience 20))
	(potential-fraud ?pId)
	=>
	(find-all-facts 
	((?provider provider-data))
	(eq ?provider:provider-ID ?pId))
	(do-for-all-facts ((?provider provider-data))
	(+ ?provider:num-fraud-claims 1)
	(printout writeFile ?provider:num-fraud-claims crlf)
	)
)

(defrule output-fraud-found
	(provider-data
	(provider-ID ?pId)
	(num-fraud-claims ?nClaims)
	)
	=>
	(if (> ?nClaims 1)
	then
		(printout writefile "FRAUD-DETECTED: " ?pId crlf))
)
(close)
