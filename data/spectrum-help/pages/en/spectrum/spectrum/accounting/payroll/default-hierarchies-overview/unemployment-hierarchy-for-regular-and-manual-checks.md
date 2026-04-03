---
title: "Unemployment Hierarchy for Regular and Manual Checks | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/unemployment-hierarchy-for-regular-and-manual-checks"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/unemployment-hierarchy-for-regular-and-manual-checks"
---

# Unemployment Hierarchy for Regular and Manual Checks

The Payroll > Check Calculation determines whether the employee has been assigned a permanent unemployment
 state, and if so, computes unemployment for that state instead of resident state and work
 state unemployment for Regular and Manual checks using the following hierarchy.

- The system first looks for a permanent unemployment state:

- Is there a permanent unemployment state designated in Employee Tax Setup?

-  If found, use the Unemployment Tax Code specified\ for the particular employee to compute unemployment 'subject to tax' and the 'tax amount' values.

- When computing 'subject to tax', any unemployment 'Tax Exclusions' are applied
 based on pay type (designated for the Permanent Unemployment State
 in Tax Table Maintenance).

- When computing 'subject to tax', any unemployment 'Tax Effects' for Add-ons
 are applied (designated for the Permanent Unemployment State in
 Deduction/Add-on Code Maintenance).

- Even if the particular Permanent Unemployment State is invalid or has no unemployment setup, that tax code is used for unemployment.

- Even if there are 'Resident Exemptions' set to 'Exempt' for the Resident or Permanent Unemployment State in Tax Table Maintenance, the 'subject to tax' and 'tax amount' for the specified Permanent Unemployment State is computed.

-  Even if the employee is set to 'Exempt' for Resident and/or Work state unemployment in Employees, the 'subject to tax' and 'tax amount' for the specified Permanent Unemployment State is computed.

- Even if the particular Permanent Unemployment State is the same tax code as the employee's resident or work state, the Permanent Unemployment State described above is used for unemployment.

- Secondarily, the system determines the unemployment 'subject to tax' and the 'tax amount' values from resident and work state tax table setup (PR_INCOME_TAX_TABLE_MC), including all add-on tax effects and exclusions.
