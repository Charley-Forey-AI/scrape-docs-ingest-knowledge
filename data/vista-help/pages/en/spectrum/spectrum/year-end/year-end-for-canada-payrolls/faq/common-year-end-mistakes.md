---
title: "Common Year-end Mistakes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/faq/common-year-end-mistakes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/faq/common-year-end-mistakes"
---

# Common Year-end Mistakes

Solutions to common year-end mistakes.

## I did not perform the Year End Update before my first payroll in January. What should I do now?

By not clearing the payroll at year-end, certain taxes that contain annual limits did not calculate correctly for most employees.
The payroll cycle must be voided and re-issued to correct this problem. Use the same cheque date when recording the void cycle, and if multiple cycles must be voided, do each one separately, newest to oldest (01/12 then 01/05, for example).
After the void process has been completed, perform the Year End Update to set all employees' year-to-date amounts to zero. You should also review the Year-End Checklist to be sure no other year-end steps were overlooked.
Finally, re-enter the payroll cycle(s), as regular or manual cheques. Regardless of whether the miscalculated cheques have been issued to employees, the system will require that new cheque numbers be assigned during this cycle. If cheques were already distributed, be sure to record the same deductions and net pay as the original cheques issued.

## In reviewing the T4 year-end figures, some employees did not show up in the file to receive a T4 Slip at all. What's wrong?

Employees with a status of "exempt" do not receive a T4 Slip. If an employee's status was set to "exempt" in error, manually add the individual to the T4 Slip Maintenance screen.

## I did not change the tax tables for the new year, but I have already processed payroll in the new year. What should I do now?

In nearly all cases, you don't need to do anything.
Any income tax surplus or deficit is resolved on an annual basis when employees file their taxes; based on any number of circumstances, even the correct tax tables cannot prevent this entirely. Small variations in withholding for one or two weeks is not a significant issue.
For instances where the amount for withholding must be a specific amount, take these steps to ensure that the quarterly and year-end reports remain accurate:

1. void the cheques

1. apply the most up-to-date tax tables

1. re-issue the cheques

## An employee loan paid off last year has started showing up on the employee's cheque again. It was a recurring deduction that reached the limit months ago. What's wrong?

It could be that the Clear employee balance at year end checkbox on the deduction code was selected, which cleared the accumulated balance at year-end. Because the accumulated balance has been erased, the deduction was taken again.
If this deduction is no longer needed for this employee, delete it from the Employee Deduction/Add-on Maintenance screen. If the January payroll in which the amount was deducted on the employee cheque has been updated, refund the amount using the same code.

## Why am I receiving an error message stating: "ERROR- Year End Update must be performed before beginning a pay cycle dated later than <the current year>?"

The Payroll > Data Entry > Payment Processing > Set New Cycle screen prohibits users from assigning a cheque date at the beginning of a new calendar year until after the Year End Update has been performed in order to prevent incorrect tax calculations. If you received the error message above, you still need to perform the Year End Update before you can continue to process payroll.

## I need to void a payroll cheque issued last year. What should I do now?

If you are replacing a cheque the employee lost, go to the Payroll > Data Entry > Replacement Cheque screen. It is important to use a current date as the replacement cheque date. This way, both the void and replacement cheque will post to the current year, thereby creating a net effect of zero in the employee history file for the current year.
If you are voiding a cheque and not replacing it, or voiding and reissuing with a different amount, it is vital to follow the instructions below to ensure that the T4 issued and current year payroll records are accurate.
Once the payroll year-end has been completed, all transactions recorded during the payroll cycle (payroll cheque, bonus cheque, etc.) must be for the new year. This is because many of the payroll calculations depend upon year-to-date information. If additional prior-year entries are made, the accumulated totals since the Year End Update will be inaccurate. This means that any additional payroll transactions for the prior year cannot be recorded in Spectrum as part of a payroll cycle.
To correct the prior year error, transactions entered in the following areas may be required:

- T4 Slip Maintenance to correct the employee's T4 information.

- General Ledger Journal Entry to correct liability and expense accounts. If subsidiary ledgers (Job Cost or Equipment Control) are affected, this can be recorded as part of the journal entry.

- Make manual notations (in ink) of changes on affected tax reports, such as Subject-to-Tax Report and the Employment Tax Report.

An alternative to the above is to reverse all new transactions, and return the Payroll module to the prior year, but Viewpoint does not recommend this option because it is riskier for a number of reasons.

- It is possible that prior-year information has already been purged during the course of normal year-end processing.

- If any payroll cycles have already been updated, you will need to void all cheques issued in the new year, using care to to void each cheque as of the same date it was issued.

- You will need to print and retain paper copies (plain paper is fine) of the T4 Listing.

## I printed my Unemployment Tax Report and the excess calculation is wrong. What should I do now?

This report provides information on excess calculations computed during each payroll cycle during the specified date range. Therefore, this report may not be correct if limits were adjusted or 'tax effects' of deductions changed during the year.
If such changes were made, there is a useful Excess Unemployment Report available for use in auditing this problem by recalculating excess amounts based on current settings. This is included as a second format when printing the Unemployment Tax Report.

## I can't find my T4 file. Where has it been created?

Different web browsers may download files from your Spectrum application in different ways. Browsers are routinely updated and you may need to refer to your browser's Help files for the latest information.
