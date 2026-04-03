---
title: "New/Edit Deduction/Add-on Code - Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties/newedit-deductionadd-on-code---properties---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties/newedit-deductionadd-on-code---properties---field-descriptions"
---

# New/Edit Deduction/Add-on Code - Properties - Field Descriptions

Use the table below for reference when completing the fields on the Properties tab of the New (or Edit) Deduction/Add-on Code screen.
FieldsDescriptions
CodeEnter the deduction code up to 10 characters. There is no limit as to the number of deductions allowed per check cycle.Note: The letter U cannot be used for deduction and add-on codes because it is reserved for use by the system as a pay type code.

DescriptionEnter the deduction/add-on code description.
TypeSelect the deduction type, depending on whether the calculated amount for this code is to be added or subtracted from the employee's pay:

- Add-on - If the amount is to be added.

- Deduction - If the amount is to be subtracted.

Allocate across time cards?Select this checkbox if you want to distribute expense based on the employee's time card lines. This checkbox is selected by default if a 'by time card' calculation method is currently assigned to the add-on code.Tip: to calculate by 'Percent of Gross by Time Card', select this checkbox and then choose the 'Percent of Gross' calculation method.

Calculation methodUse the drop-down menu to select the calculation method. For additional information, see [Calculation Method Detail](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/calculation-method-detail).
When the Allocate across time cards checkbox is selected, only six calculation method options are available by time card.
For each of these calculation methods, 'recurring add-ons' distribute expense based on employees' time card lines. This means if the time card is a 'Direct job cost' line, the add-on is charged to the same job and phase. Likewise, if the line is assigned to a 'Direct equipment cost' or 'Direct work order cost' line, the add-on is charged to the particular equipment code or work order, respectively.

Default rate or percentEnter the default rate or percent, depending upon the Calculation method field. Entry in this field is optional.
If a rate is specified, entry in the Default rate field will be used during check calculation if the corresponding rate is blank in Employee Recurring Deductions/Add-ons.

Related codeEnter the related deduction/add-on code.
The related code may be either an add-on or a deduction and may be calculated using any method.
Spectrum prevents the selection of related codes computed using a user-defined formula code that references % of Federal, % of State, % of County, or % of Local during its computation. Related codes with any other user-defined formulas and calculation methods may be selected. Spectrum also verifies that the calculation method of the Related code field is not % of related code.

Formula codeEnter the code for the user-defined formula. This field is available only if the Calculation method field is set to User-Defined Formula.
FrequencyEnter a deduction / add-on frequency code, or choose one from the drop-down menu.
Frequencies are optional. If used, be sure to enter a code for each frequency with which the deduction will be made. For example, depending on pay schedules, the company health plan deductions may be made biweekly, weekly, and/or semi-monthly; one code must be entered for each pay frequency type. Otherwise, if frequency is left blank, a single code may be used for all employees.

Week numbersEnter the payroll week number that you would like this deduction or add-on to be taken. For example, enter 135 if you would like this code to be processed on the first, third, and fifth week's payroll. Remember to enter the proper week number when setting your new pay cycle.
G/L account codeNote: Does not display if the Percent of Gross Amount calculation method is selected.
 Enter the General Ledger account code to which this deduction/add-on is to be posted. Entry in this field is required. The G/L account code description will display to the right of this field.

- If the deduction / add-on code is a deduction (for example, garnish payable), then it is a credit.

- If the deduction / add-on code is an add-on (for example, mileage expense reimbursement), then it is a debit.

Eligible for "true up" calculation?Note: Disabled if the Percent of Gross Amount calculation method is selected.
Select this checkbox if this deduction or add-on code is eligible for 'true-up'.
Note: The 'true up' calculations are performed only for employees receiving a regular check during the pay cycle in which this checkbox is selected.
This checkbox is provided for deduction and add-on codes computed as a "percent of gross" and a "percent of a related code". When this checkbox is selected, monthly limits (if any) specified in Employee Recurring Deductions/Add-ons will be ignored. Likewise, any 'per cycle limits' specified in Deduction / Add-on Code Maintenance will be disregarded during this cycle for 'true up' codes. Instead, the 'true up limit' specified on the Limits tab of the Deduction / Add-on Code Maintenance screen will be applied, if applicable.
The calculation during a 'true up' Payroll cycle will be as follows for '% of gross':

- Year-to-date gross + current check gross = Total gross

- Total gross X employee's specified % = Maximum allowable YTD deduction / add-on amount

- The maximum allowable amount is compared to the annual limit (if any) in Employee Deduction / Add-on Code Maintenance

- The maximum allowable amount is compared to the 'true up' limit (if any) in Deduction / Add-on Code Maintenance

- The minimum of the allowable amount and the two limits is determined to be the 'YTD eligible amount'

- The 'YTD eligible amount' minus the 'YTD amount taken' = 'true up' amount granted on pay check

The calculation during a 'true up' payroll cycle will be as follows for '% of related code':

- Year-to-date taken on related code + related code amount on current check = 'Total related code amount'

- 'Total related code amount' X employee's specified percentage = Maximum allowable YTD deduction / add-on amount

- The maximum allowable amount is compared to the annual limit (if any) if Employee Recurring Deductions/Add-ons

- The maximum allowable amount is compared to the 'true up' limit (if any) in Deduction / Add-on Code Maintenance

- The minimum of the allowable amount and the two limits is determined to be the 'YTD eligible amount'

- The 'YTD eligible amount' minus the 'YTD amount taken' = 'true up' amount granted on pay check

Clear employee balance at year end?Select if this Payroll deduction should be cleared at year-end.
If an employee loan or deduction spans multiple payroll years, leave this checkbox cleared so that any remaining balance carries forward to subsequent years.

Aatrix tax typeIf you are using Aatrix for eFiling tax forms, select the Aatrix electronic tax type code that maps to the Spectrum add-on/deduction code in this field.Note: Aatrix eFiling is available only to hosted customers.

Display accumulated balance on paycheck?Note: Displays only for add-ons and deductions with balances that are not cleared at year-end.
Allows Payroll Managers to flag the add-on and deduction codes that will show the accumulated balance on the check instead of the year-to-date activity total.
If this checkbox is selected, the accumulated balance displays in these places:

- Payroll Checks and Layoff Checks, instead of the YTD balance

- When applicable, the Employee Kiosk > Employee Statement and on Replacement Checks.

Include pay & hours fromUse these checkboxes to designate which time card lines to include in the calculation.
These checkboxes are not available for use if the calculation method is set to Fixed Amount, Percent of Net, or Percent of Related Code.
You can clear these checkboxes as necessary, but you cannot save a code that has all three checkboxes deselected (because this would deselect all time card lines).
Spectrum looks to each time card line to determine whether or not the add-on or deduction code should be taken.
The check file will store the total hours and gross pay for Davis-Bacon jobs and prevailing wage jobs.
For each job, these checkboxes work with the Davis-Bacon job and Prevailing Wag job checkboxes in the Job File Maintenance > Properties window.

Other jobs & non-jobsApplies to jobs that have neither the Davis-Bacon job nor the Prevailing Wage Job checkboxes selected in Job File Maintenance > Properties.
Gross Pay AdjustmentsButton appears only if the Calculation method field is set to one of these:

- Percent of Gross Amount

- Percent of Straight Time Equivalent

- User Defined

Select to open the [Gross Pay Adjustments Window](/en/spectrum/spectrum/accounting/payroll/data-entry/layoff-check-print/gross-pay-adjustments-window) to add the appropriate add-ons that should be included with the gross pay only for the calculation.Note: Gross Pay Adjustments apply only to employee recurring deductions and add-ons. Although set up in the Employee Recurring Deductions/Add-ons screen, add-ons that are allocated by time card are auto-generated by the check calculation and are not included in this calculation.
