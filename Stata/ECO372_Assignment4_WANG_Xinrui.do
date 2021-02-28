/* 	=============================================================
	This is the template do-file for Patrick Blanchenay's 
	ECO372 Assignment 4. Before anything else, rename this file, 
	changing "SURNAME" to your ACORN surname, and "Firstname" to 
	your ACORN first name. Use _ for spaces.
	
	For me, it would be: ECO372_Assignment4_BLANCHENAY_Patrick.do

	Comment your code, explain what steps you are doing. 
	You can insert comments before the instruction, or at the 
	end of lines.
	
	You should also use indentation to make your code easy to read.
	
	Remember that running this do-file does not save it.
	============================================================= */
log close _all 														// closes any previously opened log file	

/* =============================================================
	THINGS TO CHANGE
	============================================================= */

// Working directory:  This is the folder where your do-file and dataset are located
cd "C:\Users\Owner\Desktop\ECO372\Assignment\A4"

// SURNAME (Last name) as on ACORN (replace BLANCHENAY)
local surname WANG // One word only

// First name as on ACORN (replace Patrick)
local firstname Xinrui // Only the fist of your given names, as it appears on ACORN

// Student number, replace 12345678 by your student number, without quotes
local studentnumber 1003830063

																		
/* 	=============================================================
	Do not change these commands
	============================================================= */
cap log close
log using "ECO372_Assignment4_`surname'_`firstname'.log", replace text 	// This log file will regenerated everytime you run the do-file
set more off 	// This tells Stata to automatically continue if displays exceed screen capacity, instead of making user click
clear			// Removes any data from memory every time this script is run.
display "ECO372_Assignment4 " _n "`surname' `firstname' `studentnumber'" _n c(current_date) c(current_time)

/* 	=============================================================
	============ EXERCISE 1 ============
	============================================================= */
use "datasets/Dynarski2003.dta", clear			// If your files are placed correctly, you should not need to change that 
datasignature									// checks data integrity													

// YOUR COMMANDS FOR EXERCISE 1 GO HERE

//b)
describe

//c)
table fatherdec [weight = wt88], by(offer) contents(mean coll mean hgc23) ///
format(%9.3f) center

//d)
reg coll fatherdec##offer [weight = wt88] , vce(cluster hhid)
estimates store diff1

esttab diff1 using "Diff1.rtf", se ///
	keep(1.fatherdec 1.offer 1.fatherdec#1.offer) ///
	label ///
	replace mtitles("Difference-in-differences") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic")) ///
	addnote("Standard adjusted for clustering at the household level.")


/* 	=============================================================
	============ EXERCISE 2 ============
	============================================================= */
// Do not change those initial commands

clear
set seed `studentnumber'
set obs 780
gen workerID = _n
// YOUR COMMANDS FOR EXERCISE 2 GO HERE

gen byte cityA = (runiform() < 0.6) // allocate approximately 60% of workers to city A 
gen byte cityB = 1 - cityA // allocate the rest to city B
expand 7, generate(expandy) 
sort workerID expandy 
bysort workerID: gen year = 2012 + _n -1 // creates year 
drop expandy

//c)
// POST equal to 1 only for observations in year 2016 and following, and 0 otherwise
gen POST = (year >= 2016)
// HQ equal to 1 in city A in years 2016 and following
gen HQ = (POST == 1 & cityA == 1)

//d)
gen u = rnormal(0, 1.5) if cityA == 1 
replace u = rnormal(0, 1) if cityB == 1
tabulate cityA, summarize(u)

//e)
// ys2012 equal to the number of years elapsed since 2012
gen ys2012 = (year - 2012)

//f)
// generate w where κ0 = 5; κ1 = 2.1; κ2 = 0.8; κ3 = 0.4
gen w = 5 + 2.1*HQ + 0.8*(ys2012*cityA) + 0.4*(ys2012*cityB) + u

//g)
drop u HQ

//j)
reg w cityA##POST, vce(cluster workerID)
estimates store diff2
esttab diff2 using "Diff2.rtf", se ///
	keep(1.cityA 1.POST 1.cityA#1.POST) ///
	label ///
	replace mtitles("Diff-in-diff") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic")) ///
	addnote("Standard adjusted for clustering at the individual level.")

//k)
reg w cityA##POST ys2012 c.ys2012#cityA, vce(cluster workerID)
estimates store diff3

esttab diff2 diff3 using "Diff3.rtf", se ///
	keep(1.cityA 1.POST 1.cityA#1.POST ys2012 1.cityA#c.ys2012) ///
	label ///
	replace mtitles("Diff-in-diff" "Diff-in-diff w/ Time Trends") ///
	stats(N r2 F, labels("Obs." "R-squared" "F-statistic")) ///
	addnote("Standard adjusted for clustering at the individual level.")


/* 	=============================================================
	============ 	FINAL COMMANDS 	(do not change)	============
	============================================================= */
log close
graph close _all

/* 	=============================================================
	============ 			END OF SCRIPT			 ============
	============================================================= */
