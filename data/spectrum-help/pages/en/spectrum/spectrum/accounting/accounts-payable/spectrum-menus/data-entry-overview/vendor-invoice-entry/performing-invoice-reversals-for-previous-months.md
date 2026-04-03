---
title: "Performing Invoice Reversals for Previous Months | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/performing-invoice-reversals-for-previous-months"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/performing-invoice-reversals-for-previous-months"
---

# Performing Invoice Reversals for Previous Months

If an invoice is posted to G/L in July, reversal posts to G/L
 in Aug, when performing a reversal, you might find you don't have the option to
 automatically move both items to history. This is because a G/L transaction is required.
 Below is an example of the accounting process if the reversal performed manually in August
 for an invoice entered in July:
Below is an example of the accounting process if the
 reversal performed manually in August for an invoice entered in
 July:Debit
Credit

Expense
100

A/P Trade
100

Debit
Credit

Expense
100

A/P Trade
100

As you can see, the entries do not truly offset each other. The invoice is still an outstanding liability as of July 31st. Likewise, if you were to run an after-the-fact aging as of July 31st, the liability would also appear. Because the whole event (invoice update and reversal) did not take place within one period, the date-sensitivity is retained (protected) during the Reverse Invoice Update. Therefore, the zero-dollar check must be a separate event, based on accounting need.
To resolve the outstanding liability, select a specific date for the zero-dollar.
 If that check date is July, then the Aged Payables Report would not show the
 item anymore, and Accounts Payable would appear to be out-of-balance with the
 General Ledger. However, by selecting a later period to perform the reversal,
 you have elected to keep the item open for a span of time. The automatic move to
 history can only occur when the entire event transpires in both the Accounts
 Payable and the General Ledger during the same period, such as below.

The result is truly net-zero:
 Debit
Credit

Expense
100
100

A/P Trade
100
100
