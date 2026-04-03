---
title: "Merge Add-on / Deduction Codes - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/merge-add-on--deduction-codes/merge-add-on--deduction-codes---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/merge-add-on--deduction-codes/merge-add-on--deduction-codes---cost-center-information"
---

# Merge Add-on / Deduction Codes - Cost Center Information

If cost centers are being used in this company, then when
 entering a deduction or add-on code in the Merge Add-on/Deduction Codes screen, Spectrum
 verifies that the operator has permission to access the deduction/add-on code.
Spectrum compares the deduction's list of shared cost centers with cost centers in your
 operator's assigned cost center scheme, and if there are no common cost centers, then
 entry of that deduction/add-on code is disallowed.
When the Merge Add-on/Deduction Code Listing/Update is performed, you must have security authorization for all affected employees in order to perform the update. Spectrum compares the cost center assigned to each employee assigned an 'old code' with cost centers in your operator's assigned cost center scheme, and if any cost center is not included, then the update will be disallowed. Cost Center validation will only occur on files PR.EHVD (deductions posted to previous checks for that employee) and PR.EMPVD (recurring deductions for that employee). Spectrum does not verify that the operator has permission for the individual deduction and add-on codes assigned to the operator.
