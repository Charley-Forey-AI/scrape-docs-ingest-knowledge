---
title: "PR Certified Export Template | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-certified-export-template"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/payroll-reports/payroll-reports-united-states-specific-reports/pr-certified-export-template"
---

# PR Certified Export Template

You can use the PR Certified Export Template by selecting
 Payroll > Reports > PR Certified Export Template.
The PR Certified Export Template is a Crystal report that will need to be copied and modified in order to export payroll certified information to state agencies or other third party software vendors. Export formats supported for this template are Excel and CSV formats. This default template prints (and sorts) one record by Job Company/Job/Employee/Craft and Class and exports daily hours (reg, ot, dbl) in separate columns. Other columns automatically included are Gross Earnings, Net Pay, Taxes (Fed, FICA, State), and pay rates. When modifying the template, the appropriate earning, deduction, and liability codes must be entered in the following formulas (if applicable). Earn in lieu of Fringes, Employer Health and Welfare, Employer Pension, Employer Vacation, Employer Training, Employee Pension, Employee Medical, SDI, Employee Union Dues, Employee Savings, and Travel Subsistence. Also, these aforementioned codes must have the Detail on Certified field checked in the Earning and Deduction/Liabilities master forms. The two columns for Other Liabilities and Other Deductions include amounts for those codes where the Detail on Certified box is unchecked. Because Federal (and FICA, Med) and State taxes print/export in specified columns, these amounts are excluded from Other Deductions even if the Detail on Certified box is unchecked. The employee information includes social security number and employee number, but other employee data is available by dragging fields from the PREH (Employee Header) view to the report. Finally, many of the same parameters from the standard PR Certified reports are included on this report. See report description on those reports for further explanation.
 In January 2009 the Department of Labor (DOL) stopped requiring the employee's social security number for certified reports. The social security number was removed from Viewpoint's other certified reports but not PR Certified Export Template.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

PR Group (Blank for All)
Select the Field Lookup button or press F4 to select the PR group, or leave blank for all.

Payroll Ending Date
Select the Field Lookup button or press F4 to select the payroll ending date.

First Day of Week
Enter first day of week.

Last Day of week
Enter last day of week.

Include Hours Only in Pay Pd.
checkbox to only include hours in the pay period.

Beginning Job Cost Company
Select the Field Lookup button or press F4 to select the beginning job cost company.

Ending Job Cost Company
Select the Field Lookup button or press F4 to select the ending job cost company.

Beginning Job
Select the Field Lookup button or press F4 to select the beginning job.

Ending Job
Select the Field Lookup button or press F4 to select the ending job.

Total (M)aster or (F)ull Job
Enter M or F.

Enter SigJobChars
Enter significant job characters.

Print SSN. (F)ull or (P)atrial or (N)one
Enter F, P, or N.

Certified Jobs Only?
checkbox to only include certified jobs.
