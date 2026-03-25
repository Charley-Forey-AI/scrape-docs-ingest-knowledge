---
title: "Field Definitions: PM Pending Change Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form"
---

# Field Definitions: PM Pending Change Orders Form

The following is a list of field descriptions for the PM
 Pending Change Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter the project that you are creating the
 PCO for or press F4 to select a project from a list.
You can press F5 while in
 this field to open the [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)
 form.
Note: If you enter a project with a closed status (hard or
 soft), the status displays in red to the right of the project description. You will only be
 able to add or modify pending change orders for this project if you allow posting to hard-
 and/or soft-closed jobs (flags in JC Company Parameters).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PCO Type

Use this field to categorize the PCO that you are creating - for example budget transfer, billable change order, non-billable change order, etc. PCO types are created and maintained using [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form).
Click [here](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) for more information on PCOmtypes.
Enter a pending change order type or press
 F4
 to select one from a list.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PCO

Select an existing PCO
Enter an existing PCO number or press F4 to select a PCO from a list.
Create a new PCO
When creating a new PCO, you are creating a
 PCO of the type selected in the PCO Type field.
There are several ways to use this field to create a new PCO:

- Enter a "+" in this field and the system will automatically create
 a new PCO and assign it the next available number. Click the New Record icon () at the
 top of the form and then select a type in the PCO Type field. The system will
 automatically assign the PCO the next available number. How the system generated number is selected

This field will populate with an auto-generated number, but it can be modified.
The auto-generated number is calculated based
 on the selection in the Auto-Generate Pending Change Orders Using
 field on the PM Info tab of [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).
 This field can be set up to auto-number PCOs by project, or by project and type.

- Project - The system will generate the next sequential number based
 on all of the PCO’s on the project.

- Project and Type - The system will generate the next sequential
 number based on all of the PCO’s having the same document type (e.g. all PCO’s for the
 project with a document type of ‘FO’).

If there are letters in the PCO number, they are handled in the following way:

- If the PCO number ends in a letter, for example, A001a, the
 auto-generate process will ignore it when calculating the next number to assign. If the
 PCO number ends in a number, the auto-generate process will use that number when
 calculating the next number to assign. For example, if you already have PCOs numbered
 A001, A002, and A003, the next auto-generated PCO number will be A004.

Note: If you do not allow posting to hard- and/or
 soft-closed jobs (flags in JC Company Parameters unchecked), you can only view existing
 pending change orders; you cannot not add new pending change orders or modify existing ones
 (all inputs will be disabled).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Description

Enter a description of the pending change order. The value in this field can be up to 60 characters long.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Details

Enter detail information about the pending change order.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Date

This field will populate with the current date when a new pending change order is created. If this date does not apply, you can enter a different create date or click the Calendar icon to select one.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Status

Use this field to define the status or current state of the PCO. This field can also be useful in reporting, grouping, and sorting. Enter a status or press F4 to select one from a list.
This field defaults to the status set up using
 the Default
 Beginning Status field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).
When you change the status and save the PCO, a
 message appears asking if you would like to apply the status to the items on the PCO.
 Click Yes and all PCO items that do not have a final status will be updated with
 the new status. PCO items with a final status will not be affected.
Status codes are created and maintained using
 [PM
 Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form). Status codes have a final status if the Final box in
 the Type of Code section is checked on the Info tab of PM Status IDs.
When the PCO is approved using the [PM Approve PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form) form, this field populates based on the status selected in the Default Final Status field on the Info tab of the PM Company Parameters form. If a default final status is not defined, the system uses the first status found in the PM Status IDs form that is set up as a final status, and is associated with the pending change order document category. The system determines which status is first using the Status Code field on the PM Status IDs form, and based on an alphabetical sort with numbers coming before letters.
Note: Changing the status of a pending change order can impact the cost projections. Projection options are set up on a status ID using the PM Status IDs form ([Projection Option](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form/field-definitions-pm-status-ids-form#ID-0002d22c--en) field).

## Priority

Use the drop down to select the priority of the change order. This field is intended to let you indicate the urgency or importance of a PCO. You can also use this field to sort and filter pending change orders in the PM module [Work Center](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center) and other places in the application.
This field will default to Medium when creating a new pending change order.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Reason

Use this field to assign a reason code to the pending change order. This allows you to categorize the reasons why a pending change order was created - for example unforeseen site conditions, economic change, drawing revisions, design omission, etc.
Press F4 to select a reason code from a list,
 or press F5 to open [HQ Reason Codes ](/en/vista/vista/administration/headquarters/company-setup/hq-reason-codes-form) and create a new reason code.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Reference

Use this field to enter a reference number for the PCO. The value in this field can be up to 30 characters long.
Change the Field Label
You can change a field label to match your own usage or terminology using the Field Properties form. Following the steps below will change how the field label appears for all users of the application.

1. Click in the field and press F3. This will open [Field Properties](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form).

1. Open the System Overrides tab.

1. Enter the new field label in the Form Label and Col Heading fields.

1. Click the Apply button.

1. A message window will appear. Click OK to reopen the form using the new field label.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Responsible Person

Enter the person at your firm that is the responsible for the pending change order or press F4 to select them from a list.
Only contacts that are set up as a contact at
 the firm selected in the Our Firm field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) will display in the list. You can
 create a new contact by pressing F5in this field to open PM Firm Contacts,
 which is used to create and maintain the contacts associated with a firm.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Estimate

Check this box if the pending change order
 impacts the budget/estimates. When this box is checked, the estimate fields will display on
 the Estimate/Purchase Details tab: Estimate UM, Estimate Units,
 Estimate
 Hours/Unit, Estimate Hours, Estimate
 Cost/Hour, Estimate Unit Cost, Estimate
 Amount.
Note: The selection in the Pricing Method
 field also determines which fields will display on the Estimate/Purchase Details tab. Click
 [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a250--en) for more information.
This field will populate with the default
 value set up on the document type selected in the PCO Type field, but it can be changed if
 necessary. Use the Pending Change Order section on the Info tab of [PM Document Type](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) to define this default value.
Unchecking the Estimate box
A message will appear if you uncheck the
 Estimate box when there are estimates entered on the Estimate/Purchase
 Details tab. Click Yes to delete the estimates and uncheck the Estimatebox.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## SL

Check this box if the pending change order impacts a subcontract - for example a subcontract item needs to be changed due to a change in scope or a new subcontract needs to be created.
When this box is checked:

- The fields that apply to subcontracts will display on the
 Estimate/Details tab.

- Entering a subcontract cost type in the Cost Type
 field on the Estimate/Purchase Details tab will generate a subcontract detail record.
 You can view the subcontract detail record created from a PCO by selecting Tasks >  Open
 Subcontract Detail. Click [here](/en/vista/vista/project-management/subcontracts/subcontract-change-orders---overview) for general information on subcontract change
 orders.

- The Vendor(SL) box on the [PM
 PCO Add Items](/en/vista/vista/project-management/change-orders/pm-pco-add-items-form) form is enabled. This means that you can click the Add PCO
 Items button in the lower portion of the PM Pending Change Orders form,
 and then use the PM PCO Add Items form to select the subcontracts impacted by the change
 order. This will automatically add them to the Estimate/Purchase Details tab of the PM
 Pending Change Orders form.

Note: This field will populate with the default value set up
 on the document type selected in the PCO Type field, but it can be changed if
 necessary. Use the Pending Change Order section on the Info tab of [PM Document Type](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) to define this default value.Checking this box after entering items on
 the Estimate/Purchase Details tab

If you check this box after entering items on
 the Estimate/Purchase Details tab that are associated with subcontract cost types, the
 system will automatically generate subcontract detail for those items. This subcontract
 detail can be viewed using the [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form) form, which can be launched by
 selecting Tasks >  Open
 Subcontract Detail.
Unchecking the SL box
Unchecking the SL box will
 remove the SL columns from the Estimate/Purchase Details tab. If there are values in these
 fields, those values will be deleted, but any related subcontract detail created by those
 values will not be affected.
Note:You can see the subcontract detail created by a PCO
 by selecting Tasks >  Open
 Subcontract Detail, which will open [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PO

Check this box if the pending change order impacts a purchase order - for example more material on an existing PO needs to be ordered due to a change in scope.
When this box is checked:

- The fields that apply to purchase orders will display on the
 Estimate/Details tab.

- Entering a material cost type in the Cost Type
 field on the Estimate/Purchase Details tab will generate a material detail record. You
 can view the material detail record created from a PCO by selecting Tasks > Open
 Subcontract Detail . Click [here](/en/vista/vista/project-management/materials/po-change-orders-overview) for general information on PO change orders.

- The Vendor(PO) box on the [PM
 PCO Add Items](/en/vista/vista/project-management/change-orders/pm-pco-add-items-form) form is enabled. This means that you can click the Add PCO
 Items button in the lower portion of the PM Pending Change Orders form,
 and then use the PM PCO Add Items form to select the POs impacted by the change order.
 This will automatically add them to the Estimate/Purchase Details tab of the PM Pending
 Change Orders form.

Note: This field will populate with the default value set up
 on the document type selected in the PCO Type field, but it can be changed if
 necessary. Use the Pending Change Order section on the Info tab of [PM Document Type](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) to define this default value.Checking this box after entering items on
 the Estimate/Purchase Details tab

If you check this box after entering items on
 the Estimate/Purchase Details tab that are associated with material cost types, the system
 will automatically generate material detail for those items. This material detail can be
 viewed using the [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form) form, which can be launched by selecting Tasks >  Open Material
 Detail.
Unchecking the PO box
Unchecking the PO box will
 remove the PO columns from the Estimate/Purchase Details tab. If there are values in these
 fields, those values will be deleted, but any related material detail created by those
 values will not be affected.
Note:You can see the material detail created by a PCO by
 selecting Tasks >  Open
 Material Detail, which will open [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Contract

Check this box if the pending change order impacts the contract. When this box is checked, you will be able to enter the impact on the contract using the Contract Impact section on the Info tab in the lower portion of the form.
This field will populate with the default
 value set up on the document type selected in the PCO Type field, but it can be changed if
 necessary. Use the Pending Change Order section on the Info tab of [PM Document Type](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) to define this default value.
Note:A message will display if you check this box and
 enter contract information on a PCO item, and then uncheck the Contract
 box. If you click Yes, the Fixed Amount
 box will be checked and the Fixed Amount field will be set to 0,
 but the contract item will still be associated with the PCO item.
Unchecking the Contract box

A message will display if you uncheck the
 Contract box when there are contracts, add-ons, and/or markups associated
 with PCO items. Click Yesto remove the contract, add-on, and
 markups from the PCO items and then uncheck the Contract box.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Pricing Method

Use this field to select the pricing method of the change order. This will filter the columns on the Estimates/Purchase Details tab so that only the information that you need will display on the form. For example, if you select Lump Sum, the unit and unit cost fields will not display.
Note:The selection in the Estimate,
 SL, and PO boxes also determines which
 fields will display on the Estimate/ Purchase Details tab. For example, the estimate
 fields will only display on the Estimate/Purchase Details tab if you check the
 Estimates box.

This field will populate with the default value set
 up on the document type selected in the PCO Type field, but it can be changed
 if necessary. Use the Pending Change Order section on the Info tab of [PM Document Type](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) to define the default value.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## ROM Amount

The ROM Amount field on the PM Pending Change Order form, header Info tab.
Required.
Use this field to enter a rough order of magnitude (ROM) amount on the pending change order. Enter 0.00 if there is no ROM amount. This field is used for informational purposes only.
If this PCO was created using an RFI or project issue, this field will not populate with the ROM entered using the ROM Price field on PM Issues or PM Request For Information. Those fields will be used as the default contract amount when creating the PCO item.
Note: A PCO is created from an RFI or project issue using [PM Create PCO ](/en/vista/vista/project-management/change-orders/about-the-pm-create-pco-form).
[PM Pending Change Orders Form](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)

## Date Required

Specify the date by which you need this change
 order returned to you.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Date Received

 Enter the date you received the returned
 change order.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Description

This field initially defaults with the description of the change order entered on the Info tab in the header but you can change it if it does not apply. The value in this field can be up to 60 characters long.
Note: This field is disabled once the pending change order
 item is approved.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Status

Use this field to enter the status of the
 pending change order item. This field initially populates with the status code set up using
 the Default
 Beginning Status field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).
You can also change the status of PCO items
 using the Status field on the Info tab in the upper portion of the form. When you
 change the value in the Status field in the header and save the
 PCO, a message will appear asking if you would like to apply the status to the items on the
 PCO. Click Yes and all PCO items that do not have a final status will be updated with
 the new status. PCO items with a final status will not be affected.

### Item Status and PM Cost Projections

How the status that you apply to a PCO item determines if it will be included in cost projections. For more information about the PM Cost Projections process, see [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections).
.

### Printing the PM Pending Change Order Form

If you need to print this pending change order
 using the PM Pending Change Order Form report, do not assign the item the status code set
 up in the Default
 Final Status field on the Info tab of PM Company Parameters until after you
 have finished printing the report. Pending change orders assigned the default final status
 will not be included on the report.

[PM Pending Change Orders Form](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)

## Budget No

The Budget No field on the PM Pending Change Orders form, PCO Items Grid/Info tabs.
This field is only applicable if you have set up project budgets (in PM Project Budgets).
To associate this PCO item with a project budget, enter the budget number or press F4 to select from a list of valid budgets for the specified project.
Note: Entering a budget number in this field is for reference only. The budget details are not automatically added to the Estimate/Purchase Details tab; estimate detail must be entered manually. You can review the budget details as needed by pressing F5 from this field to open PM Project Budgets.

For information about creating and maintaining project budgets, see [PM Project Budgets Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form).
Note: This field is disabled once the pending change order item is approved.

## Force Phase

Check this box to override the assignment of contract items to change order phases when interfacing the change order in PM Interface. You will only need to use this option if phase contract items should always match the contract item assigned to the change order item and you have phases that do not meet this criterion. During the interface, all phases with a contract item not matching the contract item for the change order item will be changed to use the change order item’s contract item.
Leave this box unchecked if phases should use their assigned contract items, regardless of whether they do not match the contract items assigned to the change order item.
Note:Force phase functionality is only implemented during the interface to accounting. If you are using the auto-update phases to Job Cost feature (Active option checked for phases/cost types) and have checked the Force Phase option for a pending change order item, you will still need to run the interface to accounting.

This field is disabled once the pending change order item is approved.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Change in Days

Enter the number of days that the original
 contract completion date will be changed by this pending change order item. When the
 pending change order is approved, the value in this field will be added to the current days
 in contract. You can view the current days in contract using the Current field
 on the Info tab of [PM Contracts
 ](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contracts-form).
Note: This field is disabled once the pending change order
 item is approved.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Cont. Item

Enter the contract item that applies to this
 PCO item or press F4 to select it from a list. You need to select a contract item before
 approving the PCO item. You can enter the contract item now, or when the PCO item is being
 approved using the Contract Item field on the Items tab of the [PM Approve
 PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form) form (Tasks >  Approve
 PCOs).
Note: This field is disabled once the pending change order
 item is approved. Using PCO Item
 Update

If you are creating several PCO items that use the same contract item number, you can skip this field and then use the PM PCO Item Update form to assign the same contract item number to all of the PCO items that have not been assigned one. [More](/en/vista/vista/project-management/change-orders/about-the-pm-pco-item-update-form)
Create a new contract item
If you enter a contract item that does not already exist for the contract, the PM Contract Items form displays, allowing you to set up the new contract item. When finished, you are then returned to this screen.
If the change order item will not be using the same unit of measure and unit price as the contract item to which it is associated, it is suggested that you add a new contract item to ensure proper tracking of units and costs.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Date 1-3

The labels of these three fields are
 customized using [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form). Based on the document type selected in
 the PCO
 Type field, you can customize the labels of these fields or if they even
 display on the form.
There are three similar fields that can display on the PCO.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Management - Overview

## RFI

Enter the RFI associated with this pending change order.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Add-On

Displays all add-ons set up for this project
 in PM Project Add-Ons. Add-ons entered for a project after a change order item is entered
 must be entered here manually. Press F4 for a list of valid add-ons.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Basis

This field initially defaults to the basis set up in [PM Project Add-ons](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form). You can change the default but it will not update the default value defined in PM Project Add-ons.

- P = Percent

- A = Fixed Amount.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Percent %

For Add-ons with a Basis of ‘Percent’
Indicate the percentage (-999.0000 to
 999.0000) to use for calculating the add-on amount for this add-on item. Initially defaults
 to the percentage specified for this add-on in PM Project Add-Ons (which is accessed from
 the Add-Ons tab of the PM Projects form).
For Add-ons with a Basis of ‘Amount’
Initially defaults a calculated percentage for
 this add-on based on the amount specified for the add-on in PM Project Add-Ons, the Net
 Amount, and the Markup Total.
Add-On Amount / (Net Amount + Markup
 Total)
If there are add-ons prior to this one, the
 percentage is based on the Net Amount, Markup Total, and the total of the previous
 calculation.
Add-On Amount / (Net Amount + Markup Total +
 Add-On Amount of previous line)
If you change the calculated percentage, the
 Add-On Amount will be recalculated.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Add-On Amount

This field is only enabled on add-ons with
 'Amount' in the Basis column. Use this field to enter the amount of the add-on.
Note:Changing this amount will recalculate the percentage calculated for the add-on. Likewise, changing the percentage will recalculate the add-on amount.

This field defaults based on the amount set up
 in the [PM Project Add-Ons](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form) form. You can open this form by clicking
 in the Add-On field and then pressing F5. Click [here](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form) for more information about PM Project Add-Ons.
Percentage Basis Add-ons
This field is disabled for percentage basis add-ons and it displays the amount calculated for this add-on based on the Add-On %, the Net Amount, and the Markup Total.
(Net + Markup Total) x % = Add-On Amount
If there are add-ons prior to this one, the Add-On Amount is based on the Add-On %, Net Amount, Markup Total, and the total of the previous calculation.
(Net + Markup Total + Add-On Amount) x % = Add-On Amount

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

##  RFI Type

 Enter the document type (set up in PM Document Types with a category of ‘RFI’).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Date 1-3

The labels of these three fields are
 customized using [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form). Based on the document type selected in
 the PCO
 Type field, you can customize the labels of these fields or if they even
 display on the form.
There are three similar fields that can display on each PCO item.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Include

This field is display only, and it indicates whether an add-on will be included in subtotal add-on calculations. If checked, grand total add-ons will be calculated after net add-ons, with the resulting amount accumulated into the pending total. Subtotal add-ons are calculated next and will include grand total add-ons. The sum of the grand total add-ons will then be subtracted from the pending total, and the grand total add-ons recalculated.
Note:This option applies to Grand Total add-ons only; therefore, it will always show as unchecked for Net Total and Sub Total add-ons.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Total Type

This field is display only and it shows the Add-On Total Type set up in [PM Project Add-Ons](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form). The add-on type determines how the add-on will be calculated and in what order.

- Net Total – This add-on type is calculated first, and will be based on Cost, Cost plus Markup, or Total, depending on the ‘Net Add-On Calculation Level’ specified for the add-on.

- Sub Total – This type of add-on will calculate an add-on amount based on the net amount plus markups plus net total add-ons. Sub total add-ons do a cycle calculation 5 times to provide the most accurate add-on total.

- Grand Total – This type of add-on will calculate an add-on amount based on the net amount plus markups, plus net total add-ons, plus sub total add-ons.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## ECM

Indicate which quantity the unit cost represents.

- E - Unit cost is per each.

- C - Unit cost is per 100.

- M - Unit cost is per 1000.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Estimate Cost/Hour

Enter the cost per hour for this cost type. This field initially defaults to the cost per hour specified for the phase/cost type in PM Project Phases. The value in this field will populate on the Estimate Detail tab of [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form) once the pending change order is approved, and then on the Phase Detail tab of [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form) when the ACO is interfaced with accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
Note: This field only displays when the Estimate box is
 checked on the Info tab in the upper portion of [PM Pending Change Orders
 ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)and LS is not selected in the Est. UM field on the Estimate/Purchase
 Details tab.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Est. UM

Use this field to enter a unit of measure for an estimate. The value in this field will populate on the Estimate Detail tab of [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form) once the pending change order is approved, and then on the Phase Detail tab of [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form) when the ACO is interfaced with accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
Enter a unit of measure or press F4 to select one from a list. Units of measure are created and maintained using [HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form). Press F5 in this field to open this form.
Units of measure are associated with each phase and cost type combination on a project using the Cost Types tab [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form). If you select a unit of measure that does not match one set up using PM Project Phases, a message will display above the grid.
Note: This field only displays when the Estimate box is
 checked on the Info tab in the upper portion of [PM Pending Change Orders
 ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)and Unit Price is selected in the Pricing Method drop down.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Est. Units

Enter the number of units for this phase. If
 the unit of measure is LS, entry of units is allowed, but will typically be set to 0.00;
 however, if you want to post progress to the phase/cost type (i.e., percent complete), set
 the units to ‘1.00’.
Note: This field only displays when the Estimate box is
 checked on the Info tab in the upper portion of [PM Pending Change Orders
 ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)and LS is not selected in the Est. UM field on the Estimate/Purchase
 Details tab.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Est. Hrs/Unit

This field is used to enter the number of hours required to complete a single unit or measure. This field will default based on the hours per unit defined for the phase/ cost type on the Cost Types tab of [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form).
The value in this field will populate on the Estimate Detail tab of [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form) once the pending change order is approved, and then on the Phase Detail tab of [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form) when the ACO is interfaced with accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
Note: This field only displays when the Estimate box is
 checked on the Info tab in the upper portion of [PM Pending Change Orders
 ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)and LS is not selected in the Est. UM field on the Estimate/Purchase
 Details tab.
Note: This field is only enabled when the cost type selected
 in the Cost
 Type field is set to track hours. Cost types are set to track hours using
 the Track Hours box on [JC Cost Types ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-cost-types-form).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Est. Unit Cost

Enter the unit cost for this cost type. Initially defaults the unit cost specified for the phase/cost type in PM Project Phases (once units have been entered).
If you change the Hrs/Unit, Hours, or Cost/Hour, the unit cost is recalculated (based on Hrs/Unit x Cost/Hour).
Note:This field only displays when the Estimate box
 is checked on the Info tab in the upper portion of [PM Pending Change
 Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)and LS is not selected in the Est. UM field on the Estimate/Purchase
 Details tab.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Estimate Amount

Enter the estimated /budget amount of the PCO detail item. This is the change to the budget/estimate created by the PCO detail item, and it will populate on the Estimate Detail tab of [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form) once the pending change order is approved.
This field only applies to the
 estimate/budget, so it will only be enabled when the Estimate box is checked on the Info tab
 in the upper portion of this form.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Material Code

Enter the material that should be ordered or
 press F4 to select it from a list.
This is an optional field. You can skip this field if you have not set up materials.
Materials are created and maintained using the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Pur. UM

Use this field to enter the unit of measure that applies to the subcontract or purchase order. Enter a unit of measure or press F4 to select a unit of measure from a list. Units of measure are created and maintained using [HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form).
This field only applies to subcontracts and
 purchase orders, so this field only displays when the SL or PO box is
 checked on the Info tab in the upper portion of the form, and Unit Price is selected in the
 Pricing
 Method drop down.
Note: This field is disabled when a PO or subcontract item
 is selected in the PO/SL Item field.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Pur. Units

Enter the units associated with the subcontract or purchase order on the PCO detail item. This is the number of units that will be used when the subcontract change order(SCO) or PO change order is created.
Note: This field only applies to subcontracts and purchase
 orders, so it only displays when the SL or PO box is
 checked on the Info tab in the upper portion of the form, and Unit Price is selected in the
 Pricing
 Method drop down.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Pur. Unit Cost

Enter the unit cost associated with the subcontract or purchase order on the PCO detail item. This is the unit cost that will be used when the subcontract change order(SCO) or PO change order is created.
Note: This field only applies to subcontracts and purchase
 orders, so it only displays when the SLor PO box is checked on the Info tab in the
 upper portion of the form, and Unit Price is selected in the Pricing Method
 drop down.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PO Change Order

This field is only enabled when you are
 creating a new record in the Estimate/Purchase Details tab and you have not entered a phase
 and cost type in the Phase and Cost Type
 fields.
Note: This field will only display when the PO box on the
 Info tab in the upper portion of the form is checked.Select An Existing PO Change Order

Use this field to associate a PCO detail item with an existing PO change order (POCO) - for example if you already created a POCO to generate a PO change order document but now you want to add the POCO to a pending change order.
Enter a POCO number or press F4 to select a PO change order from a list. Once a PO change order (POCO) is selected, many of the fields on the tab will populate with the POCO information. This will also lock down all of the fields on the Estimate/Purchase Details tab except the estimate fields. If you want to make a change to the selected POCO, you will have to change it using [PM PO Change Orders ](/en/vista/vista/project-management/change-orders/pm-po-change-orders-form).
Note: The PO change order does not have to be approved, but
 the PO associated with the PO change order does have to be approved. POs are approved using
 the Approved box on the Info tab of [PM
 Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form).
Tip: If you pressed F4 and the POCO that you would like to
 select does not display in the list, the phase on the PCO detail item might not match a
 phase on the desired POCO. Create a new line item on the Estimate/Purchase Details tab, do
 not enter a phase or cost type, and then select the POCO in this field.Remove the PO Change Order

Since this field is only enabled when adding new records, you can't change or remove the POCO or POCO sequence number once it has been added to a PCO detail line item - you have to delete the detail line item to remove the association.
To delete a PCO detail line item, highlight it and then click the Delete icon on the toolbar at the top of the form.
If the POCO has been approved, you'll have to unapprove it using the [PM PO Change Orders ](/en/vista/vista/project-management/change-orders/pm-po-change-orders-form) form before you can delete the PCO detail line item.
Click [here](/en/vista/vista/project-management/change-orders/pm-po-change-orders-form) for information on approving/unapproving PO change orders.
Create a new PO Change Order
You can only select existing POCOs in this
 field. You cannot enter a '+' or 'NEW' in this field to create a new POCO. If you want to
 create a PO change order, select Create > PO Change
 Order. This will open [PM PCO Items Create POCOs](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-pocos-form). Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form) for more information.
Once the PO change order is created, this field will populate with the new PO change order.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview: PO Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PO Change Order Sequence

This field displays the PO change order and PO
 change order sequence number selected using the PO Change Order field.
Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a52d--en) for
 information on using the PO Change Order field.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Interface

Check this box to send this phase/cost type to accounting during the next interface.
Leave this box unchecked if this phase/cost type is not ready to be interfaced to accounting.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Notes

Use this field to enter notes on the estimate/purchase detail item.
If the detail item creates a new subcontract
 change order (SubCO) or PO change order (POCO), the notes in this field will be added to
 the Details field on the Info tab of [PM Subcontract Change Orders](/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form) or [PM PO Change Orders ](/en/vista/vista/project-management/change-orders/pm-po-change-orders-form) form when the pending change order is
 approved.
This works if:

- The system automatically creates a new SCO or POCO
 because the SubCO/PO Change Order field was
 blank.

- You manually create a new SCO/POCO using the
 Create >
 Subcontract Change Orders or PO Change Orders option.

Double-click on this field to open the Grid Notes window.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Phase

Enter
 the phase this change order item affects or press F4 to select a phase from a list.
An error message will display if the selected
 phase is not active. You can set up a phase as active using the Active  box on
 the [JC Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) form (Phases tab).

Related information

- [About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)

- [PM Pending Change Orders Form](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)

## Cost Type

Enter a cost type or press F4 to select a cost type from a list.
If you select a cost type that is a material or subcontract cost type, a material detail or subcontract detail item will be created using the information that you enter into the grid.
This only applies if you also select the
 PO
 and/or SL box on the Info tab in the upper portion of the form - material detail
 will only be created if the PObox is checked, subcontract detail will
 only be created if the SL box is checked.

- Material Detail Items - Material cost
 types are defined using the Material Parameters tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form). If you select a material cost
 type in the Cost
 Type field, the system automatically creates material detail in [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form) using the information on the PCO
 detail item. Select Tasks >  Open
 Material Detail on PM Pending Change Orders to view the created material detail.

- Subcontract Detail Items - Subcontract
 types are defined using the Subcontract Parameters tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form). If you select a subcontract cost
 type in the Cost
 Type field, the system automatically creates subcontract detail in [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form) using the information on the PCO
 detail item. Select Tasks >  Open
 Subcontract Detail on PM Pending Change Orders to view the created subcontract detail.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PO

This field is only enabled when the PO box on the
 Info tab in the upper portion of the form is checked.
Select an existing PO/Create a PO change order
Use this field to select the purchase order
 impacted by the pending change order or press F4 to select it from a list. The lookup only
 includes POs associated with the vendor selected in the Vendor field -
 the vendor in the Vendor field must match the vendor associated with the selected PO.
Only purchase orders that are approved, or
 approved and interfaced can be selected in this field. Purchase orders are approved using
 the Approved box on the Info tab of [PM
 Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form), and are interfaced using [PM
 Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
Once a purchase order is selected, use the
 PO/SL
 Item field to select the purchase order item associated with the PCO detail
 item.
Note:After a purchase order and PO item have been added
 to a PCO detail item, you can use that information to create a PO change order. Select
 Create >  PO Change
 Order, which will open [PM PCO Items Create POCOs](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-pocos-form).
Create a new PO

Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) for a tutorial on creating a new PO using the information on a pending change order - this creates a new PO, not a new item on a existing PO.
Default purchase order
If you enter a phase, cost type, and vendor on
 the Estimate/Purchase Details tab, the PO field will populate with the
 associated purchase order.
This only occurs if the following is true:

- There is only one purchase order for the vendor on the selected project.

- There are no open subcontracts on the vendor.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Estimate Hours

Enter the total number of hours required to complete this phase/cost type.
This field defaults based on the Units x the Hrs/Unit. If you change the default, the Hrs/Unit will automatically be recalculated. This field is only enabled if cost type is set to track hours.
The value in this field will populate on the Estimate Detail tab of [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form) once the pending change order is approved, and then on the Phase Detail tab of [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form) when the ACO is interfaced with accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
Why is this field displaying?
This field is only enabled if the cost type
 selected in the Cost Type field on this tab is set up to track hours.
Cost types are set up to track hours if the
 Track
 Hours box is checked on the [JC Cost Types](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-cost-types-form) form.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Vendor

Use this field to select the vendor associated
 with the subcontract or PO being entered on this PCO detail item. Enter a vendor number or
 press F4 to select one from a list. The list can be filtered to display all
 vendors or only vendors that are associated with a subcontract or purchase order on the
 project.
Tip:The sort name can be used instead of the firm number
 when selecting firms in PM module forms. Generally the sort name is the first several
 letters of the firm name.  For example when creating a subcontract in the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form for 'Bryan Electrical', you can
 enter the sort name 'bryan' in the Vendorfield instead of the firm number
 '10042'. The sort name of a firm is set up using the Sort Name
 field on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

This field is only visible when the PO or
 SL
 box on the Info tab in the upper portion of the form is checked.
Note: If a purchase order is selected in the POfield or a
 subcontract is selected in the SL field, the vendor in this field must
 match the vendor on the PO or subcontract.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## New SL

Check this box if you want to create a new
 subcontract using the detail item. The system will populate the SL field with
 the next available number and create the new subcontract when the PCO is saved. The new
 subcontract will be associated with the PCO using the [Related
 Items](/en/vista/vista/project-management/about-related-items) feature.
Create a new subcontract
When you check this box, the system will
 populate the SL field with the new subcontract number. The system will assign a
 subcontract number like the Initialize button on the [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form) form, but it will always create a new
 subcontract. It will not automatically create a new item on an existing subcontract that is
 associated with the same vendor.
You can change the automatically generated
 number if you want to assign a different number, but not after the PCO has been saved.
What happens when the New SL box is checked and you change the subcontract number in the SL field?
If the New SL box is checked and the PCO has
 already been saved, changing the subcontract number in the SLfield will
 automatically create another subcontract.
Important: For example when you check the New SL box and
 then save the PCO, the system will create the new subcontract. Changing the subcontract
 number in the SLfield will create another subcontract, not change the subcontract number
 of the new subcontract.Checking this box
 will create the subcontract when the PCO is saved

When you check this box and save the PCO, the system will create the subcontract. You can view the new subcontract using the [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) form. This means that the new subcontract is created before the PCO is approved, and it can be approved and interfaced before the PCO is approved.
 If you do not check this box
If you do not check this box, you can also do the following:

- Select an existing subcontract -
 Select an existing subcontract using the SL and PO/SL Item
 fields. This can either create a new item on an existing subcontract, or change an
 existing item on the subcontract.

- Create a new subcontract after the PCO is
 approved - If you do not want to create the subcontract until the PCO has
 been approved, you can enter the subcontract purchase information (vendor, unit, and
 purchase information but not a subcontract and item number) using the Estimate/Purchase
 Details tab. Once the PCO has been approved, open the [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form) form, select Approved COs
 in the Record
 Type drop down, and then assign the subcontract detail to a subcontract.
 Step by step instructions on creating
 a new subcontract, or performing other tasks using the PM Pending Change Orders
 form

Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) for basic
 step by step instructions on using the PM Pending Change Orders form, including how to
 create a new subcontract from a PCO.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## SL

This field is only enabled when the SL checkbox is
 selected on the Info tab in the upper portion of the form.
Create a subcontract change order(SubCO)/Select an existing subcontract
Use this field to select the subcontract
 impacted by the pending change order or press F4 to select it from a list.
Once a subcontract is selected, use the
 PO/SL Item
 field to select the subcontract item associated with this PCO detail item.
Note:After a subcontract and subcontract item have been
 added to a PCO detail item, you can use that information to create a subcontract change
 order. Select Create > Subcontract
 Change Order, which will open [PM PCO Items Create SCOs](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form).
Create a new subcontract

Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) for a tutorial on creating a new subcontract using the information on a pending change order - this creates a new subcontract, it does not create a new item on an existing subcontract.
Default subcontract
If you enter a phase, cost type, and vendor on the Estimate/Purchase Details tab, the
 SL
 field will populate with the associated subcontract if all of the following is true:

- There is only one open subcontract for the vendor on the selected project.

- There are no open purchase orders on the vendor.
What if the subcontract that you want to select doesn't display in the lookup?

Press F4  in SL field to
 select a subcontract from a list. There are generally two reasons why a subcontract doesn't
 display in this list.

- Vendor - The lookup only includes subcontracts that are associated
 with the vendor selected in the Vendor field. This means that the
 vendor in the Vendor field must match the vendor associated with the selected
 subcontract.

- Subcontract
 not interfaced - Only subcontracts that have been approved, or
 approved and interfaced using [PM
 Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) can be selected in this field. Subcontracts can be approved using
 the Approved box on the Info tab of [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PO/SL Item

Use this field to select the PO or subcontract
 item that is affected by the change, or use this field to create a new PO or subcontract
 item. This field is used in conjunction with the PO and SL field.
Select an Existing PO or Subcontract Item
Press F4 to select an existing item on the PO
 or subcontract selected in the PO or SL field.
Create a New PO or Subcontract Item
Enter a '+" or an item number that does not exist on the PO or subcontract to create a new item.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Purchase Amount

Enter the purchase amount of the subcontract
 or purchase order. This field will calculate based on the values entered in the other
 purchase fields - Purchase UM, Purchase Units,  Purchase Unit
 Cost, and ECM.
The value in this field will be used as the amount on the material detail or subcontract detail created from this item. For example, if this PCO detail item is a change to an existing subcontract item, the value entered in this field will be used as the amount of the subcontract change order line item created by the PCO item.
You can view the subcontract or material
 detail created using the PCO by selecting Tasks >  Open
 Subcontract Detail or Open Material Detail.
Note: This field only applies to POs or subcontracts, so it
 only displays when the SL or PO box is
 checked on the Info tab in the upper portion of the form.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## SubCo: Subcontract Change Order

This field is only enabled when you are
 creating a new record in the Estimate/Purchase Details tab and you have not entered a phase
 and cost type in the Phase and Cost Type
 fields.
Select An Existing Subcontract Change Order
Use this field to associate the detail item
 with an existing subcontract change order(SCO) - for example if you already created a SCO
 using the PM Subcontract Change Orders form to generate a subcontract change order document
 but now you want to add it to a pending change order.
Enter a subcontract change order number or
 press F4 to select one from a list. Once a SCO is selected, many of the fields on
 the tab will populate with the SCO information and become disabled. If you want to make a
 change to the selected SCO, you will have to change it using [PM Subcontract Change Orders,](/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form) which will update the PCO
 detail item.
Note: The SubCO selected in this field does not have to be
 approved.Remove the Subcontract Change
 Order

Since this field is only enabled when adding new records, you can't change or remove the SCO or SCO sequence number once it has been added to a PCO detail line item - you have to delete the detail line item to remove the association.
To delete a PCO detail line item, highlight it and then click the Delete icon on the toolbar at the top of the form.
If the SCO has been approved, you'll have to unapprove it using the [PM Subcontract Change Orders](/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form) form before you can delete the PCO detail line item.
Click [here](/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form) for information on approving/unapproving subcontract change orders.
Create a Subcontract Change Order
You can only select existing SCOs in this
 field. You cannot enter a '+' or 'NEW' in this field to create a new SCO. If you want to
 create a new SCO, select Create > Subcontract
 Change Order. This will open [PM PCO Items Create SubCOs](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form). Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form) for more information.
Once the subcontract change order is created, this field will populate with the new subcontract change order.

[](/en/vista/vista/project-management/subcontracts/subcontract-change-orders---overview)Overview: Subcontract Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## SubCO Seq: Subcontract Change Order Sequence

This field displays the subcontract change
 order and SubCO sequence number selected using the SubCO field.
Click [here](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form/field-definitions-pm-pending-change-orders-form#ID-0002a4f9--en) for information
 on using the SubCO field.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Active

Check the this box if the phase/cost type should be immediately updated to the Job Cost module where it can begin to accumulate costs. If you leave this box unchecked, the phase/cost is considered pending and will not update to the Job Cost module until the change order is approved and interfaced using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

##  Ins Code - Insurance Code

 For existing project phases, this field is disabled and displays the insurance code assigned to the phase in JC Job Phases or PM Project Phases. If no insurance code is assigned to the phase, displays as null.
 For new phases, enter the insurance code (from HQ Insurance Codes) that applies to this phase, if applicable. Once record is saved, phase and insurance code will be updated to JC Job Phases/PM Project Phases (applies to ‘locked phases’ jobs as well).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Bill Flag

Specify whether units and/or costs for this cost type on this phase are to be used in calculating progress complete. Used only for Job Billing.

- Y-Units and Dollars - Both units and dollars posted to this cost type will be used to calculate progress complete.

- C-Only Dollars - Only dollars will be used in calculating percent complete for this phase/cost type.

- N-Neither - Neither units nor dollars posted to this cost type will be used when calculating progress complete.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Item Unit Flag

Specify whether this cost type will be used to accumulate units complete for the contract item.
Check this box if this cost type (for this phase) will be used to accumulate units complete for the related contract item. When summarizing job costs, all costs are totaled, but only the units posted to the specified phase/cost type are counted.
Leave this box unchecked if this cost type will not be used to accumulate units complete for the related contract item.
Note:Generally, this flag is checked for only one cost type on one phase, and the phase selected would be the one most closely related to the contract item.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Phase Unit Flag

 Specify whether this cost type will be used to accumulate units complete for this phase.
 Check this box if this cost type will be used to accumulate units complete for this phase. Typically, this flag is checked for the main cost type, and only units posted to that cost type for that phase would be accumulated.
 Leave this box unchecked if this cost type will not be used to accumulate units complete for this phase.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Notes (Item)

Use this tab to enter notes on this PCO item.
 The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools >
 Spelling to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Initiated By

Use the drop down to select who initiated the pending change order.
Select the blank option if you do not want to select an initiator.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Fixed Amount

Check this box if the PCO impact on the
 contract is a fixed amount. Leave this box unchecked to use calculated amounts. This field
 only displays when the Contract box on the Info tab in the upper
 portion of the form is checked.
Note: This field is disabled once the pending change order
 item is approved.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Fixed Amount / Pending Amount

If the Fixed Amount box is not checked, this
 field’s label is ‘Pending Amt’ and is disabled. If Fixed Amount box is checked, this field’s
 label is ‘Fixed Amount’ and is enabled.
Enter the fixed amount for this pending change
 order. If LS is selected in the UM field (this is a lump sum PCO item),
 this field defaults the Schedule and Cost Impact ‘Total Price’. If you are creating a units
 based PCO item, this field defaults based on the Units x Unit Price.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## PCO Item

Enter the pending change order item, up to 10 characters, or enter ‘+’ to assign the next sequential item number.
Note:If you do not allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters unchecked), you can only view existing change order items; you cannot not add new change order items or modify existing ones (all inputs will be disabled).

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## UM: Unit of Measure

Enter the unit of measure for this change order item. A message will appear if the contract item unit of measure differs from the unit of measure indicated here.
If this occurs, you should create a new contract item to accommodate the new unit of measure and ensure that both units and costs are tracked and updated properly. If you choose to ignore this warning, be aware that only dollars will be updated to the contract item in Job Cost.
Note:This field is disabled once the pending change order item is approved.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Unit Price

Enter the unit price for this pending change order item. This field initially defaults to the unit price in [PM Contract Items](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contract-items-form) for the contract item assigned to this pending change order item.
Note:This field is disabled once the pending change order item is approved.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Units

Enter the number of units on the PCO item.
This field is only enabled when the unit of
 measure selected in the UM field is not LS (lump sum), and the
 Contractbox on the Info tab in the upper portion of the form is checked.
Note: This field is disabled once the pending change order
 item is approved.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Cost Type

Display only.
This field displays the cost type associated with the markup.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Internal Markup %

Enter the internal markup percentages for each of the cost types associated with this pending change order.
The system calculates the markup amount for each cost type (MU% x Net Amount) and displays the amount in the Internal Markup Amt column. Note that the Gross Amount (far right) is adjusted to include the calculated amount.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.

## Contract Markup %

Enter the contractual markup percentage for each cost type associated with this pending change order. Initially defaults the percentage specified for each cost type in PM Projects (Markups tab).
The system calculates the markup amount for each cost type (MU% x Net Amount) and displays the amount in the Contract Markup Amt column. Note that the Gross Amount (far right) is adjusted to include the calculated amount.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.
