---
title: "GL Updates: Work Completed Miscellaneous | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-miscellaneous"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-miscellaneous"
---

# GL Updates: Work Completed Miscellaneous

The system updates the General Ledger (GL) for work completed miscellaneous lines based on the cost type category associated with the work completed line and the cost accounts defined in SM Departments.
Miscellaneous work completed lines are used to capture any miscellaneous expenses associated with a work order that are not specifically labor, equipment, or material expenses. These expenses are not directly related to any module; therefore, no interface to other modules will occur.
When you manually enter work completed miscellaneous for a work order, the system automatically creates a batch once you save the work completed line and move off the record. If you selected the Auto Post New Work Completed checkbox in SM Company Parameters, the system posts the batch (behind the scenes). If you did not select the Auto Post New Work Completed checkbox, you must post the batch using the SM Work Order Cost Posting form.
For miscellaneous work completed lines auto-added to a work order (from standard charges or miscellaneous requirements), you must post the batch via SM Work Order Cost Posting.
The GL Usage Interface option in SM Company Parameters determines whether GL is updated when a miscellaneous batch is processed:

- If the GL Usage Interface option in SM Company Parameters is set to No Update, no updates to GL will occur; however, the system will still create the batch reports with the same information that would be included if you were updating GL.

- If the GL Usage Interface option in SM Company Parameters is set to Summary or Detail, the system creates a GL entry for the Cost or Cost WIP account (depending on whether the call type is tracking WIP) specified for the work completed line. The system also creates an offsetting entry as follows:

- If you specified a standard item for the work completed line, the system uses the override offset account defined for the standard item in SM Departments (Standard Items tab).

- If no override account is defined for the standard item or no standard item is specified for the work completed line, the system uses the override offset account defined for the line's SM cost type in SM Departments (Cost Types tab).

- If no override account is defined for the SM cost type or you did not specify an SM cost type for the work completed line, the system uses the miscellaneous cost offset account defined for the department (in SM Departments, Info tab).

For example, if you are tracking WIP for a call type, the update to GL for
 miscellaneous work completed would be as follows:

## Job Work Orders

If the work order is job-related and you selected the JC interface checkbox in SM
 Company Parameters, the system updates the Total Billable for the work completed
 line as cost to Job Cost and creates GL entries using the Cost or Cost WIP account
 (if tracking WIP) specified for the work completed line. Additionally, the system
 creates:

- an offsetting entry to the miscellaneous cost offset account defined in SM
 Departments. The cost offset account is determined as follows:

- If a standard item is defined for the line, the system uses the offset
 account defined for the standard item (on the Standard Items tab)

- If no override is defined for the standard item or no standard item is
 specified on the work completed line, the system uses the offset account
 defined for the SM cost type (Cost Types tab)

- If no override offset account is defined for the cost type or no cost
 type is specified on the work completed line, the system uses the
 miscellaneous offset account defined for the department (Info tab)

- an entry to the GL account defined for the phase or cost type in JC
 Departments for the job's department.

- an entry to the Revenue or Revenue WIP account (if tracking WIP) specified
 for the work completed line.

If you are tracking WIP for a call type, the update to GL would be
 as follows:
* If a GL account is defined for the phase (on the work order scope), the system will debit the phase's GL account, regardless of whether a GL account is defined for the cost type specified on the work completed line. The system will only use the cost type's GL account when no GL account is defined for the phase.
Note: The Costing Method defined for a work order determines the amount that will be updated to Job Cost. If the Costing Method is Actual Cost, the system sets the Total Billable for the work completed line equal to the Actual Cost amount and sends this amount to JC. If the Costing Method is Markup, the system calculates the Total Billable amount using the rate template for the scope and sends this amount to JC. However, because the Total Billable amount can include markups with this method, this may cause the amounts updated to GL to differ.
For example, using the GL account example from above, if the Cost
 Amount is $1000 and the Total Billable is $1500, the GL account updates would be as
 follows:
