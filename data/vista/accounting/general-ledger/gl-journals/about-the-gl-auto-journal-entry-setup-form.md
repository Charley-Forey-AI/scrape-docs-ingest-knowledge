---
title: "About the GL Auto Journal Entry Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-setup-form"
---

# About the GL Auto Journal Entry Setup Form

Use the GL Auto Journal Entry Setup form to set up recurring journal entries that may be run monthly in GL Auto Journal Entry.
Recurring entries may be set up to post
 fixed amounts, to post amounts calculated based on percentage or ratios of other
 amounts, or to post calculated totals. Multiple sequences may be used to calculate
 interim totals to be used in later sequences as the basis. Journal entries may be based
 on monthly or year-to-date totals and balances.
Note: When setting up auto journal entries, it is
 important that you set them up in a way to ensure the auto journal process will create
 balanced entries.

## Typical Uses

You can use auto journal entries to post depreciation, expense monthly prepaids, or
 automatically allocate overhead expenses.

- To expense prepaids monthly,
 calculate the monthly expense and set up the journal entry to debit the
 expense account and credit the prepaid account for a specified amount and
 length of time.

- Set up entries to automatically
 allocate overhead expenses based on a calculation of other accounts, such as
 sales by region.

## Entry and Sequence Numbers

An entry number should be thought of as a specific journal entry
 made up of balanced debit and credit transactions.
The sequence is the order in which the computer will process these
 items. Interim totals may be accumulated and the sequence may be significant in that
 totals must be accumulated before allocations or journal postings are made.

## Allocation Types

Allocation types allow you to identify how to allocate the
 transaction.
You may allocate by percent, ratio, or a
 fixed amount.

- Percent - Use this option to
 post a percentage of an account or total.

- Ratio - Use this option to post
 a percentage of an account or total, based on the ratio between two accounts
 and/or totals.

- Fixed Amount - Use this option
 to post a fixed amount.

You can use these allocation types
 either singly or combined to accommodate both simple and intricate entries. You can
 base the entry on fixed amounts, account balances, and/or previous totals in the
 entry.

## Using Total #s

Total #s are uniquely identified by numbers from 1 to 255 and may
 be referenced by more than one entry/sequence.
You can set up various total #s to use
 within a posting period.
To accumulate amounts to a total #,
 define the Allocation Type and value (percent, ratio, or fixed amount), the
 accumulation Source (GL Account), and the Post To Total number (1-255). Be aware
 that you can use the same Total # for all Entry/Sequences until you validate and
 post the batch, so if you do not wish to accumulate totals in this manner, use a
 numbering system for Total #s that keeps them separate. The total number can then be
 referenced in later sequences.
Using this feature, you can create
 complex sequences to calculate journal entries if you desire.

## Intercompany Journal Entries

If you allow posting intercompany journal entries (flag in GL Company Parameters),
 you can set up recurring cross-company transactions here.
You will need to set up one entry
 designating the posting company as the ‘to’ GL Co#, and then set up the offsetting
 entry for the ‘post to’ company.
The journal specified for the
 intercompany entries must be the same in all referenced companies. Although you can
 post to any journal, a suggestion would be to set up a separate intercompany journal
 in each company for which you will be posting intercompany journal entries. The
 reference code must also be the same for the intercompany journal entries.
Do not enter offsetting intercompany
 payables and receivables entries; the posting program (GL Auto Journal Entry) will
 make these entries automatically when you post the batch. In addition, all
 intercompany entries must balance to zero, regardless of how you have set the
 Allow
 Unbalanced Entries option in GL Company Parameters.
Intercompany journal entries will be
 assigned a source of GL
 JrnlXCo in GLDT (Transaction Detail). Once posted, you cannot edit
 or delete these entries. If corrections are needed, you will need to make additional
 compensating entries.
Note: If you do not allow cross-company posting, the
 GL Co# input is disabled and updates will be limited to the active company.
