---
title: "Receiving Methods | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/procedures-overview/in-depth-overview/receiving-methods"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/procedures-overview/in-depth-overview/receiving-methods"
---

# Receiving Methods

The procedure used to record receipt of purchase orders is
 dependent upon the selection option in the Receiving method section on the Purchase Order
 Installation page.
During Purchase Order Installation, the software administrator specified whether receipt of
 purchase orders is a single-step or two-step process.

## One-Step Receiving Method

The one-step receiving method allows entry of quantity and invoice information as a single process. This is desirable for operations where the arrival of the invoice triggers a one-step computer entry. Quantity received and cost are recorded and confirmed in a single page.
When a purchase order is received using the one-step method, an unposted Accounts Payable invoice is created automatically. If the Update inventory checkbox on the Purchase Order Installation page is selected, stock items are updated to inventory upon completion of the Purchase Order receipt entry. Regardless if the Update inventory checkbox is selected, items received for jobs or equipment do not update inventory. They are updated when the A/P invoice from Purchase Order Receiving is updated using the A/P Transaction Update page.
If all items on the purchase order are received, the purchase order status is automatically changed to closed. Following the receipt of the purchase orders, print the A/P Transaction Register and update. The General Ledger, Job Cost, Equipment Control, Time + Materials, and A/P files are updated with the appropriate information.

## Two-Step Receiving Method

The two-step receiving method involves first entering quantities received, often from a packing list, then entering the A/P invoice information when the invoice arrives from the vendor. This method might be desirable if materials are shipped to a warehouse or job site, but the invoice for those materials is sent to the business office. This method is available for operations that separate responsibility and control for receiving stock (quantity issues) and invoice processing (cost issues).
When an invoice is entered, it is then updated automatically to the Accounts Payable module to the A/P Invoice/Credit Memo Entry page. After entering purchase orders for invoices, print the A/P Transaction Register and update. The General Ledger, Job Cost, Equipment Control, Time + Materials, and A/P files are updated with the appropriate information.

- Stock Items When using the two-step method for stock items, if
 the Update inventory checkbox on the Purchase Order Installation page is selected,
 an additional option to use a separate step to update inventory is available. By
 selecting the Two-step with pack list update option on the Purchase Order
 Installation page, an inventory receipt is created for each item received on the
 purchase order when you update the packing list. After the pack list is updated, the
 status changes from open to received. If the "packing list update" field is set to
 no, stock inventory items update Inventory Control only when Invoice Receiving Entry
 is performed.

- Use tax, if any, is included in the unit cost when the Inventory
 Control item detail file is updated.

Regardless of the setting of the Update inventory field, items
 received for jobs or equipment do not update inventory. They are updated when the A/P
 invoice from Purchase Order Receiving is updated using the A/P Transaction Update
 page.
