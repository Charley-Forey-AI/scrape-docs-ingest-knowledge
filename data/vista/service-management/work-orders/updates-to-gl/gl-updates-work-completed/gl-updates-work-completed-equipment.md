---
title: "GL Updates: Work Completed Equipment | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-equipment"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-equipment"
---

# GL Updates: Work Completed Equipment

The following discusses the updates to General Ledger when
 posting and invoicing work completed equipment lines.
When you enter work completed equipment for a work order, the system automatically creates a batch once you save the work completed line and move off the record. If you selected to auto-post batches (you selected the Auto Post New Work Completed
 checkbox in SM Company Parameters), the system also posts the batch automatically. If you did not select the Auto Post New Work Completed
 checkbox), you must post the batch using the SM Work Order Cost Posting form.
During the batch process, the following occurs:

- If you are not interfacing equipment usage to EM (that is, the EM interface checkbox is not selected in SM Company Parameters), the batch
is still processed, but no module update occurs.

- If you are interfacing equipment usage to EM (you selected the EM interface checkbox in SM Company Parameters), the system posts
 an equipment usage batch to EM.

- If the GL Usage Interface option in SM
 Company Parameters is set to Summary or Detail, the system creates a GL entry for
 the Cost account or Cost WIP account (if tracking WIP)
 specified for the work completed line. In addition, the system creates an offsetting
 entry to the GL account defined for the line's revenue code in EM Departments.
For example, if you are tracking WIP for a call type, the update to GL for equipment work completed would be as follows:

If you set the
 GL Usage Interface
 level to No Update, no updates to GL will occur; however, the system will still create the batch reports with the same information that would be included if you were updating GL

## Job Work Orders

If the work order is job-related and you
 have checked the JC interface box in SM Company Parameters, the system will update the
 Total Billable for the work completed line as cost to Job Cost and create GL entries
 using the Cost or Cost WIP account (if tracking WIP) specified for the work completed
 line, with an offsetting entry to the GL account defined for the line's revenue code in
 EM Departments. However, it will also create additional entries to the GL account
 defined for the phase or cost type in JC Departments for the job's department, as well
 as the Revenue or Revenue WIP account (if tracking WIP) specified for the work completed
 line.
So, if you are tracking WIP for a call
 type, the update to GL would be as follows:

* If a GL account is defined for the phase
 (on the work order scope), the system will debit the phase's GL account, regardless of
 whether a GL account is defined for the cost type specified on the work completed line.
 The system will only use the cost type's GL account when no GL account is defined for
 the phase.
The Costing Method defined for a work order determines the amount that will be updated to Job Cost. If the Costing Method is Actual Cost, the system sets the Total Billable for the work completed line equal to the Actual Cost amount and sends this amount to JC. If the Costing Method is Markup, the system calculates the Total Billable amount using the rate template for the scope and sends this amount to JC. However, because the Total Billable amount can include markups with this method, this may cause the amounts updated to GL to differ.
For example, using the GL account example
 from above, if the Cost Amount is $1000 and the Total Billable is $1500, the GL account
 updates would be as follows:

## Equipment Usage Entered via PR Timecard Entry

If you entered equipment usage with a service timecard in PR Timecard Entry, the update to GL is handled in Payroll and occurs once you process payroll and run PR Ledger Update. The system updates the usage as revenue to Equipment Management using the Equipment, Revenue Code, and Usage Units posted with the timecard. It also updates the usage as costs to the work order in Service Management. The update to GL will create one revenue entry to the GL account specified for the revenue code in EM Departments, and one cost entry to the Cost or Cost WIP account specified for the work completed line (depending on whether you are tracking WIP for the call type associated with the work order scope).
