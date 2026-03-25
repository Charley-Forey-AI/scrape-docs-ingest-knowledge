---
title: "About the Subcontract Review/Approval Workflow | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/about-the-subcontract-reviewapproval-workflow"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/about-the-subcontract-reviewapproval-workflow"
---

# About the Subcontract Review/Approval Workflow

If you have the Workflow module and are using the Process Workflow feature, you can require that subcontracts meeting specific criteria go through a review and approval process.

 To enable the review/approval workflow for subcontracts, there are several setup steps you must follow, including, but not limited to, defining spending limits, assigning reviewers to roles, and setting up one or more subcontract workflows. For more information, see [Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature).
 Once set up, each time a subcontract is entered, the system determines if the subcontract requires approval based on the subcontract amount and the spending limits associated with the user who entered the subcontract.
 If a user is not set up with a spending limit, the subcontract automatically requires approval. If a subcontract requires approval, the Workflow Status changes to Approval Required and the subcontract must be submitted for approval using the Submit for Approval button. All reviewers assigned to the subcontract are notified (via email or VP message) that a subcontract is awaiting their review/approval.
 After a reviewer receives a subcontract review notification, they will use the appropriate Work Center to approve/reject the subcontract.
Note: If you have Viewpoint Field Management or Viewpoint Financial Controls, you can also approve subcontracts using the Pending PO / Subcontract Review approval page, which you can access:

- from Project Management by selecting Programs > PM Pending PO / SL Review, or

-  from Subcontract Ledger by selecting Programs > SL Subcontract Review.

 Once you fully approve a subcontract, the Workflow Status changes to Approved and you can then process the subcontract via PM Interface. Subcontracts that require the review/approval workflow process must be fully approved before you can interface them. If a subcontract is rejected, it is removed from the workflow process, the Workflow Status changes to Rejected, and the originator is notified of the rejection. The originator must then make the necessary changes and resubmit the subcontract for approval.
Note: If any user (approver or not) adds a new item to the Non-Interfaced Items tab at any time during the review/approval workflow (submitted, partially approved, fully approved, or interfaced), the system displays a message indicating that adding an item will reset the Workflow. If you select OK, the new item is added, the workflow is set back to Approval Required, and the PO Status is set to 3 - Pending. If you select Cancel, you will be unable to save the new item.

 You can review the progress of a subcontract's review/approval workflow one of two ways:

- Using the PM SL Workflow Item Reviewers form, accessed by selecting the Workflow button after a subcontract is submitted for approval. This form shows the workflow steps, approvers, approval status, and any comments or notes entered by the reviewer.

- Using the Workflow History tab. This tab displays the history of the subcontract, such as when the subcontract was submitted for approval, when it was approved or rejected, who the reviewers/approvers were, and any comments/notes entered by reviewers or other employees.

 Select the links below for more information about the workflow process.
[Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature)
[Initiate the Review/Approval Workflow for Subcontracts](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/initiate-the-reviewapproval-workflow-for-subcontracts)
[Review Subcontracts Submitted for Approval](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/review-subcontracts-submitted-for-approval)
