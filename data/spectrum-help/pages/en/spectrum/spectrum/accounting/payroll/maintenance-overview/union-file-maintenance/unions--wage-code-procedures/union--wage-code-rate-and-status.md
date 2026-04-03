---
title: "Union & Wage Code Rate and Status | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-code-rate-and-status"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/union-file-maintenance/unions--wage-code-procedures/union--wage-code-rate-and-status"
---

# Union & Wage Code Rate and Status

An effective date is assigned to a new rate in either the Payroll Union Rate or the Wage Code file.
How are the rate dates used?
Current Processing Date

- Maintenance screens

- Layoff Check Entry and Pre-Time Card Entry wage rates
Period End or Check Date (see Payroll Installation for default)

- Time Card Entry
Important: The pay rate will change to a new rate once the
 pre-time card is transferred to Time Card Entry if the wage rate change is later than
 either the Period End or Check Date (check Payroll installation). This does not apply
 to layoff checks.

## Statuses

Statuses are date-sensitive. Their purpose is to disable a deduction or add-on code, or to disable a fringe as of a certain date.
Example:
The Union fringe "Health & Welfare" was part of the union contract in 2012. However, it was not part of the contract in 2013. So a status entry is made effective 1/1/13 as Inactive. If the union contract includes the fringe in 2014, then a new status entry of Active is added as of 1/1/14. The result is three lines titled Health & Welfare – effective dates 1/1/12 and 1/1/14 are labeled Active, while the 1/1/13 is labeled Inactive.
What does this do? It allows you to reprint a union report for a prior year and produces valid numbers effective at that older date. If the report is run for any time in 2013, the Health & Welfare fringe will not produce a calculation, because it was Inactive at that time. If the report is run in 2012 or 2014, there will be a calculation for Health & Welfare.
Union deductions and add-ons can have both date-sensitive rate changes and statuses.
Example:
If the "Vacation" deduction was $1.00 in 2012, $0 in 2013 and $1.50 in 2014, you would have two different deduction rates with 1/1/12 and 1/1/14 dates, and a status "Inactive" record for 2013.
