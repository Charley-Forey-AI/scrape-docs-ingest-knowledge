---
title: "Review/Approval Process Workflow | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow"
---

# Review/Approval Process Workflow

The Process Workflow feature is used to force purchase orders and subcontracts that meet a defined criteria to follow a specific review/approval process.

For example, if purchase orders and/or subcontracts that exceed $25,000 need to be reviewed and approved before they are sent to accounting, you can set up the application to enforce that workflow/approval process.
The Process Workflow feature requires the Workflow module. The Workflow module is used to set up the review/approval workflows for purchase orders and subcontracts, as well as to optionally set up Notifier Jobs for sending notifications throughout the review approval process.
Note: The Process Workflow feature also requires setup in other modules. For more information, see [Set up the Process Workflow Feature](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/set-up-the-process-workflow-feature).

When you set up a workflow, you specify the document type (purchase order or subcontract) and set up review/approval steps to determine who will review/approve the PO/SL and in what sequence. Other setup options allow you to define the length of time for each approval step, when to send reminder notifications, and how to apply approval and spending limits (purchase orders only).
You can assign workflows to apply to all companies (in HQ Company Setup) or you can apply them to specific modules/companies, and/or specific projects/jobs, equipment departments (POs only) and inventory locations (POs only). However, you must assign workflows to at least one of these levels to enable the review/approval workflow process.
Once set up, the workflow process only applies to purchase orders and subcontracts as follows:

- Purchase Orders - Applies only to purchase orders created using the PM Purchase Orders or PO Pending Purchase Orders forms. It does not apply to POs created using the PO Purchase Order Entry form, PO change orders created using the PM PO Change Orders form, or other forms in the application that relate to purchase orders. A workflow is applied to a PO item, not to the entire PO. The PO item type can determine which workflow is applied. For example, you can set up different workflows for job, inventory, equipment, or expense type PO items.

- Subcontracts - Applies only to subcontracts created using the PM Subcontracts or PM Subcontract Detail forms; it does not apply to subcontracts entered in SL Subcontract Entry.Workflows are applied to the entire Subcontract. Unlike POs, you cannot set up different workflows by item type, since subcontracts are only associated with jobs.

The following diagram provides an overview of the Process Workflow feature, using purchase orders as the example.

With the exception of the forms used to enter subcontracts, the review/approval workflow process is the same.
Note: If the purchase order or subcontract requires approval and any user (approver or not) adds a new item to the Non-Interfaced Items tab at any time during the review/approval workflow (submitted, partially approved, fully approved, or interfaced), the system displays a message indicating that adding an item will reset the Workflow. If you select OK, the new item is added, the workflow is set back to Approval Required, and the PO or SL Status is set to 3 - Pending. If you select Cancel, you will be unable to save the new item.

Note: If you are using the PO/SL review feature in Vista Web, reviewers can also review and approve pending purchase orders and subcontracts via the Approval menu. For more information, see [Pending PO / Subcontract Review](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FM_000034:FM:FM).

For more information, select the following links:
[Create a Workflow for Purchase Orders Using the PM Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-pm-module)
[Create a Workflow for Purchase Orders Using the PO Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-po-module)
[Initiate the Review/Approval Workflow for Subcontracts](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/initiate-the-reviewapproval-workflow-for-subcontracts)
[Review Subcontracts Submitted for Approval](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/review-subcontracts-submitted-for-approval)

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)

- [User Name](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form#ID-0000f889--en)

- [Type](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form#ID-0000f896--en)

- [Sub Type](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form#ID-0000f8a1--en)

- [Spending Limit](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form#ID-0000f8b3--en)

- [Threshold](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form#ID-0000f8bd--en)
