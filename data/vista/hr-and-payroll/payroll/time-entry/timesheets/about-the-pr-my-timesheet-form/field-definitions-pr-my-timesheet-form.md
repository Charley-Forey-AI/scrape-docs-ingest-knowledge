---
title: "Field Definitions: PR My Timesheet Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-form/field-definitions-pr-my-timesheet-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-form/field-definitions-pr-my-timesheet-form"
---

# Field Definitions: PR My Timesheet Form

The following is a list of field descriptions for the PR My
 Timesheet form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Start Date

The Start Date field on the PR My Timesheets form, Grid/Info header tabs.

Enter the start date for this timesheet. The system creates timesheets in weekly increments.
Enter T to have the system default the current date.

### SM Work Orders

If this timesheet was generated from a work completed labor line (in SM Work Orders), the start date defaults based on the labor entry date and the pay period defined for the payroll group. For example, if you have a pay period of 12/01/24 — 12/14/24, and the labor entry date (in SM) is 12/02/24, the timesheet created here will have a start date of 12/01/24.
However, because timesheets are in 7-day increments, if your pay periods span multiple weeks, the system uses the pay period start "day" to determine the start date for labor hours posted in each week of the pay period. For example, say your pay period runs 12/01/24 — 12/15/24. The start date, 12/01/24, falls on Sunday, so this is the "day" the system uses when determining the Start Date for timesheets posted in each week of the pay period. Therefore, labor hours posted on 12/01/24 through 12/07/24 will have a start date of 12/01/24 and labor hours posted on 12/08/24 through 12/14/24 will have a start date of 12/08/24. Labor hours posted on 12/15/24 will have a start date of 12/15/24.
Note: If no pay periods exist before the labor 'date it uses Sunday as the start date. For example, a labor line dated 12/20/24 would use 12/15/24 as the start date when creating the PR My Timesheet entry.

## Sheet

The Sheet field on the PR My Timesheets form.
Enter a number for this timesheet. This field only allows numbers.
Depending on how timesheets are entered for your company and the number of employees, you can use sheets to represent a day in the pay period or an entire pay period.
One sheet per day in the pay period
If each employee enters his/her own time, they can enter a single sheet per day in the pay period (Day 1, Sheet 1; Day 2, Sheet 1, etc.). In this case there will be a single sequence for each sheet. If entering overtime, the employee can either post a second sequence on the same sheet or enter the overtime on a second sheet for the applicable day.

If a manager or other designated person posts timesheets for employees, then typically, one sheet is posted per day in the pay period; however, each sheet includes all employees that worked that day. In this case, there will be a separate sequence for each employee. For employees that work overtime, you can either have a second sequence for each applicable employee on the daily sheet or use a second sheet that includes the overtime hours for applicable employees.
One sheet per pay period
This method is typically most useful if employees enter their own time. In this case, the sheet will include a sequence for each day in the pay period. If entering overtime on the same sheet, then the employee would have two sequences per day, as applicable. If using a second sheet for overtime, then the second sheet would include sequences for each day the employee worked overtime.If a manager or other designated person posts timesheets for employees, one sheet per pay period may not be practical if there are numerous employees, as the timesheet could become a little unwieldy. However, you can use a single sheet per pay period if desired. In which case, you might consider using a second sheet to post overtime for the pay period.

## Seq

Enter N, New, or + in this field to create a new timesheet
 sequence.

## Employee

This field displays only when you have been assigned a timesheet permission of 2-Enter for Self and Others in VA User Profile (
 My Timesheet Permissions
 field).
This field defaults your employee number from PR Employees.
Enter the number of the employee for which your are entering timesheet data. If this timesheet entry is for an SM technician, the employee specified here must also be set up as a technician in SM Technicians.
Once you enter the employee number here, the
 system defaults information in the JC Co, Job, Phase,
 Craft, Class, Shift, and
 Earnings
 Code fields based on settings for the employee in PR Employees.

## Type

Select the type of timesheet data you are entering.

- J-Job — Use for employees that have worked on a JC job.

- S-SM Work Order - Use for technicians that have performed service work on an SM work order.

Timesheets with a type of S-SM Work Order) will automatically add a corresponding work completed labor line to the work order (in SM Work Order). Likewise, work completed labor lines added for a work order in SM Work Order will automatically create a timesheet entry here with a type of S-SM Work Order.
For Australian and Canadian companies
Entry of time to a non-job SM work order will
 automatically set the Tax Type to 3-VAT for the work completed
 labor line in SM Work Orders. The tax code for the work completed line will default from
 the Service Center or Service Site (depending on the Tax Source specified for the work
 order) and must be a VAT-type code. For this function to work, the SM company's AR company
 (defined in SM Company Parameters) must be set up with a Default Country
 of AU or CA in HQ Company Setup.

## JC Co

This field is only enabled for job timesheet
 data (i.e. sequence Type of J-Job).
Enter the JC company for which the employee performed work. Initially defaults the JC Co defined for the employee in PR Employees (if applicable). Press F4 for a list of valid JC companies.
SM Work Order Timesheets
For job-related work orders only, this field displays the JC Co to which labor costs will be posted. Defaults the JC company defined for the SM company in SM Company Parameters; cannot be changed.

## Job

This field is only enabled for job timesheet
 data (i.e. sequence Type of J-Job).
Enter the job that the employee was working on, if applicable. Initially defaults the job specified for the employee in PR Employees. Press F4 for a list of valid jobs.
SM Work Order Timesheets
For job-related work orders only, this field displays the job to which labor costs will be posted. Defaults from the work order and cannot be changed.

## Phase

This field is only enabled for job timesheets
 (i.e. the Type is J-Job).
Enter the phase on which the employee was working. Press F4 for a list of valid phases for the job.
SM Work Order Timesheets
For job-related work orders only, this field displays the phase to which labor costs will be posted. Defaults from the work order scope and cannot be changed.
Note: If the work order scope has not been assigned a phase,
 the phase will default as blank and you will be unable to save the record. Since this field
 is disabled for SM work order timesheets, you cannot assign a phase here; however, you can
 assign a phase to the work order scope by pressing F5 from the SM Wo or
 SM
 Scope fields. Once you assign a phase to the scope, you will be able to save
 the timesheet.

## SM Co

This field is only available when entering
 timesheet data for technicians (i.e. sequence Type of S-SM Work Order).
Required.
Enter the SM Company for which the specified
 technician worked when completing the specified work order. Press F4 for a list
 of valid SM companies. Initially defaults the SM company defined for this PR company in PR
 Company Parameters (SM Co # field, Job Cost / Service Mgmt tab).
This field is disabled for existing records when the specified work order/scope is closed.

## Work Order

This field is only available when entering
 timesheet data for technicians (i.e. sequence Type of S-SM Work Order).
Required.
Enter the SM work order to which this
 timesheet applies (i.e., the work order the technician worked on). Press F4 for a list
 of valid work orders.
Note: If posting to closed jobs in not allowed (i.e. the
 Allow Posting to
 Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs boxes
 are not selected in JC Company Parameters), you cannot specify a work order that is
 associated with a closed job.
This field is disabled for existing records when the specified work order/scope is closed.

## Scope Seq

This field is only available when entering
 timesheet data for technicians (i.e. sequence Type of S-SM Work Order).
Required.
Enter the work order scope to which this timesheet applies (i.e., the scope the technician worked on). Press F4 for a list of valid scopes for the specified work order.

- If you select a scope that has been closed, a warning displays and you will be unable to save the record. You must either select a different scope or reopen the scope in SM Work Orders.

Note: This field will be disabled for existing timesheets when the specified work order/scope is closed.

- For job-related work orders:
Note:

- If the Costing Method is
 Markup and the scope does not have a rate template assigned, you will be
 able add the timesheet and then post the related timecard batch; however,
 you will be unable to run PR Ledger Update until you assign a rate
 template to the scope.

- If the work order scope is not assigned a phase, a warning displays and you be unable to save the record. You can press F5 from this field to access SM Work Orders and assign a phase to the scope. Once you assign a phase to the scope, you can save the record.

## Cost Type

This field is only enabled when entering a
 technician timesheet (i.e. Type is S-SM Work Order).
Enter the SM cost type that applies to this
 timesheet entry. Press F4 for a list of valid SM cost types.
Note: Once the work order/scope specified for this entry is closed, you will be unable to change the cost type.

## Pay Type

This field is only available when entering
 timesheet data for technicians (i.e. sequence Type of S-SM Work Order).
Required.
Enter the pay type to which this timesheet data applies. The pay type specified here will determine the default earnings code for the technician, as well as the Cost Rate for the work completed labor line created when this timesheet record is saved.
Note: Once the work order/scope specified for this entry is closed, you will be unable to change the pay type.

## Earnings Code

Enter the earnings code for the work performed. Initially defaults the earnings code assigned to the employee in PR Employees. Press F4 for a list of valid earnings codes.
If entering timesheet data for a technician (sequence type S-SM Work Order), this field defaults the earnings code assigned to the specified pay type (in SM Pay Types). You may override the default as necessary; the change will not be updated to the pay type.
Note: You can only enter earnings codes that have been set
 for remote timesheet entry (the Include in Remote Timesheet Entry box is
 checked in PR Earnings Codes).

## JC Cost Type

This field is only displayed if the line Type is S-SM
 Work Order and the selected SM work order is for a job.
Required.
Enter the JC cost type (from JC Cost Types) for the work performed. Initially defaults as follows:

- If you entered an SM cost type for the line, defaults the JC cost type assigned to the SM cost type (in SM Cost Types). Default may be overridden.

- If you did not enter an SM cost type or if you entered an SM cost type, but no JC cost type is assigned to the SM cost type, this field will default the JC Cost Type from the earnings code entered for this line.

The system will use this cost type, in conjunction with the phase specified for the work order sequence, to post the costs to Job Cost (via the JC Cost Detail table).

- If the job specified for the work order is locked
 (i.e. the Phases on this job are locked box is checked in JC Jobs), this cost
 type must be set up for the job/phase in JC Job Phases; otherwise, the system
 displays a warning and you will be unable to save the line until you specify a valid
 job/phase cost type.

- If the job is not locked (i.e. the Phases on this job
 are locked box is not checked in JC Jobs), you can use any cost type
 defined for the phase in JC Job Phases or JC Phases. If you enter a cost type that is
 not defined for the job phase or phase, the system displays a warning and will not
 allow you to save the line until you specify a valid phase cost type.

- If the work order scope specified for this invoice line has not been assigned a phase, you will receive a message indicating the phase is missing; you will be unable to save the record until you assign a phase to the work order scope in SM Work Orders.

## Shift

Enter the shift associated with the employee for the specified time. Initially defaults the shift assigned to the employee in PR Employees (if applicable).

## Craft

Enter the craft associated with the employee
 for the specified working time or press F4 to select from a list of valid
 crafts.
The following table displays how this field defaults the craft.
Line Type
Uses Craft Template From
Reciprocal Agreement set to Override
Use Job Craft
Use Employee Craft

Job (with Job specified)
Job
Y
Y
N

N
N
Y

Job (no Job specified)
N/A
N/A
N/A
Y

SM Work Order (Job WO)
Job
Y
Y
N

N
N
Y

SM Work Order (Customer WO)
Work Order
Y
Y
N

N
N
Y

Note: For timesheets generated from work completed labor lines (type S-SM Work Order), this field defaults the craft specified for the labor line in SM Work Orders (Work Completed tab) or in SM Work Completed Labor.

## Class

Enter the class associated with the employee
 for the specified working time. Initially defaults the class assigned to the employee in PR
 Employees (if applicable). Press F4 for a list of valid classes.
If the craft template associated with the Job (job and SM job work order timesheets) or SM Work Order (customer work order timesheets) has a reciprocal agreement with a type of Override, the system will override the employee's standard craft with the Job Craft specified on the craft template (in PR Craft Template). If the employee's standard class does not exist for the Job Craft, you must either set up the class for the Job Craft in PR Craft Classes and in PR Craft Class Templates (for the job's craft template) or select a valid class already set up for the Job Craft.
Note: Service timecards (type S-SM Work Order) originating from Service Management will default the class specified for the labor line in SM Work Orders (Work Completed tab) or in SM Work Completed Labor.

## Day

Enter the hours worked for this day.

- The title of this field changes relative to the
 start date that you entered in the Start Date field, in the following
 format: first letter of the day of the week plus Month/Day. For example, if you enter
 9/01/XX as a start date (and it is a Monday), the Day One field in
 the detail Grid will change to M 9/1.

- Technician Timesheets:
Note:

- If you enter hours for multiple days, a separate work completed labor line will be generated on the work order for each day; other than the hours, the information will be duplicated for each line.

- Once you close a work order scope, this field is disabled and you will be unable to change the hours on the timesheet.
