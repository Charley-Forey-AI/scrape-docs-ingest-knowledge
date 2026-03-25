---
title: "North Carolina-Philadelphia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/north-carolina-philadelphia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/north-carolina-philadelphia"
---

# North Carolina-Philadelphia

Use the table below to review additional setup information for tax routines North Carolina through Philadelphia.
Federal and State Tax / Workers' Comp Routines

State
Routine
Procedure Name
Form Used
Description

Additional Information for Setup

North Carolina
NC Tax
bspPRNCTXX
PR Employees (Filing Status tab)
Use filing status of M, H, S, or W only.
Use number of regular exemptions only.

North Dakota
ND Tax
bspPRNDTXX
PR Deductions/ Liabilities
Worker’s Comp Routine: Enter same as for Nevada.

PR Employees (Filing Status tab)
Use filing status of M, S, or H only.
Use number of regular exemptions only.

Ohio
OH Tax
bspPROHTXX
PR Employees (Filing Status tab)
Use number of regular exemptions only.

Ohio Workers' Comp
None
PR State Insurance Codes
Enter weekly limit. The limit applies to all Ohio Worker’s Comp codes combined.

Ohio School District
OHSch Tax
bspPROSTXX
PR Deductions/ Liabilities
Set up code for each district.
Rate/Amount #1 = District rate
Be sure to define Ohio state tax in PR Employees (Filing Status tab). The regular exemptions specified for computing Ohio state tax will be used to compute Ohio School District tax.

PR Employee Deductions & Liabilities
Enter deduction by employee. Check the Employee-Based box, and select the Use Calculated Amount option (Calculations section).
Do not set up these codes in PR Local Codes.

Oklahoma
OK Tax
bspPROKTXX
PR Employees (Filing Status tab)
Use filing status of S, H, or M.
S = Single or Married with Dual Incomes, but filing Single on Federal form W-4
H = Head of Household
M = Married
Set up regular exemptions using the Total Number of Allowances claimed on Line
 5 of the Oklahoma Form OK-W-4.

Oregon
OR Tax
bspPRORTXX
PR Employees (Filing Status tab)
Use filing status of M or S only.
Use number of regular exemptions only.

OR MultnoMultnomah County Income TaxbspPRMultnomahORCPR
 Deductions/LiabilitiesSet up a deduction using this routine. Set the Calculation Category to Local, and add applicable basis codes.Use the Rate/Amount fields to enter the tax rates.
Rate/Amount #1 = .015
 Rate/Amount #2 = .015
Note: For tax rules, rates, and thresholds, see Chapter 11.512 of the [Multnomah County - Revenue and Taxation](https://www.multco.us/county-attorney/multnomah-county-code) document.

PR Local CodesSet up a local code using the deduction code set up for Multnomah County tax in PR Deductions/Liabilities.Note: You will only need to set up this local code if you have employees that live and/or work in Multnomah county, but the residence and/or work location is outside the Portland Metro area.

PR RoutinesSet up threshold amounts as follows:Misc Amt #1 = 200,000.00 (lower threshold, joint)
Misc Amt #2 = 400,000.00 (higher threshold, joint)
Misc Amt #3 = 125,000.00 (lower threshold, single)
Misc Amt #4 = 250,000.00 (higher threshold, single)

OR PDX MetPortland OR Metro Income TaxbspPRPDXMetroORCPR
 Deductions/LiabilitiesSet up a deduction using this routine. Set the Calculation Category to Local, and add applicable basis codes.Use the Rate/Amount fields to enter the tax rate:
Rate/Amount #1 = .01
Note: For tax rules, rates and thresholds for the Portland Metro income tax, see the [Oregon Metro](https://www.oregonmetro.gov/public-projects/supportive-housing-services-tax) webpage.

PR Local CodesSet up a local code using the deduction code set up for Portland Metro tax in PR Deductions/Liabilities.Note: If you have employees that live and/or work in both Portland and
 Multnomah county, set up another local code to represent
 both. For example, you might set up a
 local code called PDX-Mult using
 the Portland Metro deduction, and then add the Multnomah
 County deduction to the Addl Local Based
 Dedns/Liabs tab.

PR RoutinesSet up threshold amounts as follows:Misc Amt #1 = 200,000.00 (threshold, joint)
Misc Amt #2 = 125,000.00 (threshold, single)

Oregon Transit Tax
This is not a routine, it is a deduction that requires set up in PR Deductions/Liabilites and PR State Information. For more information, see [Set up Oregon Transit Tax](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-oregon-transit-tax).
Pennsylvania
None
PR Deductions/ Liabilities
Set up as a simple Rate of Gross method deduction.
Enter withholding rate in both Rate # and Rate #2 (.021 for 1988).
Set up city taxes as needed:
Also rate of gross, use Rate #1 for resident, Rate #2 for non-resident.

Philadelphia
PHCity Tax
bspPRPHCXX
PR Deductions/ Liabilities
Set up deduction using this routine.
Rate/Amount #1 – Enter the resident rate
Rate/Amount #2 – Enter the non-resident
 rate
