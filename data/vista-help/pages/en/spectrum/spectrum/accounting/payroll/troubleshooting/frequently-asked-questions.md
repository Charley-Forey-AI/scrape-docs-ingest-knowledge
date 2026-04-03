---
title: "Frequently Asked Questions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/troubleshooting/frequently-asked-questions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/troubleshooting/frequently-asked-questions"
---

# Frequently Asked Questions

Quick access to a list of helpful
 answers to questions related to the Payroll module.

## How can I change the Payroll Number on the Certified Payroll Report?

If you need to change the week number on the Certified Payroll
 Report, you will need to have posted at least one time card to the certified job. When
 determining the week number, Spectrum looks at the first payroll date posted into the
 software. Below are the steps you can follow to change the initial payroll date.

1. Go to Payroll > Period End > Employee Certified
 History.

1. Call up an employee code for someone who worked on the certified job in question.

1.  Highlight the appropriate check and click the Time Card button.

1. Change the Work
 Date to the first day the job was certified. Note: These steps only have to be performed on one time card
 line. It is not necessary to perform these steps on multiple time card lines as
 the SQL view looks to find the first date payroll was charged to the
 job.

1. Rerun the Certified Payroll
 Report. Notice that the week number has changed accordingly.

## How can I make sure that the complete add-on was paid this month?

Add-on exceptions occur when a monthly limit is specified and the scheduled payment plus
 amounts already paid do not sum to the limit. The Exception format of the Add-on History
 Report is designed to show when the full amount is not scheduled to be paid.
For example, an employee is set up to receive $25 a week for
 healthcare reimbursement, with a $100 a month limit. This weekly add-on cost needs to be
 paid regardless of whether or not the employee works every week. If the employee works
 for the first week of the month but not the second week, running this report would show
 that the employee had only received $25 so far this month, that the scheduled amount the
 employee should have been paid was $50, and therefore there is a difference of $25
 remaining.

## How can I make sure that the complete add-on was paid this month for an employee?

You can view add-ons and deductions for an employee by viewing their employee file. Go
 to Payroll > Maintenance > Employee, and search for and select the appropriate employee name. Under
 Properties, select Deductions/Add-ons.
 From this page, you can view the add-ons and deductions taken, monthly and annual
 limits, the cycle limit, and other details.

## How can I make sure that the complete deduction was taken this month?

The Exception format of the
 Deduction History Report is designed to provide information regarding recurring
 deductions that are set up with a monthly limit. It shows those employees that have not
 yet had sufficient deductions taken since the last month-end to assure that the full
 deduction amounts will be taken during the current period.
For example, if medical insurance premiums are taken as a fixed
 deduction each week but the employee does not receive a check one week, the deduction
 would not be taken and would then appear as an exception on this report. The report
 computes the scheduled amounts yet to be deducted during the month, adds deductions
 already taken, and compares the sum to the monthly limit. Any shortfall is reported as
 an exception.

## How do I move a saved time card image back into the unassigned batch
 document?

To move a saved image back into the Batch document you will need to
 restore the Batch to its original state then delete the image from the timecard. Follow
 these steps.

1. In Pre-Time
 Card Entry (or any of the pre-time card entry or time card entry
 screens that support the Document Imaging ) open the record with the image you want to move back to the
 Batch.

1. Select Batch to open Batch
 Documents then select the batch you want to restore the image to.
 The selected batch is now in the viewer with a display of all thumbnail pages that
 have not been moved to a transaction.

1. Right click any thumbnail in the batch and select
 Copy. Insert before or after or any option to restore
 the batch. The system will now display this message: "Pages of this document have
 been moved to another document. To perform the requested action, the used pages
 must be restored."

1. Click OK on the Confirm window. Note: The batch is now updated with all
 the restored images.

1. Review the remaining pages to identify images correctly moved
 to other timecard entries. Once identified, right click on the images then select
 Delete . To complete the process, delete the image incorrectly moved
 from the batch onto the time card. Select View Transaction then
 Modify Image
 Information and click Delete  from the
 Modify window.

## Does Payroll support multi-company work order entries?

The Pre-Time Card Entry, Time Card
 Entry, Layoff Check Entry, and Pre-Time
 Card Import features all support multi-company work order cost entries.
 You will be able to charge time for an employee in one company (for example, HHC) to a
 work order in a different company (for example, ARC). During the Payroll Update,
 Spectrum stores the actual labor cost history in the ARC work order cost history table.
 Likewise, after entering pre-time cards for multi-company work (in HHC), the entry is
 available for billing selection on the work order (in ARC).

## We are a non-union shop that does prevailing wage work. Should we use non-union pay
 groups or wage codes?

You can use wage codes or non-union pay groups. However, you may not
 use both at the same time.
Used together, union and wage codes can be used to create unlimited
 wage tables. Multiple wage codes can be assigned to a job and to a phase. Up to four
 add-on or deduction codes may be associated with the union code. This provides a way to
 automate recurring deductions for a specific type of work. This logic works for
 Davis-Bacon and prevailing wage jobs.
These tables can also be used to control pay rates when the employee
 is working on a piece of equipment. For example, the employee may earn $8/hour as a
 laborer and $15/hour when running the backhoe.
Pay groups provide a means to set up a series of default pay rates
 for non-union employees. Pay group features include the ability to set different burden
 rates (estimated) by employee, job, or phase. Only two add-ons or deduction codes may be
 associated with the pay group code. This is a wage table that works for Davis-Bacon,
 prevailing wage, and non-prevailing wage jobs.
If your company has both union and non-union employees, you will want
 to use the union and wage code system.
Union & Wage Codes versus Non-union Pay Groups
 Features
 Non-Union Pay Groups
 Wage Codes

A wage table that assists in data entry by defaulting
 in the proper pay rate.
 X
 X

How many can be associated with a job?
 One
 Unlimited

Supports Davis-Bacon & prevailing wage jobs
 X
 X

Provides billing rates for the Time +Material
 module
 X
 X

Ability to set specific burden rates based on type of
 labor
 X

Accrue fringes based on type of labor
 X

Ability to set defaults by job
 X
 X

Ability to set pay defaults by phase
 X
 X

Ability to gross up wages for a certain benefit
 X

Can control the worker's compensation rate
 X

Can be used with union and non-union employees
 X

Defaults in equipment rates based on type of labor
 performed
 X

Ability to set an employee specific pay rate
 X

Supports employee specific pay rates when working on a
 specific phase
 X

Set a minimum pay percentage
 X

Pay an employee a lower rate for specific phases, even
 when their normal rate is higher. For example, an employee is paid less
 while traveling to the job site verses when he is working at the job
 site.
 X


## How can we use the common paymaster approach to payroll to control pay rates and
 create certified payroll reports?

The following example outlines how to use the common paymaster approach to control pay
 rates and create reports.
Scenario
Company XYZ is the common paymaster. HHC has job 650 that is a
 certified job.
Setup for Company XYZ - Common Paymaster

- Set employees and all associated payroll information into
 this company.


- Create Pay Group 650. Remember to include any
 phase or employee overrides as needed.


Setup for Company HHC - Job Company

- Set up the "shell" for pay group 650 in this company.
 Specifically, create the pay group code and a description. Do not enter any pay
 information or other overrides. You are only creating the pay group code so you
 can "associate" it with the job.


- The rate information will default from the pay group set up
 in the common paymaster company (XYZ).


Payroll Processing - Common Paymaster Company
When processing multi-company payroll, Spectrum will look to the pay
 group within the common paymaster company (XYZ). In other words, the rates set up in
 XYZ's pay group will automatically default in during data entry.
Certified Payroll Reporting - Job Company
Print the Certified Payroll Report from the job company (in this
 example HHC).

## What are "Covered Earnings" on the Worker's Compensation Rate per $100 Report and
 how do the "Covered Earnings" differ from the Total Earnings?

If the worker's compensation method is Straight time equivalent, the covered
 earnings are the regular and straight time equivalent of the employee wages.
Example: John Doe worked 43 hours this week.
40 Regular hours @ $25/hour $1000
2 Overtime hours @ $37.50/hour 75
1 Double time hours @ $50/hour 50
Total Earnings $1125
Covered Earnings:
43 hours @ $25/hour$1075
(this amount does not include the premium value of overtime and
 double time earnings)
Covered Earnings may also include any other pay type earnings NOT
 specifically excluded in the Payroll Tax Table Maintenance > Exclusions Maintenance for this state.
The Total Earnings column on this report does not necessarily equal
 Regular Earnings plus Overtime Earnings. Total Earnings includes other pay types, such
 as Vacation, Sick, Holiday pay, and so forth; which may not be subject to worker's
 compensation tax.
Reconciling:

1. First, check the worker's compensation method in the
 Worker's Compensation Code
 Maintenance screen in the Method field. If it's Straight time equivalent, review
 the information above.

1. If the method is Total earnings, or the total
 earnings source is unknown, print the employee's Wage and Tax History Report for
 the same date range, and the Add-On History Report or the Deduction History Report
 for the same date range.

## The Payroll module states that the current processing date is 8/15/XX when the true
 system date is 8/14/XX. Why don't the dates match?

To understand the resolution, you must first understand the Spectrum
 Processing Date Change screen.
The Processing Date Change screen
 (AdminProcessing
 Date Change) allows you to define a minimum, maximum, and current date
 for each module.
Each computer's operating system has a built-in clock, which keeps
 track of the actual calendar date. Spectrum reads this date when the first user logs on
 each day. The current processing date is set using the following rules:
Computer
 Date: Use the computer's date when it is within the minimum/maximum date
 range, and it is greater than the current processing date previously entered.
Current Processing
 Date: If the computer's date is less than the existing current processing
 date, do not change the date.
Maximum
 Date: If the computer's date is past the maximum date, use the maximum
 date as the current processing date.
Why?
The current processing date is set based on the first user to log on
 to Spectrum each day. If the computer date is earlier than the current processing date,
 then it is assumed that the date on the computer is incorrect and is not used. The
 theory is that you would not want to use an earlier date just because the first person
 that logged in that day manually changed his/her computer system date.
Spectrum has always used this logic. If this is not desired, then
 manually change the current processing date accordingly.
Examples:
What will the current processing date be, based on the following
 scenarios? All assume these minimum and maximum dates:
Minimum Date 8/01/XX
Maximum Date 8/31/XX
Scenario
 What's the Current Processing Date?
 Reason

On 8/05/XX, I log on to Spectrum. The current
 processing date is 8/04/XX.
 8/05/XX
 The computer date is within the minimum/maximum dates
 and it is greater than the previous current processing date.

On 8/10/XX, I manually change the current processing
 date to 8/31/XX.
 8/31/XX
 You can reset the date with manual entry.
On 8/15/XX, I log into Spectrum. The current
 processing date is 8/31/XX.
 8/31/XX
 Current processing date does not reset to the computer
 date because it is earlier than the previous current processing date.


On 9/05/XX, I log into Spectrum. The current
 processing date is 8/31/XX.
 8/31/XX
 The computer date is past the maximum date; therefore,
 the maximum date is used.


## I want a certain deduction to be taken out on the first and third weeks of the
 month. How can I set this up in Spectrum?

Use the Week Numbers field
 when setting up deductions and add-ons. Here you can tell Spectrum which payroll weeks
 you would like the item to be used on. Once this is set up, you will need to tell
 Spectrum which week you are processing for payroll.
Setup Steps

1. On the Site
 Map screen, select Payroll  >  Maintenance  >  Deduction/Add-on Code
 Maintenance.


1. On the
 Properties tab, locate the Week Numbers field.


1. Enter the week number that you want the add-on or deduction
 to be taken on. For example, you would enter 13 or 31 for a deduction that is
 taken on the first and third weeks of the month.


Processing Payroll
When setting a new pay cycle (Payroll > Data Entry > Payment Processing), you will need to tell Spectrum what week number you are processing.
 Continuing with our example, if this was the first payroll week of the month, you would
 enter 1. If this was the second week, you would enter 2.
Any deduction or add-on codes with week numbers that are blank are
 assumed to be ALL payroll weeks and will be processed accordingly.

## How does Spectrum calculate tax on bonus checks based on how the cycle is
 set?

Select this checkbox if you want the software to annualize the standard pay plus the
 bonus amount to determine the Federal income tax amount, otherwise leave this checkbox
 clear.
Note: This feature does not affect the calculation of
 state, county, and local taxes (unless based on a percent of Federal tax).
How does Spectrum calculate tax on bonus checks based on how the
 cycle is set?
At the time of pay cycle setup, an option to calculate bonus checks
 based on annualizing the payroll tax withholding for the year is available. This option
 uses the total paid-to-date, including the bonus, and withholds taxes based on the
 annual calculation instead of withholding a fixed percent.Note: This feature does not affect the calculation of state, county, and local taxes
 (unless based on a percent of Federal tax).

## How does Spectrum calculate tax on bonus checks based on how the cycle is set? -
 Example #1

If the Pay annual bonus check
 box is selected:
Hourly employee paid weekly, single ($20/hr or $41,600 annualized)
 zero exemptions, bonus $7500.00.
Total earnings including bonus = $49,100.00
$49,100.00-zero exemption ($3,100x0) = $49,100.00
$7,500.00 divided by $49,100.00 = .15. This is the portion of the
 annualized income included bonus that is attributable to the bonus (rounded to two
 decimals).
Calculate tax for $49,100.00 = $8,445.00
(based on 2003 tax rates: $3870.00 + 25% above $30,800.00 =
 $8,445.00)
$8,445.00 x .15 = $1,266.75 tax on bonus check

## How does Spectrum calculate tax on bonus checks based on how the cycle is set? -
 Example #2

If the Pay annual bonus check
 box is NOT selected:
Hourly employee paid weekly, single ($20/hr or $41,600 annualized)
 zero exemptions, bonus $7500.00.
If you do not choose to annualize the bonus, the calculation will be
 $7,500.00 x 52 = $390,000 (based on the 2003 tax rate: $92,676.00 + 35% above $36,751
 divided by 52 = $2,245.30).
