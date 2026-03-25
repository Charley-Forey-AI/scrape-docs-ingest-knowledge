---
title: "Field Definitions: HQ User Spending Override Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form/field-definitions-hq-user-spending-override-form"
---

# Field Definitions: HQ User Spending Override Form

## User Name

The User Name field on the HQ User Spending Overrides form.
Enter the user for which to assign spending limit overrides. Press F4 to select from a list of users associated the specified role.

Related information

- [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Type

The Type field on the HQ User Spending Overrides form.

From the drop-down, select the type of document to which the spending limit applies.

- PO - Purchase Order

- SL - Subcontracts

Related information

- [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Sub Type

The Sub Type field on the HQ User Spending Overrides form.

Select the line type for the specified document type to which this spending limit applies.
Purchase Order

- Job

- Inventory

- Expense

- Equipment

- All - Select this option if the spending limit does not apply to a specific line type.

 For example, select Job if the spending limit applies to a purchase order item that is associated with a job/project.
SubcontractThis field automatically defaults to Job, which is the only valid option for this document type. Selecting any other sub type will produce an error.
For detailed descriptions of line types, see the [Type](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-000309bb--en) F1 help for purchase orders or the [Type](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form/field-definitions-sl-subcontract-entry-form#ID-0003f228--en) F1 help for subcontracts.

Related information

- [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Spending Limit

The Spending Limit field on the HQ User Spending Overrides form.

Enter the spending limit for the selected document type/sub type; that is, the amount this user can spend without requiring the review/approval workflow process.
How this spending limit is applied depends on the Approval and spending limits based on document total checkbox in WF Workflow Process.
 For example, say you set the user's limit to $15,000 for the Purchase Order document type, with a Sub Type of Job. If the Approval and spending limits based on document total checkbox is selected for the purchase order workflow process, this user can spend up to $15,000 on the total purchase order without requiring the review/approval workflow process. If the purchase order total equals or exceeds $15,000, it must go through the review/approval workflow process.
If the Approval and spending limits based on document total checkbox is not selected, the spending limit is applied to the combined total of purchase order items of the same type. So in the example above, the user can spend up to $15,000 total on purchase order items with a line type of Job without having them go through the review/approval process. If the combined total of job purchase order items equals or exceeds $15,000, the purchase order/items must go through the review/approval workflow process.
For more information, see [Approval and spending limits based on document total](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e0ab--en).

Related information

- [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Threshold

The Threshold field on the HQ User Spending Overrides form.

If this user is allowed to exceed the spending limit for the specified role, enter the percentage by which the spending limit can be exceeded.
For example if you set the spending limit to $50,000 and the threshold to 2.00% for POs, the user can spend up to $51,000 on a purchase order associated with this role. This means that if a purchase order were written for $48,000 but taxes, freight, and additional charges pushed the total cost to $50,500, the user can still approve the PO because it is within the threshold.
Leave the percentage set to 0.00 if this user is not allowed to exceed the spending limit for this role.

Related information

- [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)
