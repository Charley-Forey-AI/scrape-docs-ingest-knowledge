---
title: "About Deleting Invoice Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-deleting-invoice-transactions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-deleting-invoice-transactions"
---

# About Deleting Invoice Transactions

The method you should use to delete AP invoices/transactions depends where it is in the AP cycle.

## If the transaction has been paid

You cannot delete transactions that have been paid or even partially paid, but you can take one of the following actions:

- create a new transaction to reverse the
 outstanding payable balance using the AP Transaction Entry form; or

- void the payment using the AP Void Payments form and then proceed with the information below.

## If the transaction is not yet paid or was voided

If the month
 in which it was expensed is still open, add the transaction back into a new batch using the AP
 Transaction Entry form and change the Action to 'D' (Delete). When the batch is
 processed, the transaction is removed from all AP files and the system creates reversing entries in the affected subledgers and the General Ledger.Note: Using the Delete button (or by selecting Records > Delete) only removes the transaction record from the current batch.
If the month in which it was
 expensed is closed, you can no longer delete the open transaction.
 Instead, use the AP Transaction Entry form to post a reversing entry to back out the original
 transaction. Make sure that you use the same Trans Type, Job#, etc., as you did for
 the original so that information is also backed out of other modules.
Once you have processed the reversing entry, you may optionally use the AP Clear Transactions form to clear
 the original transaction and the reversing transaction to remove both from the
 Open Payables report.Note: Until a transaction has an assigned check #, the system considers it an open
 payable (even if it has a zero balance) and displays it on the AP Open Payables
 report.
