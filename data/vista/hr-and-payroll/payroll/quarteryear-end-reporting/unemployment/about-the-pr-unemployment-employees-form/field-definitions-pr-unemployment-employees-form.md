---
title: "Field Definitions: PR Unemployment Employees Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/about-the-pr-unemployment-employees-form/field-definitions-pr-unemployment-employees-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/unemployment/about-the-pr-unemployment-employees-form/field-definitions-pr-unemployment-employees-form"
---

# Field Definitions: PR Unemployment Employees Form

The following is a list of field descriptions for the PR
 Unemployment Employees form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  State

 Enter the state for which to maintain unemployment/wage information.

##  Quarter Ending

 Enter the last month for the calendar quarter (03/YY, 06/YY, 09/YY, or 12/YY) to which this report applies.

##  Employee

 Enter the employee for which you wish to maintain unemployment/wage report information.

##  Name: Last

 If you initialized unemployment/wage report information (PR Unemployment Process, File menu), this field defaults employee’s last name from PR Employees. Otherwise, you must enter manually.

##  Name: First

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), this field defaults employee’s first name from PR Employees. Otherwise, you must enter manually.

##  Name: Middle

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), this field defaults employee’s middle name from PR Employees. Otherwise, you must enter manually.

##  Suffix

 If you initialized unemployment/wage report information (PR Unemployment Process, File menu), this field defaults the employee’s suffix (i.e. Jr., Sr., III, etc.) from PR Employees. Otherwise, you must enter manually. Up to four characters allowed.

##  SSN# (W/O Dashes)

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), this field defaults employee’s social security number (minus the hyphens) from PR Employees.
Note: You can change an employee's SSN# here if necessary, but it does not update to the employee master (PR Employees). A message displays alerting you to the fact that change is for unemployment purposes only and that if you want to change it for payroll, you must do so manually in PR Employees.

##  Hire Date

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), this menu defaults employee’s hire date from PR Employees. Otherwise, you must enter manually.

##  Term Date

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), this field defaults employee termination date from PR Employees. Otherwise, you must enter manually.

##  Company Officer

 Check this box if this employee is an officer (e.g. President, Vice-President, Manager, etc.) of the company.
 Do not check this box if this employee is not an officer of the company.

##  Code

 Currently only used for the state of Wyoming.
 If this employee is an officer of the company, indicate which title the employee holds.
· P = President
· V = Vice President
· S = Secretary
· T = Treasurer
· O = Other

##  Seasonal Indicator

 Enter the seasonal indicator, up to two characters.

##  Employer Health Insurance

 Enter the employer’s 1-character health insurance code.

##  Employee Health Insurance

 Enter the employee’s 1-character health insurance code.

##  Probationary Code

 Enter the 1-character probationary code.

##  Wage Plan Code

 Enter the 1-character wage plan code.

##  Weeks Worked

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), and the Accumulate With SUTA Liability option in PR State Information is “Weeks Worked,” defaults the number of weeks this employee worked in the specified quarter. If the Hours Worked option is not selected, defaults to zero; may be overridden.

##  Hours Worked

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), and the Accumulate With SUTA Liability option in PR State Information is Hours Worked, defaults the number of hours this employee worked in the specified quarter. If the Weeks Worked option is not selected, defaults to zero; may be overridden.

##  Reporting Unit #

 Enter the reporting unit #, up to 10 characters, as defined by state.
 For Minnesota, use this field to enter the Unit/Locator # (i.e. employee location). The Unit/Locator # is a three digit number; however, since the record allows for four digits, the first position will be a "0". If no location is specified, the field is zero-filled.

##  Industry Code

 Enter the industry code, up to four characters, as defined by state.

## NAICS Code

 The NAICS Code field in the PR Unemployment form, Employees tab
 This field applies to Wyoming only.
 Enter the NAICS code for this employee. The
 field corresponds with the Class Code field used for Wyoming unemployment filing. During
 filing, if the employee is set as a corporate officer (you checked the Company Officer
 checkbox), the system hard codes a “C” to the value. During filing the system updates this
 field with the code specified in the NAICS Code field in PR Employees.

##  Employed In

 For each of the three months in the specified quarter, you must indicate whether the selected employee worked in a pay period that included the 12th day of month, even if the employee did not actually work on that day. For example, pay periods run the 1st through the 15th, and the 16th through the 31st of each month. If the employee in question worked during the first pay period of the 1st and 2nd month, but was on vacation during the first pay period of the 3rd month, the boxes would be checked for Mth 1 and Mth 2, but not for Mth 3.
Note: If you initialized the unemployment/wage data, the form automatically checks this box for each applicable month.

##  Wage For SUI Benefit Computation

 If your company classifies unemployment benefits, specify the wage type for SUI benefit computation.
· Benefit
· Other

##  Gross Wages

 If you initialized this unemployment/wage report information (PR Unemployment Process, file menu), defaults the employee’s gross wages for the quarter that are subject to state tax, as recorded in PR Employee Accumulations. Otherwise, you must enter manually.

##  SUI Wages

 If you initialized this unemployment/wage report information (PR Unemployment Process, File menu), this field defaults the employee’s quarterly wages that are subject to unemployment insurance, as recorded in PR Employee Accumulations. Otherwise, you must enter manually.

##  Excess Wages

 Defaults the difference between the quarterly SUI wages and the unemployment wage base (Eligible Wages).

##  Eligible Wages

 If you initialized this unemployment/wage report information (Initialize option, File menu, PR Unemployment Process), defaults the employee’s quarterly wages that are eligible for unemployment insurance, as recorded in PR Employee Accumulations. Otherwise, you must enter manually.

##  Disability Wages

 Enter the quarterly wages that are subject to disability insurance, if applicable.

##  Tip Wages

 Enter the quarterly tip income, if applicable.

## State Tax Wages

Currently only used for Massachusetts and California unemployment wage reporting.
Enter the state tax wages for this employee. Initially defaults the state taxable wages (which may differ from SUTA wages due to deductions such as 401k, Sec125, etc.) from the PRUE table (UNEMP/WAGE EMPLOYEE) during initialization (in PR Unemployment/Wage Init). This amount will be included in the electronic file.

##  State Tax

 If you initialized this unemployment/wage report information (PR Unemployment Process), defaults the employee’s state tax withheld for the quarter, as recorded in PR Employee Accumulations. Otherwise, you must enter manually.

## Annual Gross Wage

 If you initialized this unemployment/wage report information (PR Unemployment Process), this field defaults the employee’s gross wages year-to-date as of the quarter specified above, that are subject to state tax (as recorded in PR Employee Accumulations). Otherwise, you must enter manually.
For New York state: this field will be initialized with the quarterly gross wages for reporting in the first three quarters of the year and with the annual gross wages for reporting in the fourth quarter.

## Annual State Tax

 If you initialized this unemployment/wage report information (PR Unemployment Process), defaults the employee’s state tax withheld year-to-date as of the quarter specified above (as recorded in PR Employee Accumulations). Otherwise, you must enter manually.
For New York state: this field will be initialized with the quarterly state income tax withheld for reporting in the first three quarters of the year and with the annual state income tax withheld for reporting in the fourth quarter.

## New York City/Not Used

 This field is used for the state of New York
 only. The field name displays as Not Used for all other states.
If you initialized this unemployment/wage report information (PR Unemployment Process), this field defaults the employee’s New York City tax withheld for the quarter (as recorded in PR Employee Accumulations) except for the fourth quarter in which case the annual New York City tax withheld is defaulted.

## Yonkers, New York/Not Used

 This field is used for the state of New York
 only. The field name displays as Not Used for all other states.
If you initialized this unemployment/wage report information (PR Unemployment Process), this field defaults the employee’s Yonkers tax withheld for the quarter (as recorded in PR Employee Accumulations) except for the fourth quarter when the system defaults the annual Yonkers tax withheld.

##  Not Used

 Currently not in use.

## NM Workers Comp Empl 1 and 2

Use this field for the state of New Mexico
 only. The field label displays as Not Used for all other states.
These fields display the workers compensation amounts from the PRSI (Payroll State Information) form DL Code 1 and 2 fields. These two amounts are combined together and written to the employee record for ‘NM’ in the workers compensation column.
