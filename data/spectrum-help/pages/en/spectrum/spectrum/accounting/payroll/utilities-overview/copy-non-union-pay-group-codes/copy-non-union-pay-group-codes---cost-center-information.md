---
title: "Copy Non-Union Pay Group Codes - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-non-union-pay-group-codes/copy-non-union-pay-group-codes---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-non-union-pay-group-codes/copy-non-union-pay-group-codes---cost-center-information"
---

# Copy Non-Union Pay Group Codes - Cost Center Information

If cost centers are being used in this company, then when
 performing the Non- Union Pay Group File Copy update, Spectrum will copy the pay group, but
 will omit unauthorized employees recorded in the source pay group.
Spectrum will copy the employee detail only if you have permission to access the
 employee. Spectrum compares the cost center assigned to the employee with cost centers
 in your operator's assigned cost center scheme, and if the cost center is not included,
 then the employee detail is not copied.
Spectrum also verifies that you have permission to access the pay group's deduction/add-on codes. Spectrum compares each deduction's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then the non-union pay group is not copied.
