---
title: "New T4 Slip - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/t4-slip-maintenance/new-t4-slip/new-t4-slip---field-descriptions"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/t4-slip-maintenance/new-t4-slip/new-t4-slip---field-descriptions"
---

# New T4 Slip - Field Descriptions

Use the table below for reference when viewing the T4 Slip information. To edit any fields, select the Edit button.
FieldsDescriptions
EntityDisplays only if cost centers are being used and entity tracking is also enabled in the current company.
After entering or selecting an entity, a list of all employees currently receiving a T4 Slip is shown on the main screen for tax review purposes, and cost center security prevents editing employee T4s that you don't have authorization to access.

Employee codeEnter an employee code or press F4 and select one from the available Search Employees window.
Payer tax ID numberWhen adding a new record, the software auto-assigns the tax ID number from the employee's Federal tax code from [Employee Tax Setup](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-tax-setup). If this is blank, the application uses the Default federal tax code for new employee from Payroll Installation.
If no number is present, enter the payer tax ID.

Form #Defaults to '1' if this is the first T4 Slip for this employee. Numbers increase incrementally by 1. This is for use when multiple forms must be issued to the employee for the same Province.
Tax codeTax codes reflect any employment commissions, taxable allowances and benefits, deductible amounts, fisher's income, and other entries if they apply.
Province of employmentDefaults to the first two characters of the Tax code.
Social insurance #
(SIN)
When adding a new record, this number defaults from the Employees screen for the specified employee code. Spaces display after the third and sixth characters. Make sure the SIN and name you enter on the T4 slip are the same as on the employee's SIN card. If the employee doesn't have a SIN, enter nine zeros.
Last name
First name
Middle initial
When adding a new record, this information defaults from the Employees screen for the specified employee code. If the employee has more than one middle initial, enter the employee's first name followed by the initials in the First name field.
Address 1
Address 2
City
Province
Postal code
Country
When adding a new record, this information defaults from the Employees screen for the specified employee code.
CPP/QPP exempt?CPP = Canadian Pension Plan, QPP = Quebec Pension Plan.
EI exempt?EI - Employment Insurance.
PPIP exempt?PPIP = Provincial Parental Insurance Plan
Dental benefit codeThe code corresponding to the level of dental care insurance provided to the employee during the tax year.
Employment codeThis is a 2-character alphanumeric code. If employment code 11, 12, 13, or 17 is entered, do not complete box 14 (employment income). Enter the appropriate code in this box if one of the following situations applies. Otherwise, leave it blank.CodesDescriptions
11Placement of employment agency workers
12Taxi drivers or drivers of other passenger-carrying vehicles
13Barbers or hairdressers
14Withdrawal from a prescribed salary deferral arrangement plan
15Seasonal Agricultural Workers Program
16Detached employee - Social Security agreement
17Fishers - Self-employed

Employer CPP and 2nd CPP contributions Enter values here; they don't appear on the form but are used in the XML file.
Employer EI premiumsEnter a value here; it doesn't appear on the form but is used in the XML file.
Employment income 14Enter the total income before taxes. Include all salary, wages, bonuses, vacation pay, tips, honorariums, director's fees, and management fees.
Do not include retiring allowances on the T4 Slip.
 The [Build T4 Slips](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/build-t4-slips) includes the total of box 20 (Pension Plan) in box 14 (Employment Income) for each form.

CPP contributions 16 and 16AEnter any amounts deducted from the employee for contributions to the Canada Pension Plan.
Do not report the employer's share of CPP on the T4 Slip.

QPP contributions 17 and 17AEnter any amounts deducted from the employee for contributions to the Quebec Pension Plan.
Do not report the employer's share of QPP on the T4 Slip.
Note: The T4 build doesn't support QPP. You must manually enter any applicable values.

El premiums 18Enter the amount of Employee Insurance premiums deducted from the employee's earnings.
Do not report the employer's share of the EI premiums on the T4 Slip.

RPP contributions 20Enter the amount of contributions to a registered contribution plan, including any past service contributions.
Pension adjustment 52Enter, in dollars only, the amount of the employee's pension adjustment (PA) for the year.
PPIP premiums 55Enter the provincial parental insurance plan (PPIP) premiums deducted for employees working in Quebec.
Income tax deducted 22Enter the total income tax deducted from the employee's remuneration and retiring allowances.
EI earnings 24Enter the total amount of insurable earnings used to calculate the employee's EI premiums, up to the maximum insurable earnings for the year.
CPP/QPP earnings 26Enter the total amount used to calculate the employee's CPP or QPP contributions, up to the maximum pensionable earnings for the year.
Union dues 44Use this box only if it is agreed that the union will not issue receipts for union dues to employees.
Charitable donations 46Enter the amount deducted from the employee's earnings for donations to qualified donation recipients in Canada.
RPP or DPSP registration 50RPP = Register Pension Plan
PPIP earnings 56For employees working in Quebec, enter the total amount used to calculate the employee's PPIP premiums.
Other information
Code 1 / Amount
Code 2 / Amount
Use these boxes to enter codes and amounts that relate to employment commissions, taxable allowances and benefits, deductible amounts, fisher's income and other entries if they apply. If more than six codes apply to the same employee, use an additional T4 Slip.
