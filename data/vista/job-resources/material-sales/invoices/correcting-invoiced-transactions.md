---
title: "Correcting Invoiced Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/invoices/correcting-invoiced-transactions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/invoices/correcting-invoiced-transactions"
---

# Correcting Invoiced Transactions

Generally, most corrections to an invoice are made before the invoice is posted to Accounts Receivable and General Ledger. However, what happens if a correction becomes necessary after the invoice has been posted to AR/GL?
Material Sales allows you the capability of correcting invoices that have already been posted to AR/GL without creating a new invoice in Accounts Receivable. This is done by creating a new, correcting invoice and applying it to the old invoice. When the new invoice is posted to AR/GL, the system applies the transaction to the old invoice as an adjustment. The two invoices are kept together so that when printing customer statements or checking customer accounts, you will have an accurate accounting of the complete transaction. The following instructions will guide you through this process:

1.  Create a reversing entry in MS Ticket Entry or MS Hauler Time Sheet Entry (depending on the assigned transaction). This is done by creating a duplicate transaction with negative amounts equal to the positive amounts on the original transaction. Note: You should only need to enter negative Units Sold, and remaining amounts will calculate accordingly. Although the transaction number will be different, you can assign the same ticket number (or freight bill number if a time sheet) to the reversing entry. (If using the option to warn on duplicate ticket numbers in MS Company, a warning will be displayed, but the entry will be allowed). You can also use a 'dummy' ticket or freight bill number that you have designated for reversing transactions.

1.  Apply the reversing transaction to the invoice you are correcting. To do this, create a new invoice either by initialization (MS Invoice Initialize) or by manual entry (MS Invoice Edit). In the Apply To field, enter the number of the original invoice. Then, add the reversing transaction to the invoice (in the transaction grid of MS Invoice Edit).

1.  Post the invoice with the reversing entry to AR/GL (in MS Batch Process). AR will now have both the original and corrected invoice, and General Ledger will be updated with both the positive and negative amounts. Note: Invoices can be reversed even if a cash receipt has already been applied (in AR Cash Receipts).
