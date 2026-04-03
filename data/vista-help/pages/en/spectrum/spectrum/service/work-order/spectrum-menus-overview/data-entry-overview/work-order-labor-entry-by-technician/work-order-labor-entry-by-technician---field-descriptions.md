---
title: "Work Order Labor Entry by Technician - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor-entry-by-technician/work-order-labor-entry-by-technician---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor-entry-by-technician/work-order-labor-entry-by-technician---field-descriptions"
---

# Work Order Labor Entry by Technician - Field Descriptions

Use the table below for reference when completing the
 fields on this screen.
The columns in the grid on this screen correspond directly with the columns for [Work Order Labor for Job work orders](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor/work-order-labor-for-job-work-orders). The columns marked with an asterisk (*) in the table below are 'site-related' and have been added to the ones appearing in the 'job entry' grid in Work Order Labor.
Field
Description

Work Order
This column initially defaults to
 <blank> when adding a new row (by clicking the New button).
For
This column displays Site or Job, depending on the work
 order.
Work date
Enter the date worked. The work date
 defaults to the current Work Order processing date. Dates entered must fall
 within the minimum/maximum date range for Work Order.
Pay type
Pay Type options are regular,
 overtime, double time, special rate, equipment usage, equipment regular,
 equipment overtime, or equipment double-time. Indicate which type these
 hours are to be paid at: (R)egular rate, (O)vertime, (D)ouble time,
 (SR)special rate, (EU)equipment usage, (ER)equipment regular, (EO)equipment
 overtime, or (ED)equipment double time.
Time in / out
To keep a log of time in/out, enter
 the time the employee arrived at and left the site. Entry should be done in
 military time (for example, 08:00). If only total hours are desired, press
 Enter to leave
 the field blank.
Hours
If time in/out was entered, the
 software will automatically calculate the number of hours (no allowance is
 made for breaks) and skip to the next field. If time in/out was not entered,
 enter the number of hours for this work order.
Phase Ct
Enter a phase code and valid cost
 type. The phase + cost type must be set up for the selected job. The default
 cost type is specified on the Work Order Installation screen.Note: If the selected job is a sub-job of a
 master job, and the phase + cost type are not set up on the current job,
 validate against the master job and then auto-create in the
 sub-job.

Phase description
The expanded phase description
 displays up to 8 characters.
Site equipment *
This field will default from the
 task setup in the work order header, when a task code has been entered for
 the transaction. Entry will be required if the Work Order
 Installation option for 'Require equipment code for work
 order transactions?' is selected. A warning will display if the operator
 enters an inactive code, but entry will be permitted.

- This field will be view-only for pre-time card
 transactions, since the equipment code is assigned in Pre-Time Card
 Entry.

- This field will be view-only for Payroll
 transactions, since the cost has already been posted for the specified
 equipment code.

- This field will be view-only for 'Entry'
 transactions after approval and update to Pre-Time Card Entry.

Component *
Enter a component code in this field
 for the previously selected equipment. This field will only be enabled if
 components are set up for the specified piece of equipment.  If the Work Order Installation
 option for 'Require component code for work order transactions?' is
 selected, input is mandatory if the operator entered a valid equipment
 that has at least one component set up.

- This field will be view-only for pre-time card
 transactions, since the cost will be posted for the specified
 component code when the payroll is updated.

- This field will be view-only for Payroll
 transactions, since the cost has already been posted for the specified
 component code.

Contract *
Select a contract for the
 Equipment/Component combination in this field. Drill-down on the inquiry
 button to view the work order and contract description.

- This field will be hidden if the Service Contract
 module is not present, or disabled if the Service Contract module is
 present but no contract exists for the Equipment/Component
 combination.

- If the Work Order
 Installation option for 'Require equipment code for
 work order transactions?' is not selected, the operator will be
 permitted to enter a valid contract # without assigning an equipment
 code.

- If a contract is specified in the work order
 header, this contract # will default if valid for the
 Equipment/Component combination and entering a different contract will
 be disallowed.

- If the contract is not valid for the
 Equipment/Component combination, this field can be left blank for
 'non-contract work'.

- If a contract is not specified in the work order
 header, the operator will be allowed to enter any combination of
 contracts (or a blank contract) in the work order detail.

- The contract will always default from the
 contract specified in the work order header, or from the previous line
 if the operator remains in add mode to enter multiple detail lines and
 no contract is specified in the work order header.

- A contract specified in the Flat Rate Task Table
 will default when a particular task code has been specified if (a)
 there is a valid contract code assigned to the task, and (b) the
 equipment code for the task is the same as the one specified in the
 Labor Hours transaction entry window.

- A warning will display if the operator enters an
 inactive contract, but entry will be allowed.

- This field is view-only for pre-time card
 transactions since the cost will be posted for the specified contract
 code when payroll is updated.

- This field is view-only for 'Payroll'
 transactions since the cost has already been posted for the specified
 contract code.

- Entry of a 'Proposed' service contract will be
 disallowed.

Bill cust? *
Select this checkbox to bill
 customer for this labor entry. The operator will be able to change the
 status of this checkbox from any source while the status of the labor
 record is open. Billing revenue for use of company
 equipment is always updated to General Ledger through the Accounts Receivable > Sales Journal Update when the billing rate and billing hours are non-zero.

 If the pay type is 'EU', this checkbox will
 be automatically selected and the Operator will be prohibited from
 deselecting it.

Taxable?
Select whether the work order is
 taxable.If the job was setup as taxable in
 Job Cost Maintenance, this field will default
 to taxable but can be overridden.

Bill hours
The billing hours will default from
 the actual number of hours worked. Enter the hours that will be billed to
 this client, or press Enter to accept the default.  Billing hours are not necessarily equal to the number
 of hours that the employee worked; for example, if the employee spent 45
 minutes on the work order, but there is a minimum charge of one hour,
 then actual hours would be .75 and billing hours would be 1.0.


Bill code
The billing code for the selected
 labor category displays in this field, but can be overwritten, which would
 cause the billing rate to change automatically.Note: If the job work order is 'Flat rate', this column
 will be skipped and billing codes will not be assigned.

Bill rate
The software will determine whether
 site-specific or contract specific labor billing rates are assigned to the
 labor transaction. The billing rate will default based on the Labor Billing
 Rate Hierarchy.
Task
Enter the task associated with this
 line item, double-click in this field to select from a list of available
 tasks, or press Enter to leave this field blank.
Complete?
Select this checkbox if the task
 has been completed and transferred to Accounts Receivable; otherwise, leave
 this checkbox clear. This checkbox can be selected even if labor hours
 have been transferred to Payroll Pre-Time Card Entry.
Co. equipment *
If an 'Equipment' pay type is
 selected, the Company equipment usage fields will be available for entry.
 Enter a Company equipment code in this field. The equipment description will
 display below this field.

- This field is view-only for 'Entry' transactions
 after approval and update to Pre-Time Card Entry.

- This field is view-only for pre-time card
 transactions, since the cost will be posted for the specified company
 equipment code when the payroll is updated.

- This field is view-only for 'Payroll'
 transactions, since the transaction has already been posted to history
 tables. If the Payroll transaction originated in another company, the
 company code will display to the left of the equipment code.

Co. eq rate type *
Select a rate type for the Company
 equipment: Hourly, Daily, Weekly,or Monthly.
Co. eq hours *
Enter hours for the equipment in
 this field.
Co. eq bill hours *
Enter billing hours for the
 equipment in this field.

- This field is view-only for 'Entry' transactions
 after approval and update to Pre-Time Card Entry.

- This field is view-only for pre-time card
 transactions, since the hours will be posted for the specified company
 equipment code when the payroll is updated.

- This field is view-only for 'Payroll'
 transactions, since the transaction has already been posted to history
 tables.

Co. eq bill rate *
Enter a billing rate for the
 selected equipment in this field.  In a
 New window, the billing rate will default to
 the equipment rental rate when the work order is Time + Materials.
If applicable, this rate information will default the
 amount set up in the Job-Specific Equipment Charge
 Rates screen. If no job-specific record is found (or rate
 is blank), the system will determine if this job is a sub job of a master
 job and use the job-specific rate from the master job. If there is no
 job-specific rate for the job or master job, the system will read for the
 standard job rate of the equipment code.

Co. eq cost rate
The equipment costing rate will
 default from the 'Standard job and service cost rates' found on Equipment
 Charge Rates for the entered 'Rate type'.

- If the 'Rate type' = Hourly, default in the
 Hourly Full Charge rate found in the 'Standard job and service cost
 rates' section.

- If the 'Rate type' = Daily, default in the Daily
 Full Charge rate, and so on with the other types.

G/L dept
The G/L department will default
 based on the type defined for this work order during Work Order Entry.
 Changes can be made if desired. The G/L department must have been previously
 defined in the Work Order G/L Department File
 Maintenance. The system validates the
 Payroll department associated with each transaction when the
 Job Cost Installation prompt for Validate job
 div w/ gl dept is selected to assure the G/L code associated with the
 department matches the division assigned to the job.

State
Enter the code of the work state for
 this particular work order line.
County
Enter the code of the county for
 this particular work order line.
Local
Enter the local tax code for this
 particular work order line.
W/comp
Enter the workers comp code for this
 particular work order. The worker's comp code defaults based on the job file
 or job site file; otherwise, it will default based on the employee
 file.
Pay group
The pay group will default from the
 Job File Maintenance screen, but can be changed.
 Note: This field will be hidden unless
 the 'Default rate table' is set to use ' Pay groups' in
 Payroll Installation.

Wage code
The wage code defaults from the
 Payroll Employee Maintenance screen, or you can
 enter the wage code for this particular work order.
Union
If a wage code is specified for this
 work order the union code first defaults from the phase file (if the wage
 code is specified in Job Cost > Phase File Maintenance), otherwise the union code defaults from the job file (if the
 wage code is specified in Job Cost > Job File Maintenance), and lastly, the union code will default from Payroll > Employee Maintenance if no wage code if specified.Note: This field will be hidden if the 'Default rate
 table' is set to use ' Pay groups' in Payroll
 Installation.

Level
Enter the pay level for this
 particular work order.
Task description
The specified task description will
 display in this field.
