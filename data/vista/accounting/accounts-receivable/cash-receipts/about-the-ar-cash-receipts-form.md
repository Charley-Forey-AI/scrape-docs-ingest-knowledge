---
title: "About the AR Cash Receipts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form"
---

# About the AR Cash Receipts Form

Use the AR Cash Receipts form to enter cash receipts (payments) for AR invoices.
There are two types of transactions categorized
 under cash receipts: Payments and Miscellaneous Cash Receipts. Payments are
 customer-related payments that you can post to specific invoices or account balances.
 Miscellaneous Cash Receipts are payments that are not customer-related (e.g.,
 over-the-counter sales, money market fund payments, job expense refunds, etc.).

## Auto Apply Payments

Once you enter the header information and save the record,
 the AR Initialize Receipts form displays, allowing you to specify how to apply
 payments.
You can choose to apply payments to the oldest
 invoices, on account, by invoice number, or by customer job. You also have the option to
 include/exclude retainage, apply discounts, or include/exclude finance charges. The
 Don't
 Initialize option allows you to bypass initialization and apply the
 payment manually.
Once you have selected the desired options
 and click OK, the system will cycle through the specified range of invoices, applying
 payment to each invoice as the remaining balance allows until the payment is fully
 applied. If you selected to apply payment 'on account', payment will be applied to the
 account balance rather than individual invoices (typically used for Balance Forward
 accounts).Note: The Invoice Totals section (above the grid) displays
 information for each selected invoice. Be aware that the unpaid values (retainage,
 finance charges, and tax) include amounts in unposted cash receipts batches.
For more information about initializing
 payments, see [About the AR Initialize Receipt Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-initialize-receipt-form).

## Reversing a Payment

To reverse a posted payment, locate the invoice and enter an amount in the
 Total Applied column that is an exact opposite of the
 amount in the Prev Applied field.
The system flags this as a “reversing”
 entry and removes the input restrictions. Enter reversing values for all original
 values (i.e., Tax Applied, Disc Taken,
 Retg Applied, etc.) as applicable. The following example
 shows the difference between an original payment and a reversing transaction.
Payment
Total Applied
Tax Applied
Disc Taken
Tax Disc
Retg Applied
FC Applied

Original
2625.00
125.00
50.00
2.50
250.00
0.00

Reversing
-2625.00
-125.00
-50.00
-2.50
-250.00
0.00

Do not tab off the line until after you
 have completed the reversing entry, as this causes the system to reset the
 “reversing” flag and re-enables the input restrictions.
Note: If multiple lines exist on the invoice, the
 system distributes the reversal accordingly to each line. To modify the
 distribution, use the AR Payment Detail form. For more information, see the AR
 Payment Detail topic.

## Finance Charges

If finance charges were applied to an invoice, and the payment is not fully applied
 after paying tax, it is then applied to the finance charges. Once the finance
 charges are paid, any remaining amount is applied to the invoice total. If the
 payment is not sufficient to cover the finance charges, it will pay as much of the
 finance charge as is available, and none of the payment is applied to the invoice
 total. Note: The FC Applied column will only display in the
 grid if you selected the Include TaxApplied in Grid
 option from the Options menu. This option does not affect whether payments are
 applied to finance charges. If you did not elect to Exclude Finance
 Charges, payments will always be applied to finance charges,
 regardless of whether you opt to display this column or not.

If you are manually applying payments or overriding the default applied finance
 charge, you can specify any amount of the payment to apply to the finance charges,
 as long as it does not exceed the 'unpaid' finance charge amount.
Note: Although finance charges may be assessed and
 paid on contract invoices, the finance charge portion of the invoice will not be
 updated to JC. Only the invoice amount will be updated to JC.

## Changing and Deleting Previously Posted Transactions

To change a transaction, add it to the current batch using the AR
 Add Transaction to Batch form. See [About the AR Add Transaction to Batch
 Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-add-transaction-to-batch-form).

## Allocating Amounts across Multiple Invoice Lines

If you want to assign a received amount to multiple lines on an invoice, select the
 invoice in the grid and click the Payment Details button. The
 AR Payment Detail form appears, allowing you to distribute the amount across the
 invoice lines as necessary. See [About the AR Payment Detail Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-payment-detail-form).

Related information

- [Cash Receipts Setup Options](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/cash-receipts-setup-options)

- [Detail Display Options for the AR Cash Receipts Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/detail-display-options-for-the-ar-cash-receipts-form)

- [Posting Shortcuts](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)

- [About the AR Payment on Account Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-payment-on-account-form)

- [About the AR Miscellaneous Receipt Lines Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-miscellaneous-receipt-lines-form)
