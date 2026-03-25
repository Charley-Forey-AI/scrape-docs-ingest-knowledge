---
title: "Verifying 401(k) Deduction and 401(k) Catch-up Deduction Amounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/verifying-401k-deduction-and-401k-catch-up-deduction-amounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions/verifying-401k-deduction-and-401k-catch-up-deduction-amounts"
---

# Verifying 401(k) Deduction and 401(k) Catch-up Deduction Amounts

If your company has a 401(k) plan and you have employees over
 50 that participate in catch up deductions, you may want to verify that catch-up deduction
 amounts are correct on paychecks that include both the last regular 401(k) deduction and the
 first 401(k) catch-up deduction.
To verify these amounts, refer to the
 following steps and sample data:
Table 1. Sample data: current payroll in
 PR Employee Pay Seq ControlDL Code
Rate/Amount
Subject
Eligible
Amount
Limit YTD
Limit Reached?

401-1
.08
1000.00
1000.00
80.00
17490.00
No

401-2
.02
1000.00
500.00
10.00
17500.00
Yes

401-3
$30.00
1000.00
1000.00
0.00
17500.00
Yes

401-C
.05
1000.00
800.00
40.00
40.00
No

StepsExample based on
 sample data
1.Confirm that the
 401(k) standard annual contribution limit (set in the Pre-Tax Group)
 has been reached.If Yes, go to
 Step 2.
2.Determine the
 total normal 401(k) deduction amount that would have been deducted
 from the employee's paycheck if the limit had not been met.

3.Compare the
 total normal 401(k) amount to the actual calculated amount that was
 deducted on this paycheck. The actual amount will likely be less
 than the normal amount because this is the last regular 401(k)
 deduction.Normal = 130.00  /
 Calculated = 90.00 (80.00 + 10.00) 
130.00 - 90.00 =
 40.00
In this scenario,
 40.00 can be used towards 401k catch-up in this pay period.

4.Determine the
 normal catch-up deduction amount for this pay period.50.00 normal
 calculated catch-up contribution (.05 x 1000.00 = 50.00), or 50.00
 amount when Amount based.
5.Compare the
 normal 401(k) amount to the normal catch-up deduction amount. The
 system uses the lesser of these two amounts.Normal calculated
 catch-up = 50.00 
Remaining 401(k)
 allotted to catch-up for this pay period = 40.00
In this scenario,
 the system posts 40.00 to 401-C in PR Employee Pay Seq Control.


6.Check the Eligible
 amounts.
When the catch-up
 code is:

- Rate-based -
 Back calculate the Eligible amount for catch-up. 40.00 /
 .05 = 800.00

- Amount based
 - Eligible amount has little meaning and would be posted
 as 1000.00

In subsequent pay periods where only
 catch-up is calculated, the 401-C deduction code will calculate normally until which
 time the deduction limit is reached for this catch-up deduction code.
For more information about setting up pre-tax deductions, see [Set Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions).
