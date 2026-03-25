---
title: "About the CM Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/about-the-cm-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/about-the-cm-purge-form"
---

# About the CM Purge Form

Use the CM Purge form to purge information from any CM data tables to which the current user already has security access.
There are currently two purge options available:

-  Purge Closed Statements and Account Detail

- Purge Auto Clearing File

The Purge Statement and Account Detail for Closed Statement Through  option purges:

- all checks, deposits, transfers, and adjustments (CMDT) that have been reconciled on statements through the date selected

- statement control records (CMST)

- Payment history remains in AP and PR. The system will not purge the last closed statement; only those statements prior to the last closed statement can be purged.

 The Purge Statement and Account Detail for Closed Statement Through  option does NOT purge:

- payment history in AP and PR any statements for a month which is still open in subledgers

- the last closed statement; only those statements prior to the last closed statement can be purgeNote: Purging the Last StatementIf an account is closed and you need to delete the last statement, you may do so by entering a “dummy” statement in CM Statement Control (statement balance must be equal to beginning balance), and purging the last real statement in this program. Then you can delete the “dummy” statement in CM Statement Control and the account in CM Accounts

## About the Purge Auto Clearing File option

The Purge Auto Clearing File option purges imported auto clearing files through a specified date.
The Purge Auto Clearing File option purges:

- any remaining records in the CM Cleared Entries (CMCE) tableNote: This type of record is usually cleared automatically during your normal process of clearing entries. However, some entries are not cleared from the uploaded file if they do not match Vista's record in some way

-  all imported bank files through the specified date
