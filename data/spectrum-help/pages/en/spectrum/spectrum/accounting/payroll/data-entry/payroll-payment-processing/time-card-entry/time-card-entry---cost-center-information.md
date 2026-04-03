---
title: "Time Card Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/time-card-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/time-card-entry---cost-center-information"
---

# Time Card Entry - Cost Center Information

If cost centers are being used in this company, then when
 entering a time cards for an employee, Spectrum will allow entry only if you have permission
 to access that employee.
As you request each employee, Spectrum compares the cost center assigned to the employee
 with cost centers in your operator's assigned cost center scheme, and if the cost center
 is not included, then time card entries for that employee will not be allowed.
Spectrum displays all time card lines for an employee that you are authorized to view. You will not be permitted to edit or delete any time card lines if the cost center assigned to the time card line is not permitted for the operator.
If your scheme includes override settings for employee entries in Cost Center Scheme Maintenance, this update will validate the cost center assigned to the employee based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
Spectrum also verifies that the employee's cost center is authorized for the current pay cycle. Spectrum compares the cost center assigned to the employee with cost centers designated during Set Payroll Cycle, and if the cost center is not included, then time card entry will not be allowed for the employee.
Cost center entities:
If cost center entities are being used, the transfer update excludes employees who are not authorized for the entity assigned to the check cost center of the current pay cycle. Likewise, for Layoff Checks and Replacement Checks, the entity code assigned to the checks must match the entity for the current pay cycle. For deductions and add-ons, validation assures that codes recorded in Time Card Entry are not transferred into a pay cycle where the codes are already set up as an entity-specific recurring deduction/add-on in [Employee Entities](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-entities).
