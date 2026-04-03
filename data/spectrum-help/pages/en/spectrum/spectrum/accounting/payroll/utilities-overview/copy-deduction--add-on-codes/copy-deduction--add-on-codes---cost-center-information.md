---
title: "Copy Deduction & Add-on Codes - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-deduction--add-on-codes/copy-deduction--add-on-codes---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-deduction--add-on-codes/copy-deduction--add-on-codes---cost-center-information"
---

# Copy Deduction & Add-on Codes - Cost Center Information

If the Enterprise Installation option for cost centers is set
 to Yes in the destination company,
 then when performing the Copy Deduction & Add-on Codes update, Spectrum will copy the
 deduction/add-on only if you have permission to access the deduction/add-on code's G/L
 accounts in that other company.
Spectrum compares each account's list of shared cost centers with cost
 centers in your operator's assigned cost center scheme in the destination company, and
 if there are no common cost centers, then the deduction/add-on is not copied. Spectrum
 will also verify that the operator has permission to access the deduction/add-on codes
 and if not, then the deduction/add-on code is not copied.
If cost centers are set to Yes in the destination company, then
 any cost centers listed for the deduction/add-on that are valid in the destination
 company will be copied for that code.
