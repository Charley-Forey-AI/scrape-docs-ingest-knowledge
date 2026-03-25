---
title: "Create Workflow Process Approval Steps | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-approval-process/create-workflow-process-approval-steps"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-approval-process/create-workflow-process-approval-steps"
---

# Create Workflow Process Approval Steps

You can use the WF Workflow Process form to create and
 maintain the approval/review processes used in the Process Workflow feature, as well as
 create steps in each process.

Before you set up workflow approval steps, you must set up the [approval process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-approval-process) in WF Workflow Process.
When setting up approval steps, consider the following:

-
If a user enters a document (PO or SL) that requires the approval process and the process includes multiple steps, one of which the user is assigned to as an approver/reviewer, the system automatically skips the workflow step to which the user is assigned and moves to the next step.

-  If a user is associated with multiple roles and more than one of those roles is associated with a step in a workflow, the user will be added to the workflow process multiple times.

1. Open WF Workflow Process and select the applicable process.

1. Select the Workflow Steps tab and select the New Record icon in the toolbar.The system automatically creates a new step record and populates the Sequence field with the next available number.

1. In the Approver
 Type field, select the type of approver.

- Role - Select this option if the users assigned to a specific role should approve the step.

- User - Select this option if a specific
 user should approve the step

1. Depending on the approver type you selected, use the User Name or Role field to specify which user or role will review/approve the document:

- User Name - If you assign a specific user to an approval/review step, only that user will review/approve the PO or SL (depending on the document type specified for the workflow process).

- Role - If you assign a role to an approval/review step, all of the users associated with that role will be included in the review/approval process. If only specific users associated with that role should approve/review the indicated document type, you can assign those users to specific jobs/projects, inventory locations (POs only), and equipment departments (POs only) using the Roles tab on the PM Projects/JC Jobs, EM Departments, IN Locations forms.

Note:

- Users cannot
 approve their own purchase orders or subcontracts. This means the user
 creating the PO or SL is automatically removed from the workflow.


- Each role or
 user can only be used once in the process. For example, you
 cannot have the Job Superintendent role on multiple steps of
 the same approval/review process.

- Roles are
 created and maintained using the HQ Roles form, and users
are assigned to specific roles using either the Users tab on
 the HQ Roles form or the Roles tab on the VA User Profile form.

1. In the Step field, enter the number of this approval process step. For more information about approval steps, see the [Step](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e15e--en) F1 Help.

1. In the Approval
 Limit field, enter the maximum amount
 that the role/user associated with the step can approve. For more information about approval limits, see [About Approval Limits](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/about-approval-limits).

1. If the approver is not required to move to the next step, select the Not
 Required checkbox. [More](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e350--en)For more information, see the [Not Required](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e350--en) F1 Help.

1. Save the record, and then repeat the steps above to create more steps if
 necessary.

1. Add additional steps as needed.
