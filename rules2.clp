  
(open "outputfraudfount.txt" writeFile "w")

;flags reimbursements larger than 1 thousand dollars
(defrule excessive-reimbursement
	(outpatient-data
	(bene-ID ?bId)
	(claim-ID ?cId)
	(provider-ID ?pId)
	(insurance-amount-reimbursed ?amtReimb)
	)
	=>
	(if (> ?amtReimb 1000)
		then
		(assert (potential-fraud 
			(provider-ID ?pId)
			(claim-ID ?cId) 
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
	(claim-ID ?cId)
	(attending-physician ?aPhys)
	(other-physician ?oPhys)
	)
	(test (and (neq ?oPhys NULL) (eq ?aPhys ?oPhys)))
	=>
	(assert (potential-fraud 
			(provider-ID ?pId)
			(bene-ID ?bId)
		 	(claim-ID ?cId)
			(marked FALSE)
		)
	)
)

(defrule mult-claim
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	)
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	)
	(test (and (eq ?bId ?bId) (eq ?pId ?pId)))
	=>
	(assert (potential-fraud 
			(provider-ID ?pId)
			(bene-ID ?bId)
		 	(claim-ID ?cId)
			(marked FALSE)
		)
	)
)


(defrule no-physicians
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	(attending-physician ?aPhys)
	(operating-physician ?opPhys)
	(other-physician ?oPhys)
	)
	(test (and (eq ?oPhys NA) (eq ?opPhys NA)))
	=>
	(assert (potential-fraud 
			(provider-ID ?pId)
			(bene-ID ?bId)
		 	(claim-ID ?cId)
			(marked FALSE)
		)
	)
)

(defrule no-claim
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	(claim-diagnosis-code-1 ?cOne)
	(claim-diagnosis-code-2 ?cTwo)
	)
	(test (eq ?cOne *-1))
	=>
	(assert (potential-fraud 
			(provider-ID ?pId)
			(bene-ID ?bId)
		 	(claim-ID ?cId)
			(marked FALSE)
		)
	)
)

(defrule has-deductible
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	(deductible-amount-paid ?dAmount&~NIL)
	)
	=>
	(assert (potential-fraud
			(provider-ID ?pId)
			(bene-ID ?bId)
			(claim-ID ?cId)
			(marked FALSE)
		)
	)
)

(defrule minor-claim
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	(claim-start-year ?cYear)
	(claim-start-month ?cMonth)
	)
	(beneficiary
	(bene-ID ?bId)
	(has-died FALSE)
	(birth-year ?bYear)
	(birth-month ?bMonth)
	)
	=>
	(if (> (- ?cYear ?bYear) 80)	
		then	
		(assert (potential-fraud
			(provider-ID ?pId)
			(bene-ID ?bId)
			(claim-ID ?cId)
			(marked FALSE)
			)
		)
	)
)

;Because we only have the claims start year and month, this is more of an approximation.
(defrule died-earlier
	(outpatient-data
	(bene-ID ?bId)
	(provider-ID ?pId)
	(claim-ID ?cId)
	(claim-start-year ?cYear)
	(claim-start-month ?cMonth)
	)
	(beneficiary
	(bene-ID ?bId)
	(has-died TRUE)
	(death-year ?dYear)
	(death-month ?dMonth)
	)
	=>
	(bind ?cYearNum (* ?cYear 365))
	(bind ?cMonthNum (* ?cMonth 30))
	(bind ?dYearNum (* ?dYear 365))
	(bind ?dMonthNum (* ?dMonth 30))
	(if (> (+ ?dYearNum ?dMonthNum) (+ ?cYearNum ?cMonthNum))
		then
		(assert (potential-fraud
			(provider-ID ?pId)
			(bene-ID ?bId)
			(claim-ID ?cId)
			(marked FALSE)
			)
		)
	)
)

; Creating a template with a provider-ID and bene-ID should generate unique facts.
; So we can just add all the flags at the end.
(defrule add-flags
	(declare (salience -10))
	?pFraudData <- (potential-fraud
	(provider-ID ?pId)
	(bene-ID ?bId)
	(claim-ID ?cId)
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
	(declare (salience -20))
	(provider-data
	(provider-ID ?pId)
	(num-fraud-claims ?nClaims)
	)
	=>
	(printout writeFraudFile ?pId " " ?nClaims crlf)
	(if (> ?nClaims 0)
		then
		(printout writeFile "FRAUD-DETECTED: " ?pId crlf)
	)
)
