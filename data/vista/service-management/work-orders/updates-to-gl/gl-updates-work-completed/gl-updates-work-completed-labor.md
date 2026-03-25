---
title: "GL Updates: Work Completed Labor | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-labor"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-labor"
---

# GL Updates: Work Completed Labor

The system updates the General Ledger (GL) for work completed
 labor lines once you run the PR Ledger Update.
Work completed labor lines are handled somewhat differently in that no batch processing is done in SM. When you create a work completed labor line, the system creates a timesheet in PR My Timesheet.
Note: The system only creates timesheets if you selected
 the PR
 interface checkbox in SM Company Parameters. If you did not check the PR interface
 box, the system does not create timesheet entries in PR; however, labor entries added
 directly in PR My Timesheets or PR Timecard Entry will generate work completed labor lines
 (in SM).
Once you approve timesheets and post the timecard
 batches, you must then process payroll and run PR Ledger Update. If you selected the
 Interface PR to
 GL checkbox in PR Company Parameters, the system updates the Cost or Cost
 WIP account (depending on whether the call type is tracking WIP) specified for the work
 completed line with the "total amount" (gross + burden). It then creates one offsetting
 entry for the gross amount to the SM Applied Earnings account (defined by Earnings Type in
 PR Departments) and one offsetting entry for the burden amount to the SM Applied Burden
 account (defined by Liability Type in PR Departments Earnings Type).
Note: There is no interface level defined in PR; the system
 always generates a summarized entry for each applicable GL account.
For example, if you are tracking WIP for a call
 type, the update to GL for labor work completed would be as follows:

## Job Work Orders

If the work order is job-related and you
 have checked the JC interface box in SM Company Parameters, the system will update the
 Total Billable for the work completed line as cost to Job Cost and create GL entries
 using the Cost or Cost WIP account (if tracking WIP) specified for the work completed
 line, with offsetting entries to the JC Applied Earnings account and JC Applied Burden
 account in PR Departments. However, it will also create additional entries to the GL
 account defined for the phase or cost type in JC Departments for the job's department,
 as well as the Revenue or Revenue WIP account (if tracking WIP) specified for the work
 completed line.
So, if you are tracking WIP for a call
 type, the update to GL would be as follows:
* If a GL account is defined for the phase
 (on the work order scope), the system will debit the phase's GL account, regardless of
 whether a GL account is defined for the cost type specified on the work completed line.
 The system will only use the cost type's GL account when no GL account is defined for
 the phase.
Note: The Costing Method defined for a work order
 determines the amount that will be updated to Job Cost. If the Costing Method is Actual
 Cost, the system sets the Total Billable for the work completed line equal to the Actual
 Cost amount and sends this amount to JC. If the Costing Method is Markup, the system
 calculates the Total Billable amount using the rate template for the scope and sends
 this amount to JC. However, because the Total Billable amount can include markups with
 this method, this may cause the amounts updated to GL to differ.
For example, using the GL account example
 from above, if the Cost Amount is $1000 and the Total Billable is $1500, the GL account
 updates would be as follows:
