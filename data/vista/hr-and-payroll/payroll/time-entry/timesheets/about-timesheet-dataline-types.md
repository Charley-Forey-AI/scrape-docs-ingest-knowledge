---
title: "About Timesheet Data/Line Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-timesheet-dataline-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-timesheet-dataline-types"
---

# About Timesheet Data/Line Types

When entering timesheets (in PR My Timesheet), additional
 information will be required depending on the type of timesheet data you are entering
 (determined by the option selected in the Type field).
There are two types of timesheet data:

- J-Job - Use this type to enter timesheet data for time worked on a JC job.
 When selected, fields are enabled to allow specifying the jobs and phases worked on
 by you or another employee (if entering timesheets for other employees).

- S-SM Work Order - Use this type to enter timesheet data for work performed
 on an SM work order (customer or job-related). Employees specified for this type
 must be set up as technicians in SM Technicians. Selecting this type enables fields
 that allow you to specify the work orders and scopes worked on by the technician, as
 well as the pay type for deriving estimated labor costs (on the work order). For
 job-related work orders, you will also specify the JC cost type that will be used
 (along with the scope phase) to update costs to the job in Job Cost.

Timesheets entered for an SM work order will
 generate corresponding work completed labor entries in SM Work Orders (Work Completed
 tab). Any changes made to the timesheet will be updated to the corresponding work
 completed record. Likewise, changes made to a work completed labor line in SM will
 update the corresponding timesheet; however, updates will only occur if you have checked
 the PR interface box in SM Company Parameters. If the PR
 interface box is unchecked, no automatic generation or update of timesheets will occur.
 You will need to manually add or update timesheets or timecards to capture labor hours
 in PR for SM work orders.
Note: If you edit an existing timesheet record and the
 corresponding work completed labor line has already been invoiced (sent to AR), changes
 to the hours in this form will update the Cost Hours on the labor line, but not the
 Billable Hours. If you change the scope, technician, or work order, the cost information
 on the work completed line will be set to 0.00 and a new work completed line
 created.
Note: For Australian and Canadian companies: Entry of time
 to a non-job SM work order will automatically set the Tax Type to
 3-VAT for the work completed labor line in SM Work Orders. The tax code for the work
 completed line will default from the Service Center or Service Site (depending on the
 Tax Source specified for the work order) and must be a VAT-type code. For this function
 to work, the SM company's AR company (defined in SM Company Parameters) must be set up
 with a Default
 Country of AU or CA in HQ Company Setup.
