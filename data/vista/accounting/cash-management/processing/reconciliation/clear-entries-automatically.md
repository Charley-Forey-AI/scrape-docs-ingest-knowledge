---
title: "Clear Entries Automatically | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-entries-automatically"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-entries-automatically"
---

# Clear Entries Automatically

If you regularly receive a text file from your bank that contains all transactions that have been cleared by the bank, then you may use that file to clear entries.
The auto clearing file must have the Bank Account Number, Check Number, and Amount. It may optionally include the Date Cleared.
In order to use this feature, the Cleared Entries table (CMCE) must be populated with the data from the text file. You can import your data using Viewpoint's Imports module. This requires setting up an import template using the CMIMPORTCLEAR Import Form (in IM Template Header) , importing the data into a work file (in IM Import), and then uploading the work file into CMCE (in IM Upload). See [IM Template ](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form), [IM Import,](/en/vista/vista/administration/imports/processing/about-the-im-import-form) and [IM Upload](/en/vista/vista/administration/imports/processing/about-the-im-upload-form) for more information.

Once you have uploaded the data, you can then use the CM Clear Initialize form to initialize the cleared entries. Successfully cleared entries will be deleted from the CMCE table. Transactions in this table with invalid checks, wrong amounts, or any other errors will not be cleared. A report can be printed after the initialization to display any errors found; these can then be cleared manually on the main Clear Entries screen.
 To initialize cleared entries using an auto-clearing file:

1. Open CM Clear Entries.

1. In the
 CM
 Account
 field, enter the CM account for which to clear entries or press

 F4
 to select from a list of valid accounts.

1. In the
 Display Through Date
 field, accept the defaulted statement date or enter the date through which to display transactions for the CM account.

1. In the
 Default Date Cleared
 field, enter the cleared date for all transactions being reconciled. Initially defaults the statement date, but if you have items that cleared on different dates, make sure you enter the latest cleared date of the transactions to reconcile.

1. In the Check Items to Display section, select one or more of the following transaction types to clear: Checks/Electronic Payments , Deposits, Adjustments, and Transfers.Note: Although these transaction types control what items display in the grid, they also are used to designate what items you want cleared. You must select one or more transaction types in order to use the Initialize feature.

1. In the Check Items to Display section, select the
 Cleared Entries
 checkbox. This allow you to see the cleared entries after you initialize them.

1. Click
 Refresh
 to populate the grid and enable the Initialize button.

1. Click Initialize. The CM Clear Initialize form displays.

1. Select the Use Auto-Clearing File checkbox. In the Upload Date field, enter the upload date of the text file to initialize or press F4 to select from a list of upload dates.

1. In the the Clear Outstanding Entries On or Before field, enter the date through which to clear entries. The system will mark all entries dated on or before this date as cleared.

1. Click
 OK.

Related information

- [Clear CM Entries](/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-cm-entries)

- [Reset Cleared Entries](/en/vista/vista/accounting/cash-management/processing/reconciliation/reset-cleared-entries)

- [About the CM Clear Initialize Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-initialize-form)

- [About the CM Clear Entries Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-entries-form)

- [About the CM Clear Undo Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-undo-form)
