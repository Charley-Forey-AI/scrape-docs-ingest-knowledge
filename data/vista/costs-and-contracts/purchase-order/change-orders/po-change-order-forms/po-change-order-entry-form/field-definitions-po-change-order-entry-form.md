---
title: "Field Definitions: PO Change Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form/field-definitions-po-change-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form/field-definitions-po-change-order-entry-form"
---

# Field Definitions: PO Change Order Entry Form

## PO Trans#

Enter the purchase order transaction that you want to add to the current batch or press F4 to select it from a list of PO Change Detail transactions.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Sequence #

If this is a new batch, this field automatically defaults to New. The system assigns sequence numbers, so you must accept the default.
If this is an existing batch, enter the sequence number to work on, or enter New to add a new sequence to the batch.
To pull an existing change order transaction into the batch, select the Add Transaction option from the File menu. This brings up the Add PO Transactions to Batch form.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## PO #

Enter the purchase order that applies to the change order or press F4 to select it from a list. The PO must be open.
 This field is disabled when you are editing or deleting a previously posted change order.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## PO Change Order #

Enter an existing POCO number or press F4 to
 select a POCO from a list.
When creating a new PO Change Order, by
 default the system assigns the next available POCO number based on the POCO numbers already
 associated with the purchase order.

## Item#

You can use this field to either change an
 existing item or create a new line item on the PO.
This field is disabled when you are editing or
 deleting a previously posted change order.
If you want to select an existing item, enter
 an existing PO item number or press F4 to select an item from a list.
If you want to create a new item, enter a new PO item number. See [Change an Existing PO Item](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/change-an-existing-po-item) for more information on adding an item to the selected
 PO.

[PO Change Order Entry](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form#ID-0002f57c--en__ID-0002f57c)

## Change Order

Enter a change order number. The value in this field can be up to 10 characters long. This field is not required.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Date

Enter the date of change order. This field defaults to the current date when creating a new change order.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Description

Enter a description of the change order. The description can be up to 60 characters long.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Change to Current: Units

Enter the number of units by which this change order affects the units ordered. This is the amount of the change, not the new total. For example if the original amount was 1500 and the new total is 1750, enter "250" in this field.
If subtracting from the original units for the PO item, enter as a negative amount. For example, -150.000.
Note: You cannot change the units (or unit cost) on this change order if the unit cost has been changed on a subsequent change order for the same PO/PO item.
Note: When making a change to this field, the system updates information in PM Material Detail.
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Change to Current: Unit Cost

Only enter a value in this field if the unit cost of the PO item needs to be changed.
Any entry in this field will change the unit cost of the entire PO item, not just the units entered in the previous field. Any amount entered in this field will add to or subtract from the previous unit cost to calculate a new unit cost for the total quantity purchase of this item. For example if the original unit cost was $100.00 but it needs to be changed to $99.00, enter a -$1.00. If you enter $99.00 in this field, the unit cost will change to $199.00.
Most change orders will have a change of units only and no change to the unit cost. This field does not represent the unit cost of the changed units. It is a change to the current unit cost.
Once you save the change, the resulting calculations display in the fields below.
Note: You cannot change the unit cost (or units) on this change order if the unit cost has been changed on a subsequent change order for the same PO/PO item.
Note: When making a change to this field, the system updates information in PM Material Detail.
[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Change to Current: ECM

Indicate which quantity the unit cost represents:

- E – Per each

- C – Per Hundred

- M – Per Thousand

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Change to Current: Total Cost

Use this field to change to the lump sum
 amount on an existing PO item - for example if the PO item lump sum amount was $500 and is
 now $750, enter "250" in this field.
This field is only enabled when changing a
 lump sum PO item (the unit of measure on the PO item is lump sum).
See [PO Change Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form) for more information on changing the lump sum amount
 on an existing PO item.
If you are creating a new PO item, enter the
 lump sum amount of the new PO item.

## Change to Backordered: Units

Generally you do not change the value in this field.
 Click [here](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form) for more information on changing the backordered units.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry

## Change to Backordered: Total Cost

Generally you do not change the amount in this field.
Click [here](/en/vista/vista/costs-and-contracts/purchase-order/change-orders/po-change-order-forms/po-change-order-entry-form) for more information on changing the backordered total cost.

[](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form)PO Change Order Entry
