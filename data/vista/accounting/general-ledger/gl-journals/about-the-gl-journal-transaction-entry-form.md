---
title: "About the GL Journal Transaction Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-journal-transaction-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-journal-transaction-entry-form"
---

# About the GL Journal Transaction Entry Form

Use the GL Journal Transaction Entry form to enter miscellaneous and adjusting journal entries.
Most General Ledger transactions are created from other sources, such as Accounts Payable, Accounts Receivable, or Payroll, therefore, you should only need to use this program when additional entries are required to make the general ledger reflect the true business picture of the company.
If you are setting up the system during your fiscal year, post the net activity for all
 accounts for each month of the year prior to the month you will begin live processing in
 other applications. Remember to specify the correct month.
Posting may be done in any open month. The maximum number of months allowed open is
 specified in the GL Company Parameters form.

## Transaction Numbers

A unique transaction number is assigned to each journal entry within a period. The
 journal is locked while you are posting to allow it to generate sequential
 transaction numbers within the batch.

## Journals and References

Multiple journals and references may exist in a single batch. All entries within each reference must
 balance (unless the Allow Unbalanced Entries checkbox is marked in the GL Company
 Parameters form).
If you add a transaction back into a
 batch (using GL Add Transaction to Batch) and delete it, you will need to
 delete the Reference number (in GL Journal References) to remove it from the system;
 this is not done automatically.

## Intercompany Journal Entries

If you selected
 the
 Allow
 Intercompany GL Journal Entries
check box in GL Company Parameters, the system enables the
 To
 Co
 field, allowing you to specify which GL company to update with the
 journal entry.For non-intercompany
 journal entries, this company is always the posting company. However, when
 posting intercompany journal transactions, at least one entry must specify the
 posting company as the "to" company, with the offsetting entries made to another
 company.
The journal specified
 for the intercompany entries must be the same in all referenced companies. Although
 you can post to any journal, a suggestion would be to set up a separate intercompany
 journal in each company for which you will be posting intercompany journal
 entries. The reference code must also be the same for the intercompany journal
 entries.
You should not enter
 offsetting intercompany payables and receivables entries. The program will make
 these entries automatically when the batch is posted. In addition, all intercompany
 entries must balance to zero, regardless of how you have set the
 Allow
 Unbalanced Entries
 checkbox in GL Company Parameters.
Note: When processing a batch, the system groups and validates
 manual entries by journal and reference. When entering intercompany journal entries,
 AP and AR distributions are inserted to balance debits and credits between
 companies. All of these entries are assigned a source of GL JrnlXCo in GLDT (GL
 Transaction Detail). Any non-intercompany entries will also be assigned a source of
 GL JrnlXCo. To clearly distinguish intercompany and non-intercompany entries, you
 should use a different journal and/or reference number for non-intercompany entries.
 The system groups non-intercompany entries by group and reference, checks to make
 sure that debits and credits balance, and assigns these entries a source of GL Jrnl
 in GLDT.
In either case, once
 you post the entries they cannot be edited or deleted. If corrections are needed,
 you will need to make additional compensating entries.

## Posting to Memo Accounts

You can use Memo accounts
 to post statistical journal entries; that is, non-financial entries.
 Typically, you will only use memo accounts to track units (e.g. payroll hours) for
 use on financial statements where you want to show both units and dollars. Amounts
 posted to memo accounts are excluded from journal entry balancing and are not included
 in any standard reports.

## Balancing Entries

As you make journal entries in this program, the net totals of the batch, journal,
 and reference are displayed in the non-tab area of the form. Typically, these balances all need to be
 zero to validate and post the batch. You can, however, open and close the batch at
 will, regardless of the balance, until you are ready to post it.
If your balances do not net zero, you can still post the batch by first selecting the Allow Unbalanced Entries checkbox in the GL Company
 Parameters form. However, you should only do this to enable making one-sided entries to balance the GL. Once you make the entries and your GL is balanced, deselect the Allow Unbalanced Entries checkbox.

## Reversing Entries

Although you can add
 existing transactions to a batch for editing/deletion, you cannot use this program to
 edit/delete reversing transactions (i.e. transactions posted via GL Auto Reversal
 Entry).
The following are related topics:
[About the GL Company Parameters Form](/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form)
[Journal References](/en/vista/vista/accounting/general-ledger/gl-journals/journal-references)
