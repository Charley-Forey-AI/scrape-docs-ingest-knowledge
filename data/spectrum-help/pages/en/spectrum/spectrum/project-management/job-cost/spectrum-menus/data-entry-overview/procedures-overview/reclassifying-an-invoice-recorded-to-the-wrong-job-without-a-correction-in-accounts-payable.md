---
title: "Reclassifying an Invoice Recorded to the Wrong Job Without a Correction in Accounts Payable | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/procedures-overview/reclassifying-an-invoice-recorded-to-the-wrong-job-without-a-correction-in-accounts-payable"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/procedures-overview/reclassifying-an-invoice-recorded-to-the-wrong-job-without-a-correction-in-accounts-payable"
---

# Reclassifying an Invoice Recorded to the Wrong Job Without a Correction in Accounts Payable

There are two different methods that may be used to reclassify an invoice recorded to the wrong job. Which option you select is a matter of preference.

## Option A

- This option uses the Job Cost Transaction Entry screen to reclassify the invoice. In this screen you will manually adjust the invoice by applying a negative value to the job to which the invoice was incorrectly applied on line 0001 and then posting the invoice to the correct job on line 0002.

- On the Site Map screen, click Job Cost  >  Data Entry  >  Job Cost Transaction.

- At the Date field, enter the job cost transaction date or press Enter to accept the default job processing date.

- At the Type field, use the drop-down menu to select AP.

- At the Batch code field, press Enter to accept the default batch code.

- At the Vendor code, Job, and Phase fields, enter the applicable codes for the reclassification you are performing, or press F4 or double-click on any of the three fields to select a valid code.

- At the Ct field, enter the appropriate cost type code, or press F4 or double-click on this field to select from a list of available cost type codes.

- At the Invoice date field, today's date defaults. Press Enter to accept this date or press F4 or double-click on this field to select a different date from the Date Change window.

- At the Invoice # field, enter the invoice number for the invoice you are reclassifying.

- At the PO# and Check # fields, enter the purchase order number and check number respectively. If either of these fields are not applicable, leave them blank.

- At the Amount field, enter the invoice amount as a negative value by typing a minus sign preceding the amount and press Enter.

- At the Debit field, enter the G/L account code to which you want to debit the transaction, or press F4 or double-click on this field to search and select a G/L account code.

- At the Credit field, enter the G/L account code to which you want to credit the transaction, or press F4 or double-click on this field to search and select a G/L account code.

- Repeat steps 5 – 12.

- At the Amount field, enter the invoice amount as a positive value and press  Enter.

- Repeat steps 13 and 14.

Once you have completed entering reclassification information in this screen, be sure to click the Cost Updatebutton at the bottom of the screen to run the Cost Transaction Report, which will update the changes throughout the system.

## Option B

This procedure will guide you through reclassifying the invoice directly in the Job Cost History file.

- On the MenuSystem screen, click Job Cost  >  Data Entry  >  History > Reclassification to display the J/C HistoryReclassification screen.

- At the Transaction type field, use the drop-down menu to select AP.

- At the Job number and Phase number fields, enter the appropriate codes for the reclassification you are performing, or press F4 or double-click on any of the three fields to select a valid code.

- In the remaining Selections fields, enter the appropriate cost type, date, and transaction reference information.

- At the Defaults section's Batch code field, press Enter to accept the default batch code.

- In the Debit G/L code and Credit G/L code fields, enter the appropriate G/L account codes for the debits and credits that should applied to the general ledger for the reclassification. Press F4 or double-click on either field to select a valid G/L account code.

- A second screen displays with all selected A/P Job Cost History records. Make the necessary changes to the incorrect transactions.

- Once you have made the necessary corrections, click OK. The Print and UpdateOptions dialog box displays. Select the Print this report checkbox if you want to print the report, otherwise leave the checkbox clear. Click the Edit button if you find you need to make more changes before proceeding. Click OK to proceed with your changes.

- The J/C History Reclass Update screen displays. Select Continue to update your reclassification. Click OK.
Note: You can also choose to cancel or edit your reclassification.

- On the Site Map screen, click Data Entry  >  Job Cost Transaction to display theJob Cost Transaction Entry screen.

- Click the Cost Update button.

- Enter the transaction information in the Selections portion of the screen.

- Select the Format and Sort by options, and then click the Preview or Print button.
