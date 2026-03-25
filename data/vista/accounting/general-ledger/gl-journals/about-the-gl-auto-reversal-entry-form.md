---
title: "About the GL Auto Reversal Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-reversal-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-reversal-entry-form"
---

# About the GL Auto Reversal Entry Form

Use the GL Auto Reversal Entry form to automatically post reversing entries for any or all of the transactions that have been posted in a prior month to a journal flagged for reversals.

## Initializing Transactions

You must initialize auto
 reversal entries before editing or posting may take place. If
 you have not initialized entries, the GL Auto Reversal Init form
 will display automatically after you open the batch. Once you
 complete initialization, the posting form (GL Auto Reversal
 Entry) is displayed. If you wish to initialize additional
 entries after the batch is opened, you can do so by selecting
 the Initialize Entries option from the File menu.

## Editing Transactions

All of the transactions
 flagged to be reversed from the specified journal will be listed
 on this screen with their proposed reversing entries. You may
 edit them as necessary before they are posted to the General
 Ledger. As they are posted, the original transaction will be
 flagged as reversed, and the cycle is complete.
To keep a transaction
 from being posted in this batch, use the delete option. Deleting
 a transaction here does not erase it from the file, it just
 removes it from the batch. The next time you specify reversing
 entries from this journal, the transactions that are deleted
 here will appear again to remind you they have not yet been
 reversed.
Note: Once a reversal batch is posted,
 you cannot edit or delete the transactions. If you posted a
 reversal in error, you will need to make new entries (GL Journal
 Transaction Entries) to adjust/correct the error.

## Posting Transactions

When the transactions for
 this batch have been verified and edited as required, select the
 Batch Process option from the File menu to validate and post the
 entries.

## Restrictions

Once a transaction is
 reversed it cannot be called up again for later reversal.
The net journal entry for
 all reversing entries must equal zero.
Note: Memo accounts are not included in
 the balance check and therefore, will not prevent the batch from
 being posted if they are not in balance (i.e. do not net to
 zero); however, all other accounts must net to zero in order for
 the batch to be processed.
