---
title: "Record Inventory Separately from the Invoice | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/procedures-overview/tell-me-how/miscellaneous-procedures/record-inventory-separately-from-the-invoice"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/procedures-overview/tell-me-how/miscellaneous-procedures/record-inventory-separately-from-the-invoice"
---

# Record Inventory Separately from the Invoice

You can use a two-step receiving method if you want to process the AP invoice separately from the inventory/packing list.

## Important Purchase Order Settings

- (Required) Go to System Administration > Installation > Purchase Order > Properties and select Update packing list to inventory before invoicing.

- (Optional) If you want the option to to accrue purchase order costs to the general ledger before the invoice is posted, select the Update packing list to jobs before invoicing checkbox in the Purchase Order Installation window, and enter a G/L account in the Accrued purchases G/L account field. If you want future purchase orders to use this as the default behavior, also select Default new job purchases orders to accrue costs.Important:
 If you take this option, the Job Cost module (screens and reports) will display purchase order materials as job-to-date costs instead of open commitments when you receive the inventory.

- (Optional) Under the Default receiving method section, select Two-step (packing list + invoice).Note: The default setting is optional. When it comes to receiving inventory and posting the invoice, this setting must be selected.

## Set up the Purchase Order

1. Go to Purchase Order > Data Entry > Purchase Order Entry.

1. Complete all of the fields on the Purchase Order Entry page. Record the quantities of inventory items to be received.

1. On the Other Purchase Order Information window, in the Receiving method section:

1. Select Two-step (packing list + invoice).

1. If you want to accrue purchase order costs to the general ledger before the invoice is posted, select the Accrued purchase order costs checkbox.

1. Set the purchase order status to Open.

1. When all items are recorded, select Save.

## Receive the Inventory

1. On the Info Bar, go to Purchase Order > Receiving > Packing List Entry.

1. Complete the Packing List Quantity Entry screen and then select Save.

1. On the Packing List Quantity Entry page, select Update.Note: If the Edit List button displays instead of the Update button, you need to make a correction to the Purchase Order Installation settings. Go to Purchase Order Installation > Properties tab and select Update packing list to inventory before invoicing.

1. Preview the Packing List Quantity Edit Listing.

1. On the Packing List Update page, select Continue to update the Inventory Control module.

1. Preview the Inventory G/L Summary Report to update the General Ledger module.

1. On the Inventory G/L Summary Update page, select Continue.

## Process the Invoice

1. When you're ready to process the invoice, go to Accounts Payable > Data Entry > Vendor Invoices.

1. Enter the Vendor, Invoice #, and Purchase order number.

1. Choose the packing lists to be included on this invoice by selecting the Select checkbox and select OK.

1. Complete the remaining fields until the details portion of the Purchase Order Receiving Detail window displays.

1. Verify that purchase order amount information is correct and select OK.

1. Select Save to open the Save Invoice (or Save Unapproved Invoice) window.

1. Choose whether to close the P.O. now or assign the invoice to the next reviewer, and then select Continue.
