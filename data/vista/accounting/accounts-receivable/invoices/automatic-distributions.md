---
title: "Automatic Distributions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/automatic-distributions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/automatic-distributions"
---

# Automatic Distributions

If you are using the miscellaneous distributions feature, you
 can have distributions generated automatically for invoices and/or cash receipts. Automatic
 distributions are not available for miscellaneous cash receipts.
Although this feature is available for both invoices and cash receipts, it is recommended
 that you use it for one or the other, since using it for both can inaccurate distribution
 reporting.

## For Invoices

 To implement automatic distributions for invoices, check the Create Miscellaneous Distributions on Invoices
 box for each applicable customer in AR Customers. When validating an invoice batch, the
 system will automatically generate a single miscellaneous distribution record for each
 invoice, assigning a miscellaneous distribution code as follows:

- Contract-Related Invoices - Uses the miscellaneous distribution code assigned to
 the contract in JC Contract Info (JB Info tab). If no miscellaneous distribution
 code is assigned to the contract, it will use the miscellaneous distribution code
 assigned to the customer in AR Customers. If no miscellaneous distribution code is
 assigned to the customer, no miscellaneous distribution record is created for any
 invoice posted to that customer.

- Non-Contract Invoices - Uses the miscellaneous distribution code assigned to
 the customer in AR Customers. If no miscellaneous distribution code is assigned to
 the customer, no miscellaneous distribution record is created for any invoice
 posted to that customer.

Once distribution records are generated, you can modify them, if necessary, (in AR
 Invoice Entry, Misc Distributions tab), before you post the batch.

## Cash Receipts

To implement automatic distributions for cash receipts, check the
 Create
 Miscellaneous Distributions on Payments box for each applicable customer
 in AR Customers. The system will create a single miscellaneous distribution record for
 each invoice during batch validation, using the miscellaneous distribution code assigned
 to the contract in JC Contracts (contract-related invoices) or customer in AR Customers
 (non-contract invoices or contract invoices when a miscellaneous distribution code is
 not assigned to the contract).
If a distribution code is not found in JC Contracts or AR Customers,
 a miscellaneous distribution record will not be created for any invoice in the batch
 posted to that customer. Note: When using this feature for cash
 receipts, you will be unable to edit generated distributions. The system clears and
 recalculates the Misc Distributions table each time the batch is validated. Because
 the system cannot distinguish between entries generated automatically and those added
 manually, this will include overridden or added entries.

If you need to modify a generated distribution, use the following steps:

1. Close the cash receipts batch.

1. In AR Customers, clear the Create
 Miscellaneous Distributions on Payment checkbox for each applicable
 customer and save the record.

1. Reopen the cash receipts batch.

1. For each applicable receipt, adjust and/or add miscellaneous distribution records as
 applicable.

1. When you are satisfied with all distribution records for all payment sequences,
 validate and post the batch.

1. In AR Customers, recheck the Create
 Miscellaneous Distributions on Payment box for each applicable
 customer and save the record.
