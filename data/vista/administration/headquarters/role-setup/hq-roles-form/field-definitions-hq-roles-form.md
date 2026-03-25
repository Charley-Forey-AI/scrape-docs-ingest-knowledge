---
title: "Field Definitions: HQ Roles Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/role-setup/hq-roles-form/field-definitions-hq-roles-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/role-setup/hq-roles-form/field-definitions-hq-roles-form"
---

# Field Definitions: HQ Roles Form

The following is a list of field descriptions for the HQ
 Roles form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Role

The Role field on the HQ Roles form.
Enter a code for this role (up to 20 characters). Cannot be the same as a user set up in VA User Profile.
Examples of roles:

- Project Manager

- Project Coordinator

- Concrete Coordinator

- Steel Coordinator

Note: Once you assign a role to a job or project, you cannot delete it.

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)

## Description

The Description field on the HQ Roles form, Info tab.
Enter a description of the role (up to 60 characters).

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)

## Active

The Active checkbox on the HQ Roles form, Info tab.

Select this checkbox to activate this role. Once selected, you can assign the role to jobs (in JC Jobs), projects (in PM Projects), locations (in IN Locations), or equipment departments (in EM Departments)
Deselect this checkbox if this role is no longer active and should not be assigned to jobs, projects, locations, or departments.
Note:Setting a role to inactive does not remove it from F4 lookups or prevent its assignments to jobs/projects.

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)

## Usable In

The Usable In field in HQ Roles, Info tab.
Select the checkbox for each of the modules listed below in which this role is used. For example, you might have a role of 'technician' that will only be used in Service Management, but a role of Electrician that might be used in all three.

- Project Management

- Pre-Construction

- Service Management

Note:These checkboxes are informational only; they are not currently being used anywhere else in the system.

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)

## Type

The Type field on the HQ Roles form, Spending Limits tab.
From the drop-down, select the type of document to which the spending limit applies.

- PO - Purchase Order

- SL - Subcontracts

## Sub Type

The Sub Type field on the HQ Roles form, Spending Limits tab.

Select the line type for the specified document type to which this spending limit applies.
Purchase Order

- Job

- Inventory

- Expense

- Equipment

- All - Select this option if the spending limit does not apply to a specific line type.

SubcontractThis field automatically defaults to Job, which is the only valid option for this document type. Selecting any other sub type will produce an error.
For detailed descriptions of line types, see the [Type](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-000309bb--en) F1 help for purchase orders or the [Type](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form/field-definitions-sl-subcontract-entry-form#ID-0003f228--en) F1 help for subcontracts.

## Spending Limit

The Spending Limit field on the HQ Roles form, Spending Limit tab.

Enter the spending limit for this document type/sub type. Users assigned this role can spend up to this limit without requiring the review/approval workflow process.
How the spending limit is applies depends on the Approval and spending limits based on document total checkbox in WF Workflow Process.
 For example, say you set a role's limit to $15,000 for a Purchase Order type and Job sub type. If the Approval and spending limits based on document total checkbox is selected for a workflow process, users assigned to the role can spend up to $15,000 on a purchase order without requiring the review/approval workflow process. If the purchase order total equals or exceeds $15,000, it must go through the review/approval workflow process.
If the Approval and spending limits based on document total checkbox is not selected, the spending limit is applied to the combined total of purchase order items of the same type. So in the example above, the user can spend up to $15,000 total on purchase order items with a line type of Job without having them go through the review/approval process. If the combined total of job purchase order items equals or exceeds $15,000, the purchase order/items must go through the review/approval workflow process.
For more information, see [Approval and spending limits based on document total](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e0ab--en).
Note: If you have users with different spending limits, you can set up spending overrides in the HQ User Spending Overrides form (accessed by clicking the User Spending Overrides button on the Users tab in HQ Roles. For more information, see [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form).

## Threshold

The Threshold field on the HQ Roles form, Spending Limits tab.

If this role is allowed to exceed the spending limit, enter the percentage by which the spending limit can be exceeded.
For example if the spending limit is $50,000 and the threshold is 2.00%, the role will be able to spend $51,000. This means that if a purchase order were written for $48,000 but taxes, freight, and additional charges pushed the total cost to $50,500, the role could still approve the PO because it is within the threshold.
Leave the percentage set to 0.00 if this role is not allowed to exceed the spending limit.

## Active

The Active checkbox on the HQ Roles form, Spending Limits tab.

Select this checkbox if the spending limit for this role/document type is active. Spending limits only apply to the role when this checkbox is selected.
Deselect this checkbox if the spending limit is inactive.

## Notes

The Notes field on the HQ Roles form, Spending Limits tab.
Use this field to enter notes on the spending limit.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

## User Name

The User Name field on the HQ Roles form, Users tab.

Use this field to assign a specific user to this role. Press F4 to select a user from a list.
Users are created and maintained using the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form, and they can also be assigned to roles using the Roles tab on that form.
Note: You can also assign roles to a specific user using the Roles tab on the VA User Profile form. Roles set up in VA User Profile are automatically set up for the role in HQ Roles. Likewise, if you assign a user to a role in HQ Roles, the role is automatically set up for the user in VA User Profile. Any updates to the role/user in either form automatically updates the other form. For more information, see [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form).

## Active

The Active checkbox on the HQ Roles form

Select this checkbox to activate this user for this role. This checkbox must be selected in order to add this user to the role on a job (in JC Jobs), project (in PM Projects), location (in IN Locations), or equipment department (in EM Departments).
Deselect this checkbox if this user is not active for this role and should not be assigned to jobs, projects, locations, or departments.
Note: You can also set the Active status for a user/role in VA User Profile. Users added to a role in this form are automatically added to the Roles tab in VA User Profile. Likewise, roles added for a user in VA User Profile are automatically set up in the HQ Roles form. Setting the Active flag in one form automatically updates the other form.

## Notes

The Notes field on the HQ Roles form, Users tab.

Use this field to enter notes about this user/role.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

## Notes Tab

The Notes tab on forms throughout Vista.
Use the Notes tab to enter any miscellaneous notes about the selected item. The space allowance is virtually unlimited.
Note: If you are accessing this field from a grid and you need additional space for your notes, double-click in the field to access the Grid Notes form.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.
Spelling CheckClick the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
