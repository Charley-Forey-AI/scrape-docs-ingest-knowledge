---
title: "Assign \"On Account\" Payments to Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/assign-on-account-payments-to-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/assign-on-account-payments-to-invoices"
---

# Assign "On Account" Payments to Invoices

You can assign payments that you applied to a customer's account to one or more invoices.
 To apply an 'on account' payment to an invoice, you must first reverse the 'on account' payment and then assign it to the appropriate invoices.If the 'on account' payment is in an open batch, do not use these instructions. Instead, open the batch and reinitialize the
 transaction to the appropriate invoice.
If you have already posted the payment batch or you need to reverse the payment for a closed month, use the following instructions.

1. To apply on account payments to invoices when the batch month is still open:

1. From the AR Cash
 Receipts form, select File > Add
 Transaction.The AR Add Transaction to Batch form displays.

1. In the AR Transaction# field, press F4 and select the transaction to add.

1. Click Add to Batch.A message displays indicating success and asking if you want to add another transaction.

1. Click Yes to add another
 transaction or No to return to the AR Cash Receipts form.The system adds a sequence for each added transaction to AR Cash Receipts.

1. Click On Account.The AR Payment on Account form displays.

1. Enter 0.00 in the
 Amount, Tax Basis, Tax Amount, and Disc Taken fields.

1. Save the record and close the form.

1. In AR Cash Receipts, enter the payment amount to apply to each applicable invoice.

1. Process the batch (File > Process Batch.

1. To reverse an on account payment for a closed
 month:

1. Add a new transaction in
 a current month with a check amount of zero.

1. Click) to save the record.The AR Initialize Receipts form displays.

1. Select Don't Initialize and click OK.
 The AR Initialize Receipts form closes. An "on account" transaction appears at
 the top of the grid in the AR Cash Receipts form, without a specified invoice
 number.

1. Select the "on account"
 transaction and enter the original payment amount as a negative number in the
 Total Applied column.

1. Process the batch (File > Process Batch.
