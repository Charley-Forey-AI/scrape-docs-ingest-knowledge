---
title: "Process a Pending Purchase Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/process-a-pending-purchase-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/process-a-pending-purchase-order"
---

# Process a Pending Purchase Order

If you are using the Workflow module, you can create and process pending purchase orders using the PO Pending Purchase Orders form.

1. Enter the pending purchase order.

1. In PO Pending Purchase Order, enter the PO and PO item
 information.Note: This is just like entering a PO using the PO Purchase Orders Entry
 form, but the pending PO will not be processed in a batch until
 after it is approved. One exception is that the PO Pending Purchase
 Orders form also does not currently include SM Work Order type PO
 items.

1. If the PO needs to be reviewed/approved, the Workflow
 Status field displays Approval Required. If a
 workflow applies, the Workflow and Submit for Approval buttons are
 enabled. These buttons are used to process the PO.

1. Select the Workflow button to view the users that need to review/approve the PO.
 For more information about this process, see [PO Workflow Item Reviewers / PO Pending Reviewers form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-workflow-item-reviewers--po-pending-reviewers-form).

1. Notify the reviewer/approver.

1. Select the Submit for
 Approval button to submit the PO for approval. The users
 that need to review/approve the PO will be notified. Note: If you receive a "There are no approvers with a limit high enough
 to approve this PO" error message, contact the administrator that
 creates the workflows.

1. Once you submit the PO for approval, you can track its progress in
 several ways:

- Workflow History tab - This tab displays the history of the purchase order, such as when the PO was submitted for approval, when it was approved or rejected, who the reviewers/approvers were, and any comments/notes entered by reviewers or other employees.

- Work Center -
 Open the My Documents in Workflow query in the Work Center that
 you use to process purchase orders. This displays a list of
 purchase orders that you have created, and their progress in a
 workflow.

- Workflow button
 - Select the Workflow button on the form that was used to create the PO.
 This launches the PO Workflow Item Reviewers form, which
 displays the progress of the PO in the workflow process and any
 comments that have been entered.

1. If needed, enter comments for a reviewer. You can do this by selecting
 the Workflow button,
 double-clicking in the Comments field on the form that displays, and then entering the
 comments.

1. If needed, you can make changes to the PO after it has been submitted. However,
 if you change the items on a PO, the PO is removed from the workflow
 process and must be resubmitted for approval once your changes are
 complete.

1. Review and approve the PO.

1. Open the Work Center that you use to review/approve purchase orders.For information about adding a Work Center for reviewing/approving
 POs, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

1. Open the My Documents to Review option in the Work Center menu. A list
 of POs that you need to approve/review will display. This is a list of
 POs, not PO items.

1. You can now perform any of the following actions:

- View the PO Items - Double-click on a PO to drill down to the
 items.

- Edit the purchase order - Choose the PO from the list and select
 Open. The PO is opened in the form that was used to create it.
 Once you complete your changes, resubmit the PO for
 approval.

- Approve the purchase order - From the Workflow Document Review,
 choose the PO to approve and select Approve
 Document (). This automatically approves all
 items on the PO to which you are assigned as a reviewer.

- Reject the purchase order - From the Workflow Document Review,
 choose the PO to approve and select Document
 (). This automatically rejects all
 items on the PO to which you are assigned as a reviewer.

- Add comments - To add a comment, double-click on a PO in the My
 Documents to Review query in the Work Center, choose the PO item,
 and select Add Comments (). This opens the WF Document Review
 Edit form.

- Add attachments - From the My Documents to Review query, double-click on a PO and then select a PO item that displays. Select
 Attachments () to add an attachment to the
 selected PO item.

Note: Attachments added here are associated with a specific PO item and
 reviewer/approver, and will only display on the WF Document Review
 Edit form. To ensure attachments are not deleted when changes are
 made to a PO/PO Item, select the Retain attachments after record
 delete checkbox on the DM Attachment Options form.
 If the PO is edited, all attachments added here become stand-alone
 attachments, which you can view using the DM Attachment Index Search
 form and filtering by the Stand Alone option.

1. Process the PO

1. Open the approved PO in the PO Pending Purchase Orders form.

1. Verify that Approved
 displays in the Workflow Status field at the bottom of the form.

1. Select Process. This
 will open the Batch Selection form. The Batch Selection form opens.

1. Select to process the PO in an existing PO batch or create a new
 batch.Tip: You can exit this form if you do not want to post the
 batch right away. For example you can add multiple POs to a single
 batch, and then validate and post them all at once.

1. Validate the batch, preview/print the batch reports, and then post the
 batch.

The purchase order is processed and can only be
 changed by pulling it into a PO Purchase Order Entry batch.
