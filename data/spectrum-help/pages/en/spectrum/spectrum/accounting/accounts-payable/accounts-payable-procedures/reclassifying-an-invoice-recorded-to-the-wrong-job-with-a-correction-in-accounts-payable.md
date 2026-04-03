---
title: "Reclassifying an Invoice Recorded to the Wrong Job with a Correction in Accounts Payable | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/reclassifying-an-invoice-recorded-to-the-wrong-job-with-a-correction-in-accounts-payable"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/reclassifying-an-invoice-recorded-to-the-wrong-job-with-a-correction-in-accounts-payable"
---

# Reclassifying an Invoice Recorded to the Wrong Job with a Correction in Accounts Payable

There are two different methods that may be used to reclassify an invoice recorded to the wrong job which will also show the correction in Accounts Payable. Which option you select is a matter of preference.
Note: Both of these procedures are performed in the Job Cost
 module.

## Option A

This option uses the Job Cost Transaction Entry screen to reclassify the invoice. In this screen you will manually adjust the invoice by applying a negative value to the job to which the invoice was incorrectly applied on line 0001 and then posting the invoice to the correct job on line 0002.

1. On the Site Map, click Job Cost  >  Data Entry  >  Job Cost Transaction .

1. At the Date field, enter the job cost transaction date
 or press Enter to accept the default job processing
 date.

1. At the Type field, use the drop-down menu to select
 AP.

1. At the Batch code field, press
 Enter to accept the default batch code.

1. At the Vendor, Job, and
 Phase fields, enter the appropriate codes for the
 reclassification you are performing, or press F4 at
 any of the three fields to search and select a valid code.

1. At the Ct field, enter the appropriate cost type code
 or press F4 to search and select a cost type
 code.

1. At the Invoice date field, today's date defaults. Press
 Enter to accept this date or press
 F4 to select a different date from the
 Date Change window.

1. At the Invoice # field, enter the invoice number for
 the invoice you are reclassifying.

1. At the PO# and Check # fields,
 enter the purchase order number and check number respectively. If either of
 these fields are not applicable, leave them blank.

1. At the Amount field, enter the invoice amount as a
 negative value by typing a minus sign preceding the amount and press
 Enter.

1. At the Debit field, enter the G/L account code to which
 you want to debit the transaction or press F4 to
 search and select a G/L account code.

1. At the Credit field, enter the G/L account code to
 which you want to credit the transaction or press F4
 to search and select a G/L account code.

1. Repeat steps 5 – 12.

1. At the Amount field, enter the invoice amount as a
 positive value and press Enter.

1. Repeat steps 13 and 14.
Once you have completed entering reclassification information in this screen,
 be sure to click the Cost Update button at the bottom
 of the screen to run the Cost Transaction Report,
 which will update the changes throughout the software.

## Option B

This procedure will guide you through reclassifying the invoice directly in the Job Cost History file.

1. On the Site Map, click Job Cost  >  Data Entry  >  History
 Reclassification.

1. At the Transaction type field, use the drop-down menu
 to select AP.

1. At the Job number and Phase
 number fields, enter the appropriate codes for the
 reclassification you are performing, or press F4 at
 any of the three fields to search and select a valid code.

1. In the remaining Selections fields, enter the
 appropriate cost type, date, and transaction reference information.

1. In the Defaults section, at the Batch
 code field press Enter to accept the
 default batch code.

1. In the Debit G/L code and Credit G/L
 code fields, enter the appropriate G/L account codes for the
 debits and credits that should applied to the general ledger for the
 reclassification. Press F4 at either field to search
 and select a valid G/L account code.

1. A second screen displays with all selected A/P Job Cost
 History records. Make the necessary changes to the incorrect
 transactions.

1. Once you have made the necessary corrections, click OK.
 The Print and Update Options dialog box displays.
 Select the Print this report checkbox if you want to
 print the report, otherwise leave the checkbox clear. Click the
 Edit button if you find you need to make more
 changes before proceeding. Click OK to proceed with
 your changes.

1. The J/C History Reclass Update screen displays. Select
 Continue to update your reclassification. Click
 OK.
Note: You can also choose to cancel or edit your
 reclassification.

1. On the Site Map, click Data Entry  >  Job Cost
 Transaction.

1. Click the Cost Update button.

1. Enter the transaction information in the Selections
 portion of the screen.

1. Select the Format and Sort by
 options, and then click the Preview button.
