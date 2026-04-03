---
title: "Closing the Payroll Year | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/faq/closing-the-payroll-year"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/faq/closing-the-payroll-year"
---

# Closing the Payroll Year

Answers to some of the most common questions related to closing the payroll year.

## When should I close payroll for the tax year that's ending?

Plan to perform the year-end tasks any time after you complete your last payroll cheque dated in the ending year and before you issue any cheques dated in the new year. The Spectrum application does not require you to do these steps on December 31st.

## What does the Year End Update function do? What effect does it have on my permanent payroll records in Spectrum?

The Year End Update resets all employees' year-to-date balances to zero. It does not remove any historical employee data.
If the Deduction/Add-on Code flag is set to clear at year-end, the Year End Update also sets the accumulated balance in the recurring deduction file to zero.

## I want to delete (purge) records of terminated employees. How do I do this?

Employee records may be purged by using the Delete Employee from Current Company screen in Payroll > Utilities.

## My fiscal year is different than the calendar year. Is there anything special I should know?

Because payroll is based on the calendar year, you will need to perform the Year End Update in the Payroll module at the end of each calendar year, even if you maintain the rest of Spectrum on a fiscal year basis.
Run the Payroll Year End Update *only* at the end of each calendar year, and not timed with the end of your fiscal year.

## My fiscal year-end is December 31st. Is there anything special I should know?

Your Spectrum application provides an unlimited Fiscal Calendar in the General Ledger module. To add new years or historical years to this calendar, see the General Ledger Help.

## One of my employees changed their name during this last year. Should I set up a new employee code as part of year-end?

No. Spectrum populates employees' names on T4 Slips based on the field values in Employee Main Properties. No additional year-end-related changes are needed.
If you need to *change* an employee code (not only at year-end), see [Change Employee Codes](/en/spectrum/spectrum/accounting/payroll/utilities-overview/change-employee-codes).

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
For information on year-end procedures in other modules, see [Non-Payroll Year-end Processing (Canada)](/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/non-payroll-year-end-processing-canada).

## What are the important dates I need to know for filing?

Refer to the [CRA website](http://www.cra-arc.gc.ca/menu-eng.html) for filing deadlines for paper and electronic filing.
