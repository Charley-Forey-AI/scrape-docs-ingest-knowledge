---
title: "Create a Workflow Approval Process | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-approval-process"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-approval-process"
---

# Create a Workflow Approval Process

You can use the WF Workflow Process form to create and maintain the approval/review processes used in the Process Workflow feature.
Follow the steps below to create a new approval process. If a similar approval process already exists, you can save time if you copy the existing process and then modify the copy. For more information, see [WF Process Copy](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-process-copy).

1. Open the WF Workflow Process form.

1. Select the New Record icon in the toolbar and then enter a name for the new process in the Process field.

1. In the Description field, enter a description of the process.

1. From the Document Type drop-down, select one of the following:

- PO - Purchase Order

- SL - Subcontracts

You may leave this field blank if this is a generic workflow; that is, a workflow not specific to a document type. For more information, see [Document Type](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e09f--en).

1. If you want approval and spending limits applied to the document total (rather than at the item level), select the Approval and spending limits based on document total checkbox.Note: This checkbox applies to PO document types only. For subcontracts, approval and spending limits are always based on the document total.

For more information about this checkbox, see [Approval and spending limits based on document total](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e0ab--en).

1. If this workflow process is ready for use, leave the Active checkbox selected (default setting).

1. Select the Workflow Steps tab. This tab is where you add the approval steps to the approval/review process.

1. [Create the steps for the approval process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-approval-process/create-workflow-process-approval-steps). Approval steps define the specific steps of the process, the roles/users involved, and approval limits.

1. Assign the approval process to specific modules, companies, and document types.Note: Each module/company/document type combination can only be set up once. In other words, if you assign Module JC, Company 100, and Document Type PO to Process A, you cannot apply that module/company/document type to any other PO approval process. You can however, assign it to a single Subcontract approval process.

1. Select the Assigned Companies tab.

1. In the Module field, enter the module to which the approval process applies or press F4 to select from a list of valid modules.For an explanation of valid modules, see the [Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e45b--en) F1 Help.

1. In the Company field, enter the company to which the approval process applies or press F4 to select from a list of available companies.

1. From the Document Type drop down, select the document type for this approval process: PO-Purchase Order or SL-Subcontracts.

1. If the approval process is ready for use in the specified module/company/document type combination, leave the Active checkbox selected (default setting). You should only deselect this checkbox if the approval process should not yet be active for the module/company/document type combination.

1. Save the record.
