(open "outputfraudfound.txt" writeFile "w")

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
	(assert (potential-fraud ?pId))
	)
)
(close)
