---
title: "Layoff Check Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/layoff-check-entry/layoff-check-entry---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/layoff-check-entry/layoff-check-entry---field-descriptions"
---

# Layoff Check Entry - Field Descriptions

Use the table below for reference when completing the fields on the Layoff Check or Layoff Cheque screen.
Fields/ButtonsDescriptions
Employee codeEnter the employee code for whom you want to add or edit time card lines.
Select the lookup icon to view the employee's employment (pay rate, hire date, department, etc.), mailing address, and tax information, and send an email message to the current employee.

Pay rate/typeThe pay rate is effective as of the current Payroll processing date.
Check dateAdd or edit the check date. If this field is left blank, any rate scheduled pay rate changes are determined based on the current Payroll processing date.
Period endAdd or edit the period ending date.
Period start dateEntries in this optional field will display on pay stubs to make it easier for employees to verify that they have been paid properly. The pay stub also displays the sum of all hours worked on this check for added convenience and to comply with CA and NY legislation.

- If the Utilize pay cycle calendar? option is selected in Payroll Installation, and the specified Period end date is present in the pay cycle calendar, then this field defaults to one day later than the previous period end date.

- If the Require period start date on payroll cycle? option is selected in Payroll Installation, a date must be entered in this field.

Bank accountThis field is visible only if Cash Management is installed and the Post payroll transactions checkbox is selected in the Cash Management Installation screen.
Enter a bank account or double-click in this field to select from a list of available bank accounts.
Note: The application prevents any accounts (credit card or other) that are not bank accounts from being entered into this field.

- If a layoff check already exists for the entered employee, this field defaults to the current bank account on the layoff time card lines.

- If cost centers are being used and a Payroll bank account is specified; then this field is set from the cost center Payroll bank account and cannot be changed.

- If cost centers are being used and you enter a bank account, it must be valid for the cost center, if not system will return to the cost center field.

- If cost centers are NOT being used, this field defaults to the Payroll account from Cash Management.

Check #Add or edit the check number for this pay period. If time card lines have already been entered for this employee, press Enter to see the existing check number.
Batch codeBatch coding allows an individual's work-in-progress data to be identified and tracked in separate groups. The batch code usually defaults to the operator ID.
TotalsThe total hours display from the pay type column, broken down by: regular, overtime, and double time. Any equipment hours and the total extension also displays.
Transfer from Pre-Time Card Entry buttonWhile preparing a layoff check, the Payroll Manager sometimes needs to include time cards for work already recorded in Pre-Time Card Entry. In this case, the operator can use this button to review pre-time card records and 'remove' them from the pre-time card screen and then 'add' them into the Layoff Check Entry screen.
Safeguards ensure that only time cards from 'Regular' checks can be transferred (not from manual or void checks), and cost center security will prevents users from manipulating unauthorized time cards.
If multiple check sequences of pre-time cards exist, the transfer will include the time cards from the first check sequence and the proceed to the next check sequence.

CalculateIf you are reviewing lines for a salaried employee, the Calculate button displays.
Select this button and choose Yes to redistribute the salaried pay evenly among all the hours entered, or select No to leave the lines as is.
Tax Adjustments Calculations
If [Tax Adjustment Codes](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance/newedit-income-tax-details---properties-tab/newedit-tax-table---other-taxes/tax-adjustment-code-maintenance) are being used, as the income tax of each code is being calculated the system will read for adjustment codes assigned to the tax codes and increase or decrease withholding based on the adjustment type. This calculation is performed before dividing the annualized income tax deduction amount back to the current period.
If multiple adjustment codes are assigned to the Tax Table Code, the system calculates each adjustment separately in the sequence order (in order to sum up all tax adjustments, then add that total to the income tax amount).
This functionality is provided because Ontario's 'Tax Reduction' calculation includes the adjustment amount computed for Ontario Surtax.

Layoff Checks in ProgressSelect to display the Search Layoff Checks window where you can see a list of the layoff checks in progress.
AL OT ExemptSelect to open the Alabama Overtime Pay Exemption Utility window, which is used to create time card lines which effectively exempt the overtime wages for this employee's layoff check. For more information, see [Alabama Overtime Pay Exemption](/en/spectrum/spectrum/accounting/payroll/data-entry/alabama-overtime-pay-exemption).
