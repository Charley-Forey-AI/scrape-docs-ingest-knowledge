---
title: "Add Posted Transactions Back into a Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/add-posted-transactions-back-into-a-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/add-posted-transactions-back-into-a-batch"
---

# Add Posted Transactions Back into a Batch

You can add previously posted transactions to a new or existing batch so that you can edit or delete them as needed, and then repost them.
Using the criteria provided, you can filter transactions so that you include only those you want added to the batch; however, you can only select transactions that were posted in the same month as the current batch.

1. In the AP Transaction Entry form, select File > Add Transaction.The AP Add Transaction to Batch form displays.

1. Use one or more of the following options to filter transactions you want added to the batch:

- Source Batch #

- AP Transaction #

- Vendor

- Pay Control

- Pay Category

- Begin Invoice Date / End Invoice Date

1. If the transactions you are adding to the batch should be deleted from the database, select the Mark Added Transactions as "Delete" checkbox.The system automatically sets the Action field to D-Delete for all transactions added to the batch.Note: Unless otherwise selected, the system automatically sets the Action to C-Change for all transactions.

1. Click Add to Batch. A message displays asking if you want to include all of the transaction's detail lines.

1. Click Yes to include all detail lines or No to exclude the detail lines. A confirmation message displays and provides an opportunity to include another transaction.Note: If the system encounters transactions that it cannot add to the batch, an message displays, along with an exception report (AP Add Transaction Exception Report) that details the excluded transactions and exclusion reasons. However, all other transactions meeting the selection criteria are added to the batch.

1. If you clicked Yes to add additional transactions, repeat steps 2-5. If you clicked No, you are returned to the AP Transaction Entry form.

Once you return to AP Transaction Entry, you can edit the added transactions as needed and post the batch.
