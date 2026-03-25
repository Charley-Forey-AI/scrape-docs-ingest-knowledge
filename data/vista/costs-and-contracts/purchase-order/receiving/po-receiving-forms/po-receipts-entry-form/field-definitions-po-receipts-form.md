---
title: "Field Definitions: PO Receipts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form/field-definitions-po-receipts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form/field-definitions-po-receipts-form"
---

# Field Definitions: PO Receipts Form

The following is a list of field descriptions for the PO
 Receipts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

If this is a new batch, this field automatically defaults to New. The system assigns sequence numbers, so you must accept the default.
If this is an existing batch, enter the sequence number to work on, or enter New to add a new sequence to the batch.

## Action

Select the type of transaction that you are
 creating from the drop down.

- Add - if you are creating a new
 receipt.

- Change - if you are changing an
 existing receipt.

- Delete - to delete the selected
 receipt.

## PO

Enter the purchase order for the ordered goods or press F4 to select it from a list. The purchase order must have an open status.

## Item

Enter the purchase order item being received
 or press F4 to select it from a list.
You can only select items that are set up to
 be received.
Note: PO items are set up to be received when the Receiving
 checkbox on the [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form) form is selected.

## Line

PO item lines are part of the [PO Item Distribution](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview) feature. If you do not use this
 feature or there is only one PO item line on the PO, this field will populate with line
 "1". Accept the default and skip the field.
Select a PO Item Line
Enter the PO item line that you would like to receive or press F4 to select it from a list. A warning will display if the PO line item is already selected in another PO Receipts Entry batch.
If you need to create a new PO item line,
 select Tasks > Open PO Item
 Distribution to open the PO Item Distribution form, which is used to create and
 maintain PO item lines. You can also get to this form by pressing F5 in the Line field.
Tip:If you do not use the PO Item Distribution feature you can opt to remove the field from view using the Form Properties form. Click [here](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) for more information.

## Date

Enter the receiving date of this item.

## Recvd By

Enter the name (or initials) of the person receiving these goods.

## Description

Initially defaults the material’s description. Accept the default, or enter a description, up to 30 characters. This might be used to enter a ticket or receiver number.

## Receiver #

The Receiver # field on the PO Receipts Entry form.
Enter the receiver number (e.g. packing list number), up to 20 characters.
The receiver number entered here will display on the AP invoice form (AP Transaction Entry or AP Unapproved Invoice Entry) form for purchase order lines only if the following is true:

- You initialized the purchase order to an AP invoice (in AP Transaction Entry or AP Unapproved Invoice Entry) using the AP Purchase Order Initialize form, which is accessed from either form by selecting File > Initialize from PO.

- When initializing the PO, you used the Receiver # initialization option (that is, you entered the Receiver # on the Receiver # tab in AP Purchase Order Initialize).

## Changes to Received: Units

Enter
 the units being received, which will automatically adjust the remaining backordered units.
This field initially populates with the current backordered units.
Note: If this receipt is for a standing PO (i.e. the PO's total cost is 0.00), backordered units will always be 0.00; therefore, this field will always default to 0.00.
The fields in the lower portion of the form will update once you save the received item.
Note: The units posted to a job-related receipt will only be
 updated to JCCD (Cost Detail) if you have checked the Update Actual Units From AP option
 for the specified job in JC Jobs. If option is unchecked, units (and unit cost) will be set
 to 0.00 in JCCD.

## Changes to Received: Total Cost

For LS items only, defaults the current backordered amount. Accept the default, or enter the amount to be received this time.
Note: If this receipt is for a standing PO (i.e. the PO's total cost is 0.00), the backordered cost will always be 0.00; therefore, this field will always default to 0.00.
Once you accept (save) the received item, the resulting calculations display in the fields below.

## Changes to Backordered: Units

This field initially defaults to the change in backordered units, which is typically the opposite of the Changes to Received Units. In other words, if the current backordered units is 200.00, and you receive 200.00 units, then the change to backordered units is -200.00.
Although changes can be made to this amount, it is not recommended unless you are indicating that the ordered quantity has been changed.
Note: If this receipt is for a standing PO (i.e. the PO's total cost is 0.00), this field will always default to 0.00.
Once you save the received item, the resulting calculations display in the fields below.

## Changes to Backordered: Total Cost

For LS items only, initially defaults the change to backordered total cost, which is typically the opposite of the Changes to Received Total Cost. In other words, if the current backordered total cost is 200.00, and you receive 200.00 of the total cost, then the change to backordered total cost is -200.00.
Note: If this receipt is for a standing PO (i.e. the PO's total cost is 0.00), the backordered cost will always be 0.00.
Although changes can be made to this amount, it is not recommended that you do so unless you are indicating that the order has been changed.
Once you accept (save) the received item, the resulting calculations display in the fields below.
