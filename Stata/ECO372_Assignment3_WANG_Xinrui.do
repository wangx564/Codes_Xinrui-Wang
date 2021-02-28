/* 	=============================================================
	This is the template do-file for Patrick Blanchenay's 
	ECO372 Assignment 3. Before anything else, rename this file, 
	changing "SURNAME" to your ACORN surname, and "Firstname" to 
	your ACORN first name. Use _ for spaces.
	
	For me, it would be: ECO372_Assignment2_BLANCHENAY_Patrick.do

	Comment your code, explain what steps you are doing. 
	You can insert comments before the instruction, or at the 
	end of lines.
	
	You should also use indentation to make your code easy to read.
	
	Remember that running this do-file does not save it.
	============================================================= */
	
											
/* =============================================================
	THINGS TO CHANGE
	============================================================= */

// Working directory:  This is the folder where your do-file and dataset are located
cd "C:\Users\Owner\Desktop\ECO372\Assignment\A3"

// SURNAME (Last name) as on ACORN (replace BLANCHENAY)
local surname WANG // One word only

// First name as on ACORN (replace Patrick)
local firstname Xinrui // Only the fist of your given names, as it appears on ACORN

// Student number, replace 12345678 by your student number, without quotes
local studentnumber 1003830063

/* 	=============================================================
	Do not change the following commands
	============================================================= */
cap log close _all // closes any previously opened log files
set seed `studentnumber'
log using "ECO372_Assignment3_`surname'_`firstname'.log", replace text 	// This log file will be regenerated everytime you run the do-file
set more off 	// This tells Stata to automatically continue if displays exceed screen capacity, instead of making user click
clear			// Removes any data from memory every time this script is run.
display "ECO372_Assignment3 " _n "`surname' `firstname' `studentnumber'" _n c(current_date) c(current_time)
																		


/* 	====================================
	============ EXERCISE  1  ============
	==================================== */

use "datasets/Angrist_etal_Columbia2002_1.dta", clear		// Loads the file
datasignature										    // checks data integrity			

// your code for the Exercise questions a-e goes here

//a)
//browse
describe

//b)
mean math reading writing

//Get estimates of the effect of winning the voucher lottery on test scores
//c)
// express test scores in terms of standard deviations
gen totalsd = totalpts/1.002749
gen mathsd = math/1.002821
gen readsd = reading/1.003512
gen writesd = writing/1.001712

//include covariate site dummies only in regression
regress totalsd vouch0 i.t_site, robust
estimates store OLS11

regress mathsd vouch0 i.t_site, robust
estimates store OLS12

regress readsd vouch0 i.t_site, robust
estimates store OLS13

regress writesd vouch0 i.t_site, robust
estimates store OLS14

esttab OLS11 OLS12 OLS13 OLS14 using "OLS1.rtf", se ///
	drop(*.t_site _cons) ///
	label ///
	replace mtitles("OLS Total Points" "OLS Math Scores" "OLS Reading Scores" "OLS Writing Scores") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic")) ///
	addnote("Test scores are in standard deviation units.")
	
//d)
regress totalsd vouch0 i.t_site age sex mom_sch dad_sch strata svy hsvisit, robust
estimates store OLS21

esttab OLS21 using "OLS2.rtf", se ///
	drop(*.t_site age sex mom_sch dad_sch strata svy hsvisit _cons) ///
	label ///
	replace mtitles("OLS w/ Covariates") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic")) ///
	addnote("Dependent variable is Total Points. Test scores are in standard deviation units. ")

count if mom_sch == .
count if dad_sch == .
count if strata == .

use "datasets/Angrist_etal_Columbia2002_2.dta", clear		// Loads the file
//datasignature												// checks data integrity			

//f)
describe

//g)
regress scyfnsh vouch0 svy hsvisit age sex i.strata i.month, robust
estimates store OLS31

regress inschl vouch0 svy hsvisit age sex i.strata i.month, robust
estimates store OLS32

esttab OLS31 OLS32 using "OLS3.rtf", se ///
	drop(svy hsvisit age sex *.strata *.month _cons) ///
	label ///
	replace mtitles("OLS Highest grade completed w/ Covariates" "OLS Currently in school w/ Covariates") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic"))

//i)
regress usesch vouch0, robust

//j)
regress scyfnsh usesch svy hsvisit age sex i.strata i.month, robust
estimates store OLS41

ivregress 2sls scyfnsh (usesch = vouch0) svy hsvisit age sex i.strata i.month, robust
estimates store IVS41

esttab OLS41 IVS41 using "Regression.rtf", se ///
	drop(svy hsvisit age sex *.strata *.month _cons) ///
	label ///
	replace mtitles("OLS w/ Covariates" "IV w/ Covariates") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic")) ///
	addnote("Dependent variable is the highest grade completed.")
	
//k)
regress usesch vouch0 svy hsvisit age sex i.strata i.month, robust
test vouch0 //get the F statistic

//l)
ivregress 2sls inschl (usesch = vouch0) svy hsvisit age sex i.strata i.month, robust

/* 	=============================================================
	============ 	FINAL COMMANDS 	(do not change)	============
	============================================================= */
log close				// closes your log file
/* 	=============================================================
	============ 			END OF SCRIPT			 ============
	============================================================= */
