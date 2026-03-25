---
title: "Federal-Connecticut | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/federal-connecticut"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/federal-connecticut"
---

# Federal-Connecticut

Use the table below to review additional setup information for tax routines Federal through Connecticut.
Federal and State Tax / Workers' Comp Routines

State
Routine
Procedure Name
Form Used
Description

Additional Information for Setup

Federal
FED Tax
bspPRFWTXX
PR Employees (Filing Status tab)
Use filing status as follows:
S = Single or Married filing separately
M = Married filing jointly or Qualifying surviving spouse
H = Head of Household
Use number of regular exemptions only. Employees wishing to claim additional exemptions in the following states need the state income tax deduction code and number of additional exemptions added to the grid: CA, GA, IL, IN, LA, MA, MI, PR, VA.
For Federal W-4s, see [Set up an Employee's Filing Status for Federal W-4s (U.S.)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/employee-filing-status-setup-for-tax-withholding/set-up-an-employees-filing-status-for-federal-w-4s-u.s.) for information about
 Filing Status settings.

PR Deductions/ Liabilities
This routine does not round to whole dollars automatically. If you want calculations rounded, check the Round Result to Nearest Whole Dollar option for the deduction.

Federal
Addl Med
vspPRMedicare
SurchargeXX

PR Deductions/ Liabilities
Set up the following fields as indicated:
Type = Deduction
Calculation Category = F-Federal
Federal Type = 4-Medicare
Method = R-Routine
Routine = Addl Med
Rate / Amount #1 = Enter the current rate

PR Routines
Misc Amt #1 = Enter the current threshold amount.

PR Federal Info
Add the deduction code to the Additional Medicare Surcharge field.

Alabama
AL Tax
bspPRALTXX
PR Employees (Filing Status tab)
Use filing status as follows:
O (alpha) - No exemptions
S - Single or married with $1,500 exemption
F - Married and filing separately with $1,500 exemption
B - Married and filing jointly
H - Head of household
Regular Exempts = Number of dependents other than spouse.

Alaska
None

Arizona
AZ Tax
bspPRAZTXX
PR Employees (Filing Status tab)
Misc Factor = Tax Rate
Enter the rate specified by each employee on Arizona Form A-4. If the employee has opted to not have Arizona tax deducted, enter a Misc Factor of .000000.
For employees who have not yet submitted Form A-4, you can either:

- wait to set up a filing status for the Arizona deduction until the employee has submitted Form A-4 or,

- set up the filing status but leave the Misc Factor field blank.

In both cases, the system automatically uses the median tax rate defined by the State of Arizona for the current year.

Arkansas
AR Tax
bspPRARTXX
PR Employees (Filing Stats tab)
Regular exemptions = personal tax credit.
If using low income tax rates, set the filing status to S, M, or H.
If not using low income tax rates, filing status is not required.
Misc Factor = 1

California
CA Tax
bspPRCATXX
PR Employees (Filing Status tab)
Use filing status of M, S, or H.
Regular exemptions = number of regular withholding allowances.
Additional exemptions = number of additional withholding allowances for estimated deductions.

Colorado
CO Tax
bspPRCOTXX
PR Employees (Filing Status tab)
As of 1/1/2022:
Use filing status as follows:
M = Married filing jointly or Qualifying widow(er)
S = Single or Head of Household.
Use number of regular exemptions only.
For the Colorado deduction code only:

1. Select the Override Misc Amount #1 checkbox.

1. In the Misc Amount #1 field:

- If the employee submitted Form DR 0004, enter the amount from Line 2 of Form DR 0004.

- If the employee did not submit Form DR 0004 or if Line 2 on Form DR 0004 is blank, enter the appropriate amount based on the employee's expected filing status from IRS Form W-4 (see allowed filing statuses above).

Colorado
Occup Priv
CO OP Tax
bspPRCOOXX
PR Deductions/ Liabilities
For CO Occupational Privilege Tax, use the following setup:
Rate/Amount #1 = Enter the tax amount
In the Limit section:
Amount field = Enter the monthly limit.
Applied = Monthly.

Connecticut
CT Tax
bspPRCTTXX
PR Employees (Filing Status tab)
Use filing status of S, H, M, B, or F only. These codes represent Connecticut's filing codes as follows:
S = Single (Code F)
H = Head of Household (Code B)
M = Married Filing Jointly (Code C)
B = Married Filing Jointly, exemption=0 (Code D)
F = Married Filing Separately (Code A)
Use number of regular exemptions only.
