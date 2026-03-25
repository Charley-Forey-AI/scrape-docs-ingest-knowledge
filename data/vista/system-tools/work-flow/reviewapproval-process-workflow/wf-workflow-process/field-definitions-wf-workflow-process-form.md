---
title: "Field Definitions: WF Workflow Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form"
---

# Field Definitions: WF Workflow Process Form

The following is a list of field descriptions for the WF
 Workflow Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Process

The Process field on the WF Workflow Process form, Info tab.
Using this field you can either create a new process or select an existing one.
To create a new process, enter a name for the new process. The process name must be unique
 and it can be up to 20 characters long.
To select an existing process, press F4 to select an existing process from a
 list.

## Description

The Description field on the WF Workflow Process form, Info tab.
Enter a description of the approval process; up to 60 characters allowed.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Document Type

The Document Type field on the WF Workflow Process form, Info tab.

Select the document type that applies to this workflow process.

- PO - Purchase Order

- SL - Subcontracts

You may also leave this field blank to indicate a 'generic' workflow; that is, a workflow that is not specific to a document type.
 If left blank, you can assign this workflow process to:

- PO - Purchase Order document types when setting up workflows at the company level in EM, GL, HQ, IN, JC, and PM or when setting up workflows for specific equipment departments, inventory locations, jobs, or projects.

- SL - Subcontracts document types when setting up workflows at the company level in HQ, JC, and PM or when setting up workflows for specific jobs or projects.

 For example, if you set up a workflow on the Workflow tab in JC Company Parameters and select a Document Type of PO - PO Purchase Order, you can either assign a process with a PO - Purchase Order document type or a blank document type.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Approval and spending limits based on document total

The Approval and spending limits based on document total checkbox on the WF Workflow Process form, Info tab.
The selection in this checkbox applies to approval limits and the spending limits (set up in HQ Roles) on the users entering documents associated with this workflow.
When selected, approval limits and spending limits apply to the document total. For example, if a spending limit is set to $25,000, the document will be included in a workflow process once the document total equals or exceeds $25,000.
For subcontracts, this checkbox is always selected and disabled, since approval limits and spending limits always apply to the subcontract total.
For purchase orders, this field defaults as selected, but may be overridden if needed. If you deselect this checkbox, approval and spending limits are applied to item totals. The system groups PO items by item type (job, inventory, expense, or equipment) and then applies the limit to the total of items with the same type.
The diagram below outlines what happens if this checkbox is not selected and a user with a spending limit of $25,000 for purchase orders enters a PO with the following PO items.
PO Item #
PO Item Type
Amount
Included in workflow?

1
Job
$20,000
Yes. $27,500 is greater than the $25,000 spending limit, so both of these PO items will be included in a workflow.

2
Job
$7,500

3
Expense
$15,000
No

4
Inventory
$30,000
Yes

## Auto-advance workflow after:

The Auto-advance workflow after: checkbox on the WF Workflow Process form, Info
 tab.

Use this
 field to define the length of time for each approval step set up on the Workflow Steps
 tab. This does not apply to the last step in an approval process. The system will never
 automatically fully approve a PO or Subcontract.
Enter the maximum number of days for each approval step set up on the Workflow Steps tab before it will automatically move to the next step.
If you set this value to zero, the process will not
 automatically move to the next step; instead, the process will stay in the current step
 until it is approved or manually assigned to another step.

## Send reminder notification after:

The Send reminder notification after: checkbox on the WF Workflow Process form, Info tab.

Use this field to indicate when to send a reminder notification to a user who has not approved a workflow within an expected time frame.
Enter the number of days after a workflow has been initiated before sending an automatic reminder to users who have not yet approved the assigned step. For example, to send a reminder for a step that has not been approved after 5 days, enter 5 in this field.

## Active

The Active checkbox on the WF Workflow Process form, Info tab.

Select this checkbox to activate this workflow process.
When this checkbox is selected, you can assign this workflow to companies, modules, and/or specific records. For example, if you want the workflow to apply to all applicable modules (EM, GL, IN, JC, and PM), you can assign the workflow to the Workflow tab on the HQ Company Setup form.
 If you want the workflow to apply to specific modules, you can apply the workflow to the applicable company setup forms (EM Company Parameters, GL Company Parameters, IN Company Parameters, etc.). Company-level workflows override those defined in HQ Company Setup.
For workflows that apply to specific records, you can assign the workflow at the record level (equipment departments, inventory locations, jobs, and/or projects). Workflows defined at the record level override those defined at the module's company level and those assigned in HQ Company Setup.
Deselecting this checkbox deactivate the workflow process, making it unavailable to assign to a new company, module, or specific records.
Note: If a workflow is already in use, deselecting this checkbox does not deactivate it for existing assignments. However, it would not be available for new companies or records. If you want to fully deactivate a workflow, you must either remove it from all companies, modules, and applicable records or you must delete it.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Sequence

The sequence number is a key field that identifies each unique record on the grid.
Enter a '+' in this field to create a new approval step. The system will automatically create a new approval step and assign it the next available number.
This field will also automatically populate with the next available sequence number if you use the New Record icon in the toolbar at the top of the form to create the new step.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Approver Type

The Approver Type field on the WF Workflow Process form, Workflow Steps tab.
Select who will approve/review the step.

- Role - Select role if the users
 that are assigned to a specific role should approve the step. This will enable the
 Role field so that you can select the role. Roles are created and
 maintained using the HQ Roles form, and users are assigned to roles using
 either the Users tab on HQ Roles, or the Roles tab of VA User Profile. For basic information about roles and how they are applied, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

- User - Select user if a specific
 user should approve the step. This will enable the User Name
 field so that you can select the specific user. Users are created and maintained
 using the VA User Profile form.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## User Name

The User Name field on the WF Workflow Process form, Workflow Steps tab.
This field is only enabled when User is
 selected in the Approver Type field.
Use this field to select the user that should approve the step. Press F4 to select a user from a list or just enter the user name into the field.
Users are created and maintained using the VA User Profile form.
Note: A user can only be used once in a process. For example, you cannot have a user assigned as an approver in both step 1 and step 4 of a process.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Role

The Role field on the WF Workflow Process form, Workflow Steps tab.
This field is only enabled when Role is
 selected in the Approval Type field.
Use this field to assign a role to the approval step. For example, if users
 with the role Project Manager should approve purchase orders, select the Project Managers
 role. Press F4 to select a role from a list or enter the role into the field. All users
 associated with the selected role will be added to the step as an approver.
Roles are created and maintained using the HQ
 Roles form, and this is also where users are assigned to roles.
Note: You can only use a role once in a process. For
 example, you cannot have a role assigned as an approver in both step 1 and step 3 of a
 process.

### Assigning Roles to Jobs, Projects, IN Locations, and EM Departments

If there are multiple users assigned to the
 role selected in this field, you can also assign those users to specific jobs and
 projects (POs and SLs) or to inventory locations and equipment locations (POs only).
For example if you have several Project
 Managers, you can assign them to the specific jobs that they manage using the Roles tab
 on the JC Jobs form. This means that when a PO item associated with a job needs to be
 approved, only the Project Manager of that job is the approver, not all of the users
 associated with the Project Manager role.
For more information about the workflow
 process, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Step

The Step field on the WF Workflow Process form, Workflow Steps tab.
Use this field
 to designate which step this sequence represents in the approval process. You can use the step number to break the
 approval process into distinct steps.
For the following examples, we will assume the steps are for a PO workflow process.
 However, the same rules apply to Subcontract workflow processes.
Example: Two StepsSequence
Approver Type
User Name
Role
Step
Approval/Limit

1
Role

PM
1
$25,000

2
User
Mr. Smith

2
$999,999.99

In this example, the PM role and
 Mr. Smith are not on the same step.
If the PO item is less than
 $25,000, it will only be sent to the PM role for approval.
If the PO item is greater than
 $25,000, all users associated with the PM role will receive a notification that
 they have something to approve. Once a user with that role has approved the PO
 item, Mr. Smith will be notified that he has something to approve.

Example: One StepSequence
Approver Type
User Name
Role
Step
Approval/Limit

1
Role

PM
1
$25,000

2
User
Mr. Smith

1
$999,999.99

In this example, the PM and Mr. Smith
 are on the same step.
If the PO item is less than $25,000,
 it will only be sent to the PM for approval just like in the previous example.
If the PO item is greater than
 $25,000, since both Mr. Smith and the PM are on the same step, they will both
 receive notification that they have something to approve.

### Skipping Steps

Using the examples above, if the user is
 entering a PO item that needs to be processed in a workflow with multiple steps and the
 user is an approver/reviewer on a step in that workflow, the PO item will automatically
 jump to the step after the one where the user is set up as an approver/reviewer.
In the following example, if Mr. Smith enters a PO item, the PO will automatically skip
 to step 3 of the workflow process.
Sequence
Approver Type
User Name
Role
Step
Approval/Limit

1
Role

PM
1
$25,000

2
User
Mr. Smith

2
$75,000

3
User
Ms.Brown

3
$150,000

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Approval Limit

The Approval Limit field on the WF Workflow Process form, Workflow Steps tab.

Use this field to set the maximum amount that the role/user can approve.
Approval limits are either applied to the document total or to item totals, depending on the Approval and spending limits based on document total checkbox on the Info tab in WF Workflow Process. For more information about this checkbox, see [Approval and spending limits based on document total](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e0ab--en).
For more information about approval limits, see [About Approval Limits](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/about-approval-limits).

Related information

- [Approval and spending limits based on document total](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e0ab--en)

- [Work Flow](/en/vista/vista/system-tools/work-flow)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Not Required

The Not Required checkbox on the WF Workflow Process form, Workflow Steps tab.
Select this checkbox if the approver/reviewer is optional. This means that the approver/reviewer can reject the item, but their approval is not required.
For example both Mr. Smith and Ms. Brown are
 optional in the PO approval process shown below (the Not Required checkbox is selected). This means
 that they will both receive a notification when a PO item is submitted for approval. Either
 of them can reject the PO, and it is fully approved if either of them approves it.
Sequence
Approver Type
User Name
Role
Step
Approval Limit
Not Required

1
User
Mr. Smith

1
$999,999.99
Y

2
User
Ms. Brown

1
$999,999.99
Y

If the approver/reviewer is the only one assigned to a step, the selection in the Not Required
 checkbox is ignored.
In the example below,
 Mr.Smith is set up as optional but he is the only reviewer/approver on step 2. This means
 the Not
 Required checkbox is ignored. If a PO item greater than $25,000 is submitted
 for approval, it will have to be approved by both the PM and Mr. Smith even though Mr.Smith
 is set up as optional.
Sequence
Approver Type
User Name
Role
Step
Approval Limit
Not Required

1
User
Mr. Smith

1
$25,000
N

2
User
Ms. Brown

2
$999,999.99
Y

If you have multiple users on a single step
 but they have different approval limits, not all of the users will be included when the PO
 item is submitted for approval. This means that the selection in the Not Required
checkbox will be ignored if only one reviewer/approver is included.
In the example below, if a PO item of $20,000
 is submitted for approval, only Mr.Smith will be a reviewer/approver of the PO item. This
 means the selection in the Not Required checkbox is ignored and he will
 be required to approve it.
If a PO item of $$30,000 is submitted for
 approval, both Mr. Smith and Ms. Brown will be included in the workflow are
 reviewers/approvers, so the selection in the Not Required checkbox will not be
 ignored.
Sequence
Approver Type
User Name
Role
Step
Approval Limit
Not Required

1
User
Mr. Smith

1
$25,000
Y

2
User
Ms. Brown

1
$50,000
Y

## Notes

The Notes field on the WF Workflow Process form, Workflow Steps tab.
Use this field to enter notes about this workflow sequence/approval step.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Module

The Module field on the WF Workflow Process form, Assigned Companies tab.

Use this field to restrict the process to a specific module or press F4 to select from a list of modules.

- For Purchase Orders, valid modules are EM, GL, HQ, IN, and JC.

- For Subcontracts, valid modules are HQ and JC.

When you add a module/company/document type to the Assigned Companies tab, the entries are updated to the related company forms. For example, for a Purchase Orders workflow, you set up an assigned company as follows:
Module = JC, Company = 100, Document Type = PO - Purchase Order
Once you save the record, the workflow shows on the Workflow tab in JC Company Parameters for Company #100 as follows: Document Type = PO - Purchase Order, Process = Purchase Orders
Likewise, any workflows defined in a module's company setup will automatically be added to the Assigned Companies tab in WF Workflow Process for the specified workflow.
Note: Each module/company/document type combination can only be set up once. In other words, if you assign Module JC, Company 100, and Document Type PO to Process A, you cannot apply that module/company/document type to any other PO approval process. You can however, assign it to a single Subcontract approval process.

When deleting company assignments, the system automatically deletes that record in both WF Workflow Process and in the related company setup form, regardless of which form is used to delete the record.

### JC/PM Company Assignments

When assigning module/company/document type workflows using the Assigned Companies tab, the system does not allow entering PM as the module, even though you can assign workflows to a company in PM Company Parameters. Instead, you must enter the module as JC and the system will automatically update the workflow to the corresponding company in JC Company Parameters and PM Company Parameters.
Likewise, if you assign a workflow directly in PM Company Parameters, the system automatically updates the workflow to the corresponding company in JC Company Parameters and updates the Assigned Companies tab in WF Workflow Process showing JC as the module.
 Workflow company assignment for JC/PM are updated in this manner because projects become jobs once interfaced, and both JC Company Parameters and PM Company Parameters share information.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Company

The Company field on the WF Workflow Process form, Assigned Companies tab.
Enter the company to which this workflow applies for the specified module or press F4 to select it from a list.
For example, if this is a Subcontract workflow and you assign a module of JC and a company of 1, this workflow will be used on all subcontracts created in the PM module for company 1. For an explanation about how JC/PM module assignments work, see the [JC/PM Company Assignments](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e45b--en__JC-PMModuleAssign) section of the Module F1 Help.
Note: PM Each module/company/document type combination can only be set up once. In other words, if you assign Module JC, Company 100, and Document Type PO to Process A, you cannot apply that module/company/document type to any other PO approval process. You can however, assign it to a single Subcontract approval process.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Document Type

The Document Type drop-down on the WF Workflow Process form, Assigned Companies tab.

Select the type of document for the specified module and company.

-  PO - Purchase Order (Valid for modules EM, GL, HQ, IN, and JC)

- SL - Subcontracts (Valid for modules HQ and JC)

Note: Each module/company/document type combination can only be set up once. In other words, if you assign Module JC, Company 100, and Document Type PO to Process A, you cannot apply that module/company/document type to any other PO approval process. You can however, assign it to a single Subcontract approval process.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Active

The Active checkbox on the WF Workflow Process form, Assigned Companies tab.
Select this checkbox to activate this workflow for the specified module, company, and document type.
Do not select this checkbox if this workflow should be inactive for the specified module, company, and document type.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Notes

The Notes field on the WF Workflow Process form, Assigned Companies tab.
Enter any notes that apply to the selected module, company, and document type for this workflow process.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Notes

The Notes field on the WF Workflow Process form, Grid tab.
Use this field to enter notes about this workflow process/document type.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

Related information

- [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)
