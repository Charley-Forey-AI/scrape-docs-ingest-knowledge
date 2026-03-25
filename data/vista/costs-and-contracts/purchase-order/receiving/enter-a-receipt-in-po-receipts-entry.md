---
title: "Enter a Receipt in PO Receipts Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/enter-a-receipt-in-po-receipts-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/enter-a-receipt-in-po-receipts-entry"
---

# Enter a Receipt in PO Receipts Entry

You can enter receipts for purchase orders using the PO Receipts Entry form.
You will typically use this form to enter individual receipts, edit receipts created using the PO Initialize Receipts form, and edit or delete receipts that have already been posted.

1. From PO Receipts Entry, select the Add Record icon or enter a "+" in the Seq # field to create a new receipt.

1. Enter a PO number in the PO field or press F4 to select a PO from a list.

1. Enter the PO item number that you want to receive in the Item field or press F4 to select it from a list.Note: You can only receive a PO that is set up to be received. For example, when creating POs using [PO Purchase Order Entry ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form), if the PO item should be received, check the Receiving box on the Info tab in the Items section of the form.

1. The Line field is part of the [PO Item Distribution](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview) feature. Enter the line to receive. If you do not use this feature, accept the default value of "1" if you do not use this feature. Click [here](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form) for information on using this field.Tip: If you are not using the PO Item Distribution feature, you can remove the field from the form using the [F3 (Field Properties)](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form) form.

1. The lower portion of the form will populate with the PO item information. If you use the [PO Item Distribution ](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form) feature, the lower portion of the form will display the PO item line information.Note: The lower portion of the form actually always displays the PO item line selected using the Line  field, but if you do not use the PO Item Distribution feature the PO item and PO item line 1 are always the same.

1. Enter the number of units that you would like to receive using the Units field in the Changes to Received section. For example if a PO item has 10 units but only 4 are being received, enter a "4" in this field. By default the fields in the Changes to Received section will populate with all of the units/amounts that have not been received. Note: If you are receiving a PO item that is a lump sum amount, enter the amount of the receipt in the Total Cost field in the Changes to Received section. For example if you want to receive $600 of a $1000 PO item, enter $600 in this field.

1. The fields in the Changes to Backordered section will populate with the units/amounts left to be received. For example if a PO item has 10 units and you just received 4, this field will display a "6". Changing the value in these field is changing the units/amounts that you expect to receive. Generally you should not change the value in these fields.

1. Click the Save icon to save the receipt. The lower portion of the form will update with the new receipt information.

1. Now you can either enter more receipts or process the batch to post the receipts. Select File > Process Batch to process the batch.
