---
title: "Field Definitions: PM Approved Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form/field-definitions-pm-approved-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form/field-definitions-pm-approved-change-orders-form"
---

# Field Definitions: PM Approved Change Orders Form

The following is a list of field descriptions for the PM
 Approved Change Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter the project of the approved change order or press F4 to select it from a list.
Hard or soft closed jobs
If you select a soft or hard closed job and posting to those jobs is not allowed, you will not be able to create a new approved change order.
You can post to a hard or soft closed job if
 the Allow Posting
 to Hard-Closed Jobs or Allow Posting to Soft-Closed Jobs boxes
 are checked on the Info tab of the JC Company Parameters form.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## ACO

Create a new ACO
There are several ways to create a new ACO using this field:

- With the cursor in any field in the upper portion of the form, click the New Record icon() and the next available ACO number will populate in this field. Press TAB to accept the assigned number and create the new ACO for the selected project.

- Enter an approved change order number that does not
 exist on the project. You can press F4 to see a list of existing ACOs.

- Enter a ‘+’, 'n', 'N', or 'New' and the system will
 automatically populate the field with the next available number. Press TAB to accept
 the assigned number and create the new ACO.

Note:The system will ignore alpha/numeric ACO numbers when determining the next available number.
Select an existing ACO

Enter an existing ACO number or press
 F4
 to select an ACO from a list.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Description

Enter a description of this approved change
 order, up to 60 characters.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Document Type

 Use this field to categorize the ACO that you
 are creating - for example budget transfer, billable change order, non-billable change
 order, etc. Press F4 to select a document type from a list.
Document types are created and maintained
 using the [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) form. Click [here](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) for more information on document types.
Required when using 'Send with Transmittal'
If you select  >  Send with transmittal, a document type must be selected in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create & Send feature.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## New Cmplt Date

Use this field to enter the new contract completion date. When the ACO is sent to accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form), the value in this field will overwrite the projected completion date on the contract.
Note: You can view the projected completion date on a
 contract using PM Contracts> Info> Projected Completion Date field.
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  ACO Seq

 Enter the sequence number for this approved change order. Initially defaults the next highest available number. The sequence number determines the amount to be included on the Approved Change Order form in the line “The net change by previously authorized Change Orders was…”. Any change orders with a sequence number lower than the change order being printed will be included on this line.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Bill Group

 Enter the bill group for this approved change order item, if applicable. Initially defaults the bill group assigned to the change order at the header level, if one exists.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Int/Ext

- I-Internal - This change order will only affect the internal
 budget.

- E-External - This change order will affect the owner’s schedule of
 values.

This flag is updated to the Job Cost module interfacing the change order using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form). However, it is not used by any other PM program or by any standard reports. It is available for use in customer-created reports.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Date Sent

 Enter the date this approved change order was sent.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Date Req'd

Specify the date by which this change order is
 required to be completed. Initially defaults based on the Date Sent and the Default
 Standard Days Due specified for the project in PM Projects (PM Info tab).

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Date Rec'd

 Specify the date you received the approval
 for this change order.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Approval Date

 Specify the actual approval date of this change order.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Approved By

Use this field to enter who approved the change order.
This field will display the username of the approver if the change orders was approved using [PM Approve PCOs.](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form)

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Ready For Accounting

Check this box if the approved change order is ready to be interfaced. When this box is checked, the ACO can be selected and interfaced using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
This field is used in conjunction with the
 Interface box on the Estimate Detail tab. Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form/field-definitions-pm-approved-change-orders-form#ID-00022a4c--en) for more information.
 This field will default based on the following:

- It is checked when you create the ACO.

- It is unchecked if you add the ACO to a contract change order(CCO). When the CCO is approved, it will be checked. Click [here](/en/vista/vista/project-management/change-orders/pm-contract-change-orders-form) for information on CCOs.

- It is unchecked when the ACO is interfaced with the
 accounting modules using PM Interface.

- It is checked when you add items to an ACO that has already been interfaced.
Using F3 overrides in this field

You cannot use the [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) form to override the functionality of this field.
For example, if you press F3 in this
 field and then use the User Overrides or System Overrides tab on the Field Properties form
 to default the value as unchecked, the Ready For Accounting box will not be
 checked when you create the ACO, but the system will automatically check the box once an
 item is added to the ACO.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Sent To Firm

Enter the firm that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature or press F4 to select a
 firm from a list.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
Drag and Drop
 To drag and drop firms/contacts to the distribution grid, double-click the Distribution tab (label) or select View  >  Project Firms List. This displays the Project Firm Contacts list. You can then select a firm/contact and drag it to the grid.
Note:If you manually add a firm/contact to the grid that
 is not set up for the project, upon saving the record, the system displays a message
 indicating the firm/contact does not exist in PM Firms and gives you the option to add
 the firm/contact. Select Yes to add the firm/contact to the
 distribution list and to PM Firms. Select No to add the firm/contact to the
 distribution grid only.
Distribution defaults

When creating a new record, the Distribution
 tab will automatically populate with any PM firm contact set up as a distribution default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.
Using the sort name
Tip:The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can
 enter the sort name 'bryan' in the Vendorfield instead of the firm number
 '10042'. The sort name of a firm is set up using the Sort Name
 field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Sent To Contact

Enter the contact that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature, or press F4 to select
 one from a list. Only contacts associated with the firm selected in the Sent To Firm
 field can be selected.
Contacts are associated with firms using [PM Firm Contacts ](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).
Distribution defaults
When creating a new record, the Distribution
 tab will automatically populate with any PM firm contact set up as a distribution default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.

Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Send

Check this box if the contact should receive communications generated using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
When this box is not checked, the contact can
 be manually added to a Create and Send email but they will not automatically populate in
 the To,
 Cc,
 or Bcc
 fields on the Message tab of the PM Send Documents form.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If this contact was added to an email generated using the Create and Send feature, this box will be checked.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Preferred Method

Use this field to select which type of communication should be sent to the contact when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. This field defaults based on the preferred method set up using [PM Firm Contacts](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).

- M -Print — Print a hard copy of the generated PDF document(s). When this option is selected, the contact will not receive a copy of the email body text.

- E -Email — Send the generated PDF document(s) using email. The email address of the contact is pulled from the Email field on the Info tab of the PM Firm Contacts form. F -Fax — Send the generated PDF document(s) suing fax. The system will use the fax number set up on the PM Firm Contacts form.
Note:This option requires that you have a fax server set
 up in the Fax Server Name field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Send Type

Select how the contact should be added to the communication generated from the Create and Send feature: To, Cc, Bcc.
When a communication is created using the Create and Send feature (), the contact will automatically be added using the selection in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If an email generated using the Create and Send feature has already been sent to the contact, this field will display how the contact was included on the last communication.
For example if the contact was added to an
 email in the To field on the PM Send Documents form, To will display
 in this field. When a new email is created using the Create and Send form, the contact will
 automatically populate in the To field.

Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Date Sent

This field displays the date a communication was sent to the contact using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
If several communications have been sent, the most recent date will display.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Date Signed

Enter the date the contact signed the document.
Date field shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days
 in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-+
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Notes

Enter any notes that relate to this contact. You can double click in the field if you need more space to enter information.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.

Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## ACO Item

Enter the approved change order item, up to 10 characters, or enter ‘+’ to assign the next sequential item number.
Lock down ACO Items after interface option
You cannot add items to an ACO that has been interfaced if the [Lock Down ACO items after interface](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-0005b2fd--en) box is checked (PM Company Parameters> Info tab).
Hard and soft closed jobs
 If you do not allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters unchecked), you can only view existing change order items; you cannot not add new change order items or modify existing ones (all inputs will be disabled).

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## PCO Type

If approving a pending change order item, enter the pending change order type. Otherwise, leave blank.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## PCO

Enabled only if PCO Type is specified.
If approving a pending change order item, enter the pending change order. Otherwise, leave blank.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## PCO Item

Enabled only if PCO Type is specified.
If approving a pending change order item, enter the pending change order item. Otherwise, leave blank.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Description

Enter a description of the approved change
 order item. The description can be up to 60 characters and it initially defaults to the
 description of the ACO entered on the Info tab in the upper portion of the form.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Contract Item

Select an Existing Contract Item
Enter the contract item affected by the change
 order or press F4 to select it from a list.
Create a new Contract Item
Enter a contract item that does not exist. This will open [PM Contract Items](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contract-items-form), which allows you to create a new contract item.
If the change order item will not be using the
 same unit of measure and unit price as the contract item to which it is associated, it is
 strongly recommended that you add a new contract item to ensure proper tracking of units
 and costs.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
PM Approved Change Orders

## Chg In Days

Enter the number days that the original
 contract completion date is extended by the change order item. Once interfaced, this value
 cannot be changed here; it will need to be made in JC Change Orders.
This entry will adjust the contract days in
 the Contract Master table (JCCM), and will be included in the total change in days on the
 Approved Change Order form.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Units

Enter the number of units approved for this change order item. If you are approving a pending change order, this field defaults the number of units specified for the pending change order item.
Note: If you enter units and then enter LS (lump sum) as the unit of measure, this field is reset to 0.00 and the field is grayed out.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## UM

Enter the units of measure for this approved change order item. If you are approving a pending change order, this field defaults the unit of measure assigned to the specified pending change order item.
Note: If the unit of measure specified here differs from the unit of measure assigned to the referenced contract item, you will receive the following message:

            ACO Item UM XX does not equal Contract Item UM XX
At this point, it is suggested that you create a new contract item to accommodate the new unit of measure and ensure that both units and costs are tracked and updated properly. If you choose to ignore this warning, be aware that only dollars will be updated to the contract item in Job Cost.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Unit Price

Enter the unit price for this approved change order item. If you are approving a pending change order, this field defaults the unit price for the pending change order item.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Amount

For LS items, enter the approved amount for this change order item. If unit of measure is not LS, amount will default based on Units x Unit Price. If approving a pending change order, defaults the amount specified for the pending change order item.
Amount must be zero if an internal
The value in this field must be a zero if Internal is selected in the Internal field on the Info tab in the upper portion of the form.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Status

Enter the status code that identifies the current status of the approved change order item or press F4 to select it from a list.
Statuses are created and maintained using the [PM Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form) form.
 By default this field populate with the following status:

- The status selected in the Default Final
 Status field on the Info tab of the PM Company Parameters form.

- If a default final status is not defined, the system
 will use the first status found in the [PM Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form) form that is set up as a final status,
 and is associated with the pending change order document category. The system will
 determine which status is first using the Status Code field on the PM Status
 IDs form - alphabetical sort with numbers coming before letters.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Budget No

The Budget No field on the PM Approved Change Orders form, ACO Item Grid/Info tabs.
You only need to use this field if you are using the project budgets feature and need to provide a breakdown of revenue and/or costs for this change order to the owner.
Enter the budget number or press F4 to select from a list of valid budget numbers for the specified project.
Note: Entering a budget number in this field is for reference only. The budget details are not automatically added to the Estimate Detail tab; estimate detail must be entered manually. You can review the budget details as needed by pressing F5 from this field to open PM Project Budgets.

For information about creating and maintaining project budgets, see [PM Project Budgets Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form).

## Approved

Check this box if the change order item has
 been approved. Checking this box will populate the Approved Date field with the current
 date, and the Approved By field with your user account. The Approved By
 field only displays on the Grid tab in the lower portion of the form.
Note:This box does not affect if an ACO item can be interfaced using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).

By default this box is checked when:

- The ACO item was a pending change order item that was approved using [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form)

- The ACO item was created manually using PM Approved Change Orders

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Approved Date

Specify the date this change order item was approved. Initially defaults the approval date specified in the change order header.
This date will be used as the 'actual date' in JCCD (JC Cost Detail) when interfacing PO and SL change orders.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Force Phase

The Force Phase box allows you to override
 the assignment of contract items to change order phases when they are interfaced using
 [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form). You only need to use this option if the phase
 contract items should always match the contract item assigned to the change order item, and
 you have phases that do not meet this criteria. During the interface, all phases with a
 contract item not matching the contract item for the change order item will be changed to
 use the change order item’s contract item.
Leave this box unchecked if all phases should
 retain their contract item assignments even if they do not match the contract item assigned
 to the change order item.
Note: Force phase only occurs when the change order items
 are interfaced with accounting using PM Interface. If you are auto-updating phases to Job
 Cost (i.e., the Active option is checked for phases/cost types) and have checked the Force
 Phase option for the related change order item, you will still need to run the interface to
 accounting.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Bill Group

Enter a bill group or press F4 to select one from a list. Click [here](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-bill-groups-form) for more information on bill groups.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Interfaced Date

Display only, the interface date assigned to
 this change order item during the interface to Job Cost. This date is assigned as
 follows:

- If phase cost type detail exists for the approved change order
 item, the item's interface date will be updated with the last Interfaced Date from the
 phase/cost type detail.

- If no phase cost type detail exists for the approved change order
 item, the item's interface date will be the actual interface date for the item.

Note: Change order items with an interface date will be
 included in certain reports, regardless of whether phase detail exists for the item.
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Interfaced By

 Display only, the user (login) who interfaced this approved change order item. (Note: This field will be updated each time the approved change order item is interfaced.)

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Item: Notes

Use this tab to enter notes about the item.
 The space allowance is virtually unlimited.
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

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Phase

Enter the phase this change order item affects.
If you are approving a pending change order item, all phases set up for the pending change order item will be set up automatically. If you used the ‘Generate Detail’ feature, all project phases having the same contract item as the change order item will be set up here. Phases can be modified or deleted as necessary.
Note: If the phase’s assigned contract item differs from the change order item’s contract item, the following message displays above the grid:

Phase Contract Item:     XX <> PCO Item Contract Item:     XX

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Cost Type

Enter the cost type for this phase or press F4 to select one from a list.
If you are approving a pending change order item, or you selected Tasks> Generate Detail to generate the detail items, this field will defaults the cost type assigned to the specified phase.
Note:If you enter a cost type designated as one of the two material cost types in PM Company Parameters (Material Parameters tab), the system will automatically create a single material detail line for the phase/cost type in PM Material Detail with a Material Type ofP-Purchase Order.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Ins Code

If an approved pending change order, this field displays the insurance code assigned to the phase and is disabled.
If entering a new change order item:

- For existing project phases, this field is disabled and displays the insurance code assigned to the phase in JC Job Phases or PM Project Phases. If no insurance code is assigned to the phase, displays as null.

- For new phases, enter the insurance code (from HQ Insurance Codes) that applies to this phase, if applicable. Once record is saved, phase and insurance code will be updated to JC Job Phases/PM Project Phases (applies to ‘locked phases’ jobs as well).

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Units

Enter the number of approved units for this phase/cost type or enter 0.00 if unit of measure is LS. If approving a pending change order item, this field defaults the number of units specified for the selected phase/cost type. If you change the default, the Hrs/Unit (if applicable) and Amount will be recalculated.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## UM

Enter the unit of measure for this phase/cost type. If approving a pending change order item, this field defaults the unit of measure assigned to the selected phase/cost type.
Note: If you entered units in the previous field, and you enter LS (lump sum) as the unit of measure, existing units will be zeroed out.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Hrs/Unit

Enter the number of hours required to complete a single unit of the specified unit of measure (if applicable). Initially defaults the hours per unit specified for the phase/cost type in PM Project Phases or, if approving a pending change order item, the hrs/unit specified for the selected phase/cost type. If you change the default, the Hours, Unit Cost, and Amount will be recalculated.
Note:In order to track hours for a cost type, you must have checked the Track Hours option in JC Cost Types.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Hours

Enter the total number of hours for this phase/cost type. If approving a pending change order item, this field defaults the number of hours specified for the selected phase/cost type. If you change the default, the Hrs/Unit, Unit Cost, and Amount will be recalculated.
Note: In order to track hours for a cost type, you must have checked the Track Hours option in JC Cost Types.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Cost/Hour

Enter the cost per hour for this phase/cost type. Initially defaults the cost per hour specified for the phase/cost type in PM Project Phases or, if approving a pending change order item, the cost/hour specified for the selected phase/cost type. If you change the default, the Unit Cost and Amount will be recalculated.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Unit Cost

Enter the unit cost for this phase/cost type.
If you change the Hrs/Unit, Hours, or Cost/Hour, the unit cost is recalculated (based on Hrs/Unit x Cost/Hour).
Default value
This field initially defaults based on the
 unit cost entered on the selected phase/cost type in [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) (PM Project Phases> Cost Types tab> Unit Cost
 field).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders

## Estimate Amount

Enter the total amount for this phase/cost type. Initially defaults based on Units x Unit Cost. If approving a pending change order item, this field defaults the amount specified for the selected phase/cost type. If you change the default, and you are tracking hours, the Hrs/Unit, Hours, and Unit Cost will be recalculated. If not tracking hours, only the unit cost is recalculated.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

##  Active

 Check this box if this phase/cost type is ‘active’. This phase/cost type will be updated to Job Cost immediately, and will be available to accumulate costs.
 Leave this box if phase/cost type is not active. Phase will be considered ‘pending’ and will be updated to Job Cost when the change order is interfaced to accounting. No costing can occur until the phase/cost type is interfaced.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Bill Flag

Specify whether units and/or costs for this cost type on this phase are to be used in calculating progress complete. Used only for Job Billing.

- Y-Units and Dollars - Both units and dollars posted to this cost
 type will be used to calculate progress complete.

- C-Only Dollars - Only dollars will be used in calculating percent
 complete for this phase/cost type.

- N-Neither - Neither units nor dollars posted to this cost type will
 be used when calculating progress complete.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Item Unit Flag

Specify whether this cost type will be used to accumulate units complete for the contract item.
Check this box to use this cost type on this phase to accumulate units complete for the related contract item. When summarizing job costs, the costs are all totalled, but only the units posted to the specified phase/cost type are counted.
Leave this box unchecked if this cost type will not be used to accumulate units complete for the related contract item.
Note:Generally, this flag is set to Y for only one cost type on one phase, and the phase selected would be the one most closely related to the contract item.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Phase Unit Flag

Specify whether this cost type will be used to accumulate units complete for the contract item.
Check this box to use this cost type on this phase to accumulate units complete for the related contract item. When summarizing job costs, the costs are all totalled, but only the units posted to the specified phase/cost type are counted.
Leave this box unchecked if this cost type will not be used to accumulate units complete for the related contract item.
Note:Generally, this flag is set to Y for only one cost type on one phase, and the phase selected would be the one most closely related to the contract item.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Interface

Check this box if the detail item is ready to be interfaced with the accounting modules using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
To interface the ACO, the Ready For
 Accounting box on the Info tab in the upper portion of the form must also be checked. Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form/field-definitions-pm-approved-change-orders-form#ID-00022801--en) for more information.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## Phase: Notes

Use this tab to enter notes about the item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools >  Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Approved Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
