---
title: "Field Definitions: PM Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form/field-definitions-pm-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form/field-definitions-pm-change-orders-form"
---

# Field Definitions: PM Change Orders Form

The following is a list of field descriptions for the PM
 Change Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project (from PM Projects) for which you are setting up/editing this change order.
Note:If you enter a project with a closed status (hard or soft), the status displays in red to the right of the project description. You will only be able to add or modify change orders (pending or approved) for the project if you allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters checked).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## PCO Type

Enter the pending change order type or press
 F4
 to select a type from a list.
PCO types are created and maintained using the
 [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) form.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## PCO

Enter a number for this change order, up to 10 characters, or enter ‘+’ to auto-generate the next sequential number available. Numbers will be generated based on the ‘Auto Generate Pending Change Orders Using’ option designated in PM Projects (Project or Project/Type). If the option is set to ‘Project’, the system will generate the next sequential number based on all PCO’s for the project. If the option is set to ‘Project and Type’, the system will generate the next sequential number based on all PCO’s having the same document type (e.g. all PCO’s for the project with a document type of ‘FO’).

- If you are using both numeric and alphanumeric numbers, the auto-generate process will ignore alphanumeric numbers when determining the next number to assign.

- If you do not allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters unchecked), you can only view existing pending change orders; you cannot not add new pending change orders or modify existing ones (all inputs will be disabled).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

##  PCO: Description

 Enter the description of this change order, up to 60 characters.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

##  PCO: Date 1-3

 The column headings for these three date fields are determined by what was entered in the Pending Change Order Date fields in PM Document Types for the selected change order type. Additionally, each column will only show if the Show in Grid option is checked for that column.
 Date Shortcuts
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

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Pending Status

This display-only field shows the current system-assigned status for each change order. Status will be assigned as follows:

- 0-Pending - All items on the change order have a beginning or intermediate status and none have been approved. Pending change orders with no items will also be assigned this status.

- 1-Partial - At least one item on this change order has a beginning or intermediate status and has not been approved.

- 2-Approved - All items on this change order have been approved.

- 3-Final - All items on this change order are approved or final (not approved, but assigned a 'final' type status code, such as 'Rejected' or 'Canceled').

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Details

Enter detail information about the pending change order. Double click in the field to open the Grid Notes form, which gives you more space to enter the information.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Pending Tab - Impact Estimate, SL, PO, and Contract Boxes

The Impact Estimate, Impact SL,
 Impact
 PO, and Impact Contract boxes on the Pending tab
 are disabled on this form.
If you want to change the values in these
 fields you must use the Info tab in the upper portion of [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form).
The selections in these fields will default based
 on the document type selected in the PCO Type field. Use the [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) form to change how these fields will
 default.

## Pricing Method

Use this field to select the pricing method of the pending change order. The selection in this field determines which fields will display on the Estimate / Purchase Details tab in the lower portion of the [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) form.
This field will default based on the document type
 selected in the PCO Type field. Use the [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) field to change how this field
 defaults.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## ACO

Enter the approved change order number or enter ‘+’ to auto-generate the next sequential number available.
If you are using both numeric and alphanumeric numbers, the auto-generate process will ignore alphanumeric numbers when determining the next number to assign.
Note:If you do not allow posting to hard- and/or soft-closed jobs, you can only view existing approved change orders - you cannot add new approved change orders or modify existing ones. You can disallow posting to hard and soft closed jobs using [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form).

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## ACO: Description

Enter a description of the change order. The description can be up to 60 characters long.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## New Complete Date

Enter the new contract completion date. This entry will update [PM Contracts ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form) and will print on the Approved Change Order form.
Date Shortcuts
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

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## ACO Sequence

Enter the sequence number for this approved change order. This field initially defaults the next highest available number.
The sequence number determines the amount to be included on the Approved Change Order form in the line “The net change by previously authorized Change Orders was…”. Any change orders with a sequence number lower than the change order being printed will be included on this line.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Bill Group

The bill group of the change order.
 Click [here](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-bill-groups-form) for more information on bill groups.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## ACO: Internal/External

- I-Internal - Use this option to identify this approved change order as one that will only affect the contractor’s internal budget.

- E-External - Use this option to identify this approved change order as one that will affect the owner’s schedule of values.

This flag is updated to Job Cost during the PM interface. However, it is not used by any other PM program or by any standard reports. It is available for use in customer-created reports.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Date Sent

Enter the date the approved change order was sent.
Date Shortcuts
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

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Date Required

Enter the date the change order should be
 complete. This field initially defaults based on the Date Sent on the change order and the
 Default Standard
 Days Due defined for the project on the Info tab of [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).
Date Shortcuts
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

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Date Received

Enter the date the approval of the change order was received.
Date shortcuts
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

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Approval Date

Specify the actual approval date of the change order.
Date Shortcuts
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

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders

## Approved By

Specify who approved the change order. Change orders approved using PM Change Order Approval will default the login name of the person who entered the approved change order, but this can be overridden.

[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview
[](/en/vista/vista/project-management/change-orders/about-the-pm-change-orders-form)PM Change Orders
