---
title: "AP 1099 Edit Transactions Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-edit-transactions-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-edit-transactions-form"
---

# AP 1099 Edit Transactions Form

Use the AP 1099 Edit Transactions Form to review a vendor's transactions for a given expense month or paid month and to change the 1099 information as necessary.
Access this form from the AP 1099 Processing form by selecting Tasks > Edit Transactions.
1099 information is defined when a transaction is posted to the vendor in AP Transaction Entry and/or AP Recurring Invoices. If you have not yet paid the invoice and the month in which the transaction was posted is still open, you can edit the 1099 information in the posting form. However, once you pay the invoice and/or the month is closed, any changes to the 1099 information must be made in this form.
Once you enter the year-end month, you must specify whether to select transaction by expense month or paid month. The Expense Month field (default) toggles to Paid Month once you select the Select by Paid Mth checkbox. Selecting Refresh displays all valid transactions for the vendor in the transaction grid. Transactions that are currently in a batch do not appear in the grid.
The display-only information shown for each transaction includes the transaction number, the AP Reference number, the invoice date, and the amount paid against the invoice (if any). If a paid amount is shown, the Multi Pay checkbox indicates whether the payment was made by more than one check.
The 1099 information shown for each transaction is the only information that can be edited in this form.

- 1099 – Select this checkbox to include the transaction amount in the vendor's year-to-date 1099 amount. If not selected, the transaction amount is excluded from the vendor's year-to-date 1099 amount.

- Type – Use to identify the transaction's 1099 type. If you are accumulating amounts for filing purposes via Aatrix, use 1099 types MISC, DIV, NEC, or INT, as only totals accumulated under these types are included. If you will be generating your 1099 e-file in Vista and then saving it locally, only totals accumulated under the 1099 type NEC are included.

- Box # – Use to specify the 1099 box in which the total should be accumulated. Press F4 to select from a list.

All your changes are saved automatically when you close the form.
Note: When processing 1099s, the form type determines what application you must use. If you need to e-file and/or print Forms 1099-MISC, DIV, or INT, you must use Aatrix. If you need to e-file Form 1099-NEC, you can use Aatrix or Vista; however, if using Vista, you can only generate the e-file and save it locally for submission to the IRS.
