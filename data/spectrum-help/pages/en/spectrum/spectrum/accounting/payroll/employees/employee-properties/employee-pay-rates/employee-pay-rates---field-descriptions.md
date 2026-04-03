---
title: "Employee Pay Rates - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-pay-rates/employee-pay-rates---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-pay-rates/employee-pay-rates---field-descriptions"
---

# Employee Pay Rates - Field Descriptions

A reference for completing the fields on the Employee Pay Rates screen.
Fields/ButtonsDescriptions
Current pay rateThe pay type, frequency, standard hours, salary rate, hourly rate, and annualized rate for the selected employee display in this section.
When a new rate revision is added, and if the new rate is current, the calculated totals in this section update.
Important: If the Pay Type is set to Hourly, don't leave the Hourly Rate field blank. Instead, enter 0.00.

Pay typeThe pay type always defaults to Regular when adding a new entry. Typically, employees are Hourly or Salary, but Overtime and Commission are also available.

- Note that salaried employees may not receive overtime or double time pay unless the employee's pay type is Overtime salaried.

- If the pay type is an Incentive pay type, the special character designated in the Payroll Installation screen Incentive pay code field must appear before the Regular, Overtime, or Double time character.

For full-time commission employees in Spectrum:

- Set up the employee with a pay type of Salary.

- Enter 0 for the salary and hourly rates.

- During Time Card Entry, enter the pay type as Regular. The hours entered here will be used in calculating the worker's compensation. When the cursor is at the "rate" column, enter the commission amount. The system will not try to calculate hours against this amount.

Other rates and settings
Special pay rateEnter the special pay rate for this employee. The hourly pay rate recorded here defaults in Time Card Entry when the pay type SR is specified. In addition, in Work Order > Labor Hours Entry, this rate defaults when pay type SR is specified.
If the employee uses a Salary or Salary + OT pay type, the Special Pay Rate does not apply because the rate does not default into Time Card Entry.

Special pay amountEnter the special pay amount for this employee. The lump sum pay amount recorded here defaults in Time Card Entry when the pay type SA is specified.
Miscellaneous amountEnter the employee's miscellaneous allowance amount. The lump sum pay amount recorded here defaults in Time Card Entry when the pay type M is specified.
Employer benefitEnter the hourly amount of the Health & Welfare credit for this employee. If the Calculate actual pension benefits for the Davis-Bacon / Prevailing wage employer benefit credit? checkbox is selected in the Payroll Installation > Defaults screen, then this amount will be the sum of the Health & Welfare credit plus any add-ons that have been flagged to be computed as part of the Davis-Bacon and Prevailing Wage benefit (as set up in the Deduction / Add-on Code Maintenance > Add-ons window).
Billing codeNote: Used only for Time + Materials jobs. If the Time + Materials module is not installed, this field doesn't display.
Enter the employee's billing code. Press F4 or double-click on this field to select from a list of available billing codes.
Part-time?Select this checkbox if the employee is a part-time employee.
Apprentice program?This checkbox is applicable for those using the AASHTOWare XML electronic reporting feature, to allow users to record apprentice information.
When selected, two additional fields display, prompting for the apprentice ID# (required) and the Wage % (optional). This data will be written to the XML file.

Post in summary to job and equipment history (confidential employee)?Note: Displays only if the current company is NOT a Confidential Payroll company.
Select to suppress the employee name in Job Cost History and Equipment Cost History as the Payroll Update records labor cost.
Also suppress employee's hours in job and equipment history?Note: Displays only if the current company is NOT a Confidential Payroll company.
Select to omit the corresponding job and equipment cost hours in order to further reduce access to sensitive salary information.
Pay group burdenNote: Displays only if the Payroll Installation > Default rate table is set to Pay groups.
Enter a pay group burden percentage in this field.
Rate adjustmentNote: Displays only if the Payroll Installation > Default rate table is set to Pay groups.
Enter a pay rate adjustment percentage in this field for a specified pay group.
