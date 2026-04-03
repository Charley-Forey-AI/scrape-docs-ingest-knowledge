---
title: "Employee Recurring Deductions/Add-ons - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-recurring-deductionsadd-ons/employee-recurring-deductionsadd-ons---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-recurring-deductionsadd-ons/employee-recurring-deductionsadd-ons---field-descriptions"
---

# Employee Recurring Deductions/Add-ons - Field Descriptions

Use the table below for reference when completing the fields on this screen or on the Entity-Specific Recurring Deductions / Add-ons screen.
FieldsDescriptions
Other entitiesIf cost centers are being used and multiple entities are set up for the employee, a link labeled 'Other entities' (and the number of entities) displays and provides access to the [Employee Entities](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-entities) page.
Only deductions and add-ons set up in this screen are used during pay cycles for the main company entity. Setup for other entities is done in the Entity-Specific Recurring Deductions / Add-ons window in [Employee Entities](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-entities).

CodeEnter the add-on or deduction code, up to 10 characters. The description and type display to the right of this field.
StatusSelect the appropriate add-on or deduction status code from the drop-down menu:

- Inactive - deduction will not be applied now, but direct cost add-ons can be recorded. (If the work-in-progress setting = Y or E, then the add-ons have an Inactive status in this screen.)

- One time - deduction or add-on is to be applied one time only.

- Recurring - deduction or add-on is to be applied to every check.

- Skip once - deduction or add-on is not to be applied for one pay period only.

Select the Status button to specify which deduction and add-on codes display on this grid. This will help when uploading deduction and add-on codes at year-end.

FormulaIf the deduction or add-on code is calculated with a user-defined formula, enter the formula code here.
AmountIf the calculation method is All hours, Regular hours only, Fixed amount, Percentage of Gross, Percentage of Net, Overtime equivalent hours, User-defined method, Prevailing Wage Adjustment, Employer Health & Welfare Benefit, Percent of Related Code, or Non-stated fringe enter the add-on or deduction amount. If this field is left blank, the standard rate defaults from the Deduction/Add-on Code Maintenance > Properties tab.
PercentIf the calculation method is Percentage of Gross or Percentage of Net or Percentage of Gross by Time Card, enter the employee's add-on or deduction percentage.
 If the value shown is for a shared percentage, you may opt to enter a value, but if you do, it must sum to 100% when combined with its shared code's percentage.

Shared codeIf your selection in the Code field is already paired with a shared-limit code, this field displays the shared-limit code.Important:Employees may opt for only one of a commonly paired deduction or add-on.

- If the employee wants only one code, enter the one only.

- If the employee wants both codes as a deduction or add-on, use the code shown in this field as the entry in the Code field for a new row.

For more information, see [Shared Limit Setup](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/shared-limit-setup).

Shared limit
Annual limitEnter the employee's annual limit for this add-on or deduction code, if applicable. Once the accumulated amounts equal the limit, this code's status will automatically change to Inactive. The system will prompt you if and when the annual limit has been reached.Note:If the given code is a Shared Code:

- You may enter a lesser limit than the limit already assigned to the code. The limit must be the same on each code.

- Your entry in this field is ignored if you enter a limit above that which is already assigned to the code.

Monthly limitIf using shared limits, this field is disabled.
Enter the employee's monthly limit for this add-on or deduction code, if applicable. Once the accumulated amounts equal the limit, this code's status will automatically change to Inactive. The system will prompt you if and when the monthly limit has been reached.The monthly deduction/add-on limit on the Deduction History Report and the Add-on History Report is determined by the Monthly Limit field. If this field is blank, the monthly limit on the reports is determined by the Monthly limit field on the Deduction/Add-on Code Maintenance screen.
If you use monthly limits, be sure to perform the [Period End Clear](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/period-end-clear) after the last payroll cycle of each month.

Cycle limit amt
Cycle limit %
Enter the per pay cycle limit amount or limit percentage for this add-on or deduction code. This limit is a percentage of gross wages (any rate x hours, other pay types 1,2,3,SA,SR, but not counting any add-ons).
These fields are only available if the Fixed Amount, Percent of Gross Amount, or Percent of Related Code option is selected in the Calculation method field on the [Deduction / Add-on Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties) >  Properties screen. [View more info on calculation methods](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/calculation-method-detail).

Variable 1, 2, 3Enter the value of the first variable (if any) if the deduction or add-on code is calculated with a user-defined formula. You can specify up to three formula variables.
A/P vendorThe A/P vendor code defaults from Deduction Code Maintenance, if recorded there. The vendor name displays to the right of this field.
Entries in this field supersede the Deduction Maintenance vendor. If no vendor code is recorded in either screen, but the checkbox is selected, no AP invoice is created. A warning message prints on the Deduction Report alerting the reader that no invoice will be created unless a vendor code is recorded prior to update.
Add-on codes not paid to the employee on the paycheck, such as employer-matching 401(k), create invoices in Accounts Payable. Add-on codes paid to employees do not transfer to A/P at all. Voided checks create credit memos in A/P.

A/P invoice remarkIf a vendor code was specified, enter a short description. Drill-down to open the A/P Remittance Advice Remarks to enter an additional three lines of remarks.The short description prints on the check stub. The drill-down prints on the A/P check when the option to print separate remittance advice has been selected in the Accounts Payable Installation screen.

Taken YTDThe employee's add-on or deduction accumulation for the year. The accumulation is the to-date amount of add-on or deductions taken. No entry is allowed. Add-ons that are paid to the employee on the check may not create A/P invoices.
Add-ons that are not paid on the check may create invoices, not credit memos. An example of this type of code would be the employer-matching 401(k) amount. If A/P invoice is selected, but a vendor code has not been designated, then no invoice is created; in this case, the Deduction Report includes a warning for those codes.

Balance annualThe employee's add-on or deduction balance for the year. The balance is the limit less the accumulated deductions.
Taken MTDThe employee's add-on or deduction accumulation for the month.
Balance monthThe employee's add-on or deduction balance for the month.
Related codeThe related code may be either an add-on or a deduction, and may be calculated using any method. Up to 10 characters are allowed.
MethodThe calculation method description.
