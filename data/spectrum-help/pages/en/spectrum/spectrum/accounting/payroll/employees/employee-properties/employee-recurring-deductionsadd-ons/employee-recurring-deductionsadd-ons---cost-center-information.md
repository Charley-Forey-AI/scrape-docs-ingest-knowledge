---
title: "Employee Recurring Deductions/Add-ons - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-recurring-deductionsadd-ons/employee-recurring-deductionsadd-ons---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-recurring-deductionsadd-ons/employee-recurring-deductionsadd-ons---cost-center-information"
---

# Employee Recurring Deductions/Add-ons - Cost Center
 Information

If the Enterprise Installation option to use cost centers
 is set to Yes or Pending for this company, then when entering
 an employee, Spectrum will allow maintenance only if you have permission to access that
 employee.
As you request each employee, Spectrum compares the cost center assigned to the employee
 with cost centers in your operator's assigned cost center scheme, and if the cost center
 is not included, then entries for that employee will not be allowed.
When adding, editing, or deleting a deduction or add-on code,
 Spectrum also verifies that the employee has permission for the deduction/add-on code. A
 warning displays if there are deduction or add-on codes listed for the employee that the
 employee does not have permission to access. Spectrum compares each deduction's list of
 shared cost centers with the cost center assigned to the employee, and if the cost
 center is not present, then that code is identified in the warning box. For example,
 this condition might occur if the deduction was set up for the employee, and then later,
 the employee's cost center was changed to another code that was not used with the
 deduction. This could also occur if the deduction code was assigned to the employee and
 then later, that code's cost center assignment was revised.
All deduction and add-on codes currently assigned to the employee
 display, regardless of operator cost center security.
Employee deductions and add-ons that are not in the time card file
 will be assigned the employee's cost center (rather than the pay cycle cost center).
 Likewise, employer taxes (FICA, union fringe, FUTA, etc.) are assigned the employee's
 cost center.
The pay cycle cost center is used for posting to the cash G/L account
 and is saved in the check history file for use on void checks. Regardless of where the
 check is voided (Layoff Check Entry, Pre-Time Card Entry, or Time Card Entry), the Check
 Calculation step will use the original bank account on the void check.
