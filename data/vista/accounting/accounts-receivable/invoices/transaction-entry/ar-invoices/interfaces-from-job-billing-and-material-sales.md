---
title: "Interfaces From Job Billing and Material Sales | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/interfaces-from-job-billing-and-material-sales"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/interfaces-from-job-billing-and-material-sales"
---

# Interfaces From Job Billing and Material Sales

Both the Job Billing (JB) and Material Sales (MS) modules have their own invoicing capabilities.You can interface invoices generated in these modules to Accounts Receivable for tracking.
 Invoices interfaced from JB or MS must be edited in those modules.
When interfacing invoices from Job Billing or Material Sales, items are interfaced to AR in a different format than they were entered in JB or MS.

- JB — Invoices are interfaced to AR on a single transaction line per contract item basis. If there are several items posted to a contract item in JB, the system will add all the items together and send them to AR as one transaction line for that contract item.

- There are two types of invoices in Job Billing: Progress Billing and Time & Materials. After they are interfaced, they will appear in the same format as invoices entered in AR, but the description for each invoice will indicate whether it is a progress invoice or a T&M invoice.

- MS — Invoices are not posted to contracts in Material Sales; they are posted on a per customer basis. Each item on an invoice is posted to a GL account and when interfaced to AR, will be sent over as a single line item per GL account. When the interface is run, the system will total all items posted to the same GL account, and for each GL account referenced, one line item will be sent to AR.

As with JB invoices, Material Sales invoices interfaced to AR appear in the same format as AR invoices, but the description displayed for each invoice indicates that the invoice is from Material Sales.
