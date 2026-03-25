---
title: "Clear CM Entries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-cm-entries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-cm-entries"
---

# Clear CM Entries

You can use the CM Clear Initialize form to clear a range of entries for a statement date.
You can initialize entries for all transaction types or select specific transaction types to clear. Additionally, you can specify a range of transactions to clear or specify to clear all transactions through a specified date. The system will clear all transactions meeting the specified criteria.
For example, if you want to clear only checks and EFTs, you would select the Checks/Electronic Payments transaction type in the Items to Display box in the CM Clear Entries form. Then when initializing entries using this form, you can specify a
 Clear Outstanding Entries Dated On or Before
 date that includes the majority of items that have cleared. During initialization, the system will clear all items meeting the specified criteria.
To initialize cleared entries:

1. Open CM Clear Entries.

1. In the
 CM
 Account
 field, enter the CM account for which to clear entries or press

 F4
 to select from a list of valid accounts.

1. In the Display Through
 Date field, accept the defaulted statement date or enter the date
 through which to display transactions for the CM account.

1. In the Default Date
 Cleared field, enter the cleared date for all transactions being
 reconciled. Initially defaults the statement date, but if you have items that cleared
 on different dates, make sure you enter the latest cleared date of the transactions
 to reconcile.

1. In the Check Items to Display section, select one or more of the following transaction types to clear: Checks/Electronic Payments , Deposits, Adjustments, and Transfers.Note: Although these transaction types control what items display in the grid, they also are used to designate what items you want cleared. You must select one or more transaction types in order to use the Initialize feature.

1. In the Check Items to Display section, also select the Outstanding Entries checkbox. This will populate the grid with only transactions that you have not yet cleared. Click Refresh to populate the grid and enable the Initialize button.

1. Click Initialize. The CM Clear Initialize form displays.

1. In the
 Beginning
 Reference
 and
 Ending
 Reference
 fields, enter the range of reference numbers to initialize or leave
 blank to initialize all entries.

1. In the Clear Outstanding Entries On or Before field, enter the date through which to clear entries. The system will mark all entries dated on or before this date as cleared.

1. Click
 OK.

Once the initialization process is complete, you can
 use the grid in CM Clear Entries to exclude any items that were not cleared (by
 deselecting the Cleared checkbox).
You can also clear entries using an auto-clearing file. For more information, see [Initializing Cleared Entries Using an Auto-Clearing File](/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-entries-automatically).

Related information

- [Clear Entries Automatically](/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-entries-automatically)

- [Reset Cleared Entries](/en/vista/vista/accounting/cash-management/processing/reconciliation/reset-cleared-entries)

- [About the CM Clear Initialize Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-initialize-form)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

- [About the CM Clear Undo Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-undo-form)
