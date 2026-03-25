---
title: "Prevailing Wage Calculations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations"
---

# Prevailing Wage Calculations

The following examples illustrate how the system calculates prevailing wages for each of the available calculation methods.
Calculation Method

Carry
Cash Fringe Calculation by Method

Standard (S)

Uses the Prevailing fringe benefit rate to determine the OT total prevailing wage rate.

Prevailing Basic Hourly Rate:
18.00
Employee Rate:
14.00
3.00
Standard Time (ST): ((18.00*1) + 3.00) - (14.00 + 5.00) = 2.00 Cash Fringe

Prevailing Fringe Benefit Rate:
3.00
Employee L-Fringe:
5.00

Overtime (OT): ((18.00 * 1.5) + 3.00) - ((14.00 * 1.5) + 5.00) = 4.00 Cash Fringe

Prevailing Total Wage Rate:
21.00
Employee Wage:
19.00

Cash Fringe Factored (F)

Both Prevailing basic hourly rate and cash fringe rate must be factored to determine the OT total prevailing wage rate.

Prevailing Basic Hourly Rate:
-----
Employee Rate:
14.00
5.00
ST: 21.00 - (14.00 + 5.00) = 2.00 Cash fringe

Prevailing Fringe Benefit Rate:
-----
Employee L-Fringe:
5.00

OT: (21.00) - (5.00) = 16.00 Prevailing Cash Earnings

Prevailing Total Wage Rate:
21.00
Employee Wage:
19.00

OT: ((16.00 * 1.5) + 5.00) - (( 14.00 * 1.5) + 5.00) = 3.00 Factored Cash Fringe

Generous Fringe Benefit Pkg #1 (G)

Uses employers Fringe Benefit Package (Pkg) Rate (both bona fide and cash) to determine the OT total prevailing wage rate. Cash Fringe is considered part of a "Generous Fringe Benefit Pkg" the moment the employer opts to pay an employee less than the Prevailing basic hourly rate.

Prevailing Basic Hourly Rate:
18.00
Employee Rate:
14.00
5.00 + 2.00
ST: ((18.00* 1) + 3.00) - (14.00 + 5.00) = 2.00 Cash Fringe

Prevailing Fringe Benefit Rate:
3.00
Employee L-Fringe:
5.00

OT ((18.00 * 1.5) + (5.00 + 2.00) - ((14.00 * 1.5) + 5.00) = 8.00 Cash Fringe

Prevailing Total Wage Rate:
21.00
Employee Wage:
19.00

Generous Fringe Benefit Pkg #2 (B)

Uses employers Fringe Benefit Package (bona fide ONLY) to determine the OT total prevailing wage rate. Cash Fringe is NOT considered part of the "Generous Fringe Benefit Pkg" under this option.

Prevailing Basic Hourly Rate:
18.00
Employee Rate:
14.00
5.00
ST: ((18.00* 1) + 3.00) - (14.00 + 5.00) = 2.00 Cash Fringe

Prevailing Fringe Benefit Rate:
3.00
Employee L-Fringe:
5.00

OT: ((18.00 * 1.5) + 5.00) - ((14.00 * 1.5) + 5.00) = 6.00 Cash Fringe

Prevailing Total Wage Rate:
21.00
Employee Wage:
19.00

Constant Fringe Benefit Rate (C)

Once the straight-time cash fringe rate is determined, the same ST cash fringe amount is used for the OT throughout. This is loosely based on the "Generous Fringe Benefit Pkg" option.

Prevailing Basic Hourly Rate:
18.00
Employee Rate:
19.00
2.00
ST: ((18.00 * 1) + 3.00) - (19.00 + 0.00) = 2.00 Cash Fringe

Prevailing Fringe Benefit Rate:
3.00
Employee L-Fringe:
0.00

OT: (0.00 + 2.00)

Prevailing Total Wage Rate:
21.00
Employee Wage:
19.00

Related information

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)
