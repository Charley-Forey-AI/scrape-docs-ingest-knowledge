---
title: "Common Year-End Mistakes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/troubleshooting-and-faqs/common-year-end-mistakes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/troubleshooting-and-faqs/common-year-end-mistakes"
---

# Common Year-End Mistakes

Solutions to common year-end mistakes.

## I did not perform the Build W-2 Forms before my first payroll in January. What should I do now?

This should not present a serious problem because the Build W-2 Form Update can be run at any time.
When performing the update, simply enter 01/01 through 12/31 to include only prior year amounts. Be sure the FICA limits indicated on the starting screen of the build are those for the prior year. Also, because this step is being performed out of the typical order, pay particular attention during the W-2 review process to be sure all employees (including those terminated and deceased) are included.

## I did not perform the Year End Update before my first payroll in January. What should I do now?

By not clearing the payroll at year-end, certain taxes that contain annual limits (such as FICA, unemployment, and SDI) will not have calculated correctly for most employees.
The payroll cycle must be voided and re-issued to correct this problem. Use the same check date when recording the void cycle, and if multiple cycles must be voided, do each one separately, newest to oldest (01/12 then 01/05, for example).
After the void process has been completed, perform the Year End Update to set all employees' year-to-date amounts to zero. You should also review the Year End Checklist to be sure no other year end steps were overlooked.
Finally, re-enter the new year's payroll cycle(s), as regular or manual checks. Regardless of whether the miscalculated checks have been issued to employees, the system will require that new check numbers be assigned during this cycle. If checks were already distributed, be sure to record the same deductions and net pay as the original checks issued.

## In reviewing the W-2 year-end figures, some employees did not show up in the file to receive a W-2 at all. What should I do?

- You could re-build the W-2s. Any manual changes you might have made in the W-2 Form Maintenance screen will be overwritten, so take a record of what will need to be done again.

- Employees with a status of "exempt" do not receive a W-2. If an employee's status was set to "exempt" in error, manually add the individual to the W-2 Form Maintenance screen.

## I did not change the tax tables for the new year, but I have already processed payroll in the new year. What should I do now?

In nearly all cases, you don't need to do anything.
Any income tax surplus or deficit is resolved on an annual basis when employees file their taxes; based on any number of circumstances, even the correct tax tables cannot prevent this entirely. Small variations in withholding for one or two weeks is not a significant issue.
For instances where the amount for withholding must be a specific amount, take these steps to ensure that the quarterly and year-end reports remain accurate:

1. void the checks

1. apply the most up-to-date tax tables

1. re-issue the checks

## I am reviewing a January payroll and the 401(k) deduction didn't show up during the check calculation. The employee was 'over-the-limit' last year, but it should have started deducting again at the beginning of the year. What's wrong?

It appears as though the 401(k) code's Clear employee balance at year end checkbox was not selected at the time the Payroll Update was run. The Clear employee balance at year end checkbox in the Deduction / Add-on Code Maintenance screen is used to designate whether to clear accumulated balances at year-end.
Select the checkbox, but don't re-run the Payroll Update. Because the new payroll year is already in progress, it would be a mistake to re-run the update.
Instead, select the checkbox and then recalculate only this employee's payroll amounts. To do so, navigate to Payroll >  Utilities > Rebuild Employee File. This action clears out the YTD balance, which causes the deduction to resume.

## An employee loan paid off last year has started showing up on the employee's check again. It was a recurring deduction that reached the limit months ago. What's wrong?

It could be that the Clear employee balance at year end checkbox on the deduction code was selected, which cleared the accumulated balance at year-end. Because the accumulated balance has been erased, the deduction was taken again.
This deduction is no longer needed for this employee; simply delete it from the Employee Deduction/Add-on Maintenance screen. If the January payroll in which the amount was deducted on the employee check has been updated, refund the amount using the same code.

## Why am I receiving an error message stating: "ERROR- Year End Update must be performed before beginning a pay cycle dated later than <the current year>?"

The Payroll > Data Entry > Payment Processing > Set New Cycle screen prohibits users from assigning a check date at the beginning of a new calendar year until after the Year End Update has been performed. This helps prevent incorrect tax calculations. If you received the error message above, you must perform the Year End Update for the prior calendar year before you continue to process payroll for the new year.

## I need to void a payroll check issued last year. What should I do now?

If you are replacing a check the employee lost, go to the Payroll > Data Entry > Replacement Check screen. It is important to use a current date as the replacement check date. This way, both the void and replacement check will post to the current year, thereby creating a net effect of zero in the employee history file for the current year.
If you are voiding a check and not replacing it, or voiding and reissuing with a different amount, it is vital to follow the instructions below to ensure that the W-2 issued and current year payroll records are accurate.
Once the payroll year-end has been completed, all transactions recorded during the payroll cycle (payroll check, bonus check, etc.) must be for the new year. This is because many of the payroll calculations depend upon year-to-date information. If additional prior-year entries are made, the totals which have accumulated since the Year End Update was run will be inaccurate. This means that any additional payroll transactions for the prior year cannot be recorded in Spectrum as part of a payroll cycle.
To correct the prior year error, transactions entered in the following areas may be required:

- W-2 Form Maintenance to correct the employee's W-2 information.

- General Ledger Journal Entry to correct liability and expense accounts. If subsidiary ledgers (Job Cost or Equipment Control) are affected, this can be recorded as part of the journal entry.

- Make manual notations (in ink) of changes on affected tax reports, such as Quarterly Federal Tax Report and the Unemployment Tax Report.

An alternative to the above is to reverse all new transactions, and return the Payroll module to the prior year, but this option isn't recommended because it is riskier for a number of reasons.

- It is possible that prior-year information has already been purged during the course of normal year-end processing.

- If any payroll cycles have already been updated, you will need to void all checks issued in the new year, using care to to void each check as of the same date it was issued.

- You will need to print and retain paper copies (plain paper is fine) of the W-2 Listing and the W-2 Forms.

## When I performed the Build W-2 Forms, I did not enter descriptions for Boxes 12 or 14, and/or other entries are incorrect.

- The safest solution is to enter the changes you would like to make into the W-2 Form Maintenance screen. However, depending on the nature of the error during the Update, this may present a challenge in determining the correct figures.

- Another option is to perform the Build W-2 Forms again, after setting the values correctly. However, this isn't possible if terminated employees or earnings history were purged at year-end. Even if no data was purged, any changes already made in the W-2 Form Maintenance screen would need to be re-done after the update.Print and retain both the W-2 Listing and a copy of the W-2 forms (printed on plain paper) prior to re-updating. Be sure to refer to the Build W-2 Forms screen instructions when performing the Update again.

## In reviewing the W-2 year-end figures, the state wages are not correct. The Cafeteria/Section 125 or 401(k) deductions were not set up correctly when the payrolls were originally processed. What should I do now?

The figures in the W-2 Form Maintenance screen following the update represent the sum of state wages processed during each payroll cycle during the year. If 401(k) or cafeteria/Section 125 tax exempt flags were set incorrectly at any time, this would be the result.
Use the W-2 Form Maintenance screen to change these amounts manually. The State, County & Local Quarterly Tax Report and the Deduction History Report will be particularly useful during this process.

## I have a large figure showing up on the "fractions only" (aka Tax adjustments) line of the Quarterly Federal Tax Report. It's normally just a few cents. What's the problem?

Confirm that the date range used when the report was printed includes three calendar months or less. It cannot successfully be printed for a wider date range because of the three month daily grid on the lower half of the report. If for some reason you wish to print 09/27 to 12/27 (four months: 09, 10, 11, 12), print two reports and simply sum them.
If you are printing this report in January for date ranges from a prior year, it is possible that the report is incorrect because the Federal tax tables, specifically FICA rates and limits, have already been updated for the new year. If this report needs to be reprinted for the past year, temporarily return the FICA rates and limits to the prior year's figures. Note: Remember to reset them to the current year as soon as you are done!

If there is still a large "fractions only" variance after eliminating the above conditions, search for the cause by gradually narrowing the date-range of the report.

- If you are troubleshooting a problem in a certain quarter, print the three monthly 941 reports (for example, October, November, and December for Q4). It is likely that the variance will show up primarily on one of the reports.

- To further narrow the search, print a separate 941 report for each check date in the month of the variance.

- Once a single week has been identified, use the Wage and Tax History Report and/or the reports printed during the payroll cycle to try to identify the individual entry or entries.

- Take appropriate corrective action once you've found the source of the problem.

## I printed my Unemployment Tax Report (FUTA, SUTA) and the excess calculation is wrong. What should I do now?

This report provides information on excess calculations computed during each payroll cycle during the specified date range. Therefore, this report may not be correct if limits were adjusted or 'tax effects' of deductions changed during the year.
If such changes were made, there is a useful Excess Unemployment Report available for use in auditing this problem by recalculating excess amounts based on current settings. This is included as a second format when printing the Unemployment Tax Report.

## I printed my Unemployment Tax Report (FUTA, SUTA) and the tax calculation is wrong. What should I do now?

This report does not recalculate the tax based on current settings.

- This report provides information on tax liabilities actually accrued during the payroll cycles during the date range specified.

- These are the amounts that were actually debited to the expense account and credited to the liability account during each payroll cycle.

- If the rate has been changed at any time during the period, the tax amounts will not seem to 'multiply across' correctly.

To confirm that the rate has been altered, and to identify precisely when the change occurred, reprint this report for a smaller date range. Begin the search in January or during April since corrections to these rates are commonly entered as the 1st quarter filing is being prepared.

## In comparing the unemployment reports for state (SUTA) and Federal (FUTA), I see that the wages are different. What's wrong?

It may be that nothing is wrong, but this should be investigated. This condition will occur when deductions carry different tax effects for the SUTA and FUTA calculation.
The most common example of this is a Cafeteria/Section 125 plan deduction; the wages subject-to FUTA are reduced by any Cafeteria/Section 125 deductions. Your state may not allow a similar exemption.
If your state and 'US' were set up differently for tax effect in the Deduction / Add-on Code Maintenance screen, this would be the result. The Wage and Tax History Report may be helpful because the limits for subject-to wages are defined.

## I work in multiple states and the sum of the state (SUTA) reports is greater than my total wages. What's wrong?

It is likely that unemployment was accrued for employees both in the resident and work state at times during the year.
In some cases, it is appropriate to accrue tax in both places, based on lack of reciprocity agreements between states. Other times, it may mean that too much tax was accrued, because unemployment was payable to only one of those states.
To review this further, select a few employees, printing their unemployment reports for a small date range, and then compare them to the Wage and Tax History Report printed during the payroll cycle(s) falling in that date range. This will show unemployment tax accrued for each place, for each employee.
Look for instances where a single employee has wages subject to unemployment and tax accrued in two or more states during the cycle. Unemployment is a complex tax area that varies widely across the country, and it is important to discuss your specific responsibility with your CPA.
