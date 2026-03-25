---
title: "Create a Workflow for Purchase Orders Using the PO Module | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-po-module"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-po-module"
---

# Create a Workflow for Purchase Orders Using the PO Module

The Process Workflow feature is used to force purchase
 orders that meet a defined criteria to follow a specific approval/review process. You can
 create and use a workflow from the PO module.
In order to create workflows for purchase
 orders,

- you must have the Workflow module and,

- you must have set up the process workflow feature (that
 is, set up roles and workflows and assigned them to specific companies
 and/or jobs/projects). For more information, see [Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature).

1. Open the PO Pending Purchase Order form and enter
 the PO header and item information.. This is just like entering a PO using
 the PO Purchase Orders Entry form, but the pending PO will not be processed in a
 batch until after it is approved.

1. Select the Workflow button to view the
 users that need to review/approve the PO.

1. Select the Submit for Approval button to
 submit the PO for approval.  Notifications are sent to
 the users that need to review/approve the PO.

1. Once the PO has been submitted for approval, you
 can view its progress in several ways:

- Workflow History tab -
 This tab displays the history of the purchase order, such as when the PO was submitted for approval, when it was approved or rejected, who the reviewers/approvers were, and any comments/notes entered by reviewers or other employees.

- Work Center - Open the My
 Documents in Workflow query in the Work Center that you use to process
 purchase orders. This displays a list of purchase orders that you have
 created, and their progress in a workflow.

- Workflow button - Select
 the Workflow
 button on the form that was used to create the PO. This will launch the
 [PO Workflow Item Reviewers](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-workflow-item-reviewers--po-pending-reviewers-form) form, which
 displays the progress of the PO in the workflow process and any comments
 that have been entered.

1. Optional: Enter comments for the reviewer on a PO item. If you
 want to enter comments on a PO item for the reviewer/approver, select the
 Workflow button,
 double-click in the Comments field on the form that displays, and then enter the
 comments. The reviewer/approver will see these comments when they review/approve
 the PO item.

1. Optional: You can make changes to the PO after it has been
 submitted, but changing the PO items will remove the PO from the workflow
 process. Once you have made your changes, select the Submit for Approval button to
 resubmit it for review/approval.

1. Review the PO. Open the Work Center that you use
 to review/approve purchase orders. Then select the My Documents to Review query
 in the Work Center menu, which displays a list of POs (not PO Items) that you
 need to approve/review. Perform one or more of the following actions:

- View the PO Items - Double-click on a PO
 to drill down and view the PO items.

- Open/Edit a purchase order - To open or
 edit a PO/PO item, choose it from the list and select the Open () icon. This will open the PO in the form that
 was used to create it.Note: Changing a PO/Item removes
 it from the workflow process and you will need to resubmit it for
 approval.

- Approve a PO - From the My Documents to
 Review panel, choose the PO to approve and select the Approve Document
 () icon. This will approve all of the PO items on
 the purchase order where you are set up as an approver.

- Reject a PO - From the My Documents to
 Review panel, choose the PO to reject and select the Reject Document () icon. This will reject all of the PO items on
 the purchase order, and the user that created the PO will receive a message
 that the PO has been rejected.

- Add a comment - To add a comment, choose
 the PO in the My Documents to Review panel and select the Add Comments
 () icon. If there are multiple items on the PO,
 you can double-click on the PO in the My Documents to Review panel to
 display the items. Then choose a PO item and select the Add Comments () icon. This will open the WF Document Review
 Edit form.

- Add an attachment - You can add
 attachments to PO items directly from a Work Center. From the My Documents
 to Review panel, double-click on a PO and then select a PO item. Select the
 Attachments () icon at the top of the grid to add an
 attachment to the selected PO item.

Note: If you are using using the PO/SL review feature in
 Vista Web, you
 can also review and approve purchase orders via the Approval menu. For more
 information, see [Pending PO / Subcontract
 Review](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FM_000034:FM:FM).

1. Process the PO.

1. Open the approved PO in the PO Pending
 Purchase Orders form.

1. Verify that the Approved checkbox is
 selected and that the Workflow Status field is set to Approved.Note: The system automatically selects the
 Approved checkbox when the PO is approved in the
 Work Center.

1. Select the Process button. The Batch Selection
 form opens.

1. Open a batch using one of the following
 options:

- Choose the Create a new
 batch option and select OK.

- Choose the Use an existing
 batch option and select the desired batch from
 the Unposted Batches grid. Then select OK.

The PO Batch process
 form opens.

1. Validate the batch, preview/print the
 batch reports, and then post the batch. If there are errors in the
 batch, you can fix them by opening the batch using the PO Purchase Order
 Entry form.
