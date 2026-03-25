---
title: "Field Definitions: PR Check Print Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/pr-check-print-form/field-definitions-pr-check-print-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/pr-check-print-form/field-definitions-pr-check-print-form"
---

# Field Definitions: PR Check Print Form

The following is a list of field descriptions for the PR Check Print form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Enter the PR group for which to process and print checks.

##  Pay Period Ending Date

 Enter the pay period ending date that, when combined with the PR group, will identify an open pay period. Initially defaults the last accessed pay period for the current user.

##  Paid Date

Required.
Enter the paid date that will be printed on each check and used when updating CM and PR Payment History.

##  Paid Month

Enter the month to which you are posting these payments. Must be either the first or second month assigned to this Pay Period.
The paid month determines the month accumulations, CM, and GL are updated for pay sequences on these checks. Tax reports, quarterly tax reports, and W-2s are all based on paid month.
Note: The Print button and Refresh button (on Existing Checks tab) will be disabled until you enter both a Paid Date and Paid Month.

## Sort Checks By

Sort options control the order in which checks are printed. When an option is selected, the restriction range inputs change. The default sort option is Sort Name.

- N - Employee Sort Name— Checks print in employee sort name order. You may select the beginning and ending sort names to restrict the range of checks printed.

- E - Employee # — Checks print in employee number order. You may select the beginning and ending employee numbers to restrict the range of checks printed.

- J - Job, Check Print Order and Employee # — Checks print in job order, then check print order (defined in PR Employees, Add'l Info tab, Check Print Order field), then in employee number order. The job used for sorting is the current job assigned in the PR Employees form. Those employees with blank jobs and/or check print order print first. If you prefer to print in job and employee order, make sure the 'Check Print Order' field is blank for all employees.

- C - Check Print Order and Employee # — Checks print in check print order and employee number order. The check print order is assigned in the PR Employees form. Those employees with no check print order assigned print first.

- W - Crew, Check Print Order and Employee # — Checks print in order by crew, then check print order (assigned in PR Employees), then in employee number order. Those employees with no crew print first, sorted by check print order and employee number.

## Restrict by Payment Sequence #

Check this box if you want checks printed for a single payment sequence within the pay period.
Do not check this box if you want all fully processed payment sequences for each employee to print.

## Payment Seq #

Enter a valid payment sequence number to identify the sequence for which you want checks printed in this pay period.

## CM Account

Enter the override bank account (from CM Accounts) from which these checks will be paid. Defaults the CM account assigned to the payroll group (in PR Groups). If overridden, PR Employee Pay Sequence Control updates with the account specified here.

## Restrict by Employee Sort Name

This checkbox displays only when Sort Checks By
 field is set to N - Employee Sort Name.
Check this box to select the beginning and ending employee sort names by which to restrict the range of checks printed.
Uncheck this box to print checks for all employees.

## Beginning Sort Name

This field is enabled only when Sort Checks By
 field is set to N - Employee Sort Name and the Restrict by Employee Sort Name box is
 checked.
Enter the sort name with which to begin printing checks.

## Ending Sort Name

This field is enabled only when Sort Checks By
 field is set to N - Employee Sort Name and the Restrict by Employee Sort Name box is
 checked.
Enter the sort name with which to stop printing checks.

## Restrict by Employee #

This checkbox displays only when Sort Checks By
 field is set to E - Employee #.
Check this box to select the beginning and ending employee numbers by which to restrict the range of checks printed.
Uncheck this box to print checks for all employees.

## Beginning Employee #

Enter the employee number with which to start printing checks.

## Ending Employee #

Enter the employee number with which to stop printing checks.

## Restrict by Job and Employee #

This checkbox displays only when Sort Checks By
 field is set to J - Job, Check Print Order and Employee #.
Check this box to select the beginning and ending JC Co, Job, and Employee numbers by which to restrict the range of checks printed.
Uncheck this box to print checks for all employees.

## Beginning JC Co #

This field is enabled only when Sort Checks
 By field is set to J - Job, Check Print Order and Employee #and the
 Restrict by
 Job and Employee # box is checked.
Enter the JC Co# with which to start printing checks.

## Beginning Job

This field is enabled only when Sort Checks
 By field is set to J - Job, Check Print Order and Employee #and the
 Restrict by
 Job and Employee # box is checked.
Enter the job number with which to start printing checks.

## Ending JC Co #

This field is enabled only when Sort Checks
 By field is set to J - Job, Check Print Order and Employee #and the
 Restrict by
 Job and Employee # box is checked.
Enter the JC Co# with which to stop printing checks.

## Ending Job

This field is enabled only when Sort Checks
 By field is set to J - Job, Check Print Order and Employee #and the
 Restrict by
 Job and Employee # box is checked.
Enter the job number with which to stop printing checks.

## Restrict by Check Print Order and Employee #

This checkbox displays only when Sort Checks By
 field is set to C - Check Print Order and Employee #.
Check this box to select the beginning and ending Check Print Order and Employee numbers by which to restrict the range of checks printed.
Uncheck this box to print checks for all employees.

## Beginning Check Print Order

This field is enabled only when Sort Checks
 By field is set to C - Check Print Order and Employee #and the Restrict by Check Print
 Order and Employee # box is checked.
Enter the check print order (assigned to employees in PR Employees, Add’l Info tab) with which to start printing checks.

## Ending Check Print Order

This field is enabled only when Sort Checks
 By field is set to C - Check Print Order and Employee #and the Restrict by Check Print
 Order and Employee # box is checked.
Enter the check print order (assigned to employees in PR Employees, Add’l Info tab) with which to stop printing checks.

## Restrict by Crew and Employee #

This checkbox displays only when Sort Checks By
 field is set to W - Crew, Check Print Order and Employee #.
Check this box to select the beginning and ending Crew and Employee numbers by which to restrict the range of checks printed.
Uncheck this box to print checks for all employees.

## Beginning Crew

This field is enabled only when Sort Checks
 By field is set to W - Crew, Check Print Order and Employee #and the
 Restrict by
 Crew and Employee # box is checked.
Enter the crew code with which to start printing checks.

## Ending Crew

This field is enabled only when Sort Checks
 By field is set to W - Crew, Check Print Order and Employee #and the
 Restrict by
 Crew and Employee # box is checked.
Enter the crew code with which to stop printing checks.

##  Comment

 Enter a comment, up to 180 characters, that will be printed on the check stub. This entry is optional, and the default is blank.

## Beginning Check #

Enter the check number (1-9999999999) with which to begin the check print. Up to 10 digits allowed.
Note: If you need to change the check number (e.g. check number is incorrect), delete the old check number before entering the new one.

## Ending Check #

Enter the check number (1-9999999999) with which to end the check print. If the ending check number is reached before all of the employee payment sequence entries have been processed, then a message box will appear informing you that additional check numbers are required before checks can be printed.
Note: If you need to change the check number (e.g. check number is incorrect), delete the old check number before entering the new one.

##  Beginning/Ending Check #

 Specify the beginning and ending in a range of existing check numbers that you want to void or clear and reprint. All checks within this range display in the grid below, showing the employee name and number, payment sequence, and check number.

## Clear/Void Option

Clear Existing Check #'s (Numbers can be reused.) — Select this option if reprinting checks and the check numbers involved can be reused (i.e. no checks were printed and numbers are still valid). Click Clear to process the entries in the grid.
Void Existing Check #'s (Numbers cannot be reused.) — Select this option if reprinting checks and the check numbers cannot be reused (i.e. checks were printed, but due to an error or printer malfunction, checks are no longer valid). Optionally, enter a Void Memo, and click Void to process the entries in the grid.

##  Void Memo

 Enter a memo, up to 30 characters, to describe why these checks are being voided. Click the Void button to process the entries in the grid.
