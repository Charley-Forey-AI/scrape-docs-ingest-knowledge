---
title: "Initialize Purchase Orders to AP Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/initialize-purchase-orders-to-ap-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/initialize-purchase-orders-to-ap-invoices"
---

# Initialize Purchase Orders to AP Invoices

You can initialize purchase orders (created in PO Purchase Order Entry or SM Purchase Order Entry) to AP invoices or AP Unapproved Invoices using the AP Purchase Order Initialize form.
The following details how to initialize purchase orders to an AP invoice.

1. Open the AP Purchase Order Initialize form using one of the following methods:

- From AP Unapproved Invoice Entry, select an existing invoice for the PO or enter a new one. Then, with focus in either the invoice header or on an invoice line, select File > Initialize from PO.

- From AP Transaction Entry, open an existing batch or create a new one. Then enter or select an invoice for the PO, place focus on an invoice line, and select File > Initialize from PO.

The AP Purchase Order Initialize form opens, displaying all valid purchase orders for the specified vendor either by purchase order number (Purchase Order tab) or by receiver number (Receiver # tab).

1. To initialize by PO number:

1. Select the Purchase Order tab and choose the desired purchase order from the grid by highlighting the applicable row.If the list of POs is extensive and you know the PO number, you can enter it in the PO field, select Apply Filter to refresh the grid, and then select your PO.
Note: If you are initializing POs via the AP Unapproved Invoice Entry form and you specified a PO in the invoice header, selecting File > Initialize from PO from the invoice header auto-defaults the purchase order in the PO field on the Purchase Order tab in AP Purchase Order Initialize. You can select the defaulted PO or change the filter to select a different PO.

1. Select Initialize.

1. To initialize by receiver number:

1. Select the Receiver # tab and choose the desired receiver #/purchase order from the grid by highlighting the applicable row.If the list of POs is extensive and you know the Receiver number, you can enter it in the Receiver # field, select Apply Filter to refresh the grid, and then select your PO.

1. Select Initialize.

The system initializes the selected purchase order to the invoice, creating a new invoice line. You can then edit the invoice line as needed.For more information about initializing POs, see [AP Purchase Order Initialize Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form).

Related information

- [AP Purchase Order Initialize Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)
