---
title: "About the Purchase Order Review/Approval Workflow | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/about-the-purchase-order-reviewapproval-workflow"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/about-the-purchase-order-reviewapproval-workflow"
---

# About the Purchase Order Review/Approval Workflow

If you have the Workflow module and are using the Process Workflow feature, you can require that purchase orders meeting specific criteria go through a review and approval process.

 To enable the review/approval workflow for purchase orders, there are several setup steps you must follow, including, but not limited to, defining spending limits, assigning reviewers to roles, and setting up a minimum of one purchase order workflow. For more information, see [Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature).
 Once set up, each time a purchase order (PO) is entered in PM Purchase Orders, PM Material Detail, or PO Pending Purchase Order the system determines if the PO requires approval based on the PO amount and the spending limits associated with the user who entered the PO.
 If a user is not set up with a spending limit, the PO automatically requires approval. If the PO requires approval, the Workflow Status changes to Approval Required and the PO must be submitted for approval using the Submit for Approval button. All reviewers assigned to the PO are notified (via email or VP message) that a PO is awaiting their review/approval.
 After a reviewer receives a PO review notification, they will use the appropriate Work Center to approve/reject the PO.
Note: If you have Viewpoint Field Management or Viewpoint Financial Controls, you can also approve purchase orders using the Pending PO / Subcontract Review approval page, which you can access from Project Management by selecting Programs > PM Pending PO / SL Review.

 Once you fully approve a PO, the Workflow Status changes to Approved and you can then process the PO via PM Interface. POs that require the review/approval workflow process must be fully approved before you can interface them. If a PO is rejected, it is removed from the workflow process, the Workflow Status changes to Rejected, and the originator is notified of the rejection. The originator must then make the necessary changes and resubmit the PO for approval.
Note: If any user (approver or not) adds a new item to the Non-Interfaced Items tab at any time during the review/approval workflow (submitted, partially approved, fully approved, or interfaced), the system displays a message indicating that adding an item will reset the Workflow. If you select OK, the new item is added, the workflow is set back to Approval Required, and the PO Status is set to 3 - Pending. If you select Cancel, you will be unable to save the new item.

 You can review the progress of a purchase order's review/approval workflow one of two ways:

- Using the PM PO Workflow Item Reviewers form, accessed by selecting the Workflow button after a PO is submitted for approval. This form shows the workflow steps, approvers, approval status, and any comment or notes entered by the reviewer.

- Using the Workflow History tab. This tab displays the history of the purchase order, such as when the PO was submitted for approval, when it was approved or rejected, who the reviewers/approvers were, and any comments/notes entered by reviewers or other employees.

Select the links below for more information about the workflow process.
[Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature)
[Create a Workflow for Purchase Orders Using the PM Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-pm-module)
[Create a Workflow for Purchase Orders Using the PO Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-po-module)
[Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)
[About the Workflow Hierarchy](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/about-the-workflow-hierarchy)
