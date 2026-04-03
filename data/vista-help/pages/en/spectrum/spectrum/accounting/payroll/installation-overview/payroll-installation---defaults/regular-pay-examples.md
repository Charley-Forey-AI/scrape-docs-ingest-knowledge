---
title: "Regular Pay Examples | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/regular-pay-examples"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/regular-pay-examples"
---

# Regular Pay Examples

Use the regular pay examples for employee pay
 rates.
Prevailing wage=$18, Cash fringe=$5, Health & welfare=$2
Employee A is typically paid $10/hour
Employee B is typically paid $20/hour
Employee C is typically paid $30/hour
'Default employee pay rate (Y, N, H)?' is set to N:
Employee A will be paid $18/hour + $3 CF [$5 - $2]
Employee B will be paid $18/hour + $3 CF [same]
Employee C will be paid $18/hour + $3 CF [same]
'Default employee pay rate (Y, N, H)?' is set to H and new box is cleared:
Employee A will be paid $18/hour + $3 CF [same]
Employee B will be paid $20/hour + $3 CF [same]
Employee C will be paid $30/hour + $3 CF [same]
'Default employee pay rate (Y, N, H)?' is set to H and the Track prevailing wage benefits checkbox is selected:
Employee A will be paid $18/hour + $3 CF [same calculation as above since employee rate is not higher]
Employee B will be paid $20/hour + $1 CF [$5 - $2 – ($20 - $18)]
Employee C will be paid $30/hour + no CF [zero since $5 - $2 – ($30 - $18) is negative]
