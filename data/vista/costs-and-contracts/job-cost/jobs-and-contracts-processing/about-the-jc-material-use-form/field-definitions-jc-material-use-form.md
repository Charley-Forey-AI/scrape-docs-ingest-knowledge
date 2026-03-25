---
title: "Field Definitions: JC Material Use Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form/field-definitions-jc-material-use-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form/field-definitions-jc-material-use-form"
---

# Field Definitions: JC Material Use Form

The following is a list of field descriptions for the JC
 Material Use form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Sequence Number (Seq)#

Create a new transaction
 Enter N, New, or + to add a new sequence and create a new transaction. The system will automatically assign the next available sequential number.
Select an existing transaction
Enter the sequence number of an existing entry or select it using the Grid tab.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Action

Creating a new transaction
This field defaults to A (Add) and cannot be changed.
Modifying an existing transaction
If this is an existing transaction, select one of the following:

- Change - Change a transaction that
 has already been processed.

- Delete - Delete an existing
 material use transaction. Using the Delete icon on the toolbar only removes the entry
 from the batch, it does not delete the existing material use transaction in the Job
 Cost module.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Transaction Number (Trans #)

This is the transaction number assigned to a transaction when it is posted in JC Batch Process.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## JC Type

Select the transaction type.

- IN - Inventory — Select this type to post costs for materials sold from your own inventory - these are materials that have been set up in [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form). Posted units will update the on-hand quantity and records in Inventory. Although a non-standard unit of measure can be used during entry, Inventory will be updated in the standard unit of measure using the conversion factor specified for the non-standard unit of measure.

- MI - Miscellaneous — Select this type to post costs for miscellaneous materials used on your own jobs. Miscellaneous materials include valid materials that have been set up using [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) or non-valid materials (materials that have not been set up using HQ Materials).

Note: You can only select a non-valid material if the
 Validate
 Material box on the Materials tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) is not checked.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## IN Company

Enter the inventory company that sold the
 selected material or press F4 to select it from a list.
This field is only enabled when you select
 "Inventory" in the JC Type field, and it defaults from the IN Co# field on
 the Info tab of JC Company Parameters. Once a inventory company is selected, it will be the
 default for the rest of the transactions in the batch.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Location

Enter the location that the material was sold from or press F4 to select it
 from a list. Locations are created and maintained using [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form).
This field is only enabled when you select
 ‘IN-Inventory’ in the JC Type field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Material

Enter the material for this transaction or press F4 to select it from a list.

- If "Inventory" is selected in the JC Type
 field, the material selected in this field must be set up at the location selected in
 the Location field. Materials are set up in locations using the [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form).

- If "Miscellaneous" is selected in the JC Type
 field and the Validate Material box on the Material tab of the [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) form is checked, the material
 must be set up in the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.

Note: If the Validate Material box is not checked, you
 can enter any material. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form/field-definitions-jc-company-parameters-form#ID-00017068--en) for more information on the Validate
 Material box on the JC Company Parameters form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Job

Enter the job the material use applies to or press F4 to select it from a list.
Note: If you enter a soft- or hard-closed job and you allow posting to closed jobs (flags in JC Company Parameters), the job's status will display in red; however, entry is allowed. If you do not allow posting to closed jobs, a message displays indicating the job’s status and entry is not allowed.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Phase

 Enter the phase
 that applies to the material use or press F4 to select it from a list.
If phases are locked, must be a valid job phase (i.e. set up in JC Job Phases).
If phases are not locked, may be any valid
 phase (i.e. set up in JC Phases or JC Job Phases).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Cost Type

This is the cost type that will be used to post
 the material cost. Enter a cost type or press F4 to select one from a list.
The selected cost type must be set up on the
 phase using [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) or on the job phase using [JC
 Job Phases ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Field Ticket

The Field Ticket field on the JC Material Use form.
Enter the field ticket number for this material usage entry or press F4 to select from a list of valid field tickets for the specified job/contract.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to material usage for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Description

Enter a description for the transaction. The text in this field can be up to 60 characters long.
This field defaults based on the following:

- If you entered a valid HQ or IN material, defaults the description of the specified material.

- If you entered a miscellaneous material, defaults as "New Material".

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Date

Enter the date that will become the Actual Date for the transaction.
This field defaults the current date.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Transaction Account

This field is enabled if one of the two conditions apply:

- The Allow GL Account override when posting
 costs box is checked in JC Company Parameters (GL Cost tab)

-or-

- The Allow GL Account override when posting
 costs box is unchecked, but the GL account defaults as null (blank).

The transaction GL account defaults as follows:

- If an override account is defined for the phase in
 JC Departments (Phase Overrides tab), defaults the override account.

- If no override account is defined for the phase,
 defaults the GL account defined for the specified cost type in JC Departments (Cost
 Types tab).

- If no GL account specified at either the phase or
 cost type level (in JC Departments), defaults as null.

If no default account was specified, or if allowing overrides and you are overriding the default, enter the GL account to charge for this material cost. Must be a valid GL account set up (in GL Chart of Accounts) with a ‘Job’ or ‘null’ sub ledger code.
Note: If this is an intercompany transaction (i.e., you
 specified an IN company above that differs from the active JC company), the account
 specified here must be a valid GL account for the active JC company.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Offset Account

Specify the GL account (from GL Chart of Accounts) to use for the
 offsetting entry.
 If the JC Type is IN-Inventory, the account must
 have a sub ledger code of 'I' (Inventory) or 'null' (blank). The offset account will
 default from the Job Sales account (Sales Accounts tab) defined for the specified IN
 Co/Location in IN Locations, IN Location Company Override, or IN Location Co & Category
 Override.
Note: This field is disabled for IN-Inventory transactions;
 if you did not define a Job Sales account for the specified location, this account will
 default as null. You will be required to assign a Job Sales account in IN Locations before
 you can process the batch.
 If the JC Type is MI-Miscellaneous, the sub
 ledger code must be 'null'. The offset account will default as follows:

- If a non-stocked material, defaults the Non-Stocked GL
 Account defined in HQ Material Categories.

- If a miscellaneous material (not set up in HQ
 Materials), defaults the Misc Matl GL Account specified in
 JC Company Parameters (Material tab), less any tax.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

##  UM

 Defaults the standard unit of measure for the material as defined in HQ Materials. May be overridden, but must be a valid unit of measure for the material (i.e. set up on the Addl UMs tab in HQ Materials). Inventory will be updated in the standard unit of measure using the conversion factor specified for the non-standard unit of measure.
 If you entered a miscellaneous material not set up in HQ, enter a valid unit of measure (from HQ Units of Measure) for the material.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Units

Enter the number of units used.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

##  Unit Price

 If
 you entered a miscellaneous material not set up in HQ Materials, enter the unit price for
 this material.
 If you entered a stocked material, the unit
 price is calculated using the Pricing Option for Jobs specified in IN Company Parameters
 and the markup/discount rate specified for the job in JC Jobs.
 If you entered a non-stocked HQ material, the unit price defaults from HQ Materials.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## ECM

Select what quantity the unit price represents.
E = Per Each
C = Per Hundred
M = Per Thousand

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Tax Code

 Enter the tax code for this material or press
 F4 to select it from a list.
This field defaults based on the following:

- If you entered a valid material flagged as 'Taxable'
 in HQ Materials, defaults the tax code specified for the job in JC Jobs. If the
 material is not taxable, defaults as null. May be overridden.

- If you entered a non-valid material, it is assumed
 to be taxable and defaults the tax code specified for the job in JC Jobs.

This field is only enabled when the Use Tax on
 Material box on the Materials tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) is checked.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Tax Basis

 If a tax code is selected in the Tax Code field,
 this field defaults an amount based on the following formula:

Units
X
Unit Price
/
ECM

This field is only enabled when the Use Tax on
 Material box on the Materials tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) is checked.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Tax Amount

 Taxes are calculated automatically, and
 default an amount based on the tax code selected in the Tax Code field
 and the Tax
 Basis amount, but this amount can be overridden.
This field is only enabled if the Use Tax on
 Material box on the Material tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) is checked.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use

## Total Cost

This field displays the total transaction amount.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form)JC Material Use
