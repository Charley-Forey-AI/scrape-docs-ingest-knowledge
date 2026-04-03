---
title: "Layoff Check Entry Window - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/layoff-check-entry/layoff-check-entry-window/layoff-check-entry-window---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/layoff-check-entry/layoff-check-entry-window/layoff-check-entry-window---field-descriptions"
---

# Layoff Check Entry Window - Field Descriptions

Use the table below for reference when completing the fields on this screen.
FieldsDescriptions
PreviousThe data from the previous timecard displays. No entry is allowed.
EmployeeEnter the employee code for whom time card information will be entered.
Pay typeAdd or edit a pay type for this time card line. If the pay type is an
 incentive pay type, the character designated in the Payroll
 Installation screen Incentive pay code
 field must appear before the Regular, Overtime, or Double time
 character.
Press F4 or
 double-click on this field to display valid pay types. Within this window,
 two other windows are available to access the add-on or deduction
 information. If you enter a retro pay (RP) pay type, the Retro
 Pay Method window displays. If RP (retro pay) type is being
 auto-calculated then lines are only created for the specified job. Select
 Manual entry to
 return to the entry screen or select Automatic retro pay to
 open the retro pay screen.
Enter U to track all
 unpaid employee time. This pay type reflects hours that do not affect the
 General Ledger. This pay type is strictly for record-keeping purposes in
 conjunction with the Human Resources module for tracking unpaid time, such
 as unpaid medical absence, non-job 'comp' time, and so forth. When this pay
 type is specified, the cursor proceeds to the following fields only:
 Company code,
 Department,
 Day, Hours, Batch, and Message. The hours entered
 with the U pay
 type are ignored by the software during the check and layoff check
 calculations.
Note: Employee Deductions with tax affects do not reduce the
 subject-to earnings correctly if there is a mixture of taxable and exempt
 earnings.Instead of using Pay types 1, 2, 3 or SA, use a new add-on code
 with appropriate tax effects.

Company code
DepartmentAdd or edit the department code, or double-click on this field to select from a list of available department codes.
The Operator will be permitted to change the Department code only if the record is not already associated with a Work Order labor billing transaction.

JobEnter the job number, or double-click on this field to select from a list of available jobs.
PhaseAdd or edit the phase number, or double-click on this field to view a list of available phases.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Cost typeEnter the cost type for this time card line. A lookup window is available for viewing valid cost types.Note: If a new EU line is for a job, then the cost type is assigned based on
 the following hierarchy: first, the system checks the G/L account in the
 Payroll department to see if it has a cost type specified; if blank then the
 system checks the Equipment Control Installation for
 a cost type; if blank, then the import cost type is used.

EquipmentAdd or edit the equipment code, if applicable, or double-click on this field to select from a list of available equipment codes. The equipment code field only displays if an equipment department is entered and Equipment Control is installed on the software. No entry is required if the equipment status is Retired.
The equipment rates (Full or Operating) have been incorporated into the Time
 Card Entry and Pre-Time Card Entry
 screens. There is an installation prompt that gives you the option of
 defaulting the full rate or the operating rate during Time Card Entry. In
 Time Card Entry, the F or O will display just before
 the equipment rate, and you can press F4 or double-click on this
 field to change the rate, if desired. Once changed, the rate type will
 auto-repeat. This allows you to use the Full rate, but for overtime
 situations, you may want to switch to the lower operating rate. Or if you
 are using the new stand-by rates for days or weeks put on the job, then you
 can just use the operating rate exclusively to record the operating hours.
Spectrum allows multiple cost types for equipment usage transactions when
 using ER pay types. The software will look at the
 Payroll department General Ledger code and the corresponding cost type
 attached to that G/L code. If it is blank, then it will use the cost type
 specified in the Equipment Control Installation.
 Previously, the software just used the cost type from the
 Equipment Control Installation screen.

CertifiedSelect this checkbox if this job is certified. This field will default from
 the Job Cost > Phase File Maintenance > Properties window when Yes or
 No is specified. Only the certified override in
 Payroll takes precedence over the setup in the phase file in Job Cost.
If the Department is a 'Direct work order cost' type, this field will be unavailable.

DateThe cursor stops at this field for all pay types, including Miscellaneous, Special Amount, and OTHER (1,2,3) pay types. It also prompts for day when entering an add-on for a job. This optional information will then be stored permanently in the time card history file upon update of the Payroll cycle.
If the Use full date in time
 card entry checkbox on the Payroll
 Installation screen is selected:

- Enter the date (for example, for hours that the employee worked on the 14th, enter "14"). To type the complete date, press the window function key.

If the department entered previously does not allow work in process for the entered pay type, then the job, phase and cost type fields will be skipped and no entry will be allowed. If the department code and pay type, indicate that this is a work in process account, then a valid job, phase and cost type must be entered.
If the Use full date in time
 card entry checkbox on the Payroll
 Installation is not selected:

- If this is a certified job and hours are required by day, enter the appropriate day of the week (1 through 7).

- If it is not a certified job and day-by-day reporting is not necessary, press
 Enter to accept the default day zero and
 group all the hours for the pay cycle on one line.

Wage codeIf the Wage codes / union option is not selected on the
 Payroll Installation screen, this field will not
 display.
The rate is determined by the wage/union code combined together with the rate
 level. The rate level defaults from the phase file, the job file or the
 employee file, unless the Default pay rate field is set to Employee pay rate
 or Higher of the two rates (and the employee rate is higher) in the
 Payroll Installation screen. View the [Wage/Union Code Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/wageunion-code-hierarchy).
A window is available in the pay level field within the wage window that displays the default pay rates for the pay group code.
You may also press F4 or double-click on this field to
 enter unions, pay levels, and pay groups if the Payroll
 Installation is set to use pay groups.

Union codeAdd or edit the union code for this employee, or press Enter to accept the current union code. An alert message will display if the union code entered has an Inactive status, but you will be allowed to continue entry.
Rate levelAdd or edit the rate level number (1-9), or press F4  to select from a list of available rate levels for this time card line.
When adding a time card record assigned to a 'Direct work order cost'
 department, this fields will default to the corresponding fields in Work Order > Site File Maintenance.
If a company code other than the current company is specified, the rate level will default from the Site associated with the work order in the newly-selected company.

Work stateAdd or edit the work state tax code for this time card line, or press F4 to select from a list of available states.
When adding a time card record assigned to a job, the Work state field defaults according to the following hierarchy:

- Job Phases

- Jobs

- Employees

When adding a time card record assigned to a 'Direct work order cost'
 department, this field will default from the corresponding field in Work Order > Site File Maintenance. If the site does not have a work state, then the work state
 will default from the employee Perm work state field in Employee File Maintenance > New/Edit Employee code > Taxes tab. If the Perm work state field for an employee is blank,
 then the work state will default from the employee Resident state field in
 the Taxes tab.
If a company code other than the current company is specified, the work state will default from the site associated with the work order in the newly-selected company, unless the code is not valid in the company. If the code is not valid, the employee's default code will be assigned.
If related taxes have been set up for the employee's work state tax code,
 select the Related Taxes button to view the related tax codes and tax
 instructions.

Work countyAdd or edit the county tax code for this time card line, if applicable, or press F4to select from a list of available states.
When adding a time card record assigned to a 'Direct work order cost'
 department, this fields will default to the corresponding fields in Work Order > Site File Maintenance.
If a company code other than the current company is specified, the work state will default from the Site associated with the work order in the newly-selected company, unless the code is not valid in the company. If the code is not valid, the employee's default code will be assigned.
If related taxes have been set up for the employee's work county tax code,
 select the Related Taxes button to view the related tax codes and tax
 instructions.

Work localAdd or edit the local tax code for this time card line, or press F4 to select from a list
 of available states.
When adding a time card record assigned to a 'Direct work order cost'
 department, this fields will default to the corresponding fields in Work Order > Site File Maintenance.
If a company code other than the current company is specified, the work state will default from the Site associated with the work order in the newly-selected company, unless the code is not valid in the company. If the code is not valid, the employee's default code will be assigned.
If related taxes have been set up for the employee's work local tax code,
 select the Related Taxes button to view the related tax codes and tax
 instructions.

Work compAdd or edit a valid Worker's Compensation Class Code for this employee, or
 press F4 to select
 from a list of available worker's compensation codes.
If the 'Always use this worker's comp code on time card?" checkbox is selected in Employees, the worker's compensation code for that employee will automatically default in this field and no changes will be allowed.
When adding a time card record assigned to a 'Direct work order cost'
 department, this fields will default to the corresponding fields in Work Order > Site File Maintenance.
If a company code other than the current company is specified, the work state will default from the Site associated with the work order in the newly-selected company, unless the code is not valid in the company. If the code is not valid, the employee's default code will be assigned.

CrewAdd or edit a crew code for this employee (if applicable), or press F4 or double-click on this
 field to select from a list of available crew codes. The software will
 validate that the crew code entered is from the same company in which the
 job is set up.
MessageEnter a descriptive message, or make changed to an existing message for this time card line.
Check
SequenceSequence numbers are assigned and maintained by the software. The check type and check number information then defaults based on the sequence number.
TypeThe check type defaults based on the sequence number.
NumberThe check number defaults based on the sequence number entered.
Regular hoursThe number of regular hours worked during this pay period displays.
OvertimeThe number of overtime hours worked during this pay period displays.

Double timeThe number of double time hours worked during this pay period displays.

BatchThe batch code generally defaults to the operator ID. Batch coding allows an individual's work-in-progress data to be identified and tracked in separate groups.
Employee
RateOptions when adding or editing the employee's pay rate:

1. Press Enter to accept the default pay rate for this employee. The pay rate will default based on the work date. If the work date is changed, the software will perform a pay rate recalculation.

1. Manually enter the rate amount. If this is a salaried employee, enter the
 salary amount; if this is an hourly employee, enter the pay rate per
 hour, or press F4 or double-click on this field for quick entry
 rates.If there is no rate for pay types M, SR, or SA already set up in Employees –Financials, the software will stop at this field and allow entry of the rate for those pay types.
If the pay type for this line is ER, EO, ED, or EU, the equipment rate will display on a second line. This rate defaults from the equipment file.
After hours have been entered using the Quick Time Card Entry window at the hours field, an additional window is available which allows the user to override the regular and overtime rates before the quick time card lines are created. This window will open automatically when the Quick Time Card Entry window is used and the default regular pay rate is overwritten.

1. For pay groups, see the [Pay Group Rate Default Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-group-rate-default-hierarchy) topic. Otherwise, enter the desired pay rate. If this is an add-on entry, enter the amount to be added on this line of the time card entry.

Billing codeIf the time card is for a job, the T+M labor billing code and description display. If the time card is for a work order the WO labor billing code and description display.
Changes are allowed in this field and a drop-down search window lets you select a different valid code; the employee billing rate will adjust accordingly.

Billing rateThe employee's billing rate displays, no entry is allowed. This field displays
 regardless of whether or not the Show pre-time card pay
 rates checkbox is selected on the Payroll Installation > Properties tab.
The software will determine whether site-specific or contract-specific labor billing rates are assigned to the labor transaction. The billing rate will default based on the following hierarchy:

1. The contract-specific billing rate will default, if present.

1. If a contract-specific rate is not present, the site-specific rate will default.

1. If neither the contract-specific billing rate or site-specific rate are present, the customer specific rate will default.

1. If no override rates are present, the standard rate will default.

1. If no labor billing rates are present, the billing rate will be blank.For Time + Material jobs, the billing rate will default based on the bill code
 specified in Wage Code File Maintenance (and
 then Union File Maintenance) for the rate level
 of the phase as the highest priority. If the bill code is blank or if
 there is no phase override, then the existing hierarchy will be used
 to default the Time + Material rate.
If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.

HoursAdd or edit the number of hours worked, or press F4 or double-click on this field to display the [Quick Hours Entry](/en/spectrum/spectrum/accounting/payroll/data-entry/quick-hours-entry) window.
If this line is referencing an incentive pay type, then the Quick
 Hours Entry window opens automatically when you press
 Enter. After
 entering the regular, overtime, and/or double time hours, you can then enter
 the incentive pay amount and hourly rate, or press F4 or double-click on this
 field to display the Incentive Pay Calculation window
 and have the system calculate the incentive pay amount for you.

Equipment
RateEnter the equipment rate for this time card line, or press F4 or double-click on this field to change the rate type.
This field only displays for equipment time card lines.
Hierarchy for Charge Rates
If applicable, this rate information will default the amount set up in the Job-Specific Equipment Charge Rates screen. If no job-specific record is found (or rate is blank), the system will determine if this job is a sub job of a master job and use the job-specific rate from the master job. If there is no job-specific rate for the job or master job, the system will read for the standard job rate of the equipment code.

Billing codeThe T+M equipment billing code and description display. Changes are allowed in this field and a drop-down search window lets you select a different valid code; the equipment billing rate will adjust accordingly.
Billing rateWhen the Pay type is
 ER, EO,
 ED, or EU the software will
 prompt for the (company) equipment billing rate. This field only displays if
 an equipment department is entered, and Equipment Control is installed on
 the software. In the 'New' window it will default to the equipment rental
 rate when the work order is Time & Material. If an equipment billing
 rate is specified, the Payroll Update will store this default equipment
 billing rate in the Work Order cost history table.
Repeat entry until all hours for this job have been entered. When entry is complete, select OK until the fields clear. Enter a new job number and repeat until time cards have been entered for all employees on all jobs.
If this is a sub-job billed from a master job, the software will read for
 job-specific setup rates for the master job, and if none are found use
 standard settings. If this is a sub-job billed at the sub-job level, the
 software will read for job-specific setup rates for the sub-job first, and
 if billing rates are not found then the master job, and if none are found
 there use standard settings.

HoursIf the pay type for this line is ER, EO, ED, or EU, the number of employee hours will display on a second line as the number of equipment hours. The equipment hours may be changed by arrowing back from the "rate" field. This field displays only if an equipment department is entered and Equipment Control is installed on the software.
If this time card line originated in Work Order > Labor Hours Entry, or has already been selected for billing, this field will be
 display-only.

Related information

- [Pay Type Definitions](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions)

- [Retro Pay](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/retro-pay)
