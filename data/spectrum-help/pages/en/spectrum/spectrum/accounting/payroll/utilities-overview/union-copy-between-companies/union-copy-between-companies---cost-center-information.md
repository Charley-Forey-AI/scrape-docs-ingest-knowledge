---
title: "Union Copy Between Companies - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/union-copy-between-companies/union-copy-between-companies---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/union-copy-between-companies/union-copy-between-companies---cost-center-information"
---

# Union Copy Between Companies - Cost Center Information

If cost centers are being used in the destination company,
 then when performing the Union Copy Between Companies update, Spectrum copies the union only
 if you have permission to access the union's G/L accounts in that other company.
Spectrum compares each account's list of shared cost centers with cost
 centers in your operator's assigned cost center scheme in the destination company, and
 if there are no common cost centers, then the union is not copied. Spectrum will also
 verify that the operator has permission to access the union's deduction/add-on
 codes.
On the confirmation screen for the Union Copy Between Companies
 update, when cost centers are used in the destination company, Spectrum will allow entry
 of a G/L account code only if the operator entering the G/L account has permission to
 assign that code in the destination company and if not, then that G/L account cannot be
 assigned.
The Union Copy Between Companies Exception Report indicates cost
 center security errors when a requested union is not copied.
