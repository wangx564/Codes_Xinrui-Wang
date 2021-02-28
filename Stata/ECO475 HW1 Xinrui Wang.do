// Working directory
cd "C:\Users\Owner\Desktop\ECO475\Assignment"

log close _all
log using "ECO475 HW1 XinruiWang log", text replace 

set more off 	

use "hw1data.dta", clear			


//a) 
probit y x1 x2 x3 x4 x5 x6
eststo model1
esttab model1 using "model1.rtf", replace mtitles("Probit Model")

//b)
margins, dydx(x2)
margins, dydx(x5)

//c)
logit y x1 x2 x3 x4 x5 x6
eststo model2
esttab model2 using "model2.rtf", replace mtitles("Logit Model")

//d)
margins, dydx(x2)
margins, dydx(x5)


log close
