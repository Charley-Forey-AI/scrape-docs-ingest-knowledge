---
title: "Employee Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/inquiries-overview/employees/employee-properties/employee-main-properties/employee-main-properties---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/inquiries-overview/employees/employee-properties/employee-main-properties/employee-main-properties---field-descriptions"
---

# Employee Main Properties - Field Descriptions

Use the table below for reference when viewing the Employee Main Properties screen. To edit any information, select the Edit button.
FieldsDescriptions
Employee codeThe selected employee code and name displays.
The Employee Name Detail window allows you to edit the selected employee's first, middle, and last names. This window automatically populates the name component fields (First, Middle, Last) from the employee name on the main screen using standard rules. In addition, you can use the corresponding paging screen in Payroll Error Recovery to maintain these fields.

Legal nameEnter the employee's full legal name, if different from the name above, up to 200 characters.
If the employee name does differ from the legal name, verify these entries are correct and select Verify to continue.

Alpha referenceDefaults to the first eight characters of the employee's last name. To accept this default, press Enter. Otherwise, enter the desired alphabetic reference name.
If cost centers are enabled for the current company
Cost centerEnter a cost center to assign to this employee.
Entity affiliationLinks indicating the authorized entity (or the entity count when there is more than one authorized entity). Select one of the available links to open the Employee Entities screen.
Employment info
TitleIf wage codes are used, the wage code description defaults as the employee's title. Press Enter to accept the default, or enter the desired title.
OccupationEnter the employee's occupation, or press F4 or double-click this field to select from a list of valid occupations.
TradeEnter the employee's trade, or press F4 or double-click this field to select from a list of valid trades.
SupervisorEnter the supervisor code for this employee. Press F4 or double-click this field to select from a list of available supervisor codes.
EEO classificationEnter the EEO classification code for this employee. This must be a valid code previously defined in EEO Classification Maintenance. Press F4 or double-click this field to select from a list of available EEO classification codes.
Work classSelect the union work class code for this employee from the drop-down menu. If you leave this field blank, the Employee Utilization Report indicates 'No Work Class'.
LocationEnter the employee's location (for example: Building 23, Manhattan office, and so forth).
If the Human Resources module is installed, you can press F4 or double-click this field to select a location from the Search Locations window. Additionally, this field's information will default for all new HR files. If you make changes, they do not automatically update the HR module.

Time card defaults
DepartmentEnter the employee's home department code, or press F4 or double-click this field to search and select. This will be the default code during Pre-Time Card Entry and Time Card Entry. Entry required.
Worker's compensationEnter a valid Worker's Compensation Class Code for this employee, or press F4 or double-click this field to select from a list of available codes. Entry required.
Select the Always use this worker's compensation code on time card? checkbox to always assign this worker's compensation code from Employees. By selecting this checkbox, this setting will override all other worker's compensation code hierarchies.
Worker's Compensation Code Hierarchy:

- During Pre-Time Card Entry and Time Card Entry, the worker's compensation code will default first from the Phase Maintenance.

- If no code is defined for the phase, the code will default from the Job Maintenance screen.

- If no code is defined for the job, the worker's compensation code will default from Payroll Department Expense Maintenance.

- If no information is recorded there, the code will default from the Wage Code File Maintenance screen.

- If no information is recorded there, then the code defaults from this field.

UnionAdd or edit the employee's standard union code or press F4 or double-click this field to select from a list of available union codes. This will be the default code Pre-Time Card Entry and Time Card Entry for this employee. If this is a non-union employee, press Enter to leave the field blank. Note: Does not display if the Payroll Installation option for Default rate table is set to Pay groups.

Wage codeEnter the wage code for this union employee, if applicable, or press F4 or double-click this field to select from a list of available wage codes. This will be the default code during Pre-Time Card Entry and Time Card Entry. If this is a non-union employee, or if wage codes are not being used, press Enter to leave the field blank. Note: Does not display if the Payroll Installation option for Default rate table is set to Pay groups.

Pay levelEnter the pay level code (1-9) from the wage or union file. This will be the default level during Pre-Time Card Entry and Time Card Entry. Press F4 to search and select from a list of valid union rate codes.
Last worked onEnter the last job code and equipment code the employee worked on. These codes are maintained by the system based on Time Card Entry. The job name and equipment name and latest work date (if available) display to the right of their respective fields.
You can enter optional company codes for the specified job and equipment codes. If you specify company codes, the job code and equipment codes are validated with the company codes. If you don't specify company codes, non-valid job and equipment codes are allowed.

AttributesAdd preset contact attributes to this employee. Double-click this field to open the Build Contract Attributes List window to select and/or deselect contact attributes.
Allows assignment of one, multiple, or ALL preset attributes to an employee. This classification schema will serve as a flexible classification tool, for use in grouping employees when searching for contacts.

Employee Status
Status, Status typeSelect a status for this employee. Status codes are configured on the [Employee Status Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/employee-status-code-maintenance) screen.

- New hires that are onboarded from Trimble Construction One will have a status of 'In Review' by default. Review the employee details and make any necessary changes, and then change the status to 'Active'.

- Deceased or terminated employees' records are always kept on file until the end of the year to allow preparation of required tax forms. It is recommended that these records remain on file for three to five years. This allows for prior-year-date-sensitive reports (such as unemployment reports, and so forth) to continue to include those figures.

- If the Purge employees at year end option is checked for the selected record, clear this option and instead use the [Delete Employee from Current Company](/en/spectrum/spectrum/accounting/payroll/utilities-overview/delete-employee-from-current-company) utility to purge employees.

Health coverageUse this drop-down to identify this employee as Full time, Part time, Unassigned or Variable hour.
Supports compliance with the Patient Protections and Affordable Care Act. Under this act, employers must determine for each employee whether health coverage must be provided (based on whether the employee is 'full time' or 'part time').
For more information, refer to the [Average Hours Report](/en/spectrum/spectrum/accounting/payroll/payroll-reports/average-hours-report), which displays one line per employee, totaling the hours for selected pay types over a specified date range and dividing the total to present the average hours/week.

Employer dentalFrom the dropdown, select the code corresponding to the level of dental care insurance provided to the employee.
Milestones
Date fieldsEnter the employee's Original hire, Latest rehire, and/orLatest termination date, as applicable. Enter the employee's Last review date and the number of months for their Review cycle.
Hire Date HistorySelect to display the Employee Hire Date History window (for reference purposes only). Rehire and termination dates that have been added in the main screen will automatically appear in this window when you select Save on the main screen, and no additional changes will be allowed in this window.If you select this button before entering an termination date, New/Edit/Delete buttons appear at the top of the Employee Hire Date History window and you can use these to enter a date, type, and a Comment for record keeping purposes.

Employee imageUse the Add button to upload an image file of the Employee that will then display as a thumbnail on the related InfoBar throughout the system. Select the Picture drop-down in the InfoBar to hide the image.
