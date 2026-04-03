---
title: "Out-of-Balance Accounts | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/procedures-overview/out-of-balance-accounts"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/procedures-overview/out-of-balance-accounts"
---

# Out-of-Balance Accounts

At any given moment, the sum of all of your open receivables should be equal to the balance in your General Ledger Accounts Receivable account(s). If the amounts do not appear to match, the following steps may be useful in determining the source of the difference.

## Out of Balance - Part I

1. Make sure everything is updated from A/R to G/L The first step is to confirm that no Accounts Receivable entries are in progress. You should attempt to update both invoices and cash receipts. If any of these selections produce a report, update accordingly.

1. Make sure customer accounts are internally in balance Print the A/R Trial Balance in Accounts Receivable. There should be no customer accounts out-of-balance. If any exceptions are found, these customers need to be fixed. Printing the Customers screen for each out-of-balance customer may help identify the source of the problem. Please call the Viewpoint Support Desk if you encounter a customer out-of-balance situation.

1. Compare A/R balances in G/L and Accounts Receivable Now that you have determined that Accounts Receivable module is internally in balance and all A/R transactions have been updated to General Ledger, you should plan to compare balances in the two modules. Enter all open G/L accounts with an open balance (AR trade, retention, etc.) into a GL report (Trial Balance Report or Transaction Journal). The total of this report should be compared with the AR Aged Open Items Report, with paid invoices included.

## Out of Balance - Part II

1. When was the last time the two modules agreed? If this is a recently converted company, compare the conversion amounts in the balance-forward Journal Entry to the conversion aged open item report. If you were in balance last month, has the G/L balance of that date changed? If it has not changed, this will help you to focus on a relatively short date range. If it has changed, you should investigate the source of that change.

1. Have any of the "Post to G/L" flags been deselected at any time recently? These flags are found in the General Ledger Installation. Typically, they are blank only during the conversion phase, then are permanently selected. If for some reason they had been deselected during normal operations, the update would not post any entries to General Ledger module.

1. Did you recently pass from one fiscal year to the next? If so, it may be appropriate to run the G/L Open Forward Balance Update in order to roll ending balances into the current year.

1. Are there any journal entries in the G/L Accounts Receivable account(s)? If so, this may be the source of your out-of-balance problem. If a Journal Entry is made to an Accounts Receivable G/L account, there is no corresponding adjustment performed on an individual customer's account. In addition to journal entries, you would be looking for entries from other sources, such as A/P or J/C. Any transaction not from invoicing or cash receipts is suspect.

1. Is General Ledger in balance (debits=credits)? To determine whether G/L is in balance, print the G/L Monthly Activity Balance File Report for all accounts. Look at the total line; all totals should be zero. If any other amounts appear, please call our office for assistance.
We hope that at least one of the above suggestions will help with the out-of-balance situation. If not, you may need to match individual entries in your General Ledger to A/R source documents. This is a laborious exercise, so you will hope to avoid this step if possible.
Assuming you determine and correct the out-of-balance problem, you may wish to monitor the balances in G/L and AR more frequently to confirm you maintain accurate G/L records. It is not necessary to wait until month-end to check your balances.
