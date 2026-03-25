---
title: "AP 1099 Processing Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-processing-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-processing-form"
---

# AP 1099 Processing Form

Use the AP 1099 Processing form to maintain 1099 totals by vendor, calendar year, and 1099 type in preparation for processing.

The system accumulates 1099 amounts automatically as transactions are paid. With this form you can:

- Edit 1099 totals manually

- Manually update 1099 information on vendors for invoices paid prior to going live on the system.

Although 1099 amounts are normally accumulated to the 1099 Type and Box # specified for each vendor in the AP Vendors form, you can accumulate 1099 amounts to whatever 1099 Type and Box # is appropriate for each transaction by overriding 1099 defaults during transaction entry in the AP Transaction Entry and/or AP Recurring Invoices forms.
The description/label for each field on this form changes depending on the 1099 type selected.
Note: If you need to enter data that will print in Box 7 of the 1099-DIV and 1099-Int forms (Copy B and Copy C), use the Div or Int Box 7 field. (The Box 7 Total field is disabled for both DIV and INT 1099 types.)
If you need to edit 1099 information for transactions, you can do so in the originating transaction entry form, as long as the invoice has not been paid and the month is still open. However, once payment has been made, and/or the month is closed, any changes to the 1099 information must be made in the AP 1099 Edit Transactions Form. You can access AP 1099 Edit Transactions from this form by selecting Tasks > Edit Transactions. For more information, see [AP 1099 Edit Transactions Form](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-edit-transactions-form).

## Printing and Filing 1099s

You can use Aatrix or Vista to print 1099s or generate e-files for submission to the IRS.
 When you are ready to run 1099s, select Tasks > Download to access the AP 1099 Download form. Once you enter the appropriate information, click Launch Aatrix to open the Aatrix application and continue processing your 1099s, or click Download to save your 1099 e-file (NECs only) locally for later submission to the IRS.
You can also print your 1099-NECs from Vista using the AP 1099 NEC Recipient Copies report (available in the AP Reports menu or from the AP 1099 Processing form by selecting Options > Reports > AP 1099 NEC Recipient Copies.
For more information about processing 1099s via Aatrix, see [AP 1099 Aatrix Print and eFile Form](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-aatrix-print-and-efile-form).
If you are using Aatrix and need to make corrections after you have already submitted your 1099s, you must do so directly in Aatrix. For more information, see [Make Corrections to Regulatory Filings via Aatrix](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/make-corrections-to-regulatory-filings-via-aatrix).
If you used Vista to generate and save your 1099-NEC e-files, and have already submitted them to the IRS, any corrections needed must be handled in Aatrix. you cannot make corrections via Vista. For more information, see [Correct 1099-NECs Generated in Vista](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/correct-1099-necs-generated-in-vista).

## 1099-NEC

As of January 2021, the IRS no longer accepts 1099-MISC forms for reporting non-employee compensation (Box 7). Instead, the IRS is requiring the new form 1099-NEC (Box 1).
 For proper tracking, you must assign the NEC type (defined in AP 1099 Types) to applicable transactions during entry in AP Transaction Entry or via the AP 1099 Edit Transactions form. You can also assign the NEC type to vendors in the AP Vendors form to ensure the NEC type defaults for all new transactions.

Related information

- [AP 1099 Edit Transactions Form](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-edit-transactions-form)

- [AP 1099 Download Form](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-download-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)
