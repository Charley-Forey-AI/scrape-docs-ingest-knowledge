---
title: "Report Calculations - Deduction History Report, Exception | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/payroll-reports/deduction-history-report/report-calculations---deduction-history-report-exception"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/payroll-reports/deduction-history-report/report-calculations---deduction-history-report-exception"
---

# Report Calculations - Deduction History Report, Exception

The following table describes how each column is calculated on this report.
Column
Descriptions

Limit
This amount comes from the Employee Deduction/Add-onMaintenance screen, using the employee and deduction code selected for this report.

Amount Taken
This amount is the total deduction amount for the month for the employee and deduction code specified.

Scheduled Amount
For Fixed Amount deductions, this amount is equal to the Pay Periods Remaining multiplied by the Deduction amount.
For Regular Equivalent Hours, Overtime Equivalent Hours, and All hour deduction methods, this amount is equal to the Pay Periods Remaining times the Deduction amount times the Standard hours for the employee.
For Percent of Gross and Percent of Net deduction methods, this amount is equal to the Standard Hours multiplied by the Pay Rate, multiplied by the Pay Periods Remaining, multiplied by the Deductions Percent divided by 100.

Difference
This amount is equal to the Employee Monthly Limit less the Amount Taken, less the Scheduled Amount.
