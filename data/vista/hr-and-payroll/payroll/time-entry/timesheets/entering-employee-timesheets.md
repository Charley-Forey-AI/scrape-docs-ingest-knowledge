---
title: "Entering Employee Timesheets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-employee-timesheets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-employee-timesheets"
---

# Entering Employee Timesheets

When you are a foreman/manager, you can use PR My Timesheets to enter your employees timesheets into the system.
Using this form you can enter weekly timesheet details into the system, which will then be reviewed and approved by your manager.
Note: In order for you to be able to access PR My Timesheet, you must be set up with a timesheet permission in VA User Profile. See [Setting Up Timesheet Permissions for Users](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/setting-up-timesheet-entry/set-timesheet-permissions) for more information.
The following instructions detail how to enter timesheets using PR My Timesheet.

1. [Create a timesheet](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/create-a-timesheet) using the header section of the form.

1. On the detail Grid tab,
 enter N, New, or + in the Seq
 field to create a new detail record. The new record defaults the following
 fields with information based on your employee settings in PR Employees:
 Employee, JC Co, Job, Craft, Class, Shift, and Earnings Codes.

1. In the Employee field, enter the employee whose timesheet data you are entering, or accept the default if entering your own timesheet data.

1. From the Type drop-down, select the type of timesheet data you are entering.

- Select J-Job (default) to enter timesheet data for time worked on a job.

- Select S-SM Work Order to enter timesheet data for time worked on an SM work order.

- For Australian and Canadian companies, [click here](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-form/field-definitions-pr-my-timesheet-form#ID-0003949d--en) for important information about entering time for SM work orders.

1. For job timesheet data only, enter (or change) the values in the JC Co, Job, and Phase fields, as necessary. For more information about a specific field, refer to the F1 help.For SM work order timesheet data only, enter the appropriate values in the SM Co, Work Order, Scope, and Pay Type fields. Entry in these fields is required. For more information about a specific field, refer to the F1 help.
Note: If the job associated with the timesheet data (both Job and job-related SM Work Order lines) is closed and you do not allow posting to closed jobs (i.e. the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs boxes are checked in JC Company Parameters), you will be unable to save the record.

1. Enter (or change) the information in the Craft, Class, Shift, and/or Earnings Code fields, as necessary. For more information about a specific field, refer to the F1 help.

1. Enter the totals for each day in the appropriate fields. The Totals section of the grid updates with the appropriate hours. Note: For work order timesheet data only, if you enter hours for multiple days, the system will generate a separate work completed labor line for each day.

1. You only need to create one sequence per week, assuming that the employee did not work on multiple jobs/phases or work orders/scopes (depending on timesheet data you are entering), earnings codes, shifts, and/or crafts/classes. You can enter totals once a day or enter all totals at the end of the week.However, if the employee worked on multiple jobs/phases or work orders/scopes and shifts, or for multiple crafts and classes during a specific work day, enter more than one detail line. For example, if the employee worked for five hours on job 1, phase 2, shift 3 and worked for three hours on job 7, phase 3, and shift 3 for another job, the detail grid would look like this:
Seq
JC Co
Job
Phase
Craft
Class
Shift
Earnings Code
Day One

1
100
1
2
-
-
3
1
5.00

2
100
7
3
-
-
3
1
3.00

1. Save the record as normal.

1. Repeat steps 4 - 10 for each of your employees.

1. On the Info tab on the header section of the form, click the Lock button. The system disables the fields in the detail section of the form. The timesheet is now [ready for approval](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/approving-timesheets).

Related information

- [About the PR My Timesheet Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-form)

- [Entering Personal Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-personal-timesheets)

- [Set Timesheet Permissions](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/setting-up-timesheet-entry/set-timesheet-permissions)
