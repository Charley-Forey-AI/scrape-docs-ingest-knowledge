---
title: "New/Edit Deduction/Add-on Code - Tax Effects | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---tax-effects"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---tax-effects"
---

# New/Edit Deduction/Add-on Code - Tax Effects

Use the settings on this tab to override the default calculation method and reduce the subject-to wages.
By default, Spectrum calculates taxes on the gross wages.
When any checkbox on this tab is selected, Spectrum calculates on the subject-to wages rather than on the gross wages.
When you save the add-on, the software will save all 'Tax effects' even if the Paid to employee on the paycheck checkbox is not selected on the Add-ons tab (in other words, even tax effects NOT PAID to the employee on the pay check will be saved and may result in tax deductions that will impact the employee's net check amount).

- For deductions, if the checkboxes are selected, these selections are NOT taxed.

- For add-ons, if the checkboxes are selected, these selections ARE taxed.

Example:
Gross wages = $1000
401(k) deduction = 100
Subject-to amount = $900
On the Tax Effects tab, if you select any of the checkboxes, Spectrum calculates on the subject-to wages of $900 rather than the gross wages of $1000. For the purposes of a 401(k), select only the Income tax checkbox and clear the Employee, Employer, Unemployment, and Worker's comp checkboxes. This means for federal withholdings, Spectrum will calculate taxes based on $900; all other (non-Federal) taxes will be taxed based on the $1000 amount.
Note: The Payroll Check Calculation will NOT create subject-to earnings and taxes for a deduction with tax effects for all taxes in a state that is tax exempt but has a deduction code that reduces gross wages for that state.
