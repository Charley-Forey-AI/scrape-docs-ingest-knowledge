---
title: "Field Definitions: IN Material Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form/field-definitions-in-material-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form/field-definitions-in-material-order-entry-form"
---

# Field Definitions: IN Material Order Entry Form

The following is a list of field descriptions for the IN
 Material Order Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter NEW to create a new entry or enter the batch sequence number of an existing entry you wish to display.

##  Action

 When adding new entries, this field defaults to A-Add and cannot be accessed.
 If this is an existing transaction, specify the action for this entry.

- C-Change – Use this action to make
 changes to transactions that have already been processed.

- D-Delete – Use this action to
 delete the transaction from all files in IN. (The delete functions in the toolbar and
 Records menu only delete the entry from the batch.)

## Material Order

Use this field to define the material order number. The material order number must be unique and it can be up to 10 characters long.
Note: This field is disabled if you are editing a material order that has already been posted. Automatically Generated Material Order Numbers
This field will automatically populate with a
 material order number if the Auto Generate MO#s box on the Info tab of
 the [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form)form is checked.
The generated number will populate based on
 the value in the Last Used MO # field on the Info tab of the [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form. [More](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form/field-definitions-in-company-parameters-form#ID-00013779--en)

## Description

 Enter a description of this material order. The description can be up to 60 characters long.

## JC Company Number

Required.
Enter the Job Cost module company for this
 material order or press F4 to select one from a list. The jobs
 associated with the material order must all be associated with the company selected in this
 field.
Note: This field is disabled if you are editing a material order that has already been posted.

## Job

Required.
Enter a valid job for this material order ore
 press F4
 to select a job from a list. This job will be default on all items on this
 material order, and will also be the job by which material orders will be selected in the
 close process in the [IN Material Order Close ](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-close-form) form.
Note: If you enter a soft- or hard-closed job, the status displays in red above the tab page. Entry is only allowed if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

## Order Date

Enter the order date for this material order. This can be the date the materials were actually ordered or the date the material order was entered.
This field will populate with the current date when entering a new material order.

##  Ordered By

 Enter the name or initials of the person who ordered the materials on this material order. Up to 20 characters allowed.

##  Status

 This field indicates the status of this material order.

- 0- Open

- 1- Complete

- 2- Close

 When entering a new material order, this field defaults to "Open" and is disabled. If editing an existing material order (one that has already been processed), this field is enabled.
 The status of a material order can be changed from “Open” to “Complete” or from “Closed” or “Complete” to “Open.” However, to close a material order, use IN Material Order Close.

## Item #

Enter a material order item number, up to 5
 digits, or enter New, N, or + to have the system assign a sequential
 number.

##  Action

 When entering a new item, this field defaults to A (Add) and cannot be accessed.
 If this is an existing item, specify the action for this entry.

- C-Change – Use this action to make changes to transactions that have already been processed.

- D-Delete – Use this action to delete the transaction from all files in IN. (The delete functions in the toolbar and Records menu only delete the entry from the batch.)

##  Location

 Required.
 Enter the location that is supplying the material specified on this item. This must be a valid, active IN location.

## Material

Enter a material or press F4to select one from a list. The material must be
 set up at the location selected in the Locationfield.
You can set up a material at a location using
 the [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form) form.

##  Description

 Initially defaults the description defined for the material in HQ Materials; may be overridden. Up to 60 characters allowed.

## Job

Required.
Enter the job that this material is being
 charged to or press F4 to select one from a list. This field defaults the job selected in the
 Job
 field in the upper portion of the form.

-  If this is an existing material order and this item has been confirmed, this field is disabled and cannot be changed.

- If you enter a soft- or hard-closed job, entry is only allowed if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

## Phase

Enter the phase that is being charged with
 this material or press F4 to select a phase from a list.
 This field defaults with the phase entered in
 the Matl
 Phase field on the Info tab of the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.
Note: This field cannot be changed if this is an existing material order and the item has been confirmed.

## Ticket

The Ticket field on the IN Material Order Entry form, Items section.
Enter the field ticket number for this material order item or press F4 to select from a list of valid field tickets for the specified job/contract.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to material order items is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

##  Cost Type

 Enter
 the cost type to which this material is being charged, or press F4 to select a
 cost type from a list. If [phases are locked](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form/field-definitions-jc-jobs-form#ID-00018cec--en) in[JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form), the cost type must be a valid cost type for this
 phase or job phase.
Initially defaults from the Matl CT field
 from the Info tab of [HQ Materials](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) (if specified for the material).
Note: If this is an existing material order and this item has been confirmed, the cost type cannot be changed.

##  GL Account

 This is the job expense account to debit when posting confirmations for this item. Initially defaults from the JC department assigned to the job specified for this item. This may be overridden if allowing overrides to GL account (option in JC Company Parameters); otherwise, field is disabled.

##  Date Req

 Specify the date this material is required.

## UM - Unit of Measure

 Enter the unit of measure for this material
 or press F4
 to select it from a list. This field populates with the standard unit of
 measure set up on the material using the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.
You can change the unit of measure, but it must be a valid unit of measure for this material.
 This will be the 'posted' unit of measure when updating JC detail. If this unit of measure matches (or can be converted to) the unit of measure for the specified phase/cost type, then 'posted' units will also become JC units.

## Units

Specify the number of units of this material needed. If the units entered here exceed the 'on hand' units for the material (in IN Location Materials), a warning is displayed, but the entry is allowed.

## Unit Price

Enter the unit price for this material.
This field defaults based on the Pricing Option for Jobs in [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) and the following:

- If you selected a unit of measure in the UMfield
 that is set up as an additional unit of measure on the Additional UM tab on the [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)form, this field will default
 based on the unit cost set up in IN Location Material.

- If you selected a unit of measure in the UMfield
 that is not set up in IN Locations, the Unit Price field will default based
 on the unit price set up using the Additional Units of Measure tab on the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.

## ECM

Specify the quantity that the unit price represents. Initially defaults the unit price's ECM based on the Pricing Option for Jobs in IN Company Parameters and the current unit cost/unit price values in IN Location Materials.

- E - Per Each

- C - Per Hundred

- M - Per Thousand

##  Total

 This field displays the calculated total on the material (Units x Unit Price). This is the total committed cost to the job for this material (less tax).
If you change the value in this field, the
 system will recalculate the Unit Price field.

##  Tax Code

 This field is null and disabled if the "Use Tax"
 flag is unchecked for this company (JC Company Parameters).
 Specify the tax code for this material. If
 the material is flagged as taxable (HQ Materials), this field defaults the tax code
 specified for the job (in JC Jobs); otherwise, defaults as null; may be overridden.
 Tax amount is calculated, but is not included in the Total amount. Additionally, if you have specified a JC Tax Phase/Cost Type for the tax code (in HQ Tax Codes), tax amount will be posted to that phase/cost type. Otherwise, taxes will be posted to this item's phase/cost type.
Note: If this is an existing material order and this item has been confirmed, the tax code cannot be changed.
