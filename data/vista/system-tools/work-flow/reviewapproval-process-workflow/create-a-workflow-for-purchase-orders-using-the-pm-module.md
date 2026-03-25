---
title: "Create a Workflow for Purchase Orders Using the PM Module | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-pm-module"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-pm-module"
---

# Create a Workflow for Purchase Orders Using the PM Module

The Process Workflow feature is used to force purchase
 orders that meet a defined criteria to follow a specific approval/review process. You can
 create and use a workflow from the PM module.
In order to create workflows for purchase orders,

- you must have the workflow module and,

- you must have set up the process workflow feature (that
 is, set up roles and workflows and assigned them to specific companies
 and/or jobs/projects). For more information, see [Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature).

1. Create the PO and PO items. You can do this using
 any of the following forms.

- Estimate / Purchase Details tab on the
 [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) form

- [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form) - You can use this form
 to create PO items and assign them to a PO

- Non-Interfaced tab of [PM Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form) form - You can use this
 form to create the PO and PO items at the same time

1. Open the PO in the PM Purchase Orders form. The
 panel at the bottom of the form is used to process the purchase order using the
 Process Workflow feature. This panel only displays if you have the Workflow
 module.

1. Select the Workflow button to view the
 users that need to review/approve the PO.

1. Return to the PM Purchase Orders form and select
 the Submit for
 Approval button. The system sends a notification to all users
 that need to review/approve the PO.

1. Once the PO has been submitted for approval, you
 can view its progress in several ways:

- Workflow History
 tab - Comments display on the Workflow History tab on the
 form used to create the PO, for example the [PM Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form) or [PO Pending Purchase Orders](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-pending-purchase-orders-form) form. This tab displays the history of the purchase order, such as when the PO was submitted for approval, when it was approved or rejected, who the reviewers/approvers were, and any comments/notes entered by reviewers or other employees.

- Work Center - Open the My
 Documents in Workflow query in the Work Center that you use to process
 purchase orders. This displays a list of purchase orders that you have
 created and their progress in a workflow.

- Workflow button - Select
 the Workflow
 button on the form that was used to create the PO (PM Purchase Orders or PO
 Pending Change Orders). The [PO Workflow Item Reviewers](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-workflow-item-reviewers--po-pending-reviewers-form) form opens and
 displays the progress of the PO in the workflow process, along with any
 comments that have been entered.

1. Optional: If you want to enter comments on a PO item for the
 reviewer/approver, select the Workflow button, double-click in the Comments field on the form
 that displays, and then enter the comments. The reviewer/approver will see these
 comments when they review/approve the PO item.

1. Optional: You can make changes to the PO after it has been
 submitted, but changing the PO items will remove the PO from the workflow
 process. Once you have made your changes, select the Submit for Approval button to
 resubmit it for review/approval.Note: If the PO has already been approved, the status of
 the PO will be Approved and you won't be able to change it.

1. Open the Work Center that you use to
 review/approve purchase orders and then open the My Documents to Review option
 in the Work Center menu. A list of POs that you need to approve/review will
 display. Perform an action:

- View the PO Items - Double-click on a PO
 to drill down and view the PO items.

- Open/Edit a purchase order - To open or
 edit a PO/PO item, choose it from the list and select the Open () icon. This will open the PO in the form that
 was used to create it. For example if the PO was entered using the PO
 Pending Purchase Orders form, the PO will open in that form. When you edit
 the items on a PO, you take ownership of the PO and become its originator.
 This means that you are pulling the PO out of the current work flow. If the
 PO needs to be processed in a workflow after you make the changes, you will
 have to submit the PO for approval just like if you were the one that
 originally created the PO.

- Approve a purchase order - When you
 approve a PO, you approve all of the PO items where you are set up as a
 reviewer/approver. This means that you cannot approve/reject specific items
 on the PO.

- Approve the PO. From the Workflow
 Document Review, select a PO that needs to be approved and select the
 Approve Document () icon. This will approve all of the PO items on
 the purchase order where you are set up as an approver. If there are items
 on the PO that need to be approved by others, the PO will change to the
 "Partially Approved" status. You can see this by opening the PO /PO item in
 the form that was used to create it, and looking in the Workflow Status
 field.

- Reject a PO - When you reject a PO, you
 reject the entire PO, not just the PO items where you are set up as a
 reviewer/approver. This means you cannot reject specific items on a PO. If
 any portion of the PO is rejected, the originator of the PO receives a
 message that the PO has been rejected and the entire PO is pulled out of the
 workflow process. From the Workflow Document Review, select a PO that needs
 to be rejected and select the Document () icon. This will reject all of the PO items on
 the purchase order, and the user that created the PO will receive a message
 that the PO has been rejected.

- Add a comment - To add a comment,
 double-click on a PO in the My Documents to Review query in the Work Center,
 and then select a PO item and select the Add Comments () icon. This will open the [WF Document Review Edit ](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-document-review-edit) form.

- Add an attachment - You can add
 attachments to PO items directly from a Work Center. From the My Documents
 to Review query, double-click on a PO and then select a PO item that
 displays. Select on the Attachments () icon at the top of the grid to add an
 attachment to the selected PO item.

Note: If you are using using the PO/SL review feature in
 Vista Web, you
 can also review and approve purchase orders via the Approval menu. For more
 information, see [Pending PO / Subcontract
 Review](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FM_000034:FM:FM).

1. Process the PO.

1. Open the PO in the PM Purchase Orders
 form.

1. Verify that the Approved checkbox is
 selected and that the Workflow Status field is set to Approved.Note: The system automatically selects the
 Approved checkbox when the PO is approved in the
 Work Center.

1. Open the [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) form. The approved PO will
 now display on this form.

1. Interface the PO to send it to the PO
 module.
