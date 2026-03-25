---
title: "AP Purchase Order Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-purchase-order-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-purchase-order-initialize-form"
---

# AP Purchase Order Initialize Form

Use the AP Purchase Order Initialize form to add purchase orders to an AP invoice transaction in AP Transaction Entry or AP Unapproved Invoice Entry.

From either invoice entry form, you can access the AP Purchase Order Initialize form using an existing invoice or once you enter invoice header information for a new invoice.

- In AP Transaction Entry, place focus on the line item and select File > Initialize from PO.

- In AP Unapproved Invoice Entry, place focus in the header or on the line item and select File > Initialize from PO.

Note: The use of this form to add purchase orders to a transaction is not required; you can manually enter purchase order items in either entry form.

This form has two tabs:

- Purchase Order - This tab allows you to select purchase orders by number.

-  Receiver # - This tab allows you to select purchase orders by receiver number. However, you can only use this option for purchase orders that you received via the PO Receipts Entry form and for which you assigned a receiver number in the transaction header. Although this tab displays all POs for the vendor that were received in PO Receipts Entry, you can only initialize those that are assigned a receiver number.

Each tab has a grid that displays all available purchase orders for the vendor specified in the Vendor field of the transaction form, along with applicable information including the purchase order or receiver number, description, amount left to invoice or amount received, compliance status, and whether the PO is in an open batch.
If the list of purchase orders on either tab is extensive, you can filter the list to show only the purchase order you want and then select Apply Filter. If you are using the Receiver tab, you can filter by receiver number or PO number.
Note: Keep in mind that the PO and Receiver # filter results will show all PO or Receiver numbers that start with the numbers you enter. For example, if filtering by PO#, entering 1155 will show all POs that begin with that number (for example, 1155, 11550, 11552, etc.).

If you are initializing POs in AP Unapproved Invoice Entry and you select File > Initialize from PO while focus is in the invoice header, if you entered a purchase order in the header PO field, the PO field on the Purchase Order tab (only) in AP Purchase Order Initialize automatically defaults the PO specified on the invoice. If you want to initialize a different PO, you can either clear the PO number or enter a different one and select Apply Filter.

## Initializing POs in an Open Batch

Purchase orders that exist in open batches are highlighted in red. If you are adding purchase orders via AP Transaction Entry, you cannot add these purchase orders to the batch. If you are adding purchase orders via AP Unapproved Invoice Entry, you can add these purchase orders as long as there are units left to be invoiced (determined by invoiced amounts plus amounts in open AP batches and unapproved invoice sequences).
There is one exception when adding POs to an AP Transaction Entry batch. If the PO exists in the current batch, it is not highlighted in red. You can add the PO to the same batch multiple times, as long as there are units left to invoice. You might typically do this when entering multiple invoices for a vendor where more than one of the invoices applies to the same PO. Each initialization of the PO will bring in the units remaining from the prior entry. For example, if you initialize a PO with 500 units and adjust the invoiced units to 250, initializing the PO to another invoice in the batch will default the remaining 250 units.

For more information about using this form, see [Initialize Purchase Orders to AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/enter-unapproved-invoices/initialize-purchase-orders-to-ap-invoices).
