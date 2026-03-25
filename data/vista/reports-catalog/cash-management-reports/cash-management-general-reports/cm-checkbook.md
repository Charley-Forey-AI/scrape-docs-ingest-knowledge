---
title: "CM Checkbook | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/cash-management-reports/cash-management-general-reports/cm-checkbook"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/cash-management-reports/cash-management-general-reports/cm-checkbook"
---

# CM Checkbook

You can use the CM Checkbook report to print all
 transaction details from the Beginning Date through the Ending Date by selecting
 Cash Management > Reports > CM Checkbook.
The report prints a Running Total of checkbook balances for the CM Bank
 Account specified. Daily Totals may be included if requested.
The beginning balance may either be calculated automatically or overridden with an amount entered at runtime. When calculating the Beginning Balance automatically, the report first finds the Statement Balance of the last statement prior to the Beginning Date. It then adds/subtracts to the Statement Balance the transaction amounts (deposit, checks, adjustments excluding voids) between the last statement date and the Beginning Date parameter. If calculating automatically, DO NOT enter an amount in the Beginning Balance input at runtime with the following exception. A Beginning Balance MUST be entered if no prior closed statements exist before the Beginning Date parameter.
Report Parameter
Description

Company
Accept the default, or press F4 to select a company.

CM Account (Required)
Select the Field Lookup button or press F4 to select Bank Account.

Statement Date
Select the Field Lookup button or press F4 to select Statement Date or manually enter Statement Date.

Beginning Date
Enter beginning date (MM/DD/YY) or leave blank to include all entries.

Ending Date
Enter ending date (MM/DD/YY) or leave blank to include all entries.

Automatically Calculate Beginning Balance?
checkbox to have system automatically calculate beginning balance. Leave unchecked to enter a beginning balance in next field.

If NOT Auto Calculating, Enter Beginning Balance Override
Leave blank if auto calculating beginning balance, otherwise, enter beginning balance override amount.

Daily Subtotals?
checkbox to give daily subtotals. Leave unchecked to exclude daily subtotals.
