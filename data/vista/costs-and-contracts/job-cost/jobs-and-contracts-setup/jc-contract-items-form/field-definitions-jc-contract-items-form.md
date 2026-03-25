---
title: "Field Definitions: JC Contract Items Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form/field-definitions-jc-contract-items-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form/field-definitions-jc-contract-items-form"
---

# Field Definitions: JC Contract Items Form

The following is a list of field descriptions for the JC
 Contract Items form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract Item

Enter a number for this contract item, up to 16 characters. Items do not
 have to be sequentially numbered.
Note: Once added, items can be deleted only if they are not assigned to a job’s phase and no revenue detail exists for the item.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Standard Item Code

Enter a standard item code for the region set up on the contract or press
 F4
 to select one from a list.
Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) for more information standard item codes.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Description

Enter the description of the contract item.
This field defaults based on the following:

- If a standard item code was entered, this field will default with the item code description. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) for more information on item codes.

- If you are not using standard regions/item codes, default will be based on the item description.

- If contract was set up automatically (via JC Jobs),
 the first contract item will default the job description. All other items will
 default as described above.

- If imported from PM, default will be description assigned to item in PM.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Department

Enter the department for the contract item or press F4 to select
 one from a list.
This field defaults based on the department
 entered on the contract ([JC
 Contracts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)> Info tab> [Department](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form/field-definitions-jc-contracts-form#ID-000173cd--en) field).
Departments are created and maintained using
 the [JC Departments ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form) form, and they define which GL accounts
 will be used when posting contract revenue and job costs.
Important: If you change this department after contract revenue or job costs have been posted, the system WILL NOT transfer previously posted amounts into the GL accounts of the new department. You must manually make the necessary GL adjustments.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Tax Code

Enter the tax code that will be used as a default when posting Accounts
 Receivable (AR) and Job Billing (JB) transactions to this contract item.
This field defaults based on the tax code on
 the contract, which is set up using the Tax Code field on the Info tab of [JC Contracts ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Unit of Measure

Enter the unit of measure of the contract item or press F4 to select
 one from a list. Enter LS  for lump sum.
 Other types of units can be posted to job phases associated with this item, but only units for this unit of measure will be sent to Job Billing.
Units of measure are created and maintained using the [ HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form) form.
Standard Item Code
If you selected an item code in the Standard Item
 Code field, this field will populate with the unit of measure on the item
 code. [More](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form)

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Units

 Enter the original units for the contract item.
This field is only enabled when the unit of
 measure selected in the Unit of Measure field is not lump sum
 (LS).
Do not enter any amounts related to change orders here. Changes should be made using the change order forms in Job Cost or Project Management.

- Click [here](/en/vista/vista/project-management/change-orders/change-management---overview) for an overview on change orders in the PM module.

- Click [here](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form) for information on change orders in the JC
 module.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Unit Price

Enter the unit price of the contract item. This field is disabled if
 LS
 is selected in the Unit of Measure field.
Metric Conversions
If using metric units of measure, this field will default based on the conversion factor set up for the metric unit of measure in JC Metric Conversions. If you did not specify a conversion factor, the unit price defaults to 0.00.
Standard Item Codes
If you selected an item code in the Standard Item
 Code field, this field will populate with the unit price on the item code.
 [More](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form)

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Amount

Specify the original dollar value for this contract item. If units and unit
 price have been entered, the amount will default based on the units x unit price. The
 amount may be overridden; however, the unit price will not be recalculated. A warning will
 display indicating that units/unit price may be incorrect, but the amount will be accepted.
 This allows for rounding the contract amount, while leaving the agreed upon unit price
 intact.
Note: Amounts entered here will update the Contract’s total dollars, as shown in the display-only Total Original Contract field in the upper right-hand corner of screen.
Do not enter any amounts related to change orders here. Changes should be made using the Change Order programs in Job Cost or Project Management.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Start Month

Required.
Specify the start month for this contract item. Initially defaults from the contract start month (header). This month will be used to store original contract amounts and cost estimates for this contract item.
Note: If you change the start month for this contract item, the item's original contract amount and cost estimates will be moved to the new month. 
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Retainage %

Enter the retainage percent for this contract item. When creating a new
 contract item, this field defaults with the retainage percent set up on the contract
 (Default
 Retainage Percentage field in the JC Contracts form).
When you create new subcontract items in the
 PM and SL modules, this value will be used as the default retainage percentage.
The diagram below outlines how the system will select the default retainage percentage for subcontract items when they are created in the PM and SL module.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Markup

Enter the markup rate for this contract item. Enter 5% as .05, 25% as .25,
 100% as 1.00.
This rate will be used during T&M billing when the Markup Opt for a template sequence is 'Rate' and no markup rate is specified for the template sequence. Each item on the billing will use its own markup rate when calculating the billing amount. For total addons, if a contract item is assigned to the template sequence, that contract item's markup rate will be used. If no markup rate is specified for that contract item, the markup rate for each individual item on the billing is used.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Initialize Subcontractors

For use with subcontract worksheets.
Check this box to have the percent complete for subcontractors (linked to this item) to be the same as the percent complete for this item.
Note: You will typically only check this box if there is a one-to-one relationship between subcontractor and contract item (e.g. an electrical contract item with one electrical subcontractor), but not if there were many subcontractors on a single contract item such as General Conditions or Mobilization.
Leave this box unchecked if you do not want the percent complete for subcontractors (linked to this item) to be the same as the percent complete for this item.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Bill Group

Enter the bill group for this contract item. Bill groups are used to group
 sets of contract items together on invoices. Used by Job Billing.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Bill Description

Initially defaults the contract item’s description. May be overridden, up
 to 60 characters. Description entered here will be the description displayed on JB
 invoices.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Bill Type

Indicate the bill type for this contract item. Initially, this defaults to
 the bill type specified for the contract (header).

- Progress - Select this option to have costs for this item billed on a percent complete or units complete basis.

- T & M - Select this option to have costs for this item billed on a Time and Materials basis.

- Both - Select this option to have costs for this item billed on a Time & Materials and/or Progress basis. You might typically use this option for items you bill on a T&M  basis with a Progress backup.

- None - Select this option if you are not billing costs through Job Billing.

Note: If you change the bill type after an item has been billed, a message displays informing you that the item has been previously billed and that the change may result in differences on the Previous Billed amounts in JB. However, record will be saved.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items

## Initialize As $0.00

This option determines how This Bill WC Units/This Bill WC Amount values
 are initialized for contract item's in JB Bill Initialization (using options P, B, or X
 only). When checked, initialization sets the contract item's This Bill WC Units/This Bill
 WC Amount values to 0.00 in JB Progress Billings (Items tab). You can edit item amounts as
 necessary in JB Bill Edit (Items tab).
You might typically check this box for:

-  contract items that have been over billed (e.g. mobilization, equipment movement, etc.).

- fully billed negative contract items

- contract items for which you are billing negative change orders

Note: Percent complete calculations do not handle negative amounts, so checking this box will prevent generating positive billings for negative amounts during the bill initialization process.
Tip: If you do not want bill amounts initialized for any
 contract items, you can set an F3 on the Initialize As $0.00 field to default to
 checked when you add a new contract item.
 If the Initialize As $0.00 box is unchecked, the
 system will initialize the contract item's This Bill WC Units as a calculation of the To
 Date Units minus Previous Units. For LS item's, This Bill WC Amount will be initialized as
 calculation of To Date Amount minus Previous Amount.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contracts-form)JC Contracts
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-items-form)JC Contract Items
