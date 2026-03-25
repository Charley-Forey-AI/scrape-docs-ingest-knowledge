---
title: "GL Updates: Work Completed Inventory for Non-Stocked Materials | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-non-stocked-materials"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-non-stocked-materials"
---

# GL Updates: Work Completed Inventory for Non-Stocked Materials

The following discusses the updates to General Ledger when
 posting and invoicing work completed lines for non-stocked materials.
Batch posting for non-stocked materials (those in HQ Materials only) and non-standard materials (those not in IN or HQ) is handled a little differently than batches posted for stocked materials in that the system creates and posts a miscellaneous batch rather than an inventory batch. Like the batches posted for miscellaneous work completed lines, the expenses for these materials are not directly related to any module, so no module interface will occur.
If you are auto-posting batches (that is, you selected the Auto Post New Work Completed checkbox in SM Company Parameters), the system posts the batch automatically once you move off the Work Completed tab. If you did not select the Auto Post New Work Completed checkbox, you must manually post the batch using the SM Work Order Cost Posting form.
If you set the GL Usage Interface option in SM Company Parameters to Summary or Detail, the system creates a GL entry for the Cost account or Cost WIP account (if tracking WIP) specified for the work completed line. The system also create an offsetting entry as follows:

- If you specified an SM cost type for the work completed line, the system uses the override offset account defined for the cost type in SM Departments, Cost Types tab.

- If no override offset account is defined for the cost type or if you did not specify a cost type for the work completed line, the system uses the miscellaneous cost offset account defined for the department in SM Departments, Info tab.For example, if you are tracking WIP for a call type and you entered an SM Cost Type, the update to GL would be as follows:

## Job Work Orders

If the work order is job-related and you have selected the JC interface checkbox in SM Company Parameters, the system updates the Total Billable for the work completed line as cost to Job Cost and creates GL entries using the Cost account or Cost WIP account (if tracking WIP) specified for the work completed line. The system also:

- creates an offsetting entry to the override cost offset account defined for the SM cost type in SM Departments (Cost Types tab). If no override account is defined for the SM cost type or if no SM cost type is specified on the work completed line, creates an offsetting entry to the miscellaneous cost offset account defined for the department (SM Departments, Info tab).

- creates an entry to the GL account defined for the phase or cost type in JC
 Departments for the job's department.

- creates an entry to the Revenue account or Revenue WIP account (if tracking WIP) specified for the work completed line.

So for example, if you are tracking WIP for a call type, the update to GL would be as follows:

*If a GL account is defined for the phase (on the work order scope), the system will debit the phase's GL account, regardless of whether a GL account is defined for the cost type specified on the work completed line. The system will only use the cost type's GL account when no GL account is defined for the phase.
The Costing Method defined for a work order determines the amount that will be updated to Job Cost. If the Costing Method is Actual Cost, the system sets the Total Billable for the work completed line equal to the Actual Cost amount and sends this amount to JC. If the Costing Method is Markup, the system calculates the Total Billable amount using the rate template for the scope and sends this amount to JC. However, because the Total Billable amount can include markups with this method, this may cause the amounts updated to GL to differ
For example, using the GL account example from above, if the Cost Amount is $1000 and the Total Billable is $1500, the GL account updates would be as follows:

Related concepts

- [Updates to GL](/en/vista/vista/service-management/work-orders/updates-to-gl)

- [GL Updates: Work Completed Inventory for Stocked Materials](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-stocked-materials)

- [SM Work Order Cost Posting Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-cost-posting-form)
