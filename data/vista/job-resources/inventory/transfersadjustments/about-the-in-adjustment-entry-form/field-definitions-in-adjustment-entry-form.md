---
title: "Field Definitions: IN Adjustment Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-adjustment-entry-form/field-definitions-in-adjustment-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-adjustment-entry-form/field-definitions-in-adjustment-entry-form"
---

# Field Definitions: IN Adjustment Entry Form

The following is a list of field descriptions for the IN
 Adjustment Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Sequence Number

By default this field will populate with "NEW". Press TAB and move through the field and the system will create a new record and automatically assign it the next available sequence number.
 The sequence number must be unique to the adjustment entry batch.

## Action

When adding new entries, this field defaults
 to A (Add)
 .
Select one of the following action when changing an existing item.

- C-Change – Use this action to make changes to transactions that have already been processed.

- D-Delete – Use this action to delete the transaction from all files in IN.

Note: Using the Delete icon in the toolbar at the top of the form will only delete the entry from the batch; it will not delete the transaction.

## IN Transaction

This field displays the transaction numbers associated with the adjustment and is always disabled.

##  Date

 Enter the actual posting date for this adjustment entry.
This field automatically populates with the current date.

## Location

Enter the location of the adjustment entry or
 press F4 to select a location from a list.
Locations are associated with materials using the [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form) form.

## Material

Enter a material code or press F4 to select a
 material from a list. The material must be set up at the location selected in the
 Location field.
Materials are set up in locations using the [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form) form.

##  GL Account

 The expense account entered here will be used to record the use of the
 material.
This field populates with the inventory
 adjustment account set up using the Adjustments field on the Inventory
 Accounts tab of the [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)form. If there is a GL account set up in the
 Adjustments field on the [ IN Location Category Override ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-category-override-form) form, that account will be
 used instead.

## Units

Enter the number of units for this adjustment. This is the number of units that the On Hand and Booked quantities on the selected material will be changed.

- Enter a positive number to increase inventory.

- Enter a negative number to decrease inventory.

- Enter a zero if there is no change to the On Hand and Booked units.

You can see the On Hand and Booked units associated with a material using the Costs/Quantities tab on the [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form) form.

## Unit Cost

This field is only available when the Allow Unit Cost Overrides checkbox is selected in IN Company Parameters.
Defaults a unit cost for this material (from IN Location Materials) based on the Cost Method for the location or category (i.e. if the Cost Method is Average Cost, then the Avg Unit Cost defined for the material in IN Location Materials will default here.)
Unit Cost may only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters). Override value must be equal to or greater than 0.00.
Note: Entry in this field will only be updated to Inventory if the GL account for this adjustment entry is the same as the Inventory Adjustments account specified for the location or category. Unit cost updated is determined by Cost Method.

## ECM

Select what quantity the unit cost represents.
 You can only change the selection in this field if the Allow Unit Cost Overrides box on the
 Additional Information tab on the [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form is checked.

- E – Per Each

- C – Per Hundred

- M – Per Thousand

## Total Cost

Defaults an amount based on Units x Unit Cost. If Units are 0.00, the defaults will be 0.00. This value may be overridden and can be a positive, negative, or zero amount. This field updates to GL unless the value is 0.00.

## Memo

Use this field to enter a description of this adjustment.
 The memo can be up to 30 characters long.
