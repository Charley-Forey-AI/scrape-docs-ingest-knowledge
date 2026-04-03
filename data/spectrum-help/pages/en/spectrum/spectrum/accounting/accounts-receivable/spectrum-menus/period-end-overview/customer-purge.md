---
title: "Customer Purge | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/period-end-overview/customer-purge"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/period-end-overview/customer-purge"
---

# Customer Purge

Use the Customer Purge update to purge customers and records from associated files in the work order, service contract, address, order processing, invoice, or payment history files. Running this update will purge all customers selected. For these selected customers, any records in the work order, service contract, address, order processing, invoice, or payment history files will also be deleted.
Customers will not be purged when any of the following conditions exist:

- Their balances are non-zero

- If their last bill date or paid date is later than the purge through date

- If they have orders or unposted invoices in Order Processing

- If they have work orders with a complete date later than the purge through date or an incomplete status

- If they have a service contract with an end date later than the purge through date

- If they have a contract that the associated job is Active or the completed date is later than the purge through date.
Important: Make a backup before records are purged from the software.
