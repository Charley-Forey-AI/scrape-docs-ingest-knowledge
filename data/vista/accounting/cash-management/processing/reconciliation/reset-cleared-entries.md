---
title: "Reset Cleared Entries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/reconciliation/reset-cleared-entries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/reconciliation/reset-cleared-entries"
---

# Reset Cleared Entries

You can use CM Clear Entries to reset cleared entries for a statement back to being outstanding entries.
When you "undo" entries, the system resets the specified entries to "outstanding" by deselecting the
 Cleared
 checkbox for each applicable entry. The entries reset will depend on the transaction types you select in the Check Items to Display section.
To reset cleared entries:

1. Open CM Clear Entries.

1. In the
 CM
 Account
 field, enter the CM account or press
 F4
 to select from a list of valid accounts.

1. In the
 Display Through Date
 field, accept the defaulted statement date or enter the date through which to display transactions for the CM account.

1. In the
 Default Date Cleared
 field, enter the cleared date for all transactions being reset. Initially defaults the statement date, but if you have items cleared on different dates, make sure you enter the latest cleared date of the transactions you want to reset.

1. In the Check Items to Display section, select the transaction types you want to reset. Options are: Checks/Electronic Payments , Deposits, Adjustments, and Transfers.Note:Although these transaction types control what items display in the grid, they also are used to designate what items you want reset. You must select one or more transaction types in order to use the Undo feature.

1. In the Check Items to Display section, select the Cleared Entries checkbox. This will populate the grid with only transactions that you have marked as cleared. Click Refresh to populate the grid and enable the Undo button.

1. Click Undo. The CM Clear Undo form displays.

1. Click OK.

The system resets all cleared entries matching the transaction types you selected to "outstanding"; that is, sets the Cleared checkbox to unselected. You are returned to the CM Clear Entries form, where you can clear individual entries as needed or use the Initialize feature to clear a specific range of entries.Note: If you used an Auto Clearing File to initialize cleared
 entries and you undo the entries, you cannot reuse the text file again unless you
 reload it.
