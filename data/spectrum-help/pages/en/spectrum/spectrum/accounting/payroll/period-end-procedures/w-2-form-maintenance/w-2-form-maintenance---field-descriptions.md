---
title: "W-2 Form Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/w-2-form-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/period-end-procedures/w-2-form-maintenance/w-2-form-maintenance---field-descriptions"
---

# W-2 Form Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
FormsSelect to clear the W-2 file and calculate W-2 information based on the payroll earnings history file.
ListingSelect to print W-2 information entered on this screen.
Print W-2Select to print W-2s at year end.
Print W-3Select to print W-3 "Transmittal of Wage and Tax Statements" transmittal forms.
ExportSelect to compile W-2 information in order to file W-2 forms electronically.
Update State IDIf you are uploading W-2s to Nelco for electronic processing, you are required to have a State ID, even if your state does not have a state income tax. Select this field if you want to overwrite the State ID number entered in Box 15 with the current State ID number entered in Tax Table Maintenance.
If entity tracking is enabled in the current company, Spectrum will look to the entity table for the Tax ID first.

BackupSelect to open the Backup W-2 Records to History window. This utility stores the current W-2 information into a history table for future use.
EntityThis field only displays if cost centers are being used and entity tracking is also enabled in the current company.
After entering or selecting an Entity, a list of all employees currently receiving a W-2 will be shown on the main screen for tax review purposes, and cost center security prevents editing employee W-2s that the operator does not have authorization to access.

Employee codeEnter the code of the employee whose W-2 information is to be modified, or double-click on this field to select from a list of available employee codes.
Form #If an employee works in more than two states or local jurisdictions, an extra W-2 is created (no Federal dollars will display on the extra W-2). In that case, the number entered here (form number) indicates which additional form is being viewed. Employees working in three or four states would receive one extra W-2 form, employees working in five or six states would receive two extra W-2 forms, and so forth.
b. Employer's identification #The employer's Federal ID number displays, as set up in the US Income Tax Table. No entry is allowed.
If entity tracking is enabled in Enterprise Installation, then the Payer tax ID number assigned to the US tax code displays.

d. Employee's social security #The employee's social security number displays. If a number is entered, do not type the hyphens; they will be automatically inserted by the system.
e. Employee's name and addressThe employee's name and mailing address display. Press Enter to accept them or enter the desired changes. Enter the alternate/additional name or legal representative, if applicable.
Spectrum searches for suffixes Jr, Sr, II, and III, with or without a period at the end (these are the only suffixes recognized by Spectrum).

Foreign Address buttonSelect to open the Foreign Address window. If applicable, add or edit this employee's foreign address.
1. Wages, tips, other compThe wages, tips, and other Federal income tax applicable compensation to be reported displays.
2. FIT withheldThe federal income tax withheld displays.
3. Social security wagesThe social security wages to be reported displays.
4. SS tax withheldThe amount of social security tax to be withheld displays.
5. Medicare wages, tipsThe Medicare wages and tips to be reported display. If the amount is zero, leave this field blank. This field must be left blank if the type of employment is RRTA. The amount in this field must equal or exceed the combined entries of Boxes 3 and 7.
6. Medicare tax withheldThe Medicare tax withheld displays. When the amount is zero, leave this field blank. The amount entered cannot exceed 1.45% of the amount entered in Box 5. This field must be left blank if Box 5 is blank or if the employment type is RRTA.
7. Social security tipsThe social security tips to be reported display. This field must be blank if the type of employment is MQGE or RRTA. The value in this field cannot be greater than the amount in Box 3. If this field contains a value, then Boxes 4 and 12 must contain amounts with the alpha code "A" and Box 5 must contain an entry.
8. Allocated tipsThe Medicare wages and tips to be reported display. If the amount is zero, leave this field blank. This field must be left blank if the type of employment is RRTA. The amount in this field must equal or exceed the combined entries of Boxes 3 and 7.
9. Not usedNot used.
10. Depend care benefitsThe amount for dependent care displays. When the amount is zero, leave this field blank.
11. Nonqualified plansThis value must be in dollars and cents and cannot be a negative amount. If this amount only represents a section 457 plan distribution, the amount must be preceded by the alpha code G and contain at least one blank space. Only one entry is permitted.
12a - d. 401k and other codesThe 401(k) dollar amount displays. To the left of the 401(k) amount is the alpha code for Box 13 amounts. Use code D for 401(k) amounts. A window is available at the alpha code field for use in recording two additional Box 13 amounts; for example, Group Life Insurance (Code C).

- This field is conditionally completed if the Retirement plan field on W-2 Form Update screen is set to K – Check only for 401k participants and alpha code type D or S is non-zero.

- Form W-3 includes a 12b box for HIRE exempt wages and tips. This box sums the W-2 CC amounts (which may be entered in any box 12 field on the W-2).

13. Statutory employee?
Retirement plan?
Third-party sick pay?
Select the checkboxes that apply to the current employee.

- A statutory employee is one whose remuneration is subject to social security and Medicare withholding, but not Federal income tax.

- The pension plan default indicator was defined in W-2 Form Update. This checkbox is automatically selected if the Retirement plan field on the W-2 Form Update screen is set to K – Check only for 401k participants or Y – Yes, check retirement on all W-2s. If the Retirement plan field is set to N – No, leave retirement blank on all, this checkbox is left clear.

- Select the last checkbox if this employee received third-party sick pay.

14. OtherThe type, code, dollar amount, and description of the deductions display in this window.
The following fields are NOT required by the Social Security Administration.
15. St State ID NoThe state abbreviation displays. Information for two states can display. If an employee works in more than two states, an extra W-2 is needed (no Federal dollars will display on the extra W-2). The cursor will move through the information for the first state, then advance down one line and move through the information for the second state.
The employer's state ID displays, as set up in the Tax Table Maintenance screen.

16. St wagesThe wages and tips to be reported for this state display.
17. State taxThe amount withheld for state income tax displays. Repeat income tax, wages/tips, and name for a second state, if applicable.
18. Loc wagesThe wages and tips to be reported display.
19. Local taxThe amount withheld for local income tax displays.
20. Locality and CodeThe locality name and code display.
