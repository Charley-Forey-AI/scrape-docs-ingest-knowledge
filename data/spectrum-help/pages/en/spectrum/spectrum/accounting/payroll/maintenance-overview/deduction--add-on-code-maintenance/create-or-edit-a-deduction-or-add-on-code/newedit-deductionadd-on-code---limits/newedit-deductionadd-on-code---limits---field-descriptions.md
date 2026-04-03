---
title: "New/Edit Deduction/Add-on Code - Limits - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---limits/newedit-deductionadd-on-code---limits---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---limits/newedit-deductionadd-on-code---limits---field-descriptions"
---

# New/Edit Deduction/Add-on Code - Limits - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
Apply limits to union?Select if you want the union amounts to be capped at the Pay cycle, Monthly, and/or Annual limit designated (below) for the particular code.During [Check Calculation](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation), as each successive union time card line is calculated, the software determines whether the amount taken for that line would exceed the specified limit. Once the employee reaches the limit for the particular code (across unions), Check Calculation stops calculating additional amounts for that code from the Union setup for the rest of the limit period. 'Monthly' and 'Annual' limits are controlled by Period End processing, and 'Pay cycle' limits start over with each new pay cycle.

Multi-cycle limit
Monthly limitEnter the default monthly limit, or press Enter to leave this field blank.The monthly deduction/add-on limit on the Deduction History Report and the Add-on History Report is determined by the Monthly Limit field on the Employee Deduction/Add-on Maintenance screen. If that field is blank, the monthly limit on the reports is determined by the Monthly limit field on the Deduction/Add-on Code Maintenance screen.

Annual limitEnter the default annual limit, or press Enter to leave this field blank.Note: If a shared limit is in use, this field is disabled and displays the limit which was set up in the [Shared Limit Setup](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/shared-limit-setup) window.

Per cycle limitSelect the deduction or add-on code's per pay cycle limit.This section is available only if the Fixed Amount, Percent of Gross Amount, or Percent of Related Code option is selected in the Calculation method field on the Properties tab.
Examples of using Percent limit when a Percent of Related Code option is selected as the Calculation Method, and there is a limit on the match itself.

- Employer matches 50% of the employees' 401(k) contribution, up to a maximum of 4% of wages. If employees contribute more than 4% of their wages, the match is capped. Determine Percent limit by multiplying the 4% by 50% (.04 * .5 = .02) to get a rate of 2%

1. Employee has a contribution rate of 50%, with gross pay of $400. Employee contributes $200. The match is $8. With no limit the match would be 50%, or $100. With the limit, the match is $400 x 4% x 50% (or $200 x 2%) = $8.

1. Employee has a contribution rate of 3%, with gross pay of $400. Employee contributes $12. The match is $6, because the employee is below the match level of 4%.

- Employer matches 25% of the employees' 401(k) contribution, up to a maximum of 10% of wages. If employees contribute more than 10% of their wages, the match is capped. Determine Percent limit by multiplying the 10% match by 25% (.1 * .25 = .025) to get a rate of 2.5%

1. Employee has a contribution rate of 50%, with gross pay of $400. Employee contributes $200. The match is $10. With no limit the match would be 25%, or $50. With the limit, the match is $400 x 10% x 25% (or $200 x 2.5%) = $10.

1. Employee has a contribution rate of 3%, with gross pay of $400. Employee contributes $12. The match is $3, because the employee is below the match level of 10%.

Percent/Per cycle limitThis set of limits shows up only when the Eligible for true up calculation option is selected in the [Set Payroll Cycle](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/set-payroll-cycle) screen.

- If the Percent of gross option is selected, enter the percent of gross limit for this deduction/add-on code.

- If the Fixed amount option is selected, enter the per pay cycle limit amount for this deduction/add-on code.

True up limitSelect the limit type.
