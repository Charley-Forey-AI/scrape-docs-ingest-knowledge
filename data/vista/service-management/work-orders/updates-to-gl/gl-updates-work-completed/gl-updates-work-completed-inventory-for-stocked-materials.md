---
title: "GL Updates: Work Completed Inventory for Stocked Materials | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-stocked-materials"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-stocked-materials"
---

# GL Updates: Work Completed Inventory for Stocked Materials

The system updates the General Ledger (GL) for work completed
 inventory lines based on the cost type category associated with the work completed line, the
 cost accounts defined in SM Departments, and the offset account defined for the inventory
 location.
When you capture work completed for stocked materials on a work order, the system automatically creates a batch once you save the work completed line and move off the record. If you selected the Auto Post New Work Completed checkbox in SM Company Parameters, the system also posts the batch (behind the scenes). If you did not select the Auto Post New Work Completed checkbox, you must post the batch using the SM Work Order Cost Posting form.
If you are interfacing material usage to the Inventory module (that is, you selected the IN interface checkbox in SM Company Parameters), the system posts the material usage to IN. If you are not interfacing material usage to IN, you can still post the batch, but no module update occurs.
If the GL Usage Interface option in SM
 Company Parameters is set to Summary or Detail, the system creates a GL entry for the
 Cost or Cost WIP account (depending on whether the call type is tracking WIP) specified
 for the work completed line. In addition, the system creates an offsetting entry to the
 Inventory account defined for the location in either IN Location Category Override
 (based on material category) or IN Locations (if no category override exists).
For example, if you are tracking WIP for a call
 type, the update to GL for work completed inventory would be as follows:
If you set the GL Usage Interface level to No
 Update, no updates to GL will occur; however, the system still creates the batch reports
 with the same information that would be included if you were updating GL.

## Job Work Orders

If the work order is job-related and you
 have checked the JC interface box in SM Company
 Parameters, the system will update the Total Billable for the work completed line as
 cost to Job Cost and create GL entries using the Cost or Cost WIP account (if
 tracking WIP) specified for the work completed line. An offsetting entry will be
 created for the Inventory account defined for the location in either IN Location
 Category Override or IN Locations (if no category override exists). In addition, the
 system will create entries to the GL account defined for the phase or cost type in
 JC Departments for the job's department, as well as the Revenue or Revenue WIP
 account (if tracking WIP) specified for the work completed line.
So for example, if you are tracking WIP
 for a call type, the update to GL would be as follows:
* If a GL account is defined for the phase (on the work order scope), the system will debit the phase's GL account, regardless of whether a GL account is defined for the cost type specified on the work completed line. The system will only use the cost type's GL account when no GL account is defined for the phase.
Note: The Costing Method defined for a work order determines the amount that will be updated to Job Cost. If the Costing Method is Actual Cost, the system sets the Total Billable for the work completed line equal to the Actual Cost amount and sends this amount to JC. If the Costing Method is Markup, the system calculates the Total Billable amount using the rate template for the scope and sends this amount to JC. However, because the Total Billable amount can include markups with this method, this may cause the amounts updated to GL to differ.
For example, using the GL account
 example from above, if the Cost Amount is $1000 and the Total Billable is $1500, the
 GL account updates would be as follows:
