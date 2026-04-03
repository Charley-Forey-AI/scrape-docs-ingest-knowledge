---
title: "New Employee | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/inquiries-overview/employees/new-employee"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/inquiries-overview/employees/new-employee"
---

# New Employee

Use this window to set up basic information for new employees. The information you enter appears in the Employee Main Properties screen for the employee.
Fields/ButtonsDescriptions
Employee codeEnter a unique employee code in this field. If the Auto-number employee codes
 checkbox is selected on the Payroll Installation > Properties tab, Spectrum automatically generates new employee codes
 based on the next employee number (and mask, if applicable).

NameEnter the employee name as it should appear on paychecks, or select the drill-down button to display the Employee Name Detail window.

Cost centerIf cost centers are enabled for the current company, enter the cost center associated with this employee.
Legal nameIf different from the employee name entered above, enter the employee's full legal name, up to 200 characters.
New hire information
Hire dateEnter the employee's hire date.
Social security #Enter the employee's social security #.
 If
 Payroll reporting is set to 'Canada' in [Payroll Installation - Properties](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties), the
 number entered here is formatted to comply with Canadian mask
 guidelines, including a single space between the 3rd and 4th digits and a
 single space between the 6th and 7th digits.
Note: The social security # will not print on reports.

DepartmentEnter the employee's home department code, or press F4 or double-click on this field to search and select. This will be the default code during Pre-Time Card Entry and Time Card Entry. Entry in this field is required.

Worker's compensationEnter a valid Worker's Compensation Class Code for this employee, or press F4 or double-click on this field to select from a list of available codes. Entry in this field is required.
During Pre-Time Card Entry and Time Card Entry, the worker's compensation code
 will default first from the Phase Maintenance; if no
 code is defined for the phase, the code will default from the Job
 Maintenance screen; if no code is defined for the job, the
 worker's compensation code will default from Payroll Department
 Expense Maintenance; if no information is recorded there, the
 code will default from the Wage Code File Maintenance
 screen; if no information is recorded there, then the code defaults from
 this field.

StatusEnter the employee's employment status code, or press F4 or double-click on this
 field to select a status code from the Search Status
 Codes window.
Time card lines can be entered in Time Card Entry or Pre-Time Card Entry for
 employees with status codes that have status type of
 Active.

Pay rate information
Pay typeSelect the employee's pay type from the drop-down menu. Options include:
 Hourly, Salary,
 Commission, and Salary + OT.
For employees with a pay type of Salary, the system doesn't allow overtime pay. If overtime pay should be allowed, optional overtime salary must be authorized here.
For full-time commission employees in Spectrum:

- Set up the employee with a pay type of Salary.

- Enter a 0 (zero) for the salary and hourly rates.

- During Payroll Time Card Entry, enter the pay type as Regular. The hours
 entered at that time will be used in calculating worker's compensation. When
 the cursor is at the Rate column, enter the
 commission amount. The system will not try to calculate the hours
 against this amount.

FrequencySelect the employee's pay frequency from the drop-down menu.
Hourly rateEnter the hourly rate based on the Pay type specified above. Use the Human Resources > Rate Management screen to manage employee pay
 rates.Important: If the Pay Type is set to Hourly, don't leave the Hourly Rate field blank. Instead, enter 0.00.

Tax information
FederalEnter a federal filing status for the employee, the number of federal exemptions (if applicable), and any income tax overrides (% of gross, fixed amount, add-on) and amounts.
Resident stateEnter the employee's state of residence and filing status in their state of residence, the number of exemptions in their state of residence (if applicable), and any new W-4 information or income tax overrides (% of gross, fixed amount, add-on) and amounts.
Default exemptions for state, county and localEnter the number of default exemptions for state, county and local jurisdictions (if applicable).
