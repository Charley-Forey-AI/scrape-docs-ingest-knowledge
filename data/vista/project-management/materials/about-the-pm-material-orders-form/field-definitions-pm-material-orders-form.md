---
title: "Field Definitions: PM Material Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/about-the-pm-material-orders-form/field-definitions-pm-material-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/about-the-pm-material-orders-form/field-definitions-pm-material-orders-form"
---

# Field Definitions: PM Material Orders Form

The following is a list of field descriptions for the PM
 Material Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project for which to enter/modify material orders. Must be a valid project set up in PM Projects.
Note:If you enter a project with a closed status (hard or soft), the status displays in red to the right of the project description. You will only be able to add or modify material orders for the project if you allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters checked).

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  IN Co

 Specify the Inventory company providing the materials specified on this material order. Must be a valid company set up in IN Company Parameters.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

## Material Order

Create a new material order
When you are creating a new material order, you are creating it for the project and Inventory company selected in the
 Project
 and
 IN Co
 fields.
There are several ways to create a new material order:

- Enter a material order number that does not exist for the project and Inventory company. The material order number can be up to 10 characters long. The format of the number can by anything, but you should probably use the format set up for MO numbers in PM Company Parameters.

- Enter a '+' in this field if you would like the
 system to automatically assign the MO the next available number. The system will select
 the next available number if Project/Sequence is selected in the MO Number Type
 field on the Material Parameters tab in the [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) form.

- Click the New Record icon () at the top of the form, and then
 complete the IN
 Co field. The system will automatically populate the Material Order
 field with the next available number if Project/Sequence is selected in the MO Number Type
 field on the Material Parameters tab in the PM Company Parameters form.
Select an existing material order

Enter an existing material order number, or press F4 to select an MO from a list.
[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

## Description

Enter a description of this material order, up to 30 characters.
Note: If the material description is blank and you checked
 the Default
 Material Descriptions from Phase Description box in PM Company Parameters,
 the phase description will be used as the material description. If the Default Material
 Descriptions from Phase Description box is unchecked, the system will
 default the material description from the contract item assigned to the phase.
[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

## Date Ordered

Enter the order date materials of the material order.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Ordered By

 Enter the name (or initials) of the person who ordered the materials for, or initiated, this material order, up to 10 characters.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Approved

 Check this box if this material order has been approved. This box must be checked in order for this material order to be interfaced to Inventory.
 Leave this box unchecked if this material order has not been approved.
By
 If the material order’s Approved box is checked, this display-only field indicates who approved the material order. This will always be the current login.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Item

Manually enter the item number, or enter a '+', 'n', 'N' or 'New' if you want the system to automatically assign the new item the next available number.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Location

 Enter the IN location from which these materials were ordered. Must be a
 valid location set up in IN Locations.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Material

 Specify the material ordered. Must be a valid HQ material set up for the location in IN Location Materials.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

## Item Description

Enter a description of this material order item, up to 60 characters. Initially defaults the material description.
Note: If the material description is blank and you checked
 the Default
 Material Descriptions from Phase Description box in PM Company Parameters,
 the phase description will be used as the material description. If the Default Material
 Descriptions from Phase Description box is unchecked, the system will
 default the material description from the contract item assigned to the phase.
[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Phase

 Enter the phase that will be charged for this material. Initially defaults the phase specified for the material in HQ Materials, if one exists. Otherwise, defaults as null.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

## Cost Type

Enter the cost type that will be charged for this material. Initially defaults the cost type specified for the material phase in HQ Materials. If no cost type specified in HQ Materials, defaults the Material Cost Type specified in PM Company Parameters. Otherwise, defaults as null.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Units

 Enter the number of units ordered of this material.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  UM

 Specify the unit of measure in which this material was ordered. Initially defaults the sales UM specified for the material in HQ Materials. May be overridden, but must be either the standard unit of measure for the material or a valid unit of measure for this material and location (i.e. set up for the material and location in IN Material Units of Measure).

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Unit Cost

 Specify the unit cost for this material. Initially defaults an amount based on the Pricing
 Option for Jobs in IN Company Parameters, the cost or price values in IN Location
 Materials, and the markup/discount rate specified for the job in JC Jobs. If no
 markup/discount rate specified for the job, uses the markup/discount rate for jobs in IN
 Location Materials.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  ECM

 Specify the quantity the unit cost represents.

- E = Per Each Unit

- C = Per 100 Units

- M = Per 1,000 Units

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Amount

 Initially defaults an amount based on the Units x Unit Cost. Overriding this amount will cause the unit cost to be recalculated.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Date Required

 Specify the date by which this material is required.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Send

 Check this box if this material order item is ready to be interfaced. This box must be checked in order for this item to be updated when the material order is interfaced to IN (via PM Interface).
 Leave this box unchecked if this material order item is not ready to be interfaced. Item will be skipped when the material order is interfaced to IN.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  ACO

 For non-interfaced items only, displays the approved change order to which this material order item applies (if applicable).

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  ACO Item

 For non-interfaced items only, displays the approved change order item to which this material order item applies (if applicable).

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Tax Code

 Specify the tax code for this material, if applicable. If the material is flagged as ‘taxable’ (in HQ Materials), this field defaults the tax code specified for the project (if one exists). If the material is not taxable, defaults as null.

[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders

##  Notes

 Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or select
 Tools >  Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field, right
 click the mouse while focus is in the field and select Standard
 Notes from the shortcut menu, which opens the Standard Note Copy window.
 Then enter the standard note to copy (or select from F4 lookup) and click OK. The
 system inserts the selected note into the field.
[](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form)PM Material Orders
