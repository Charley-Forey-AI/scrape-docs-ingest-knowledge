---
title: "Vac/Hol/Sick G/L Accrual Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update/vacholsick-gl-accrual-update---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/human-resource-module/spectrum-menus/data-entry-overview/vacholsick-gl-accrual-update/vacholsick-gl-accrual-update---cost-center-information"
---

# Vac/Hol/Sick G/L Accrual Update - Cost Center Information

If the cost center feature is enabled in the
 Enterprise Installation screen, the employee list displays only
 employees associated with cost centers that your operator is authorized to access. The update
 will apply the override G/L accounts specified in Payroll > Department Expense Maintenance, based on cost center.
Validation for cost centers applicable to each department are stored in the Payroll > Department Expense Maintenance screen. Spectrum verifies that the employee's cost center is valid for
 that department. If the employee's cost center is not included in the list of valid cost
 centers on the Cost Center tab of the Edit
 Department window (in Payroll > Department Expense Maintenance), then that employee will be shown on the Exception Listing and accruals
 will not be computed.
When this report is compiled, the G/L accounts are assigned from the Payroll > Department Expense Maintenance screen based on the employee's home department. The Edit Department – Overrides tab, which is accessible in this screen, provides the option to specify
 alternate G/L accounts by cost center. Spectrum will apply these override accrual G/L
 accounts, if specified, when the Vac/Hol/Sick G/L Accrual Report is compiled. If the
 override G/L account is non-valid, the error will appear on the Exception Listing. If no
 override G/L account is specified, then the accrual G/L account from the
 Vac/Hol/Sick Accrual tab will be applied.
All General Ledger activity for authorized employees will appear on the report. The Vac/Hol/Sick G/L Accrual Report shows the cost center associated with each transaction line on the report.
When the G/L Error Correction window appears due to an
 invalid or inactive G/L account code, Spectrum will allow entry of a replacement G/L
 account code only if you have permission to assign that code. Spectrum compares the G/L
 account's list of shared cost centers with cost centers in your assigned scheme, and if
 there are no common cost centers, then that G/L account cannot be assigned. The screen
 will display the cost center, and verify that the new G/L account entered is valid for
 that cost center. Note also that if overrides are used, your interpost accounts will
 appear out-of-balance for the specified cost center.
During the update, Spectrum stores the cost center associated with each accrual transaction in the Vac/Hol/Sick accrual history file.
