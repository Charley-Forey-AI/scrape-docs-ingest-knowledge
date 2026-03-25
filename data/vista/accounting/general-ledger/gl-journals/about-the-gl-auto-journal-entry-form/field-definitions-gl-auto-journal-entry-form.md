---
title: "Field Definitions: GL Auto Journal Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-form/field-definitions-gl-auto-journal-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-auto-journal-entry-form/field-definitions-gl-auto-journal-entry-form"
---

# Field Definitions: GL Auto Journal Entry Form

The following is a list of field descriptions for the GL Auto
 Journal Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

 This number identifies the order in which each transaction (defined in GL Auto Journal Entry Setup) was added to this batch. This sequence number is not the same as the Auto Entry sequence number shown below.

## Trans Date

 Defaults the transaction date specified during initialization. May be overridden.

## To Co#

 This field is only accessible if you allow intercompany journal entries (flag in GL Company Parameters).
 Defaults the company specified as the ‘post to’ GL company in GL Auto Journal Entry Setup. You may override the default if necessary; however, you must have at least one entry specifying the posting company as the ‘to’ company. Offsetting entries must be posted to a different company.

## Journal

 Defaults the journal to which this entry applies (as defined in GL Auto Journal Entry Setup). May be overridden; however, entry will change the journal to which these transactions have been automatically set up to post.
Note: This journal must be the same in all specified
 companies. A suggestion would be to have a separate 'intercompany journal' set up in each
 company for which you will be posting intercompany journal entries.

## Reference

 Defaults the reference defined for this auto journal entry (in GL Auto Journal Entry Setup). May be overridden; however, the reference code must be the same for all related entries.
Note: References allow you to group related journal entries
 together. All entries sharing the same reference within a journal and month must balance.
 References are not validated, but will be added as the entries are posted to GL.

## Description

 Initially defaults the description from Auto Journal Entry Setup. May be overridden.
Note: This field allows entry of up to 60 characters. If more space is needed for a description or details on this journal entry, you might consider using the Notes tab of GL Journal References for the journal reference specified in the Reference field above.

## GL Account

 The GL Account assigned to this entry in the Auto Journal Entry Setup program.

## Amount

 The transaction amount for this entry, based on the allocation type (percent, ratio, fixed amount) defined in Auto Journal Entry Setup). This field can be edited if desired.
Note: This amount represents the accumulation of actual
 (negative and positive) totals. For example, 3000.00(DR) and ‑1000.00(CR) will produce a
 balance of 2000.00 (3000 + -1000).

## Dr/Cr

 Debit or Credit as assigned to this entry in the Auto Journal Entry Setup program. This field can be edited if desired.
