---
title: "GL Updates: Work Completed Purchase | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-purchase"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-purchase"
---

# GL Updates: Work Completed Purchase

The following discusses the updates to General Ledger when posting and invoicing work completed purchase lines.
Work completed purchase lines are created automatically when you enter and post PO items for an SM work order using SM Purchase Order Entry or PO Purchase Order Entry, or distribute PO items to an SM work order via PO Item Distribution.
Although posting a PO batch generates work
 completed lines, no GL updates occur. The update to GL occurs when you receive the
 purchase order in PO Receipts Entry. If the GL Expense Interface option in PO Company
 Parameters is set to Summary or Detail, the system creates a GL entry for the Cost or
 Cost WIP account (depending on whether the call type is tracking WIP) specified for the
 work completed line. In addition, the system creates an offsetting entry to the Accrual
 account defined in PO Company Parameters.
For example, if you are tracking WIP for a call
 type, the update to GL for purchased materials would be as follows:
Note: If you set the update level to No Update or if you are not
 expensing receipts (Update GL/Sub-Ledgers on Receipt box is not checked in PO Company
 Parameters), no updates to GL will occur; however, the system still creates the batch
 reports with the same information that would be included if you were updating GL.
Note: If you are not receiving purchase orders in PO
 Receipts Entry (i.e. the Receiving box is unchecked for the PO
 item), receiving will occur at the time you invoice the purchase order in AP Transaction
 Entry.
When you invoice the purchase order in AP
 Transaction Entry, the system then backs out the existing cost and accrual entries, and
 then adds entries as follows:

## Job Work Orders

For job-related SM work orders, the system
 handles posting of purchase orders in the same manner as it does for non-job work
 orders. A work completed purchase line is created, but no updates to GL will occur.
 However, the system will update committed costs to Job Cost.
When you receive the purchase order (in PO
 Receipts Entry), the system updates the Cost or Cost WIP account (depending on whether
 the call type is tracking WIP) specified for the work completed line, and creates an
 offsetting entry to the Accrual account defined in PO Company Parameters.
However, unlike the other transaction types
 (equipment, labor, miscellaneous, and inventory), if you are interfacing to Job Cost
 (the JC interface box is checked in SM Company Parameters), the additional
 updates that occur for job-related work orders will only occur at the time you invoice
 the purchase order in AP Transaction Entry. In this case, the system will create
 additional entries to the GL account defined for the phase or cost type in JC
 Departments for the job's department, as well as the Revenue or Revenue WIP account (if
 tracking WIP) specified for the work completed line.
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
