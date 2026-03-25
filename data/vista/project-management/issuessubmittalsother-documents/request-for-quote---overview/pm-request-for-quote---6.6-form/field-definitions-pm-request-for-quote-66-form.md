---
title: "Field Definitions: PM Request for Quote-66 Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-request-for-quote---6.6-form/field-definitions-pm-request-for-quote-66-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview/pm-request-for-quote---6.6-form/field-definitions-pm-request-for-quote-66-form"
---

# Field Definitions: PM Request for Quote-66 Form

The following is a list of field descriptions for the PM
 Request for Quote-66 form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter the project for which to set up this RFQ. If you accessed this form via the RFQ Distribution tab in PM Pending Change Orders, defaults the project specified for the pending change order.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## PCO Type

Enter the pending change order type for this
 RFQ. Must be a valid, active type set up in PM Document Types (with a Document Category of
 'Pending Change Order').
If you accessed this form via the RFQ
 Distribution tab in PM Pending Change Orders, defaults the PCO Type for the active pending
 change order.
Note: To display a description field for this field on the
 Grid tab, access Field Properties (F3) and select an option from the Description in
 Grid drop-down.
[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## PCO

Enter a pending change order number or press
 F4
 to select one from a list. This is the PCO associated with the RFQ.
 You cannot use this field to create a new pending change order. You can only select an existing PCO. If you would like to create a new PCO, use the [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) form.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## RFQ

Create a new RFQ
There are several ways to create a new RFQ using this field:

- Enter a "+" and then press TAB. The field will populate with the
 next available RFQ number and create a new RFQ.

- Enter an RFQ number that has not already been set up for the
 selected PCO
 Type and PCO. The RFQ number can be up to 10
 characters long. You can also press F4 to see which RFQ numbers have already been
 used.

- Click the New Record icon () and then
 enter a PCO type and PCO. The system will populate the RFQ field
 with the next available number.

Note: The system will ignore alphanumeric numbers when
 determining the next number to assign. Select an existing RFQ

Enter an existing RFQ number or press
 F4
 to select it from a list.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## Description

Enter a description of the RFQ. This field initially defaults with the description of the pending change order.
The description can be up to 60 characters long.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## RFQ Date

Enter the date that the RFQ was created. This field defaults to the current date.
Changes to this date will not update the
 Date
 Sent field on records on the Distribution tab.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## Date Due

Enter the due date for this RFQ. Initially defaults a date based on the Default Standard Days Due option in PM Projects. If no ‘default days due’ specified, defaults as null.
Note: Changing the RFQ Date will automatically recalculate
 this date, even if you overrode the original default date. Changes to this date, however,
 will not update the Date Req’d for records on the Distribution tab.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## Status

Enter the status of this RFQ, or press
 F4
 to select one from a list.
Status codes are created and maintained in [PM Status IDs ](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form).

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## Responsible Person

Enter the person responsible for this RFQ. Must be a valid contact set up for the ‘Project Our Firm’ specified in PM Projects or if no ‘our firm’ specified for the project, the ‘Our Firm’ specified in PM Company Parameters. This contact will be included as the person to call for information or questions regarding the change order.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## Date Req'd

Specify the date by which you need this RFQ returned to you. Initially defaults a date based on the Date Sent (previous field) and the Default Standard Days Due specified in PM Projects. Due date is calculated using calendar days. If no Default Standard Days Due is specified for the project, default will be null.
The date specified here will print on the Request for Quote form.
Note: Changes to the Date Due (Info tab) will not update this date; however, changes to the Date Sent will cause a recalculation of this date.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

## Response

Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
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

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6

##  Date Rec'd

 Enter the date you received the returned RFQ.

[](/en/vista/vista/project-management/issuessubmittalsother-documents/request-for-quote---overview)RFQs - Overview of new process
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Request For Quote - 6.6
