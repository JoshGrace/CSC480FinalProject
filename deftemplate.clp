(deftemplate prospect
"template representing an insurance claim"
; field representing the make of a car
(slot Make
; type of field
(type STRING)
; default value of field name
(default "NONE"))

; field representing the Incident area
(slot incident_area
; type of field
(type STRING)
; default value of field assets
(default "NONE"))
; name of field
(slot age
; type. NUMBER can be INTEGER or FLOAT
(type NUMBER)
; default value of field age
(default 80)))
