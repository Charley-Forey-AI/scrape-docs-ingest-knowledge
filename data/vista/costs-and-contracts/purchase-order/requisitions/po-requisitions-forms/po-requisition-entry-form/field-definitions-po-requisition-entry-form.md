---
title: "Field Definitions: PO Requisition Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form/field-definitions-po-requisition-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form/field-definitions-po-requisition-entry-form"
---

# Field Definitions: PO Requisition Entry Form

The following is a list of field descriptions for the PO
 Requisition form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## RQ ID

If you are adding a new requisition and are using the 'auto-generate' numbers feature, enter 'N', 'New' or '+' to have the system assign the next available requisition number (based on the Last Used RQ # in PO Company Parameters).
If you are not using the 'auto-generate' feature, enter a requisition number (or alphanumeric code) up to 10 characters.
Note: Requisition numbers may be assigned manually, regardless of whether you are using the auto-generate feature. However, if using both methods, be aware that manually assigned numbers do not update the Last Used RQ # field. If the 'auto-generate' process encounters an existing number, it will pull up the existing requisition. You will need to enter 'N', 'New', or '+' to start a new requisition with the next available number.
[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Date

 Enter the requisition date. If you
 initialized requisitions, defaults the date specified at time of initialization. Otherwise,
 defaults as null.

##  Requested By

The Requested By field on the PO Requisition Entry form, header Info tab.
 Enter the name or initials of the person who initiated the requisition. Up to 128 characters allowed.
If you initialized requisitions using the PO Requisition Initialization form, this field populates with the name or initials specified at time of initialization.
If you entered and initialized requisitions using the PM Material Detail form, this field populates with the user's login name (that is, the User Name specified in VA User Profile)

##  Description

 Enter a description of this requisition, up to 60 characters. If you initialized requisitions, defaults the description specified at time of initialization. Otherwise, this field defaults as blank.

##  Item

 Enter an item number (0-32,767), or enter 'N', 'New', or '+' for the next sequential item number.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Type

Select an item type from the drop down menu.

- Job – Use this type to requisition materials for jobs.

- Inventory – Use this type to requisition materials for inventory.

- Expense – Use this type to requisition materials that are not for a job, inventory, work order, or equipment (i.e. office supplies, office machines, etc.).

- Equipment – Use this type to requisition materials for use with equipment.

- Work Order – Use this type to requisition parts needed to complete work orders set up in the EM module.

Note: If you initialized requisitions based on 'low stock' or 'open work orders', the type will default as 2 (Inv) or 5 (Work Order).
[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  JC CO#

 For Job requisition lines only.
 Specify the Job Cost company in which job/phase/cost type information for this requisition line will be validated, and to which the material expense will be posted.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Job

For
 Job requisition lines only.
Specify the job (from JC Jobs) to which the
 material on this requisition line will be charged.
Note: If you enter a soft- or hard-closed job, the status displays in red to the right of the item description. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Phase

 For
 Job requisition lines only.
 Specify the phase (from JC Jobs or JC Job
 Phases) to which this material is being charged. Initially defaults the material phase from
 HQ Materials (if specified for the material).

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  CT

 For Job requisition lines only.
 Specify the cost type (from JC Cost Types) to which the material is being charged. Must be a valid cost type for this phase or job phase. Initially defaults the material cost type from HQ Materials (if specified for the material).

## Ticket

The Ticket field on the PO Requisition Entry form, items Info tab.

This field displays for Job lines only.
Enter the field ticket number that applies to this requisition item or press F4 to select from a list of valid field tickets for the specified job/contract.
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to requisition items for a job is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

##  IN Co#

 For Inventory requisition lines only.
 Specify the Inventory company for which you are purchasing the specified material.
 If you initialized requisitions based on 'low stock', will default the IN company based on initialization criteria.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Location

 For Inventory requisition lines only.
 Specify the location (from IN Locations) for
 which you are purchasing the specified material.
 If you initialized requisitions based on 'low stock', will default the IN location based on initialization criteria.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  EM Co #

 For Equipment or Work Order requisition lines only.
 Specify the EM company for which you are purchasing the specified material.
 If you initialized requisitions based on 'open work orders', will default the EM company based on initialization criteria.
[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Equipment

For Equipment requisition lines only.
Specify the equipment (from EM Equipment) for
 which you are purchasing the specified material.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Comp Type

For Equipment requisition lines only.
Specify the component type (from EM Component Types) for the equipment, if applicable.

##  Component

 For Equipment requisition lines only.
 Specify the component for which you are purchasing the specified material. If you entered a component type in the previous field, this field will default the first component of this type for the indicated equipment (as defined in EM Equipment). May be overridden, but must be a valid component for this equipment.

##  Work Order

 For Work Order requisition lines only.
 Specify the work order for which you are purchasing the specified material. Must be an existing work order set up in EM Work Order Edit.
 If you initialized requisitions based on 'open work orders', will default the work order based on initialization criteria.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  WO Item

 For Work Order requisition lines only.
 Specify the work order item for which you are purchasing the specified material. Must be a valid item for the specified work order.
 If you initialized requisitions based on 'open work orders', will default the work order item based on initialization criteria.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Cost Code

 For Equipment and Work Order requisition lines only.
 Specify the cost code to which this requisition line applies.
 For Equipment lines, if you specified a component type and component, defaults the cost code assigned to the component type (in EM Component Types).
For Work Order lines, defaults the cost code assigned to the work order item.

##  CT

 For Equipment and Work Order requisition lines only.
 Specify the EM cost type to which this material will be charged. Must be a valid cost type for the specified cost code.

##  Material

 Specify the material for this requisition line.
 If this is a Job, Expense, Equipment, or Work Order line, you can enter any material, valid or non-valid. If material is valid, the description, unit of measure, and unit cost will default from HQ Materials.
 If this is an Inventory line, you must enter a valid, stocked material (from HQ Materials), and the material must be set up and flagged as 'Active' for the specified location in IN Materials.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Vendor

 Enter the vendor (from AP Vendors) from which you are purchasing the material on this
 requisition line.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Vendor Matl #

Enter the vendor’s identification number for this material, if applicable. Press F4 for a list of vendor material numbers.
Note: When using the F4 lookup, sort by the HQMT Material column. This enables the standard and substitute vendor materials to be grouped together for selection.
If you have set up vendor overrides for the specified HQ material (PO Vendor Materials), this field will automatically default the vendor material ID# assigned in PO Vendor Materials, if one was specified. If one was not specified, and you enter one here, it is not updated to the PO Vendor Materials file; you will need to enter it manually.
Because the vendor’s material ID# is used as a cross-reference to the HQ material, you can enter this number if you do not know the HQ material number, and the HQ material number will be provided. This feature is only applicable to materials set up in PO Vendor Materials.
You can also enter the vendor material ID# for any substitute materials that may have been set up for the HQ material in PO Vendor Materials, and have the HQ material number provided.
Note: Vendor material numbers are not validated.
[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  GL Co #

 For Expense requisition lines only.
 Specify the GL company to which this line applies. Initially defaults the GL company specified in AP Company Parameters for this requisition company's AP company.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  GL Account

 For Expense requisition lines only.
 Specify the GL account (from GL Chart of Accounts) to which this requisition line will be posted. May be left blank; however, once this requisition line is initialized to a PO, the GL account will need to be entered before the PO batch can be posted.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Description

 Enter a description for this requisition line, up to 30 characters. Initially defaults the material description.

##  Required Date

 Enter the date this material is required. If you initialized requisition lines, defaults the required date specified at time of initialization.

##  Ship Location

 Enter the shipping location (from PO Shipping Locations) for this requisition line. The ship location is used to default a “Ship To” address for the material.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Route

The Route dropdown on the PO Requisition Entry form, Item Info tab.
Use this field to select what process the requisition will go through to acquire the materials.

- Quote – You need price quotes from vendors for the materials being requisitioned. Materials are set up on a quote, sent out to the vendors for pricing, then added to a purchase order once an acceptable quote is received.

-  Purchase – You will be bypassing the quote process and adding materials directly to a purchase order.

-  Stock – The requisition materials will be pulled from stock. Requisitions that were originally flagged for quote or purchase may be flagged with this status once the purchasing manager determines the item can be pulled from stock. Requisition lines assigned this route type do not require any further processing.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  UM

 Enter the unit of measure for the specified material. Initially defaults the purchase unit of measure assigned to the material in HQ Materials. If you have set up a vendor override for this material (PO Vendor Materials), this field defaults the unit of measure specified in PO Vendor Materials.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Units

 Required (if not LS).
 Enter the number of units needed of the specified material. Cannot be 0.00.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  UC

 Enter the unit cost for the specified material or enter 0.00 if the unit cost is not yet known. Initially defaults the unit cost for this material as specified in HQ Materials.
 If you specified a vendor and have set up vendor pricing overrides in either PO Category Discounts and/or PO Vendor Materials, the unit cost will default from these overrides accordingly. If a discount exists for the vendor and material category (in PO Category Discounts), it will apply the discount to the standard unit price in HQMT to determine the default cost. If an override exists for the material and vendor in PO Vendor Materials, it will default a unit cost based on the cost option (std unit cost, vendor unit cost, std book price less discount, or vendor book price less discount) or the job override (if one exists).

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## ECM

Specify which quantity the unit cost represents, or accept the default.

- E – Cost is per each unit.

- C – Cost is per 100 units.

- M – Cost is per 1000 units

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Total Cost

 If the unit of measure is LS (lump sum), specify the total cost for this material (or enter 0.00 if not known).
 If unit of measure is not lump sum, defaults an amount based on the units x unit cost / ECM. If overridden, the unit cost will be recalculated.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Address

Enter the shipping address for this requisition item.Initially defaults a
 shipping address based on line type as follows:

- Job – Defaults shipping address from JC Jobs.

- Inventory – Defaults shipping address from IN
 Locations.

- Expense – Defaults shipping address from previous line.

- Equipment – Defaults shipping address from previous line.

- Work Order – Defaults shipping address from the IN location specified in the work order header.

For all line types, if a Ship Location is specified, it overrides all other defaults. Shipping address will be pulled from PO Shipping Locations.

##  Attention

Enter the name of the person who you are shipping this material to. Up to 30 characters allowed.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## City

Specify the city to which this material is to be shipped (or accept the default).

## State

Specify the city to which this material is to be shipped (or accept the default).

## Zip Code

Specify the zip code, up to 10 characters (or accept the default).

## Country

Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

## Add'l Address

Enter the additional address information for this shipping location, up to 60 characters (e.g. Bldg 1, Suite 250).

##  Shipping Instructions

 Specify the shipping instructions for this requisition line, up to 30 characters.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

## Reviewer

Specify the reviewer (from HQ Reviewers) for
 this requisition line. If you require approval for quote or purchase, and have specified a
 quote and/or purchase reviewer in PO Company Parameters, the quote and/or purchase reviewers
 will default here.
Press F4 in the Reviewer field for
 a list of active reviewers.
Press F5 in the Reviewer field to
 access HQ Reviewers.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)

##  Reviewer Status

 This field is display only and shows the reviewer’s status for the line.

## Notes

Use this tab to enter any miscellaneous notes
 about this item. The space allowance is virtually unlimited; however, there is a maximum
 allowance of 8k.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
[About Creating and Routing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions)
