/* 	=============================================================
	This is the template do-file for Patrick Blanchenay's 
	ECO372 Assignment 1. Before anything else, rename this file, 
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
cd "C:\Users\Owner\Desktop\ECO372\Assignment\A2"

// SURNAME (Last name) as on ACORN (replace BLANCHENAY)
local surname WANG // One word only

// First name as on ACORN (replace Patrick)
local firstname Xinrui // Only the first of your given names, as it appears on ACORN

// Student number, replace 12345678 by your student number, without quotes
local studentnumber 1003830063

/* =============================================================
	Do not change the commands below
	============================================================= */
log close _all // closes any previously opened log files
log using "ECO372_Assignment2_`surname'_`firstname'.log", replace text 	// This log file will be regenerated every time you run the do-file
set more off 	// This tells Stata to automatically continue if displays exceed screen capacity, instead of making the user click
clear			// Removes any data from memory every time this script is run.
set seed `studentnumber' // Fixes randomization issues
display "ECO372_Assignment2 " _n "`surname' `firstname' `studentnumber'" _n c(current_date) c(current_time)
																		

/* ====================================
	============ EXERCISE  =============
	==================================== */

use "datasets/medicalexpenses_2000.dta", clear			
datasignature										// checks data integrity			

// your code for the Exercise questions goes below this

//a)
//(i)~(iii)
browse
describe docvis
//(iv)
count if docvis == . //check for NA
mean docvis

//b)
count if income == .
reg docvis income, robust

//c)
reg docvis income

//d)
count if private == .
reg docvis c.income##private, robust

//e)
count if firmsize == .
reg docvis firmsize, robust
reg private firmsize, robust

//g)
count if noreast == .
count if midwest == .
count if south == .
reg docvis c.income##noreast c.income##midwest c.income##south, robust

//another option:
count if msa == .
reg docvis c.income##msa, robust  

//h)
count if female == .
reg docvis c.income##female, robust

//i)
keep if female == 1 //take out the data for female only
tabulate female
count if married == .
reg docvis c.income##married, robust


/* 	=============================================================
	============ 	FINAL COMMANDS 	(do not change)	============
	============================================================= */
log close				// closes your log file
/* 	=============================================================
	============ 			END OF SCRIPT			 ============
	============================================================= */
