---
title: "About Approval Limits | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/about-approval-limits"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/about-approval-limits"
---

# About Approval Limits

You can set up approval limits for workflow processes to control how much a role or user can approve on purchase orders and subcontracts.

When you assign an approval limit, the system determines how that limit is applied based on how you set the Approval limit is based off of document total checkbox on the Info tab of the WF Workflow Process form.
For subcontracts, approval limits will always apply to the subcontract total. Therefore, this checkbox defaults as selected and is disabled.
For purchase orders, the following applies:

- If you select the checkbox, the approval limit is applied to the total purchase order. For example, if the approval limit is $25,000, the user/role can approve purchase orders up to $25,000.

- If the checkbox is not selected (purchase orders only), the system applies the approval limit at the item level, based on the item type. The system groups items together by type (job, inventory, expense, or equipment), depending on the Sub Type specified for PO document type (in HQ Roles). For example if the PO document type for the role had a Sub Type of Job and the approval limit is set to #25,000, the approver can approve up to $25,000 of Job type PO items on each purchase order.

## Approval Limits and the Workflow Process

If there is more than one user/role in a step, the approval limit determines which users/roles are included in the workflow process.
For example, if you have multiple users on a single step for a purchase order workflow, but they have different approval limits, not all of the users will be included when a PO item is submitted for approval.
Sequence
Approver Type
User Name
Role
Step
Approval Limit

1
User
Mr. Smith

1
$25,000

2
User
Ms. Brown

1
$50,000

 In this example, the system handles the workflow as follows:

- If a PO item of $20,000 is submitted for approval, only Mr.Smith will be the reviewer/approver of the PO item.

- If a PO item of $30,000 is submitted for approval, both Mr. Smith and Ms. Brown will be included in the workflow are reviewers/approvers.

If you want both Mr. Smith and Ms. Brown to be included as reviewers, you should give them the same approval limit. With the setup below, both Mr.Smith and Ms.Brown will be included as reviewers/approvers.
Sequence
Approver Type
User Name
Role
Step
Approval Limit

1
User
Mr. Smith

1
$25,000

2
User
Ms. Brown

1
$25,000

Note: The function of approval limits is related to the Not Required checkbox. For more information, see [Not Required](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e350--en).

## Approval Limits Override Spending Limits

If a user is entering a Purchase Order or Subcontract, and they are included in an associated workflow process as a reviewer/approver, their approval limit in that workflow process will override their spending limit.
Sequence
Approver Type
User Name
Role
Step
Approval Limit

1
User
Ms. Brown

1
$25,000

2
User
Mr. Smith

1
$50,000

For example, if Ms. Brown is associated with a role that has a spending limit of $10,000, but the workflow process shown above applies to the purchase order she is creating, her approval limit of $25,000 will override her spending limit of $10,000. This means that she will be able to enter POs/PO items up to $25,000 before they will be included in the workflow process.
