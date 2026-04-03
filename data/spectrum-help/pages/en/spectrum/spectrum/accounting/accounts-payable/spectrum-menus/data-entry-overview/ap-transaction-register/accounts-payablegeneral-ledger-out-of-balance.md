---
title: "Accounts Payable/General Ledger Out Of Balance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register/accounts-payablegeneral-ledger-out-of-balance"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register/accounts-payablegeneral-ledger-out-of-balance"
---

# Accounts Payable/General Ledger Out Of Balance

This section provides troubleshooting and correction instructions. If, for example, accounts are out-of-balance, information from this section may be used as a resource in discovering the reason for the error. Once the error has been found, corrections may be made.
Every effort should be made to discover the source of an out-of-balance situation. Extreme caution should be used in performing a one-sided Journal Entry. At all times, correct accounting procedures should be followed; do not force the General Ledger to balance.
At any given moment, the sum of all of your open payables should be equal to the balance in your General Ledger Accounts Payable account(s). If the amounts do not appear to match, the following steps may be useful in determining the source of the difference.

## Part I

1. MAKE SURE EVERYTHING IS UPDATED FROM A/P TO G/L. The first step is to confirm that no Accounts Payable entries are in progress. Print an [A/P Transaction Register](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register) of invoices/credit memos. Print a Manual Check Register, a Void Check Register, a Pre-check Register, a Check Register and a Payments G/L Detail Report. If any of these selections produce a report, update accordingly.

1. MAKE SURE VENDOR ACCOUNTS ARE INTERNALLY IN BALANCE Print the [Trial Balance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/period-end-overview/trial-balance). There should be no vendor accounts out-of-balance. If any exceptions are found, they need to be fixed. Printing the Vendor Detail Inquiry screen for each out-of-balance vendor may help identify the source of the problem. Please call the Viewpoint office if you encounter a vendor out-of-balance situation.

1. COMPARE A/P BALANCES IN GENERAL LEDGER & ACCOUNTS PAYABLE Now that you have determined that Accounts Payable module is internally in balance and all A/P transactions have been updated to General Ledger, you should plan to compare balances in the two modules. Use Display Total A/P Balance to learn the current balance in A/P; then determine the current balance in your A/P General Ledger account(s). It is important to compare the current balances in both modules to determine whether an out-of-balance situation still exists.

## Part II

Having determined that General Ledger and Accounts Payable modules are out-of-balance, the following areas should be explored:

1. When was the last time the two modules agreed? If this is a recently converted company, compare the conversion amounts in the balance-forward journal entry to the conversion aged payable report. If you were in balance last month, has the G/L balance of that date changed? If it has not changed, this will help you to focus on a relatively short date range. If it has changed, you should investigate the source of that change.

1. Have any of the Post to G/L checkboxes been cleared at any time recently? These checkboxes are found in the General Ledger Installation. Typically, they are left unselected only during the conversion phase, then are permanently selected. If for some reason they had been unselected during normal operations, the update would not post any entries to General Ledger module.

1. Did you recently pass from one fiscal year to the next? If so, it may be appropriate to run the G/L Opening Forward Balance Update in order to roll ending balances into the current year.

1. Are there any journal entries in the G/L Accounts Payable account(s)? If so, this may be the source of your out-of-balance problem. If a journal entry is made to an Accounts Payable G/L account, there is no corresponding adjustment performed on an individual vendor's account. In addition to journal entries, you would be looking for entries from other sources, such as A/R or J/C. Any transaction not from Accounts Payable module is suspect.

1. Is General Ledger in balance (debits=credits)? To determine whether G/L is in balance, print the G/L Monthly Activity Balance File Report for all accounts. Look at the total line; all totals should be zero. If any other amounts appear, please call our office for assistance.

1. Have any A/P invoices been distributed to the Accounts Payable G/L account (instead of an expense account)? To determine whether this may have occurred, print the A/P G/L Distribution Report for the Accounts Payable G/L account(s). Look for entries in which the same account was debited and credited. Also, look for use of an Accounts Payable G/L account other than your usual G/L account.

1. Compare the payments made on Accounts Payable invoices to the General Ledger. Run the Check Register History Report, and compare to the General Ledger Trial Balance Report run with a source of A/P Payments.

1. Compare the Accounts Payable invoice distribution to the General Ledger. Run the A/P G/L Distribution, sorted by G/L account, and compare to the General Ledger Trial Balance Report run with a source of A/P Invoices.
We hope that at least one of the above suggestions will provide help with the out-of-balance situation. If not, you may need to match individual entries in your General Ledger to A/P source documents. This is a laborious exercise, so you will hope to avoid this step if possible.
Assuming you determine and correct the out-of-balance problem, you may wish to monitor the balances in G/L and A/P more frequently to confirm you maintain accurate G/L records. It is not necessary to wait until month-end to check your balances.
