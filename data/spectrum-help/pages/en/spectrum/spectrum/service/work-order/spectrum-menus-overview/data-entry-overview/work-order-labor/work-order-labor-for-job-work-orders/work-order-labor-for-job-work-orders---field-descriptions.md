---
title: "Work Order Labor for Job work orders - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor/work-order-labor-for-job-work-orders/work-order-labor-for-job-work-orders---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-labor/work-order-labor-for-job-work-orders/work-order-labor-for-job-work-orders---field-descriptions"
---

# Work Order Labor for Job work orders - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Technician
Enter the code of the technician whose hours are to be entered. Entry in this field is required. If the Payroll module is present, the software will verify the employee status is active before proceeding.
Employees not set up in the technician file can still be used in Labor Hours Entry as long as they have been set up in the Payroll module. The technician maintenance screen gives you flexible costing options.
The employee name will automatically display to the right of this field once a code is entered. Verify that this is the correct technician before proceeding.

Pay type
Pay Type options are regular, overtime, double time, special rate, equipment usage, equipment regular, equipment overtime, or equipment double-time. Indicate which type these hours are to be paid at: (R)egular rate, (O)vertime, (D)ouble time, (SR)special rate, (EU)equipment usage, (ER)equipment regular, (EO)equipment overtime, or (ED)equipment double time.

Work date
Enter the date worked. The work date defaults to the current Work Order processing date. Dates entered must fall within the minimum/maximum date range for Work Order.

Time in / out
To keep a log of time in/out, enter the time the employee arrived at and left the site. Entry should be done in military time (for example, 08:00). If only total hours are desired, press Enter to leave the field blank.

Hours
If time in/out was entered, the software will automatically calculate the number of hours (no allowance is made for breaks) and skip to the next field. If time in/out was not entered, enter the number of hours for this work order.

Phase Ct
Enter a phase code and valid cost type. The phase + cost type must be set up
 for the selected job. The default cost type is specified on the
 Work Order Installation screen.
Note: If the selected job is a sub-job of a master job, and the
 phase + cost type are not set up on the current job, validate against the
 master job and then auto-create in the sub-job.

Taxable?
Select whether the work order is taxable.
If the job was setup as taxable in Job Cost
 Maintenance, this field will default to taxable but can be
 overridden.

Bill hours
The billing hours will default from the actual number of hours worked. Enter
 the hours that will be billed to this client, or press
 Enter to accept the default.
Billing hours are not necessarily equal to the number of hours that the
 employee worked; for example, if the employee spent 45 minutes on the work
 order, but there is a minimum charge of one hour, then actual hours would be
 .75 and billing hours would be 1.0.

Bill code
The billing code for the selected labor category displays in this field, but can be overwritten, which would cause the billing rate to change automatically.

Bill rate
The software will determine whether site-specific or contract specific labor billing rates are assigned to the labor transaction. The billing rate will default based on the Labor Billing Rate Hierarchy.

Task
Enter the task associated with this line item, double-click in this field to
 select from a list of available tasks, or press Enter
 to leave this field blank.

Complete?
Select this checkbox if the task has been completed and transferred to Accounts Receivable; otherwise, leave this checkbox clear. This checkbox can be selected even if labor hours have been transferred to Payroll Pre-Time Card Entry.

Equipment
Enter an equipment code. This field displays only if the pay type is Equipment Regular, Equipment Overtime, Equipment Double time, or Equipment Usage.
 If this equipment's status is set to Retired in the Equipment Control module, entry is not allowed. If the equipment's status is set to Inactive in the Equipment Control module, entry is allowed in this screen, however the software will warn you of the equipment's status.
Note: All of the equipment fields will be hidden if the Equipment
 Control module is not present.

Eq rate type
Enter the equipment rate type: Hourly, Daily, Weekly, or Monthly.
This field displays only if the pay type is Equipment Regular, Equipment Overtime, Equipment Double time, or Equipment Usage.
Hierarchy for charge rates:
If applicable, this rate information will default the amount set up in the
 Job-Specific Equipment Charge Rates screen. If no
 job-specific record is found (or rate is blank), the system will determine
 if this job is a sub job of a master job and use the job-specific rate from
 the master job. If there is no job-specific rate for the job or master job,
 the system will read for the standard job rate of the equipment code.

Eq hours
Enter the number of equipment hours for this work order.

Eq bill hrs
Enter the number of billing hours for this piece of equipment.

Eq bill rate
Enter the equipment bill rate for the specified piece of equipment.

State
Enter the code of the work state for this particular work order line.

County
Enter the code of the county for this particular work order line.

Local
Enter the local tax code for this particular work order line.

W/comp
Enter the workers comp code for this particular work order. The worker's comp code defaults based on the job file or job site file; otherwise, it will default based on the employee file.

Pay group
The pay group will default from the Job File
 Maintenance screen, but can be changed.
Note: This field will be hidden unless the 'Default rate table' is
 set to use ' Pay groups' in Payroll Installation.

Wage code
The wage code defaults from the Payroll Employee
 Maintenance screen, or you can enter the wage code for this
 particular work order.

Union
If a wage code is specified for this work order the union code first defaults
 from the phase file (if the wage code is specified in Job Cost > Phase File Maintenance), otherwise the union code defaults from the job file (if the
 wage code is specified in Job Cost > Job File Maintenance), and lastly, the union code will default from Payroll > Employee Maintenance if no wage code if specified.
Note: This field will be hidden if the 'Default rate table' is set
 to use ' Pay groups' in Payroll Installation.

Level
Enter the pay level for this particular work order.

G/L dept
The G/L department will default based on the type defined for this work order
 during Work Order Entry. Changes can be made if desired. The G/L department
 must have been previously defined in the Work Order G/L
 Department File Maintenance.
The system validates the Payroll department associated with each transaction
 when the Job Cost Installation prompt for Validate
 job div w/ gl dept is selected to assure the G/L code associated with the
 department matches the division assigned to the job.

Task description
The specified task description will display in this field.

Phase description
The specified phase description will display in this field.
