---
title: "Field Definitions: GL Auto Journal Entry Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-setup-form/field-definitions-gl-auto-journal-entry-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-setup-form/field-definitions-gl-auto-journal-entry-setup-form"
---

# Field Definitions: GL Auto Journal Entry Setup Form

The following is a list of field descriptions for the GL Auto
 Journal Entry Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Journal

 Enter a valid 2-character journal code (from the GL Journals maintenance form) in which to post this recurring journal entry.

## Entry #

 One entry number will typically include all calculations and transactions, individually set up as sequences, which combine to make equal debit and credit entries representing a single process. For instance, one entry might be to allocate undefined overhead costs back to profit center accounts based on a specified ratio.

## Sequence #

 Enter the sequence (0-255) of this transaction within the journal entry. The system will post the entries in sequential order when the batch is processed.

## Allocation Type

 Select the allocation method for this transaction.

- 1=Percent – Select this option to allocate a fixed percentage (specified below) of an account or a total.

- 2=Ratio – Select this option to allocate a percentage of an account or a total based on the ratio between two accounts and/or totals. Use the Ratio 1 and 2 sections to indicate the accounts and/or totals.

- 3=Fixed Amount – Select this option to post a fixed amount (specified below).

## Percent

 Enabled only when the Allocation Type is ‘Percentage’.
 Specify the percentage to apply (-100 to 100) when calculating the allocation amount for this sequence. If entering a negative value, set the Post As option to ‘Either’ (which allows the entry to be posted as a debit or credit).

## Amount

 Enabled only when the Allocation Type is ‘Fixed Amount’.
 Specify the fixed amount to use when calculating the allocation amount for this sequence.

## Source

 Specify whether the source is an account or a total. (Note: Percent and Ratio allocation types require a source account or a total amount.)

- GL Account – Select this option if the source is a GL account (specified below). The balance of the specified GL account will be used as the basis for calculating this sequence.

- Total – Select this option if the source is a Total number (specified below). Before you can enter a total number, the total must have been established in the ‘Post To’ section of a prior sequence. The total number specified below will be used as the basis for calculating this sequence.

## Source: GL Account

 Specify the source GL account. The balance of this account will be used as the basis for calculating this sequence.

## Source: Basis

 Enabled only when the source is ‘GL Account’.
 Select the basis for the source account.

- M=Month to Date. Select this option to use the month-to-date balance as the basis for calculating this allocation.

- Y=Year to Date. Select this option to use the year-to-date balance as the basis for calculating this allocation.

## Source: Total

 Enabled only when source is ‘Total’.
 Specify the source Total (1–255) for this allocation.

## Post To

 Specify whether to post to an account or a total.

- GL Account – Select this option to post this entry to a GL account (specified below).

- Total – Select this option to post to an intermediate total (specified below).

## Post To: GL Co#

 This field is only accessible if you allow intercompany journal entries (flag in GL Company Parameters).
 Enter the GL company to which this auto journal entry should be posted. Defaults the currently active company.
Note: You will need to set up one entry designating the
 posting company as the ‘to’ GL Co#, and then set up the offsetting entry for the ‘post to’
 company.

## Post To: GL Account

 Enabled only when the Post To option is ‘GL Account’.
 Specify the GL account to which this entry/sequence transaction will be posted.

## Frequency

 Enter a valid frequency code (set up in HQ Frequency Codes) to use when selecting which auto journal entries to post.

## Last Month to Post

 Designate the last month to which this transaction should be posted. Leave blank to post indefinitely.

## Reference

 Enabled only when the Post To option is ‘GL Account’.
 Specify the reference number/code to use when this entry is posted. All entries with the same reference must balance.

## Trans Description

 Enabled only when the Post To option is ‘GL Account’.
 Enter the description, up to 60 characters, of this transaction as it should appear in the journal entry.
Note: If more space is needed for a description or details on this journal entry, you might consider using the Notes tab of GL Journal References for the journal reference specified in the Reference field above.

## Post To: Total

 Enabled only when the Post To option is ‘Total’.
 Specify the Total number (1–255) in which to accumulate this allocation.

## Post As

- Debit – Select this option to post this entry as a debit.

- Credit – Select this option to post this entry as a credit.

- Either – Select this option to post this entry as either a debit or a credit, depending on the result.

## Ratio 1

 Enabled only if the Allocation Type is ‘Ratio’.
 Specify whether the amount for this ratio is based on a GL account balance or a Total number. The system uses the ratio between two accounts and/or totals to calculate a percentage. The amount found in this source will be divided by the amount from the Ratio 2 source (numerator).

- GL Account – Select this option if the first amount is based on a GL account (specified below).

- Total – Select this option if the first amount is based on a Total (specified below).

## Ratio 1: GL Account

 Enabled only if the Allocation Type is ‘Ratio’ and the ratio amount is based on a GL account.
 Specify the first GL account used when calculating the ratio. The balance of this account will be divided by the amount from the Ratio 2 source (numerator).

## Ratio 1: Basis

 Enabled only if the Allocation Type is ‘Ratio’ and the ratio amount is based on a GL account.
 Specify the basis for the account in Ratio 1.

- M=Month to Date. Select this option to use the month-to-date balance of the specified GL account as the basis of Ratio 1.

- Y=Year to Date. Select this option to use the year-to-date balance of the specified GL account as the basis of Ratio 1.

## Ratio 1: Total

 Enabled only if the Allocation Type is ‘Ratio’ and the ratio amount is based on a Total.
 Specify the first Total (1-255) to use when calculating the ratio. This total will be divided by the amount from the Ratio 2 source (numerator).

## Ratio 2

 Enabled only if the Allocation Type is Ratio.
 This is the second source of the ratio. Specify whether the amount for this ratio is based on a GL account balance or a Total number. The amount found in this source will be divided into the amount of Ratio 1 (denominator).

- GL Account – Select this option if the second amount is based on a GL account (specified below).

- Total – Select this option if the second amount is based on a Total (specified below).

## Ratio 2: GL Account

 Enabled only if the Allocation Type is ‘Ratio’ and the ratio amount is based on a GL account.
 Specify the second GL account used when calculating the ratio. The balance of this account will be divided into the amount from the Ratio 1 source (denominator).

## Ratio 2: Total

 Enabled only if the Allocation Type is ‘Ratio’ and the ratio amount is based on a Total.
 Specify the second Total (1-255) to use when calculating the ratio. This total will be divided into the amount from the Ratio 1 source (denominator).

## Ratio 2: Basis

 Enabled only if the Allocation Type is ‘Ratio’ and the ratio amount is based on a GL account.
 Specify the basis for the account in Ratio 2.

- M=Month to Date. Select this option to use the month-to-date balance of the specified GL account as the basis of Ratio 2.

- Y=Year to Date. Select this option to use the year-to-date balance of the specified GL account as the basis of Ratio 2.
