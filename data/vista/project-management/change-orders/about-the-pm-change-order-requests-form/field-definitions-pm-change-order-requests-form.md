---
title: "Field Definitions: PM Change Order Requests Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form/field-definitions-pm-change-order-requests-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form/field-definitions-pm-change-order-requests-form"
---

# Field Definitions: PM Change Order Requests Form

The following is a list of field descriptions for the PM
 Change Order form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract

Enter a contract or press F4 to select one from a list.
Only pending change orders for projects associated with this contract can be added to the Change Order Request.
Note:You cannot select a pending contract in this field. The contract must be interfaced with accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) before you can create a change order request on it.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## COR: Change Order Request

Create a new COR
There are three ways to create a new change order request (COR) using this field:

- Click the New Record icon () at the top of the form. The
 system will populate the field with the next available COR number once you enter a
 contract number in the Contract field. Press TAB to accept
 the assigned number and the COR will be created.

- Enter a '+' and the field will populate with the next available COR number. Press TAB to accept the assigned number and create the new COR.

- Entering a COR number that does not exist on the project and then press TAB to create the COR. You can also press F4 to see a list of CORs that have already been created. The COR number must be between 32,767 and -32,768
Open an existing COR

Enter an existing COR number or press F4 to select an existing COR from a list.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Description

Enter a description of the change order request. The value in this field can be up to 60 characters long.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Details

Use this field to enter detailed information about the change order request.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

##  Document Type

 Use this field to categorize the change order
 request that you are creating. Press F4 to select a document type from a
 list.
Document types are created and maintained
 using the [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) form. Click [here](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) for more information on document types.
Required when using 'Send with Transmittal'
If you select  > Send with
 transmittal, a document type must be selected in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create & Send feature.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/pm-contract-change-orders-form)PM Change Order Requests

## Date

Enter the change order request date. When creating a new change order request, this field will populate with the current date.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Status

Use this field to define the status of the change order request. For example, if the COR has been sent for approval, or has been approved by the customer. Enter a status ID or press F4 to select one from a list.
Note: Status IDs are created and maintained using [PM Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form). You can open this form be pressing F5 while
 in this field.
By default this field will populate with the
 default beginning status defined using the Default Beginning Status field on the
 Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM change Order Requests

## Change in Days

Use this field to enter the number of the days
 that the project is extended by the change order request. This field will be used to
 calculate the default value of the New Completion Date field, and it can be
 added to the Change Order Request document generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature on this form.
Note:This field will not affect the change in days entered on the PCO items associated with this change order request.

This field will default based on the change in days associated with the pending change orders attached to the COR using the PCO tab. You can override this calculated value if desired.
Note:You can add a change in days to PCO items using the
 Change in
 Days field on the Info tab in the lower portion of [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form). When the pending change
 orders are approved, the change in days on each pending change order item will update
 the change in days on the contract in PM Contracts> Info> Days in Contract>
 Current field.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## New Completion Date

Use this field to enter the new completion date of the project.
By default, this field will populate with the
 Projected Completion Date on the Contract plus the number of days entered in the Change In Days
 field on this form.
Note:The projected completion date is entered on a
 contract using the Project Completion Date field on the
 Info tab in [PM Contracts
 ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Sent

Use this field to enter the date the change order request was sent. By default this field will populate with the current date when the change order request is created.
You can also change the label of this field and use it for a different purpose.
Change the Field Label
You can change a field label to match your own usage or terminology using the Field Properties form. Following the steps below will change how the field label appears for all users of the application.

1. Click in the field and press
 F3. This will open [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form).

1. Open the System Overrides tab.

1. Enter the new field label in
 the Form
 Label and Col Heading fields.

1. Click the Apply
 button.

1. A message window will
 appear. Click OK to reopen the form using the new field label.
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change
 Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order
 Requests

## Due Back

Use this field to enter the date the change order request in due back from the owner.
You can also change the label and use the field for a different purpose.
Change the Field Label
You can change a field label to match your own usage or terminology using the Field Properties form. Following the steps below will change how the field label appears for all users of the application.

1. Click in the field and press
 F3. This will open [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form).

1. Open the System Overrides tab.

1. Enter the new field label in
 the Form
 Label and Col Heading fields.

1. Click the Apply
 button.

1. A message window will
 appear. Click OK to reopen the form using the new field label.
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change
 Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order
 Requests

## Received

Use this field to enter the date the change order request was received back from the owner.
You can also change the label of this field and use it for a different purpose.
Change the Field Label
You can change a field label to match your own usage or terminology using the Field Properties form. Following the steps below will change how the field label appears for all users of the application.

1. Click in the field and press
 F3. This will open [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form).

1. Open the System Overrides tab.

1. Enter the new field label in
 the Form
 Label and Col Heading fields.

1. Click the Apply
 button.

1. A message window will
 appear. Click OK to reopen the form using the new field label.
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change
 Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order
 Requests

## Approved

Use this field to enter the date the change order request was approved.
You can also change the label and use the field for a different purpose.
Change the Field Label
You can change a field label to match your own usage or terminology using the Field Properties form. Following the steps below will change how the field label appears for all users of the application.

1. Click in the field and press
 F3. This opens [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form).

1. Open the System Overrides tab.

1. Enter the new field label in
 the Form
 Label and Col Heading fields.

1. Click the Apply
 button.

1. A message window will
 appear. Click OK to reopen the form using the new field label.
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change
 Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order
 Requests

## Project

Use this field to select the project associated with the PCO that you would like to add to the change order request. Enter a project number or press F4 to select a project from a list.
Note:Only projects associated with the contract entered
 in the Contract field in the upper portion of the form can be selected in this
 field. Projects are associated with specific contracts using the Contract
 field on the Info tab of [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).
 You can open PM Projects from this form by pressing F5 while in this field.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## PCO Type

Use this field to select the type of PCO that
 you would like to add to the change order request. Enter a PCO type or press F4 to select
 one from a list.
PCO types are document types that are set up
 to be used with pending change orders. Document types are created and maintained using
 [PM Document Types](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) , and a document type is a PCO type if
 Pending Change
 Order is selected in the Document Category drop down on the Info
 tab. Once a PCO type is created, it is associated with a PCO using the PCO Type field
 on PM Pending Change Orders.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## PCO

Select the PCO that should be on the change order request. Enter a PCO number or press F4 to select a PCO from a list.
Note:Only PCOs associated with the project, and PCO type
 selected in the Project and PCO Type field can be selected in this
 field.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Project

This field displays the project associated with the contact.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

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
 tab will automatically populate with any PM firm contact set up as a distribution
 default.
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
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

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
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

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
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Preferred Method

Use this field to select which type of communication should be sent to the contact when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. This field defaults based on the preferred method set up using [PM Firm Contacts](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).

- M -Print — Print a hard copy of the generated PDF document(s). When this option is selected, the contact will not receive a copy of the email body text.

- E -Email — Send the generated PDF document(s) using email. The email address of the contact is pulled from the Email field on the Info tab of the PM Firm Contacts form. F -Fax — Send the generated PDF document(s) suing fax. The system will use the fax number set up on the PM Firm Contacts form.
Note:This option requires that you have a fax server set
 up in the Fax Server Name field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

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
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Date Sent

This field displays the date a communication was sent to the contact using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
If several communications have been sent, the most recent date will display.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)PM Change Order Requests

## Date Signed

Enter the date the contact signed the document.
Date field shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Notes (Contact)

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
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests

## Notes tab

Use this field to enter notes on the change order request.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-order-requests-form)PM Change Order Requests
