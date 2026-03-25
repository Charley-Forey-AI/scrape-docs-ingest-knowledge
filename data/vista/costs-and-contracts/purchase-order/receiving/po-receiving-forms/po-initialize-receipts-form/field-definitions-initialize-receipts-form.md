---
title: "Field Definitions: Initialize Receipts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-initialize-receipts-form/field-definitions-initialize-receipts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-initialize-receipts-form/field-definitions-initialize-receipts-form"
---

# Field Definitions: Initialize Receipts Form

The following is a list of field descriptions for the PO
 Initialize Receipts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Receipt Date

Enter the receipt date of the POs in the batch. By default this field will populate with the current date.

## Received By

Use this field to identify the person receiving the purchase order.
By default this field will populate with your user login.

## PO #

Enter the purchase order being received or press F4 to select a PO from a list.
The purchase order number can be up to 30 characters long.

## Receiver #

The Receiver # field on the AP Purchase Order Initialize form.
Enter the receiver number, for example the packing list number. The value in this field can be up to 20 characters long.
The receiver number entered here will display on the AP invoice form (AP Transaction Entry or AP Unapproved Invoice Entry) form for purchase order lines only if the following is true:

- You initialize the purchase order to an AP invoice (in AP Transaction Entry or AP Unapproved Invoice Entry) using the AP Purchase Order Initialize form, which is accessed from either form by selecting File > Initialize from PO.

- When initializing the PO, you use the Receiver # initialization option (that is, you enter the Receiver # on the Receiver # tab in AP Purchase Order Initialize).

## Receive All

The selection in this checkbox determines how
 the fields in the lower portion of the form populate.

Select this checkbox if you want to automatically
 receive all of the units left on all of the PO items. This receives the
 full backordered amount for each item on the PO and sets the Backordered amount to 0.00.
For example, select this checkbox if you are receiving a PO with multiple items, and all remaining units on those PO items.

Leave this checkbox cleared if you want to manually select
 which PO items to receive. The Received This Time amount is set to 0.00
 and the Backordered amount is set to the current backordered amount.
For example, leave this box unchecked if you
 are receiving a PO with several items, but only a portion of the units on those PO items.

## Received This Time

If you checked the Receive All box,
 this field defaults the current backordered amount for each item, and the Backordered field
 is set to 0.00. If you did not elect to automatically receive all backorders, this field
 defaults 0.00; may be overridden.
Note: If this receipt is for a standing PO (i.e. the PO's total cost is 0.00), this field will always default to 0.00, regardless of how you set the
 Receive All
 checkbox.

## Backordered

This field displays the number of units left to be received on each PO item. Changing the value in this field is changing the units that you expect to receive on the PO item - for example if the order has changed, or you are recording a shortage and creating a new PO for the shortage amount.
Note: If this receipt is for a standing PO (i.e. all items on the purchase order have 0.00 units and/or unit cost), this field will always default to 0.00.

## Notes

Enter any miscellaneous notes about this
 item.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
