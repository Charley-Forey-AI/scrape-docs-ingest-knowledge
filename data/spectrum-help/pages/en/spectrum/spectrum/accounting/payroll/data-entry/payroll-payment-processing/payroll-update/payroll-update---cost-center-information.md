---
title: "Payroll Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/payroll-update/payroll-update---cost-center-information"
---

# Payroll Update - Cost Center Information

If cost centers are being used in this company, Spectrum
 verifies that your operator has authorization for all cost centers included in the current
 payroll cycle.
Spectrum compares the cost centers designated by the cost group set for the cycle with cost
 centers in your operator's assigned cost center scheme, and if any cost center is not
 included, then the update will not be performed and an error message displays.
The 'Check cost center' applied to the pay cycle overrides the employee's home cost center during this update. If the Operator's scheme includes override settings for employee entries in Cost Center Scheme Maintenance, Spectrum will validate the cost centers designated by the cost group set for the cycle based on these overrides. The override cost center(s) supercede the cost center list defined for the scheme in general. Note that your inter-post accounts will appear as out-of-balance on the G/L Error Correction Change Log for the specified cost center.
For multi-company users, Spectrum will assign the inter-company G/L account code for the balancing entry (in both companies) when the update is run. Specifically, the software will read the company code of the time card line and then determine if that company code has been assigned a particular inter-company G/L account. For entries in the payroll company, the Payroll Installation setup is used and for the entries of the company referenced in the time card line, the Payroll Installation setup of that other company is used. Inter-post entries are not applicable for these transaction lines.
This list shows how different G/L accounts will be posted when the Payroll Update is run.
