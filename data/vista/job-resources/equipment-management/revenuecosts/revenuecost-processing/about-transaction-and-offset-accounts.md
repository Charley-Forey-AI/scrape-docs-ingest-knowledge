---
title: "About Transaction and Offset Accounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-transaction-and-offset-accounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-transaction-and-offset-accounts"
---

# About Transaction and Offset
 Accounts

## Transaction GL Accounts

When posting cost adjustments, you must assign each transaction line a
 transaction account. This account number initially defaults the cost type GL account
 (specified in EM Departments) or the cost code GL account (if an override is set up for
 cost code in EM Departments). If no GL account was specified for the department/cost
 type, you must specify one on the transaction line, making sure the account has a
 subledger code of ‘E’ (Equipment) or blank (null).Note: You can
 only override the GL account if you have specified to allow overrides to GL accounts
 in EM Company Parameters.

## Offset GL Accounts

The Offset Acct identifies the offsetting GL account for the Transaction account. You
 should only need these for transactions that are posting additional costs or making
 accrual or reversal entries. They are not required on transactions that are merely to
 correct an equipment code, component, cost type, or cost code, or when you enter two
 transactions that offset each other or use the same account.
Offset accounts will be used any time you modify the detail records in another batch. If
 you do not assign an offset account, you must create an ‘offsetting’ transaction (i.e.
 another transaction to balance the first transaction). Any amount of the current batch
 not yet distributed to offsetting accounts displays in the ‘Undistributed’ section at
 the top of the form (above the tab pages).
If you enter a non-stocked material, this account defaults based on
 the Non-Stocked GL Account stored in HQ Material Categories for the specified material.
 If you specify a stocked material, this account defaults based on the Equipment Sales
 account designated for the specified location in IN Locations. When you process the
 batch, the update creates a credit entry to the Inventory account and a debit entry to
 the Cost of Goods Sold account (both defined in IN Locations).

Note: If you have flagged a transaction for automatic reversal, you must enter an offset
 account for that transaction, making sure to assign an account with a blank (null) sub
 ledger code.
