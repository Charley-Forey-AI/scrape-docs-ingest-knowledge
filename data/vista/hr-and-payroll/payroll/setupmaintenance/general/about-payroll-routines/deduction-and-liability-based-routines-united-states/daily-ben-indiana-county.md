---
title: "Daily Ben-Indiana County | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/daily-ben-indiana-county"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/deduction-and-liability-based-routines-united-states/daily-ben-indiana-county"
---

# Daily Ben-Indiana County

Use the table below to review additional setup information for tax routines Daily Ben through Indiana County.
Federal and State Tax / Workers' Comp Routines

State
Routine
Procedure Name
Form Used
Description

Additional Information for Setup

Daily Ben
Daily Ben
bspPRDailyBen
PR Routines
Set up daily rates in the Misc Amt fields as follows:
Misc Amt #1 - Weekdays
Misc Amt #2 - Saturday
Misc Amt #3 - Sunday
You should only use this routine if you have varying hourly benefits depending on the day of the week (e.g., separate rates for Mon-Fri, Sat, and Sun/Holidays). It assumes there are no regular time hours on Saturday, Sunday, or holidays.

Delaware
DE Tax
bspPRDETXX
PR Employees (Filing Status tab)
Use filing status S, M, or F.
M = Married, filing jointly
F = Married, filing separately
Use number of regular exemptions only.

District of Columbia
DC Tax
bspPRDCTXX
PR Employees (Filing Status tab)
Use filing status S, M, or F.
M = Married, filing jointly
F = Married, filing separately
Use number of regular exemptions only.

Exempt Rate of Gross

bspPRExemptRateOfGross
PR Routines
Set up a separate routine for each applicable
 local, and assign bspPRExemptRateOfGross
 as the procedure.

PR Deductions/ Liabilities
Enter the exemption amount in Misc Amt #1.
Assign routine to appropriate deductions.
Set up tax rates where applicable (e.g., Federal, State, Local, Craft, Employee), and make sure to update taxes when needed.

FICA
Reimb
FICA
Reimb
vspPRFICAReimbursement
PR Earn Codes
Set the method to R-Routine; set the routine to FICA Reimb; in the Dedn / Liabs tab, add only the FICA-related DL codes (typically Social Security, Medicare, and Additional Medicare). Assign a number to the code that is higher than all other earn codes so that it is always the last earn code calculated.

PR Routines
Use F4 to locate and assign
 vspPRFICAReimbursement as the
 procedure.

PR Deductions/ Liabilities
There can be no deductions assigned as Basis Codes on the SS, Med, or Add'l Med deductions (i.e., they cannot be pretax).

PR Crafts or
PR Craft Classes
Add the earn code to the grid in the Add-on Earnings tab. The routine only calculates on timecard lines with the Craft. Since FICA will calculate on all lines, it should be expected that the resultant Add-on earnings will equal FICA deductions only for lines that are set to the craft.

Florida
None

Georgia
GA Tax
bspPRGATXX
PR Employees (Filing Status tab)
Use filing status S, H, M, F, or B
S = Single
H = Unmarried, head of household
M = Married filing jointly, one spouse working
F = Married filing separately
B = Married both working
Regular exemptions = number of dependents other than spouse.

Guam
GU Tax
bspPRGUT10
PR Deductions/ Liabilities
Setup a deduction using this routine. Specify the same earnings codes as set up for the Federal deduction. If you rounded the calculations for Federal, check the Round Result to Nearest Whole Dollar option for the deduction.

PR State Information
Set up Guam as a state, using the GU tax deduction code.

Hawaii
HI Tax
bspPRHITXX
PR Employees (Filing Status tab)
Use filing status of M or S only.
Use number of regular exemptions only.

Idaho
ID Tax
bspPRIDTXX
PR Employees (Filing Status tab)
Use filing status of M or S only.
Head of Household use filing stats of S
Use number of regular exemptions only.

Illinois
IL Tax
bspPRILTXX
PR Employees (Filing Status tab)
Regular exemptions (Line 2) = enter the number of exemptions that were entered on Line 1 of Form IL-W-4.
Additional exemptions (Line 3) = enter the number of exemptions that were entered on Line 2 of Form IL-W-4.

Indiana
IN Tax
bspPRINTXX
PR Employees (Filing Status tab)

Regular exemptions (Line 2) = enter the number of exemptions that were entered on Line 4 of Form WF-4.
Additional exemptions (Line 3) = enter the number of exemptions that were entered on Line 5 of Form WH-4.

Effective 1/1/23:
 If you are claiming the adopted children allowance, use the Misc Factor field to enter the number of adopted children.

Effective 9/15/23:
If you are claiming the first-time dependent allowance, add 1 to the number of Additional exemptions.

Indiana County
INCnty Tax
bspPRINCXX
PR Employees (Filing Status tab)
Use the Regular Exemptions field to specify the number of personal exemptions and the Add'l Exempt's field to specify the number of dependent exemptions.

Effective 1/1/23:
 If you are claiming the adopted children allowance, use the Misc Factor field to enter the number of adopted children.

PR Deductions/Liabilities
Enter the resident rate in the Rate/Amount #1 field, and the non-resident rate in the Rate/Amount #2 field.

PR Local Codes
Add a local code for the county, and select 0-Posted Local Only option from the Calculation Option drop-down.

PR Company
On State/Local tab, check the Use Job or Office Local for Local Tax option. This will take care of non-residents that work in a taxable county based on the job.
