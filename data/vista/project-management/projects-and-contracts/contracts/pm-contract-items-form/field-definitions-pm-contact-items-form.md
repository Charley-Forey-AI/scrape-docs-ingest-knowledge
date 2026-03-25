---
title: "Field Definitions: PM Contact Items Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contract-items-form/field-definitions-pm-contact-items-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contract-items-form/field-definitions-pm-contact-items-form"
---

# Field Definitions: PM Contact Items Form

The following is a list of field descriptions for the PM
 Contact Items form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract Item

Enter a number for this contract item, up to 16 characters. Items do not have to be sequentially numbered.
Note:Once added, items can be deleted only if they are not assigned to a project’s phase and no revenue detail exists for the item.

## Standard Item Code

Enter a standard item code for the region set
 up on the contract or press F4 to select one from a list.
Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) for more information standard item codes.

## Description

Enter a description of the contract item.
This field defaults based on the following:

- If a standard item code was entered, this field will default with the item code description. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) for more information on item codes.

- If you are not using standard regions/item codes, default will be based on the item number. For example, if you enter '001' as the item number, the description will be 'Item 001'.

- If contract was set up automatically (via PM Projects), the first contract item will default the job description. All other items will default as described above.

- If imported (via PM Imports), default will be description assigned to item in PM Import Edit.

## Department

Enter a department for the contract item or press F4 to select
 one from a list. The department determines which GL accounts are updated when revenue and
 costs are posted.
This field defaults based on the department
 set up on the contract (PM Contracts > Info tab > Department field).
Departments are created and maintained using
 the [JC Departments ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-departments-form) form.
Important:If you change the department selected in this field after contract revenue or project costs have been posted, the system WILL NOT transfer previously posted amounts into the GL accounts of the new department. You must manually make the necessary GL adjustments.

##  Tax Code

 Enter the tax code that will be used as a default when posting Accounts Receivable (AR) and Job Billing (JB) transactions to this contract item. The description for this tax code displays below the tax code.

## Unit of Measure

Enter the unit of measure of the contract item
 or press F4 to select one from a list. Enter LS for lump sum.
 Other types of units can be posted to job phases associated with this item, but only units for this unit of measure will be sent to Job Billing.
Units of measure are created and maintained using the [ HQ Units of Measure ](/en/vista/vista/administration/headquarters/company-setup/hq-units-of-measure-form) form.
Standard Item Code
If you selected an item code in the Standard Item
 Code field, this field will populate with the unit of measure on the item
 code. [More](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form)

## Units

Enabled only if the unit of measure is other than LS (Lump Sum).
Indicate this contract item’s original units. If adding a contract item on the fly (via PM Pending Change Orders, PM Approved Change Orders, or PM Change Order Approval), this field is disabled and set to 0.00.
Do not enter changes to an item’s units here. Changes should be made using the Change Orders programs in Project Cost or Project Management.

## Unit Price

Enter the unit price of the contract item.
 This field is disabled if LS if selected in the Unit of Measure
 field.
If adding a contract item on the fly using PM Pending Change Orders, PM Approved Change Orders, or PM Approve PCOs, this field is disabled and set to 0.00.
Metric Conversions
If using metric units of measure, this field will default based on the conversion factor set up for the metric unit of measure in JC Metric Conversions. If you did not specify a conversion factor, the unit price defaults to 0.00.
Standard Item Codes
If you selected an item code in the Standard Item
 Code field, this field will populate with the unit price on the item code.
 [More](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form)

## Amount

Specify the original dollar value for this contract item. If units and unit price have been entered, the amount will default based on the units x unit price. The amount may be overridden; however, the unit price will not be recalculated. A warning will display indicating that units/unit price may be incorrect, but the amount will be accepted. This allows for rounding the contract amount, while leaving the agreed upon unit price intact.
If adding a contract item on the fly using PM Pending Change Orders, PM Approved Change Orders, or PM Approve PCOs, this field is disabled and set to 0.00.
Amounts entered here will update the Contract’s total dollars, as shown in the display-only Total Original Contract field in the upper right-hand corner of screen.
Note:Do not enter any amounts related to change orders here. Changes should be made using the Change Order programs in Job Cost or Project Management.

## Start Month

Enter the start month of the contract item. This month will be used to store original contract amounts and cost estimates for this contract item.
This field defaults based on the start date on
 the contract (PM Contracts > Info tab > Contract Start
 Month field).
Note: If you change the start month for this contract item,
 the item's original contract amount and cost estimates will be moved to the new
 month.

## Retainage %

Enter the retainage percent of the contract item.
This field defaults based on the retainage
 percent entered on the contract (PM Contracts > Info tab > Default
 Retainage % field).

##  Markup

 Enter the markup rate for this contract item. Enter 5% as .05, 25% as .25, 100% as 1.00.
 This rate will be used during T&M billing when the Markup Opt for a template sequence is 'Rate' and no markup rate is specified for the template sequence. Each item on the billing will use its own Markup rate when calculating the billing amount. For total add-ons, if a contract item is assigned to the template sequence, that contract item's markup rate will be used. If no markup rate is specified for that contract item, the markup rate for each individual item on the billing is used.

##  Initialize Subcontractors

 For use with subcontract worksheets.
 Check this box to have the percent complete for subcontractors (linked to this item) to be the same as the percent complete for this item. (Note: You will typically only check this box if there is a one-to-one relationship between subcontractor and contract item (e.g. an electrical contract item with one electrical subcontractor), but not if there were many subcontractors on a single contract item such as General Conditions or Mobilization.)
 Leave this box unchecked if you do not want the percent complete for subcontractors (linked to this item) to be the same as the percent complete for this item.

## Bill Group

Enter the bill group for this contract item or press F4 to select one from a list. Bill groups are used to group sets of contract items together on invoices.
Bill groups are created and maintained using the [ JB Bill Groups ](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-bill-groups-form) form.

## Bill Description

Enter the description that should display on JB invoices.
This field defaults with the description of the item.

## Bill Type

Indicate the bill type for this contract item. Initially, this defaults to the bill type specified in the contract header.

- Progress - Select this option to have costs for this item billed on a percent complete or units complete basis.

- T & M - Select this option to have costs for this item billed on a Time and Materials basis.

- Both - Select this option to have costs for this item billed on a Time & Materials basis with a Progress backup. Contract items with a bill type of both can only be initialized to T&M billings; however, once the T&M billing is generated, the system produces a progress billing with the same dollars.

- None - Select this option if you are not billing costs through Job Billing.

Note:If you change the bill type after an item has been billed, a message displays informing you that the item has been previously billed and that the change may result in differences on the Previous Billed amounts in JB. However, record will be saved.

## Initialize As $0.00

Check this box to set 'this bill' units/dollars to 0.00 when initializing progress billings (using options P, B, or X in JB Bill Initialization) for this contract item. You might typically use this feature for contract items that have been over billed (e.g. mobilization, equipment movement, etc.).
Leave this box unchecked to initialize 'this bill' units/dollars for this contract item based on the item's To Date Units/Amount minus Previous Units/Amount.
