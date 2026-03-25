---
title: "PM Subcontracts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/pm-subcontracts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/pm-subcontracts-form"
---

# PM Subcontracts Form

Use this form to create and maintain project subcontracts.
Each subcontract you set up defines the scope of work and/or materials that are being provided by a specific subcontractor (vendor). This is done by adding items to the subcontract. You can add subcontract items manually via the Non-Interfaced Item tab, using the PM Subcontract Detail form, or by adding subcontract items to a change order in PM Subcontract Change Orders.
All subcontract items, regardless of how they are added, appear on the Non-Interfaced tab. You can modify these items as needed, as long as you have not yet interfaced them. Once you interface them, they are moved to the Interfaced tab and cannot be edited. If you have entered notes for a subcontract item, you can edit them as needed, even after the item is interfaced. However, once you close the subcontract, you can no longer edit any information, including notes.

## Inclusions/Exclusions

The Inclusions/Exclusions tab allows you to record any inclusions or exclusions associated with a subcontract. If you want them included on the PM Subcontracts report (Reports > PM Subcontracts), select the Print Inclusions/Exclusions checkbox.
If you have the Pre-Construction module, inclusions or exclusions on subcontract detail that was created from the PC module will also display on this tab once that subcontract detail is associated with a subcontract. For information about creating subcontract detail from the PC module, see [Create PM Subcontract Detail](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/potential-project-conversion/create-pm-subcontract-detail).
Note: You can also view inclusions and exclusions entered on this tab using the Inclusions/ Exclusions tab on the SL Subcontract Entry form once you interface the subcontract using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).

## Available Estimate / Non-Interfaced / Remaining Estimate

These display-only fields are only visible when you select the Non-Interfaced Items tab, and show estimate information for the selected sequence. These values are calculated as follows:
FieldCalculation
Available EstimateCurrent Estimated Cost - Actual Cost - Remaining Committed Cost + Non-Interfaced Estimated Cost
Non-InterfacedThis is a more complex calculation that takes a number of factors into consideration. However, in general, this calculation is the sum of the amount and taxes from PM Subcontract Detail and based on certain factors, the subtraction of some SL Item and SL Change Order detail costs (which can include taxes), plus Non-Interfaced Estimated.
Remaining EstimateAvailable Estimate - Non-Interfaced

## Distribution Audit

Use the Distribution Audit () feature to view:

- All of the documents generated using the Create and Send feature - for example change orders, RFIs, drawing logs, project issues, etc.

- Any communications sent using the Create and Send feature - for example if you resend a document to a project contact.

For more information, see [PM Document Distribution Audit Form](/en/vista/vista/project-management/document-tracking/pm-document-distribution-audit-form).

## Review/Approval Workflow

If you have the Workflow module and are using the Process Workflow feature, the system determines when a subcontract requires approval based on the subcontract amount and the spending limits associated with the user who entered the subcontract. If a user is not set up with a spending limit, the subcontract automatically requires approval.
If a subcontract requires approval, the Workflow Status changes to Approval Required and you must then submit the subcontract for approval using the Submit for Approval button. All reviewers assigned to the subcontract are notified (via email or VP message) that a subcontract is awaiting their review/approval.
After a reviewer receives a subcontract review notification, they will use the appropriate Work Center to approve/reject the subcontract. Once the subcontract is fully approved, the Workflow Status changes to Approved and you can then process the subcontract via PM Interface.
Note: Subcontracts that require the review/approval workflow process must be fully approved before you can interface them.

If a subcontract is rejected, it is removed from the workflow process, the Workflow Status changes to Rejected, and the originator is notified of the rejection. The originator must then make the necessary changes and resubmit the subcontract for approval.
Note: If a subcontract requires approval and any user (approver or not) adds a new item to the Non-Interfaced Items tab at any time during the review/approval workflow (submitted, partially approved, fully approved, or interfaced), the system displays a message indicating that adding an item will reset the Workflow. If you select OK, the new item is added, the workflow is set back to Approval Required, and the SL Status is set to 3 - Pending. If you select Cancel, you will be unable to save the new item.

You can review the progress of a subcontract's review/approval workflow one of two ways:

- Using the PM SL Workflow Item Reviewers form, accessed by selecting the Workflow button after a subcontract is submitted for approval. This form shows the workflow steps, approvers, approval status, and any comment or notes entered by the reviewer.

- Using the Workflow History tab. This tab displays the history of the subcontract, such as when the subcontract was submitted for approval, when it was approved or rejected, who the reviewers/approvers were, and any comments/notes entered by reviewers or other employees.

Select the links below for more information about the workflow process.
[Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature)
[Initiate the Review/Approval Workflow for Subcontracts](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/initiate-the-reviewapproval-workflow-for-subcontracts)
[Review Subcontracts Submitted for Approval](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/review-subcontracts-submitted-for-approval)
[About Subcontract Buyout](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)
[About Subcontract Buyout](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)
