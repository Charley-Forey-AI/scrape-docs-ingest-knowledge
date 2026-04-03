---
title: "Check Calculation - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation/check-calculation---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/check-calculation/check-calculation---cost-center-information"
---

# Check Calculation - Cost Center Information

If cost centers are being used and entity tracking is
 enabled in Enterprise Installation, the Check Calculation will compute entity-specific
 earnings and taxes, based on year-to-date activity for the particular entity.
Limits (such as for Social Security) will be based on year-to-date activity solely for
 the specified entity. For recurring deductions and add-ons, and for vacation, holiday
 and sick accruals, the software will look for entity-specific setup.
For [New/Edit Deduction/Add-on Code - Limits](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---limits), the software will read the employee's entity-specific month-to-date and year-to-date amounts taken if the current pay cycle is for a non-blank entity code.
The entity code to be used during Check Calculation is determined by reading the 'Check cost center' assigned during Set Payroll Cycle.
