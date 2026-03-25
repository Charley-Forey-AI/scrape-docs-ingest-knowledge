---
title: "Field Definitions: GL Journal Transaction Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-journal-transaction-entry-form/field-definitions-gl-journal-transaction-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-journal-transaction-entry-form/field-definitions-gl-journal-transaction-entry-form"
---

# Field Definitions: GL Journal Transaction Entry Form

The following is a list of field descriptions for the GL
 Journal Transaction Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter N, New, or + to create a new transaction, or enter the batch sequence number of an existing transaction that you wish to display.

##  Date

 Enter the date of the transactions posted in this session.

##  To Co

 Enabled only if allowing intercompany journal entries (flag in GL Company Parameters).
 Specify the company that will be updated with this journal entry.
 For intercompany journal entries, this company must be the same as the posting company for at least one entry. Offsetting entries must be posted to a different company.

##  Journal

 Specify the journal (set up in GL Journals) to which this entry will be posted.
 For intercompany journal entries, this journal must be the same in all specified companies. A suggestion would be to have a separate 'intercompany journal' set up in each company for which you will be posting intercompany journal entries.

##  Reference

 Enter a reference code for this transaction, up to 10 characters, or press F4 to select from a list of pre-defined reference codes (set up in GL Journal References). For intercompany journal entries, this code must be the same for all entries.
 References allow you to group related journal entries together. All entries sharing the same reference within a journal and month must balance.
Note: References will not be validated, but will be added as the entries are posted to GL.

##  Description

 Enter a description of the journal entry, up to 60 characters. Initially defaults the reference description for the month, journal and reference code, if one exists. Otherwise, defaults as null.
Note: If more space is needed for a description or details on this journal entry, you might consider using the Notes tab of GL Journal References for the journal reference specified in the Reference field above.

##  GL Account

 Specify the GL account (set up in GL Chart of Accounts) that this transaction will update.
Note: If you are tracking units, such as payroll hours, you can specify a memo account here. However, be aware that amounts posted to memo accounts will not be included in journal balancing, nor will they be included in any standard reports.

##  Amount

 Enter the amount of this transaction.

##  Dr/Cr

 Indicate whether this transaction will debit (Dr) or credit (Cr) the specified GL account.

- Debit = D, 1, or +

- Credit = C, 2, or -

##  Adj Pd Entries

 Display only, indicating whether the entry is an adjusting entry.
 Adjusting entries can only be made in the last month of the fiscal year and if the Adjustment Period Entries option was checked when you created the batch (in the Batch Selection form).
 If the Adjustment Period Entries option was checked, all entries in the batch will be adjusting entries. If it was not checked, none of the entries in the batch will be adjusting entries.
