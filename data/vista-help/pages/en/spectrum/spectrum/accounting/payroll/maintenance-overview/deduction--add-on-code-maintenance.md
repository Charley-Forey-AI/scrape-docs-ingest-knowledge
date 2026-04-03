---
title: "Deduction / Add-on Code Maintenance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance"
---

# Deduction / Add-on Code Maintenance

 Use this screen to set up and maintain deduction and add-on codes for use by employees.
A unique code is assigned to each deduction or add-on, which can be applied by employees in Employee Deduction / Add-on. The software recognizes the code and automatically calculates deductions and add-ons based on the details entered here. Individual monthly limits can be set in Employee Recurring Deductions/Add-ons after the code has been set up in this screen.
You can also use this screen to set up matching 401(k) non-cash add-on codes in order to calculate adjusted gross pay amounts for specific add-ons and deductions. This makes it easier to calculate 401(k) matching amounts based on the gross pay amount without worrying about how allowances, fringe benefits, or deductions might affect the gross pay.

- Add-on and deduction amounts for Federal jobs (which fall under Davis-Bacon laws); state, county, and local jobs (which fall under prevailing wage laws) and private work (including non-job activities) are stored for each code; in turn, this information yields the total employer contribution for each code. Protection is included so that if you accidentally set up a circular calculation (for example, one in which an add-on relies on another add-on to perform the adjusted gross calculation), the software ignores the adjustment, completes the calculation, and produces a Calculation Error Report during payroll calculation or layoff check calculation. You can then fix the error or proceed with what has been calculated.

- During payroll check calculation, the recurring deduction and add-on codes are sorted so that any codes which are dependent on other codes (for example, gross pay adjustments) are calculated after the dependent codes. Furthermore, if a deduction amount is changed in the Check Adjustment Entry screen, the software recalculates the deductions that are dependent on the (changed) code and displays the old and new amounts before prompting you to confirm the changes.

- The software prevents deletion of a deduction code if that code is still referenced in Union File Maintenance.

- If the payroll cycle is currently in progress, a warning message displays in the header and this screen is view only. If checks have already been calculated, no changes can be made until the cycle is complete.

- For more information about the Prevailing Wage Adjustment and Health & Welfare calculation methods, see [Prevailing Wage and Davis-Bacon Processing](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/summary-of-prevailing-wage-benefits/prevailing-wage-and-davis-bacon-processing).

## Buttons on this screen

ButtonResultRelated Help
NewNew Deduction/Add-on Code window[Create or Edit a Deduction or Add-on Code](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code)
SetupDeduction/Add-on Cost Code Center Setup screen[Deduction / Add-on Code Maintenance - Cost Center Information](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/deduction--add-on-code-maintenance---cost-center-information)
ListingDeduction/Add-on Code Listing screen[Deduction / Add-on Code Listing](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/deduction--add-on-code-listing)
Shared LimitsShared Limit Setup window[Shared Limit Setup](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/shared-limit-setup)
When the grid is displaying on-screen
EditEdit Deduction/Add-on Code window[Create or Edit a Deduction or Add-on Code](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code)
DeleteConfirmation or error messageNote:Spectrum prevents a code used in Union File Maintenance from being deleted from the system.
n/a

Related information

- [New/Edit Deduction/Add-on Code - Properties](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties)

- [New/Edit Deduction/Add-on Code - Tax Effects](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---tax-effects)

- [New/Edit Deduction/Add-on Code - Add-ons](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---add-ons)

- [New/Edit Deduction/Add-on Code - Limits](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---limits)

- [New/Edit Deduction/Add-on Code - A/P Invoice](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---ap-invoice)

- [Deduction Code Routing Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/deduction-code-routing-hierarchy)

- [Union & Wage Code Rate and Status](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-code-rate-and-status)

- [Calculation Method Detail](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/calculation-method-detail)

- [Create or Edit a Deduction or Add-on Code](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code)

- [Report Employee Health Care Benefits](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/report-employee-health-care-benefits)

- [Canadian Vacation Pay](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay)
