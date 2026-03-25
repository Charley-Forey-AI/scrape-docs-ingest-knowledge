---
title: "Field Definitions: CM Outstanding Entries Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/transaction-entry/about-the-cm-outstanding-entries-form/field-definitions-cm-outstanding-entries-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/transaction-entry/about-the-cm-outstanding-entries-form/field-definitions-cm-outstanding-entries-form"
---

# Field Definitions: CM Outstanding Entries Form

The following is a list of field descriptions for the CM Outstanding Entries form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq #

Enter NEW to create a new entry or enter the batch sequence number of an existing entry you wish to display.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## CM Trans

Display only for existing transactions, blank for new entries. Transaction numbers are assigned to new entries when the batch is posted.

## CM Acct

Enter the CM Account number for this entry. The description displays to the right.

## Type

Specify whether you wish to post cash adjustments, additional outstanding checks, or deposits.

- 0-Adjust

- 1-Check

- 2-Deposit

As you make entries to each of these types, a running total is displayed in the Totals section above the Info/Grid tabs.

## CM Reference

Enter the reference to this transaction, such as check number, deposit number, or other identifying code. Use F4 to see a list of valid reference numbers.

## Ref Seq

Enter a reference sequence number to distinguish between entries with the same CM Reference number. Default will be the next available sequence number for this CM reference.
Note: The CM Reference and Reference Seq # must be unique for a given CM account and transaction type.

## Date

Enter the date of this transaction or select the date using the calendar to the right.

## Amount

Enter the transaction amount. Adjustments may be either negative or positive; enter as negative if they represent a decrease to this cash account, or positive if they represent an increase to the cash account.
Enter checks and deposits as positive amounts. Check amounts are assumed to reduce cash and are stored internally as negative values.

## Payee

Enter the payee of the check. Not required.

## Void

Voids do not affect the statement balance, and they are not posted to GL.
Y = Check is void.  N = Check is not void.

## Description

Enter the transaction description, up to 30 characters.

## GL Account

Enter the offset GL account code for this entry. The cash account is automatically debited or credited depending on type and whether a positive or negative amount. The account description displays to the right.

## Tax Code

This field displays for Australian companies (as set up in HQ Company Setup).
Enter a tax code for including bank interest and fees in the appropriate GST amounts. These amounts will be included in GST amounts in HQ BAS Process (GST/PAYG Amounts tab) when this tax code is associated with a BAS reporting item. See [Preparing a Business Activity Statement or Annual Return for GST Reporting](/en/vista/vista/administration/headquarters/australian-setup/business-activity-statements/business-activity-statements-for-gst-reporting) for more information.
Note: The CM account that you specify in the CM Account
 field will override the account that you specified for the tax code in the Credit GL
 Account field (HQ Tax Codes).
