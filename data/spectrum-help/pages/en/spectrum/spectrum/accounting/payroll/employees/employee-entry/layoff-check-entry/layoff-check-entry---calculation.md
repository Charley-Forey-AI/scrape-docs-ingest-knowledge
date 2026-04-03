---
title: "Layoff Check Entry - Calculation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/layoff-check-entry/layoff-check-entry---calculation"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/layoff-check-entry/layoff-check-entry---calculation"
---

# Layoff Check Entry - Calculation

Layoff Check calculation also computes the worker's
 compensation rate per $100 amounts up to the limit (if any) specified in the Tax Table Maintenance >  Unemployment / FICA / SDI window.
For Pay per
 cycle limits, the computation applies the tax rate for an employee up to the
 specified limit. For Annual
 limits, the computation applies the tax rate on a year-to-date basis for an employee up to
 the specified limit. The 'subject to' earnings, used to calculate worker's compensation,
 will be the extension of the time card line (unless it is an exempt pay type), adjusted for
 straight-time equivalent, if applicable for the code, then subject to the limit, if any.
 Subject-to earnings for add-ons in the time card file will be computed if the state
 specified on the time card line is set up to Y (taxable) in the Tax Effects window of [Deduction / Add-on Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance). Layoff Check Entry will also calculate union add-ons and deduction limits based on
 setup in the [New/Edit Deduction/Add-on Code - Limits](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---limits) tab.
If the wage code has been assigned a benefit tier, the application uses the override settings to apply a tier-specific rate. If there is no override
 setting assigned to that benefit tier, the standard union rate will be applied instead. If
 the union add-on has been assigned the non-standard fringe calculation method, the standard
 pay rate will include the non-stated fringe and the employee rate will be adjusted
 automatically. The portion of the Layoff Check calculation that generates entries to
 allocate recurring add-on amounts by time card will conditionally assign the "Burden" phase
 and/or cost type from Job Payroll Setup for the Job code specified on the time card. If a
 "Burden" cost type is defined for the job, then this screen will assign that cost type.
 Otherwise, if the field is <blank> in Job Payroll Setup, the cost type from the time
 card line will be used. If the recurring add-on has been assigned the non-standard fringe
 calculation method, the add-on amount will be skipped.
If the graduated table option on the Tax Adjustment Code Maintenance screen is not selected for the tax adjustment, the lookup amount is based on the highest tax bracket that applies multiplied by gross earnings or income tax. The result will then be added to the 'Fixed amount' on the row.
If the Set to zero anniversary? checkbox was selected on the [Time Off Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/time-off-code-maintenance) screen, the vacation, holiday and sick balances will be calculated for the current year only based on the employee's anniversary date.
If the Extra pay period this year checkbox is selected in [New/Edit Tax Table - Income Tax tab](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---income-tax-tab), layoff check calculations will be adjusted to include an extra pay period for the current year to annualize wages for weekly and bi-weekly employees when calculating all taxes (federal, state, county, local).
If related tax codes have been set up for the employee code, the Layoff Check will
 calculate tax for each of the time card records.
Note: During Layoff Check Calculation, the application performs a
 number of validation checks and issues exception reports when errors are found. If the
 employee's federal tax status is set to 'Exempt' and the 'Foreign employee' checkbox is
 not selected, the Layoff Check Calculation Error Report will generate an error message. The
 Operator will need to either change the employee's federal tax status or select the
 Foreign employee checkbox
 before the update is re-run.
