---
title: "Auto Reversing Journal Entries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/auto-reversing-journal-entries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/auto-reversing-journal-entries"
---

# Auto Reversing Journal Entries

The GL system includes a feature for processing automatic reversing journal entries.
 To do this, define a journal in GL Journals for accrual entries to be made and and reference another journal (or the same journal) for the automatic reversing entry to be posted in the next (or later) month.
 There are numerous common uses for automatic reversing journal entries. A typical example is if you are using Asset and Liability accounts to record Work in Process and Billings, you may post monthly entries to record income and expenses based on a Percentage of Completion method, using figures from a Work in Process report from Job Cost. These entries may then be automatically reversed in the following month.
 The original accrual entries are made in one month in the GL Journal Transaction Entries program. The reversing entries are made in the following month automatically by running the GL Auto Reversal Entries program. Each entry may be reviewed before posting. An entry may be held and reversed in a later month than the first month following the accrual.
