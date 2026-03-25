---
title: "Field Definitions: EM Departments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-departments-form/field-definitions-em-departments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-departments-form/field-definitions-em-departments-form"
---

# Field Definitions: EM Departments Form

The following is a list of field descriptions for the EM
 Departments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Department

 Enter a code that uniquely identifies this department, up to 10 characters.

##  Description

 Enter a description of this department, up to 30 characters.

##  Invoice Reviewer

 Enter the invoice reviewer (from HQ Reviewers) for this department. The reviewer specified here will be used as the default reviewer for unapproved EM invoices posted to this department in AP Unapproved Invoice Entry.
Press F4 for a list of active Reviewers from
 which to choose.
Press F5 in the Reviewer field
 to access HQ Reviewers.

## Invoice Reviewer Group

Optional field.
Enter the reviewer group that defaults for
 each line referencing this equipment in AP Unapproved Invoice Entry. Press F4 for a list
 of active reviewer groups. Press F5 to access HQ Reviewer Group. For more
 information on reviewer groups, refer to Related Topics below.

Related information

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)

##  Purchase Reviewer

 Enter the purchase reviewer (from HQ Reviewers) for this department. This reviewer will default as the assigned reviewer for equipment and work order requisitions posted to this department (in Requisition Entry).

##  Accumulated Depreciation GL Account

 Required.
 Specify the GL account to use for accumulated depreciation. This account will be credited to offset each depreciation debit entry. Other accounts used for depreciation are defined for each asset in EM Asset Setup.
Note: This is a required field, even if you are not using
 Vista™ software to process your depreciation. Any valid GL account may be used.

## Labor Fixed Rate GL Account

Specify the GL account to credit when posting fixed-rate timecards in EM Maintenance Timecard Entry.

##  Cost Codes: Cost Code

 Enter the cost code (from EM Cost Codes) associated with this department. You will typically only need to add cost codes that require posting to a different GL account than those specified for the department cost types.

##  Cost Codes: Exclude PR

 Check this box if this cost code override will not be used for transactions with a Payroll source. Transactions with a payroll source will instead be posted to the GL account specified for the earnings type, liability type, or cost type.
 Leave this box unchecked if the cost code override will always be used, regardless of the transaction's source.

##  Cost Codes: GL Account

 Specify the override GL account to which costs should be posted for this department/cost code.

##  Cost Types: Cost Type

 Enter the cost type (from EM Cost Types) associated with this department.

##  Cost Types: GL Account

 Specify the default GL expense or asset account (i.e., those assigned an ‘account type’ of ‘E-Expense’ or ‘A-Asset’ in GL Chart of Accounts) to which costs will be posted for this department/cost type.

##  Earnings Types: Earn Type

 Specify the earnings type (from HQ Earn Types) associated with this department. You will typically only need to add earn types that require posting to a different GL account than those specified for the department cost types.

##  Earnings Types: GL Account

 Specify the override GL account to which this earnings type will be posted when entering mechanics' timecards. This account will be used in place of the labor cost type GL account.

##  Liability Types: Liability Type

 Specify the liability type (from HQ Liability Types) associated with this department. You will typically only need to add liability types that require posting to a different GL account that those specified for the department cost types.

##  Liability Types: GL Account

 Specify the override GL account to which this liability will be posted when entering mechanics' timecards. This account will be used in place of the GL account for the corresponding cost type.

##  Revenue Codes: Revenue Code

 Enter the revenue code (from EM Revenue Codes) to associate with this department. You will typically only need to add revenue codes that require posting to a different GL account than those specified for the department revenue breakdown codes.

##  Revenue Codes: GL Account

 Specify the default GL income account to which revenue (also referred to as usage) will be posted for this department/revenue code.

## Rev BdownCodes: Revenue Breakdown Code

Enter the revenue breakdown code (from EM Revenue Breakdown Codes) associated with this department.

##  Rev BdownCodes: GL Account

Enter the default GL income account to which revenue (also referred to as usage) will be posted for this department/revenue breakdown code.

## Active

Check this box if the selected role and user should be used when the system is calculating the workflow to apply to a PO. The system will only use this user/role if this box is checked.

## Lead

Check this box if the user is the lead at the selected role.Currently the selection in this box has no affect on how which workflow is applied. This box is informational only.

## Notes

Use this field to enter notes on a role/user.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

## Role

 Use this field to select a role. Press
 F4
 to select one from a list. Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for more information about how roles work in the Process Workflow
 feature.
Roles are created and maintained using the
 [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form. You can launch this form by pressing
 F5
 in this field.

##  User Name

 Use this field to select a user account. You
 can only select a user that is associated with the role selected in the Role field.
Roles are created and maintained using the HQ Roles form, and users are associated with roles using either of the following forms:

- Users tab on the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form - You can access this form by pressing F5
 in the Job
 Role field.

- Roles tab on the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form - You can access this form by
 pressing F5 in the User Name field.

## Process

The Process field on the EM Departments form, Workflow tab.
Enter the workflow process to perform on purchase orders or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the PO-Purchase Order document type or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type. However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). You can assign these generic workflows to PO document types if applicable.

Note: The workflows defined here override those defined in EM Company Parameters or HQ Company Setup.

## Notes

The Notes field on the EM Departments form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

## Document Type

The Document Type field on EM Departments form, Workflow tab.
 Specify the type of document to which the workflow applies. Currently, PO-Purchase Order is the only option available.Note: You can have only one process for each document type.

Note: The workflows defined here override those defined in EM Company Parameters or HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Active

The Active checkbox on the EM Departments form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs or Subcontracts (depending on the document type) are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).
