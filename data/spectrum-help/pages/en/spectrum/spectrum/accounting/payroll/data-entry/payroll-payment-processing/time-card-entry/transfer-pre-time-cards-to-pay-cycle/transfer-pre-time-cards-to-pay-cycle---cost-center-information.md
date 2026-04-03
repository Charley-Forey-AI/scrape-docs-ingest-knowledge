---
title: "Transfer Pre-Time Cards to Pay Cycle - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/transfer-pre-time-cards-to-pay-cycle/transfer-pre-time-cards-to-pay-cycle---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/transfer-pre-time-cards-to-pay-cycle/transfer-pre-time-cards-to-pay-cycle---cost-center-information"
---

# Transfer Pre-Time Cards to Pay Cycle - Cost Center Information

If cost centers are being used in this company and a cost
 group or cost center is specified, then the update includes only employees assigned to cost
 centers in that group (based on the cost center assigned in Employees).
If you specify a cost center on the update starting screen, Spectrum verifies that your
 operator has permission to access that cost center before proceeding.
During the Pre-Time Card Update to Time Card, Spectrum will transfer time
 cards from Pre-Time Card Entry only if the employee's cost center is valid for the
 current pay cycle, and only if you have permission to access the employee. If not, or if
 the employee does not have an assigned cost center, then pre-time cards will not be
 transferred for the employee.
If your operator's scheme includes override settings for employee entries in Cost Center Scheme Maintenance, this update will validate the cost center assigned to the employee based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
Note: Any manual checks (and associated cost center and bank
 account information) will be transferred, even if your operator does not have security
 to the check cost center. Cost center entities:
If cost center entities are being used, the transfer update excludes employees who are not authorized for the entity assigned to the check cost center of the current pay cycle. Likewise, for Layoff Checks and Replacement Checks, the entity code assigned to the checks must match the entity for the current pay cycle. For deductions and add-ons, validation assures that codes recorded in Pre-Time Card Entry are not transferred into a pay cycle where the codes are already set up as an entity-specific recurring deduction/add-on in [Employee Entities](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-entities).
