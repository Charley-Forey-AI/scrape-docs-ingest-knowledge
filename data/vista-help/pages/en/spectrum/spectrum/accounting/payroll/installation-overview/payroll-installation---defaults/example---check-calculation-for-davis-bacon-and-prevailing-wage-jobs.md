---
title: "Example - Check Calculation for Davis-Bacon and Prevailing Wage Jobs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/example---check-calculation-for-davis-bacon-and-prevailing-wage-jobs"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/example---check-calculation-for-davis-bacon-and-prevailing-wage-jobs"
---

# Example - Check Calculation for Davis-Bacon and Prevailing Wage Jobs

A company with a 401(k) program continues to contribute to
 the 401(k) program for their state prevailing wage jobs and their Federal Davis-Bacon jobs.
The prevailing wages are $20 base rate and a $5 fringe rate. The employer benefit is $2 per
 hour for medical, dental, and other benefits (stored in the employee file).

- Select the Calculate actual benefits for the D-B/Prevailing wage employer benefit credit checkbox in the Payroll Installation- Defaults screen.

- In the Deduction / Add-on Code
 Maintenance screen, set up the 401(k) non-cash add-on (for example,
 2K), select to include pay and hours for all three job types (Davis-Bacon, prevailing
 wage, and other), and select the checkbox to compute this add-on as part of the
 D-B/Prevailing wage employer benefit (located in the Add-on tab).
Note: If your 2K code (employer match) is a function of the
 employee contribution (that is, if the calculation type is 'Percent of related
 code'), then the employee contribution MUST also be subject to Davis-Bacon,
 prevailing wage, and private jobs.

- In the Non-Union Pay Group File Maintenance  >  Prevailing Wage window, the setup would be as follows for both prevailing wage and Davis-Bacon Jobs:
Health & Welfare: H1 Health & Welfare method: Health & Welfare
Pension: none
Cash fringe benefit:
 CF Cash Fringe Pay method: Prevailing Wage AdjustmentNote: Make
 sure the two "Disable…" checkboxes are clear.

- Attach the add-on (2K) to the employee in Employee Deduction/Add-on Maintenance.

- Complete the employee time card: 10 hours on private job, base pay $15.00/hr 20 hours on prevailing wage job, base pay $20.00/hr 10 hours on Davis-Bacon job, base pay $20.00/hr

- The total 401(k) benefits calculated for this check ($750 gross, simple 10%) = $75.00. The prevailing wage 401(k) portion is $400 gross x 10% = $40.00. The Davis-Bacon 401(k) portion is $ 200 gross x 10% = $20.

The check calculation results for the prevailing wage job and Davis-Bacon job would be as follows:

## Check Calculation Results

DB/PW Hours
Base Pay
Fringe Pay
Employer Benefit
401(k) Benefit
Pension

30 hrs
600.00
150.00
60.00
60.00
120.00
0.00
30.00

(30x2)
(40+20)
(60+60)
(150-120)

If the checkbox to compute this add-on as part of the D-B/Prevailing wage employer benefit (located in the Deduction / Add-on Code Maintenance  >  Add-on screen) was left clear, the calculation results for this example would appear as follows:

##  Check Calculation Results

DB/PW Hours
Base Pay
Fringe Pay
Employer Benefit
401(k) Benefit
Health & Welfare
Pension
Cash Fringe

30 hrs
600.00
150.00
60.00
60.00
60.00
0.00
90.00

(40+20)
(30 + 60)

Related information

- [Health & Welfare](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/health--welfare)

- [Cash Fringe](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/example---check-calculation-for-davis-bacon-and-prevailing-wage-jobs/cash-fringe)
