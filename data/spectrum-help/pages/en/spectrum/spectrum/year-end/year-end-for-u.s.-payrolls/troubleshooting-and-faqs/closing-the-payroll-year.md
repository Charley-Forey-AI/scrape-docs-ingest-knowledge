---
title: "Closing the Payroll Year | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/troubleshooting-and-faqs/closing-the-payroll-year"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/troubleshooting-and-faqs/closing-the-payroll-year"
---

# Closing the Payroll Year

Answers to some of the most common questions related to closing the payroll year.

## When should I close payroll for the tax year that's ending?

Plan to perform the year-end tasks any time after you complete your last payroll check dated in the ending year and before you issue any checks dated in the new year. The Spectrum application does not require you to do these steps on December 31st.

## What does the Year End Update function do? What effect does it have on my permanent payroll records in Spectrum?

The Year End Update resets all employees' year-to-date balances to zero. It does not remove any historical employee data.
If the Deduction/Add-on Code flag is set to clear at year-end, the Year End Update also sets the accumulated balance in the recurring deduction file to zero.

## May I start my first January payroll before printing W-2s?

Yes, but take the standard precautions because once the Year End Update is performed and the first payroll cycle is run, revising the previous year's information is much harder.�
After finishing the last payroll of the year that's ending, go to the W-2 Form Maintenance screen and perform a W-2 Build, and review the totals. Do this prior to the Year End Update step. The W-2 print does not have to be performed at this time.

## How do I go about reviewing the accuracy of the W-2 information?

It is best to review the information stored in each box on the W-2, beginning with your company name, address, and employer identification number and then working through each amount box after that. You should also check the totals page on the W-2 Listing, compare it to balanced payroll records, and then review the individual W-2s.

## What happens if the first payroll in the new year has a period end date in December of the prior year?

This is not a problem. W-2s are produced on a strictly calendar-year basis (using check date), so this cycle will be part of the new-year totals regardless of the period end date.
If you have the Period-end date or Work date expense accrual options selected on the Payroll Installation Properties tab, then expenses for this cycle will be reflected in December.

## I want to delete (purge) records of terminated employees. How do I do this?

Employee records may be purged by using the Delete Employee from Current Company screen in Payroll > Utilities.

## My fiscal year is different than the calendar year. Is there anything special I should know?

Because payroll is based on the calendar year, you will need to perform the Year End Update in the Payroll module at the end of each calendar year, even if you maintain the rest of Spectrum on a fiscal year basis.
Run the Payroll Year End Update *only* at the end of each calendar year, and not timed with the end of your fiscal year.

## My fiscal year-end is December 31st. Is there anything special I should know?

Your Spectrum application provides an unlimited Fiscal Calendar in the General Ledger module. To add new years or historical years to this calendar, see the General Ledger Help.

## How do you recommend I balance payroll for W-2s?

There is no substitute for sound procedures throughout the year. In general, the basis for year-end balancing should reflect the sum of accurate quarterly filings and routine reconciliation of liability accounts and bank statements.

- Bank Statement reconciliation. The best method for detecting manual and void checks that have not been entered into the system is through the bank statement reconciliation, which should be completed through 12/31, prior to issuing W-2s.

- Balance GL payroll. Verify that all General Ledger payroll liability account balances are reconciled through 12/31, prior to issuing W-2s. Use the Payroll > Reports > Liabilities Reconciliation report for this purpose.

For reconciling individual W-2 boxes:

- Boxes 1-6: Reconciling boxes 1-6 on the W-2 should focus on matching the sum of the four Payroll > Reports > Quarterly Federal Tax Reports, sometimes referred to as the 941 Federal Quarterly Report, filed during the year. If a difference is found (beyond 'fractions')

- Reprint the Quarterly Federal Tax Report in Spectrum to determine whether changes may have occurred after the filing was made (backdated checks or voids).

- To locate a difference, reconcile the figures on the quarterly report to the Tax History Report for the same date range.

- The source information for both the Build W-2 Forms and this history report is the employee state tax history file.

- Boxes 9-14: Print the Deduction History and Add-on History Reports to help you reconcile boxes 9-14 for dependent care benefits, 401(k), and other amounts.

- Boxes 15-20: Print the Wage and Tax History Report or the Subject-to-Tax Report to help you reconcile boxes 15-20 for state and local information.

## We've instituted a Heath Savings Account (HSA) this year. How do we record this on the W-2?

Create a deduction for the employee portion, and an add-on for any employer contribution. Both the add-on and deduction codes are added to Box 12 when Spectrum builds the the W-2.
See [Benefit Setup](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/year-end-preparatory-actions/year-round-benefit-setup-for-year-end-reporting) for details on recording benefits in Spectrum.

## How should our company report the total cost of employee Health Care Benefits?

Spectrum's W-2 Build can be set to net Add-on and Deduction codes. To do this, select both in the setup for Box 12. See [Payroll Year-end Processing](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/payroll-year-end-processing) for more information.

## I cannot locate the "Totals Only" option. Where can I find this report?

The Listing option on the W-2 Form Maintenance screen provides a 'Totals only' option.

## How do 401(k) and Cafeteria/Section 125 amounts show up on the W-2?

The 401(k) amounts deducted from employee earnings are shown in Box 12. "D" represents 401(k) amounts. You will also notice that the wages for Federal income tax are shown net of 401(k) deductions.
The rules for Cafeteria/Section 125 amounts vary depending on the type and amount of the deduction. Generally Section 125 amounts are not included in Federal wages. Some Section 125 benefits paid by employers must be reported on the W-2. See IRS publications covering Section 125 plans for more information and/or consult with a CPA on your specific company's obligation.
Wages subject to income tax at the state and local level may or may not be affected by Cafeteria/Section 125 or 401(k) amounts. Verify this with your CPA.

## How do I show 'pension/retirement' on the W-2?

On the W-2 form, an "X" may be needed in the Retirement plan box (contained in box 13 of the W-2) for some or all of your employees.
During the Build W-2 Forms, this can be set automatically, by selecting Yes – check retirement on all W-2s or K – check only for 401k participants from among the options for the Retirement plan. The field can also be edited manually, on an employee-by-employee basis, in the W-2 Form Maintenance screen.

## I want to manually add employees to the W-2 file so they will be included when I print and file W-2s in Spectrum. How do I do this?

The W-2 Form Maintenance screen is available for this purpose. See [Payroll Year-end Processing](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/payroll-year-end-processing).

## Our company works in multiple states. I see that the state wages total on the "totals" page of the W-2 Listing is larger than my total payroll. Is there something wrong?

It's not necessarily wrong. The total of all states' wages appear as one total. It is the sum of all of the state amounts. Review the recap cross tabs for individual state wage and tax totals below the summary total on the W-2 Listing.

## One of my employees changed their name during this last year. Should I set up a new employee code as part of year-end?

No. Spectrum populates the employee's names on the W-2 based on the field values in Employee Main Properties. No additional year-end-related changes are needed.
If you need to *change* an employee code (not only at year-end), see [Change Employee Codes](/en/spectrum/spectrum/accounting/payroll/utilities-overview/change-employee-codes).

## Our company's 401K plan includes an employer matching program. How can Spectrum be used to track this?

1. Go to Payroll > Maintenance > Deduction/Add-on Code and set up a new add-on code. Note: If you select the Percent of related code option as your calculation method, you will be able to attach the 401(k) deduction code that you want to base the calculation on the related code field.

1. On the Add-ons tab, select the Print on paycheck checkbox. Do not set up tax effects or vendors. Spectrum calculates the match based on the 401(k) amount deducted each pay cycle.

The Add-On History Report can be used to review these amounts at period end.

## I'm trying to reconcile my Payroll liabilities in General Ledger, but there are no January beginning balances. What's wrong?

If December 31st is your fiscal year-end and there are no January beginning balances, it means the G/L Opening Forward Balance Update has not yet been performed.
This important update sets the beginning balances and retained earnings for the new year, and should be performed each time you post additional amounts into the prior year.
If the Opening Forward Balance Update has been performed and and there are still no January beginning balances, verify the account type in the G/L master file for the Payroll Liabilities is set to Liability. If an incorrect account type is found, change the type to Liability, and then re-run the Opening Forward Balance Update to set the beginning balance.
Tip: The Equipment Control and Materials Management modules also have Opening Forward Balance Updates that should be run before year-end and re-run each time you post additional amounts into the prior year.

## Even though I have closed payroll and am now doing activity in the new year, I haven't closed other modules yet. Is that a problem?

For modules other than payroll, you can continue to record prior year transactions for as long as you need. It's common for A/P invoices and other transactions to show up for some time after the year has ended. As each module is closed, set the minimum processing date to fall in the new year and move on to the next module.
CAUTION: As for the Payroll module, once it has been closed at the end of the year, do not attempt to record more prior-year payroll activity. Doing so will corrupt the new year-to-date totals, and taxes will be incorrectly calculated. If prior year entries must to be made, we've included a special troubleshooting section in this guide that addresses this problem.

## Are there any year-end steps I should plan to do for other modules?

If the Human Resources module is installed, use the Time Off Management screen to revise vacation/holiday/sick account balances.
For information on year-end procedures in other modules, see [Non-Payroll Year-end Processing](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/non-payroll-year-end-processing).

## How do I increase the net distribution on cash earnings, such as a bonus, so that tax deductions will not be included in the distribution amount?

Gifts of cash, bonuses, and other cash equivalents can be considered wages for tax purposes, and the employer must withhold and remit all applicable taxes. On occasions when the employer wants to cover the employee share of payroll taxes, the taxes that normally would be an employee liability are treated as additional income to that employee because the employer is paying them.
Example:
You want to award a year-end bonus of $1000. You will pay the employee portion of Federal income tax (assume 14%), FICA (7.65%) and State income tax (8%). The wages you will need to record and report are calculated as follows:
Wage = $1,000/(1 - sum of applicable tax rates)
In this example it is $1,000/(1-(0.14 + 0.0765 + 0.08))=$1,421.46
The gross pay of $1,421.46 is then recorded in Payroll > Time Card Entry using one of the user-defined pay types of 1, 2, 3, or SA. Make certain that this pay type you have selected is set up with the correct tax effects in Tax Exclusion. Adjustments to the check can be made in Payroll > Check Adjustment Entry to generate the desired net amount.
