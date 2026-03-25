---
title: "Field Definitions: PO Purchase Order Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-copy-form/field-definitions-po-purchase-order-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-copy-form/field-definitions-po-purchase-order-copy-form"
---

# Field Definitions: PO Purchase Order Copy Form

The following is a list of field descriptions for the PO
 Purchase Order Copy form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Source: Purchase Order

Enter the purchase order to copy or press F4 to select it from a list.
The selected PO cannot be in an open batch but it can have a "closed" status.
Note: You can create new purchase orders using [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form).

## Destination: Purchase Order

Enter the destination PO number. Must be a 'new' PO or an existing PO in the current batch. If entering a new purchase order, and you are using the 'auto generate' feature (flag in PO Company Parameters), enter NEW or '+' to have the system assign the next sequential PO number (based on the "Last Used PO#" specified in PO Company Parameters).

## Vendor

 Enter the vendor (from AP Vendors) that is supplying the merchandise on this purchase
 order. If copying to a new purchase order, defaults the vendor assigned to the 'source'
 purchase order. If copying to a purchase order existing in the current batch, defaults the
 vendor from the 'destination' purchase order (and field is disabled).

## Description

 Enter a description of the destination purchase order, up to 30 characters. If copying to a new purchase order, defaults the description from the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults the description from the 'destination' purchase order (and field is disabled).

## Order Date

 Enter the date that this order was placed. If copying to a new purchase order, defaults the current date. If copying to a purchase order existing in the current batch, defaults the order date from the 'destination' purchase order (and field is disabled).

## Ordered By

 Enter the name (or initials) of the person who placed this order. If copying to a new purchase order, defaults from the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults from the 'destination' purchase order (and field is disabled).

## Expected Date

 Enter the expected arrival date for this purchase order. If copying to a new purchase order, defaults the current date. If copying to a purchase order existing in the current batch, defaults the expected date from the 'destination' purchase order (and field is disabled).

## SM Co #

SM Co # field on the PO Purchase Order Copy form.
Enter the SM Company, or press F4 for the SM Company Lookup from which to select a company.

## Work Order

Work Order field on the PO Purchase Order Copy form.
Enter the work order, or press F4 for the SM Work Order Lookup from which to select a work order.

## JC Co#

 Specify the Job Cost company to which this PO should be posted. If copying to a new purchase order, defaults the JC company assigned to the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults the JC company from the 'destination' purchase order (and field is disabled).

## Job

 Specify the job to which this purchase order applies. If copying to a new purchase order, defaults the job from the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults the job from the 'destination' purchase order (and field is disabled).

## Ship Location

 Specify the ship location (set up in PO Shipping Locations) for this purchase order. If copying to a new purchase order, defaults the ship location from the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults the ship location from the 'destination' purchase order (and field is disabled).

## IN Co#

Specify the Inventory company to which this PO should be posted. If copying to a new purchase order, defaults the IN company from the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults the IN company from the 'destination' purchase order (and field is disabled).

## Location

 Specify the inventory location from which the material for this item will be purchased. Specified material must be valid for this IN location.If copying to a new purchase order, defaults the IN location from the 'source' purchase order. If copying to a purchase order existing in the current batch, defaults the IN location from the 'destination' purchase order (and field is disabled).

## Clear Header Notes

 Check this box to exclude header notes during copy process. When checked, if header notes exist for the 'source' purchase order, they will be skipped during the copy process.
 Do not check this box if you want the header notes for the 'source' purchase order copied to the destination purchase order.

## Clear User Memos

 Enabled only when user memo fields exist in the purchase order header.
 Check this box to exclude header memos during the copy process. When checked, memos existing in the header of the 'source' purchase order will be skipped during the copy process.
 Do not check this box if you want to copy the header user memos from the 'source' purchase order.

## Copy Work Order Types

Check this box to copy work order type items to the destination purchase order. Work Order type items with the "Incl" option checked will be copied to the new purchase order. Those with the "Incl" option unchecked will be skipped.
This field is only enabled when Work Order type items exist on the 'source' purchase order.
 Do not check this box if you do not want to copy work order type items to the destination purchase order.

## Override

Work Orders
Enabled only if the 'Copy Work Order Types'
 checkbox is selected.
Select this checkbox to override the work
 order information for the destination purchase order. When selected, the EM Co# and Work
 Order inputs are enabled, allowing you to change the default work order information for the
 destination purchase order.
If not selected, work order information is
 copied from the 'source' purchase order.

Equipment
Enabled only if the 'Copy Equipment Types'
 checkbox is selected.
Select this checkbox to override the
 equipment information for the destination purchase order. When selected, the EM Co# and
 Equipment inputs are enabled, allowing you to change the default equipment information for
 the destination purchase order.
If not selected, equipment information is
 copied from the 'source' purchase order.

## EM Co#

Work Orders
Enabled only if the work orders 'Override'
 checkbox is selected.
There are any Work Orders associated with this
 PO, specify the EM company for the Work Order(s).

Equipment
Enabled only if the equipment 'Override' check
 box is selected.
If there is any equipment associated with this
 PO, specify the EM company of that equipment.

## Work Order

 Enabled only if the 'Override' option is Y (checked)
 Enter the work order that applies to the destination purchase order. If you are copying multiple work order items, all items will be assigned this work order, regardless of whether they were originally assigned to different work orders.

## Copy Equipment Types

 Enabled only if Equipment type items exist on the 'source' purchase order.
 Check this box to copy equipment type items to the destination purchase order. Equipment type items with the "Incl" option checked will be copied to the new purchase order. Those with the "Incl" option unchecked will be skipped.
 Do not check this box if you do not want to copy equipment type items to the destination purchase order.

## Equipment

 Enabled only if the 'Override' option is Y (checked)
 Enter the equipment that applies to the destination purchase order. If you are copying multiple equipment items, all items will be assigned this equipment, regardless of whether they were originally assigned to different equipment.

## Keep Pricing

 Check this box to copy the pricing from the 'source' purchase order.
 Do not check this box if you do not want to copy pricing from the 'source' purchase order. When unchecked, pricing will default from the appropriate sources.

## Set Quantities to One

 Check this box to set the quantities for all items on the destination purchase order to '1'.
 Do not check this box if you want to copy the quantities from the 'source' purchase order items.

## Clear Item Notes

 Check this box to exclude item notes during the copy process. If notes exist for purchase order items, they will be skipped during the copy process.
 Do not check this box if you want all item notes for the 'source' purchase order to be copied to the destination purchase order.

## Clear Item User Memos

 Enabled only when user memo fields exist in the purchase order items section.
 Check this box to exclude item memos during the copy process. When checked, memos existing for items on the 'source' purchase order will be skipped during the copy process.
 Do not check this box if you want to copy the item user memos from the 'source' purchase order.

## Include

 Check this box for each purchase order item you want copied to the destination work order. (Default is Y.) If you have specified to copy work order and/or equipment items, make sure to check this box for only those work order and/or equipment items you want copied.
 Do not check this box if you do not want this purchase order item copied to the destination work order. If you have specified to copy work order and/or equipment items, make sure to uncheck this box for all work order and/or equipment items you do not want copied.
