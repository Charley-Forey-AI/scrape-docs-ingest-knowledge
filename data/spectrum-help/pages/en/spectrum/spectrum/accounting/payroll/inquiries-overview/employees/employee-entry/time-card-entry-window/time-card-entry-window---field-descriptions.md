---
title: "Time Card Entry Window - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/inquiries-overview/employees/employee-entry/time-card-entry-window/time-card-entry-window---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/inquiries-overview/employees/employee-entry/time-card-entry-window/time-card-entry-window---field-descriptions"
---

# Time Card Entry Window - Field Descriptions

Below is a list of all fields that may display on this window, depending upon the pay type and cost type settings.
Fields
Descriptions

Previous
The data from the previous timecard
 displays. No entry is allowed.
Employee
Enter the employee code for whom time
 card information will be entered. Press F4 or double-click on this
 field to select from a list of available employee codes, names, titles,
 supervisors, and unions. Note: If you access this window
 from the Time Card Entry by Job screen, no changes
 can be made to the employee code here. If cost center
 entities are being used, the software verifies that the employee is
 authorized for the entity identified during [Set Payroll Cycle](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/set-payroll-cycle).


Pay type
Enter a valid pay type; up to 10
 characters are allowed. The pay type always defaults to Regular when adding a
 new entry. Note that salaried employees may not receive overtime or double time
 pay unless the employee's pay type is Overtime salaried. If the pay type is an
 incentive pay type, the special character designated in the Payroll
 Installation screen Incentive pay code
 field must appear before the Regular, Overtime, or Double time character. Enter
 U to identify and process unpaid time. This pay type is
 strictly for record keeping purposes, allowing you to track unpaid time
 (such as unpaid medical absence, comp time, and so forth). These hours will
 not be included as part of paid hours to employees and will not affect the
 General Ledger. They cannot be charged to jobs. This pay type will not
 appear on any Payroll reports or inquiries, other than the Edit Listing and
 Time Card History Report.
Press F4 or double-click on this
 field to display valid pay types. Within this window, two other windows are
 available to access the add-on or deduction information. If you enter a
 retro pay (RP) pay type, the Retro Pay Method window
 displays. If RP (retro pay) type is being auto-calculated then lines are
 only created for the specified job. Select Manual entry to return to
 the entry screen or select Automatic retro pay to open the retro pay screen.
Note: If the Show pre-time card pay rates check
 box is not selected on the Payroll Installation > Properties tab, then the automatic retro pay option is disabled.

The purpose of the JX pay type is as a
 front-end to auto-create job cost transactions so that the user can enter
 the information for the job in one place, instead of two. The JX lines are
 not intended to be posted in the payroll update; instead, they are posted to
 history when the job cost transactions they create are posted. Therefore, no
 reports (for example, job distribution, labor distribution, and so forth)
 show these JX. The user receives a hard copy of transactions to the job when
 they run the job cost transactions listing and update. The costs for JX also
 post to G/L at this point, not during Payroll Update. The payroll update is
 intended to create the unposted job cost transactions in Job Cost Transaction Entry. The operator must then use Job Cost Transaction Report and
 Update to complete the process.

Company code
The company code will default into this
 field, but can be changed if desired.If the reporting
 currency of the current (payroll) company is different than the reporting
 currency of the destination company and the Multi-Currency module is
 present, validation will be provided to ensure that a valid currency code is
 assigned to the specified account and is the same as the reporting currency
 of the current company.

Department
The department code will determine
 which General Ledger account codes are used for posting payroll information to
 the General Ledger. Press Enter to accept the default department, or enter the department
 to which this time card line should be applied. If
 multi-company payroll is being used and a different company code was entered
 in the previous "cc:" field, the department entered here will be the expense
 department in the destination company. Verification is performed for the G/L
 account code referenced in the Department Expense
 Maintenance of the destination company to assure the account
 is valid, has the proper 'direct cost' setup in G/L Master File
 Maintenance.
You will be permitted
 to change the Department code only if the record is not already associated
 with a Work Order labor billing transaction.
Note: Two types of transactions can be entered in Time Card Entry: repairs to a
 piece of equipment, and usage of equipment on jobs. The repairs to equipment
 need to be posted to an equipment expense account (General Ledger
 Master File Maintenance Direct cost = Equipment cost not Job
 cost). Because it is an "Equipment" the user should be prompted for
 equipment code and cost category. Time is entered as "R" or "O" to charge
 the cost of labor for repairing the equipment. The other transaction is
 usage of equipment on jobs. This is posted to Direct cost = Job cost
 accounts using ER, EO, ED or EU pay types. The expense account per
 Department Expense Maintenance is debited and a
 contra expense account (set up in ECI – job rental revenue) is credited.
 This contra revenue account should be set up in the same section of the
 chart of accounts as the equipment repairs accounts, not the direct job cost
 accounts. Payroll Department for equipment repair
 (R,O, or D), should be set up as Direct cost = Equipment cost, the
 posting goes to the salary and wages account in that department
 (General Ledger Master File Maintenance Direct
 cost = Equipment cost). The Payroll department for the equipment usage
 (ER, EO, ED, EU) is a Direct cost = Job cost, and the posting goes to the
 equipment expense account in that department (General Ledger
 Master File Maintenance Direct cost = Job
 cost).

Job
Enter the job number, or press
 F4 or double-click
 on this field to select from a list of available jobs.
Phase
Add or edit the phase number, or press
 F4 or double-click
 on this field to view a list of available phases. No entry is required if the
 phase status is Complete. If this is a sub-job
 transaction set up on a master job, double-click on this field to search
 phases for the sub-job. This will allow you to easily select a phase set up
 on a master job, but not present on the sub-job. Spectrum will add a new
 phase to the sub job if the current job is a sub-job of a valid master job,
 the phase lengths of both jobs match, and the Phase + Cost type combination
 for the current job is valid and not 'Complete'.

Cost type
Enter the cost type for this time card
 line. This field will default from the Default labor cost type field
 in Job Cost Installation.If the
 cost type for the General Ledger account does not match the cost type
 entered here, an error message will display. Also, each cost type may be
 associated with one General Ledger account during cost type maintenance
 under the job cost system. If this is done, then the department General
 Ledger code must match the G/L code entered for the cost type.
If the previously-entered department is a direct
 equipment cost department (Direct cost = Equipment cost) or non-job (Direct = No direct cost),
 this field will be skipped.

Equipment
Add or edit the equipment code, if
 applicable, or press F4 or double-click on this field to select from a list of
 available equipment codes. The equipment code field only displays if an
 equipment department is entered and Equipment Control is installed on the
 software. No entry is required if the equipment status is Retired. The equipment rates (Full or Operating) have been
 incorporated into the Time Card Entry and
 Pre-Time Card Entry screens. There is an
 installation prompt that gives you the option of defaulting the full rate or
 the operating rate during Time Card Entry. In Time Card Entry, the
 F or O will display just before
 the equipment rate, and you can press F4 or double-click on this
 field to change the rate, if desired. Once changed, the rate type will
 auto-repeat. This allows you to use the Full rate, but for overtime
 situations, you may want to switch to the lower operating rate. Or if you
 are using the new stand-by rates for days or weeks put on the job, then you
 can just use the operating rate exclusively to record the operating hours.

Spectrum allows multiple cost types for equipment
 usage transactions when using ER pay types. The software will look at the
 Payroll department General Ledger code and the corresponding cost type
 attached to that G/L code. If it is blank, then it will use the cost type
 specified in the Euipment Control Installation.
 Previously, the software just used the cost type from the
 Euipment Control Installation screen.

Cost category
Enter a cost category code for the
 previously selected equipment type. If an inactive cost
 category is entered in this field, a warning displays, but does not prevent
 further data entry.
This field displays only if the
 Department
 field is set to use a department that is Direct cost = Equipment
 code. Department direct cost settings are set up and
 maintained in the  Department Expense Maintenance >  New/Edit Department window.
When adding a new time card,
 Spectrum will verify the assigned G/L account is not a restricted G/L
 account for this cost category.

- If no records are found for this cost category in
 the restrictions table, you will advance to the next column.

- If the cost category is found and the G/L account is
 not among the list of allowed accounts, and error message appears and you
 will not be able to proceed.

Eq. work order
Enter an equipment work order number, or double-click on this field or press F4 to select from a list of available equipment work orders.
If a closed work order is entered in this field, a warning displays, but does not prevent further data entry.
This field displays only if the Cost category field contains a cost category is set to
 require an equipment work order number or entry of an equipment work order
 is optional. This setting is maintained in the Equipment Control >  Cost Category Field / Maintenance screen's Data
 entry field. Please refer to the Equipment Control Help filed
 for more details.

Certified
The certified flag checkbox indicates
 whether or not this time card line should appear on a certified payroll report
 for this job.

- If day zero is entered, this field will be skipped.

- If the job is not a certified job, this checkbox
 will be clear. If the job is a certified job, the certification flag for
 this field defaults from the employee's master file; if a different
 setting is desired, arrow back to this field (for example, sometimes a
 project manager will charge time to a certified job, but should not
 appear on that job's Certified Payroll Report).

- If the Department is a 'Direct work order cost'
 type, this field will be unavailable.

Date
The cursor stops at this field for all
 pay types, including Miscellaneous, Special Amount, and OTHER (1,2,3) pay
 types. It also prompts for day when entering an add-on for a job. This optional
 information will then be stored permanently in the time card history file upon
 update of the Payroll cycle.If the department code and
 pay type indicate that this is a work in process account, then a valid job,
 phase and cost type must be entered. If it is not a certified job and
 day-by-day reporting is not necessary, press Enter to accept the default day
 zero and group all the hours for the pay cycle on one line.

Wage code
Press Enter to accept the default,
 or enter the wage code for this time card line. A lookup window is available
 for viewing or entering valid wage codes, union codes, and pay levels. Up to 10
 characters are allowed.If the Wage codes / union option
 is not selected on the Payroll Installation screen,
 this field will not display.
The rate is determined
 by the wage/union code combination together with the rate level. The rate
 level defaults from the phase file, the job file or the employee file,
 unless the Default pay
 rate field is set to Employee pay rate or
 Higher of the two
 rates (and the employee rate is higher) in the
 Payroll Installation screen. To view the
 wage/union codes default hierarchy, click [Wage/Union Code Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/wageunion-code-hierarchy).

Union code
Add or edit the employee's standard
 union code; up to 10 characters are allowed. This will be the default code
 Pre-Time Card Entry and Time Card Entry for this employee. If this is a non
 union employee, press Enter to leave the field blank.
Rate level
Add or edit the rate level number
 (1-9), or press F4 to
 select from a list of available rate levels for this time card line. When adding a time card record assigned to a 'Direct work
 order cost' department, this field will default to the corresponding field
 in Work Order > Site File Maintenance. If a company code other than the current company is
 specified, the rate level will default from the Site associated with the
 work order in the newly-selected company.

Work state
Add or edit the work state tax code for
 this time card line, or press F4 to select from a list of available states. If related taxes have been set up for the employee's work
 state tax code, click the Related Taxes
 button to view the related tax codes and tax instructions.

Work county
Add or edit the county tax code for
 this time card line, if applicable, or press F4 to select from a list of
 available states.When adding a time card record assigned
 to a 'Direct work order cost' department, this fields will default to the
 corresponding fields in Work Order > Site File Maintenance.
If a company code other than the
 current company is specified, the work state will default from the Site
 associated with the work order in the newly-selected company, unless the
 code is not valid in the company. If the code is not valid, the employee's
 default code will be assigned.
If related taxes
 have been set up for the employee's work county tax code, click the Related Taxes button to view the related
 tax codes and tax instructions.

Work local
Add or edit the local tax code for this
 time card line, or press F4 to select from a list of available states.When adding a time card record assigned to a 'Direct work
 order cost' department, this fields will default to the corresponding fields
 in Work Order > Site File Maintenance.
If a company code other than the
 current company is specified, the work state will default from the Site
 associated with the work order in the newly-selected company, unless the
 code is not valid in the company. If the code is not valid, the employee's
 default code will be assigned.
If related taxes
 have been set up for the employee's work local tax code, click the Related Taxes button to view the related
 tax codes and tax instructions.

Work comp
Add or edit a valid Worker's
 Compensation Class Code for this employee, or press F4 to select from a list of
 available worker's compensation codes. If the 'Always use
 this worker's comp code on time card?" checkbox is selected in Employees,
 the worker's compensation code for that employee will automatically default
 in this field and no changes will be allowed.
When
 adding a time card record assigned to a 'Direct work order cost' department,
 this fields will default to the corresponding fields in Work Order > Site File Maintenance.
If a company code other than the
 current company is specified, the work state will default from the Site
 associated with the work order in the newly-selected company, unless the
 code is not valid in the company. If the code is not valid, the employee's
 default code will be assigned.

Crew
Add or edit a crew code for this
 employee (if applicable), or press F4 or double-click on this
 field to select from a list of available crew codes. The software will validate
 that the crew code entered is from the same company in which the job is set
 up.
Message
Enter a descriptive message, or make
 changed to an existing message for this time card line.
Check

Sequence
Sequence numbers are assigned and
 maintained by the software. The check type and check number information then
 defaults based on the sequence number.
Type
The check type defaults based on the
 sequence number.
Number
The check number defaults based on the
 sequence number entered.
Regular hours
The number of regular hours worked
 during this pay period displays.
Overtime
The number of overtime hours worked
 during this pay period displays.
Double time
The number of double time hours worked
 during this pay period displays.
Employee

(Employee) Rate
Here are your options when adding or
 editing the employee's pay rate:

- Press Enter to accept the default pay rate for this employee.
 The pay rate will default based on the period end date and the wage/union
 code information from the Job Cost  > Phase File Maintenance  >  Properties window, unless the Payroll Installation
 prompt for Default pay
 rate is set to Employee pay rate or
 Higher of the two
 rates, in which case the rate field will default from
 Employees,
 or from Equipment Control if equipment usage is entered. The software
 will then look at the job file for the correct union associated with this
 wage code. If no union is set up in the job file, the software will look
 in the employee master file for a union code.

- Manually enter the rate amount. If this is a
 salaried employee, enter the salary amount; if this is an hourly
 employee, enter the pay rate per hour, or press F4 or double-click on
 this field for quick entry rates.If there is no
 rate for pay types M, SR, or SA already set up in Employees
 –Financials, the software will stop at this field and
 allow entry of the rate for those pay types.
If the pay type for this line is ER, EO, ED, or EU, the equipment
 rate will display on a second line. This rate defaults from the
 equipment file.
For prevailing wage jobs with
 non-stated fringe, the standard pay rate will include the non-stated
 fringe and the employee rate will be adjusted automatically.
After hours have been entered using the Quick Time Card
 Entry window at the hours field, an additional window
 is available which allows the user to override the regular and
 overtime rates before the quick time card lines are created. This
 window will open automatically when the Quick Time Card
 Entry window is used and the default regular pay rate
 is overwritten.

- For pay groups, see the [Pay Group Rate Default Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/pay-group-rate-default-hierarchy) topic. Otherwise, enter the desired pay rate.
 If this is an add-on entry, enter the amount to be added on this line of
 the time card entry.

(Employee) Billing code
If the time card is for a job, the T+M
 labor billing code and description display. If the time card is for a work
 order the WO labor billing code and description display. Changes are allowed in this field and a drop-down search window lets you
 select a different valid code; the employee billing rate will adjust
 accordingly.

(Employee) Billing rate
The employee's billing rate displays,
 no entry is allowed. This field displays regardless of whether or not the
 Show pre-time card pay
 rates checkbox is selected on the Payroll Installation > Properties tab.The software will determine whether
 site-specific or contract specific labor billing rates are assigned to the
 labor transaction. The billing rate will default based on the following
 hierarchy:

- The contract-specific billing rate will default, if
 present.

- If a contract-specific rate is not present, the
 site-specific rate will default.

- If neither the contract-specific billing rate or
 site-specific rate are present, the customer specific rate will default.

- If no override rates are present, the standard rate
 will default.

- If no labor billing rates are present, the billing
 rate will be blank.

For Time + Material jobs, the billing rate will
 default based on the bill code specified in Wage Code File Maintenance
 (and then Union File Maintenance) for the rate level
 of the phase as the highest priority. If the bill code is blank or if there
 is no phase override, then the existing hierarchy will be used to default
 the Time + Material rate.
If this is a sub-job
 billed from a master job, the software will read for job-specific setup
 rates for the master job, and if none are found use standard settings. If
 this is a sub-job billed at the sub-job level, the software will read for
 job-specific setup rates for the sub-job first, and if billing rates are not
 found then the master job, and if none are found there use standard
 settings.

(Employee) Hours
Add or edit the number of hours worked
 for this pay type/job/phase.If the time card line
 originated in Work Order > Labor Hours Entry, or the time card has already been selected for billing in Work Order > Labor Hours Entry, this field will be display-only.

Equipment

(Equipment) Rate
Enter the equipment rate for this time
 card line, or press F4 or double-click on this field to change the rate type.This field only displays when the Pay type is ER, EO, ED or
 EU and Equipment Control is installed on the software.
Hierarchy for charge rates
If
 applicable, this rate information will default the amount set up in the
 Job-Specific Equipment Charge Rates screen. If no job-specific record is
 found (or rate is blank), the system will determine if this job is a sub job
 of a master job and use the job-specific rate from the master job. If there
 is no job-specific rate for the job or master job, the system will read for
 the standard job rate of the equipment code.

(Equipment) Billing code
The T+M equipment billing code and
 description display. Changes are allowed in this field and a drop-down search
 window lets you select a different valid code; the equipment billing rate will
 adjust accordingly.
(Equipment) Billing rate
When the Pay type is ER, EO, ED or EU
 the software will prompt for the (company) equipment billing rate. This field
 only displays if an equipment department is entered, and Equipment Control is
 installed on the software. In the 'New' window it will default to the equipment
 rental rate when the work order is Time & Material. If an equipment billing
 rate is specified, the Payroll Update will store this default equipment billing
 rate in the Work Order cost history table.Repeat entry
 until all hours for this job have been entered. When entry is complete,
 click OK until the
 fields clear. Enter a new job number and repeat until time cards have been
 entered for all employees on all jobs.
If this is a
 sub-job billed from a master job, the software will read for job-specific
 setup rates for the master job, and if none are found use standard settings.
 If this is a sub-job billed at the sub-job level, the software will read for
 job-specific setup rates for the sub-job first, and if billing rates are not
 found then the master job, and if none are found there use standard
 settings.

(Equipment) Hours
If the pay type for this line is
 ER, EO, ED, or EU, the number of employee
 hours will display on a second line as the number of equipment hours. The
 equipment hours may be changed by arrowing back from the "rate" field. This
 field only displays if an equipment department is entered and Equipment Control
 is installed on the software.If this time card line
 originated in Work Order > Labor Hours Entry, or has already been selected for billing, this field will be
 display-only.

Options button
Click this button to open the [Time Card Entry Fields Window](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults/time-card-entry-fields-window) where you can select the fields you would like to
 skip during Time Card Entry, helping to save you time during the entry process.
 Skipped fields can still be accessed by pressing Shift + Tab.

Related information

- [Retro Pay](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/retro-pay)

- [Pay Type Definitions](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/pay-type-definitions)
