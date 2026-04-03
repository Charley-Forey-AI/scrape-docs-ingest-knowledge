---
title: "Calculation Edit Reports - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/calculation-edit-reports/calculation-edit-reports---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/calculation-edit-reports/calculation-edit-reports---cost-center-information"
---

# Calculation Edit Reports - Cost Center Information

If cost centers are being used in this company, when running the Calculation Reports and a cost group or cost center is specified, then the reports will show only employees assigned to cost centers in that group (based on the cost center assigned in Employees, and provided your operator has permission to access that cost center).
When an employee is included on the reports, all information for that employee displays, even if you do not have permission to access certain time card lines for that employee.
Cost center entities
If cost center entities are enabled in Enterprise Installation, all earnings within the current pay cycle will be accrued for the entity assigned to the 'Check cost center', and will become part of the employee's year-to-date total earnings for that entity. The software identifies entity-specific year-to-date values in order to properly compute taxes, and if no entity is specified the main company entity will be used and the Check Calculation will only include history records that do not have an assigned entity.

- For deductions and add-ons, the software reads for recurring deductions and add-ons from Employee Entities to apply to checks in the pay cycle.

- For vacation, holiday and sick time, the software reads for accruals to apply to employees in the pay cycle.

When cost center entities are enabled in Enterprise Installation, the entity name will display on the report in place of the company name when an entity is stored for the check cost center of this pay cycle.
