---
title: "About the GL Auto Journal Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-form"
---

# About the GL Auto Journal Entry Form

Use the GL Auto Journal Entry form to post journal entries predefined in GL Automatic Journal Entry Setup.
Journal entries that lend themselves to this process include recurring entries for a set amount (including 0.00 amount entries used for varying monthly values), an allocation of accounts to other accounts, and recurring journal entries that are to be made for a specific number of months. This program simply automates part of the posting process; nothing happens here that couldn't be done manually in Journal Transaction Entry.

## Initializing Transactions

You must initialize auto entries before editing or posting may take place. If you
 have not initialized entries, the GL Init Auto Jrnl Entries form will display
 automatically after you open the batch. Once you complete initialization, the
 posting form (GL Auto Journal Entry) is displayed. If you wish to initialize
 additional entries after the batch is opened, you can do so by selecting the
 Initialize Entries option from the File menu.

## Editing Transactions

Transactions may be changed or deleted on the GL Auto Journal Entry form, as
 required, before the batch is validated and the entries are posted to the General
 Ledger.

## Intercompany Journal Entries

f you allow posting intercompany journal entries (flag in GL Company Parameters), the
 ‘To Co’ input is enabled, allowing you to specify the GL company to update with the
 journal entry. The ‘post to’ company automatically defaults as set up for the
 intercompany entries, which you may override as necessary; however, you must have at
 least one entry specifying the posting company as the 'to' company, with the
 offsetting entries made to another company. The journal specified for the
 intercompany entries must be the same in all referenced companies, as must the
 reference code. Note: Intercompany journal entries are all assigned a source of 'GL
 JrnlXCo' in GLDT (Transaction Detail). Once posted, these entries cannot be
 edited or deleted. If corrections are needed, you will need to make additional
 compensating entries.

## Posting Transactions

When the transactions for this batch have been verified and edited as required,
 select Batch Process from the File menu to post entries in the batch.Note: Memo
 accounts are not included in the balance check and therefore, will not prevent
 the batch from being posted if they are not in balance (i.e. do not net to
 zero); however, all other accounts must net to zero in order for the batch to be
 processed.

For information about initializing auto journal entries, see [About the GL Init Auto Jrnl Entries Form](/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-init-auto-jrnl-entries-form)
