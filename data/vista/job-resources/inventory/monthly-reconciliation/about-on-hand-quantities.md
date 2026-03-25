---
title: "About On-Hand Quantities | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-on-hand-quantities"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-on-hand-quantities"
---

# About On-Hand Quantities

The on hand quantity of a material is the total of two
 quantities: invoiced and received/not invoiced.
Invoiced Stock is the current
 quantity of a material that has been received and invoiced in AP. The following forms
 update this field.

- [AP Transaction Entry ](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form) - Increases the invoiced
 stock quantity each time you post to a material using an inventory transaction.


- [AP Intercompany Invoices ](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/about-the-ap-intercompany-invoices-form) -Increases the
 invoiced stock quantity each time Material Sales tickets for inventory transfers
 are posted from sister companies.

- [IN Adjustment Entry ](/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-adjustment-entry-form)- This form will either
 increase or decrease the invoiced quantity, depending on whether the adjustment
 is a positive or negative amount.

- [ IN Transfer Entry ](/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-transfer-entry-form) - This form will decrease
 the invoiced quantity for the location transferring the material, and increase
 the invoiced quantity for the receiving location.

- [IN Physical Count Worksheet ](/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form) - If a physical
 count produces discrepancies with the quantities on record, then the invoiced
 quantity will either be increased or decreased, depending on whether the
 discrepancy is a positive or negative amount.

- [IN Material Order Confirmation ](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form) - Decreases the
 invoiced quantity once a posted material order has been confirmed.

- [JC Material Use ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-material-use-form) - Decreases the invoiced
 quantity for inventory charged to jobs.

- [MS Ticket Entry ](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form) - Decreases the invoiced
 quantity for materials sold to customers, used on jobs, or sold to other
 inventory locations, including sister companies. Increases invoiced quantities
 at the sold to location.

Received N/Invoiced is the current quantity
 that has been received on POs, but not yet invoiced in AP. The following forms update
 this field.

- [PO Receipts Entry ](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form) / [PO Initialize Receipts ](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-initialize-receipts-form) - These forms increase
 the received/not invoiced quantity when you post a receipt of the material on an
 inventory purchase order.

- [AP Transaction Entry ](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form) - Decreases the
 received/not invoiced quantity when you post to a material on a purchase order
 transaction.
