---
title: "Clear Comdata Credit Service Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-comdata-credit-service-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/reconciliation/clear-comdata-credit-service-payments"
---

#  Clear Comdata Credit Service Payments

If you use Comdata as your credit service provider to pay vendors by credit card, you can use the CM Clear Initialize form to clear a range of credit card payment transactions.
Once you have sent your files to Comdata and received a file back from them, you will need to import and upload your data using Viewpoint's Imports module. You can then use the CM Clear Initialize form to initialize the cleared entries.
Note: The import and upload process requires setting up a template
 for importing Comdata credit service payments (using the CMIMPORTCLEAR import form) in
 IM Template, importing the data into a work file in IM Import, and then uploading
 the work file into the Cleared Entries table (CMCE) in IM Upload.

To initialize cleared credit service payments:

1. Using the AP FTP form, retrieve the AC28 file provided by Comdata to use for reconciliation.

1. Save the AC28 reconciliation file to your desktop or another easily accessed location.

1. In IM Import, [import the AC28 file](/en/vista/vista/administration/imports/processing/about-the-im-import-form) using the COMDATA_R template.

1. In IM Work Edit, verify your imported data is correct and there are no errors.

1. Using the IM Upload form, upload your data to CMCE.

1. Open CM Clear Entries.

1. In the
 CM Account
 field, enter the CM account used to create the credit service file.

1. In the
 Display Through Date
 field, accept the defaulted statement date or enter the date through which to display transactions for the CM account.

1. In the
 Default Date Cleared
 field, enter the cleared date for all transactions being reconciled. Initially defaults the statement date, but if you have items that cleared on different dates, make sure you enter the latest cleared date of the transactions to reconcile.

1. In the Check Items to Display section, select
 Checks/Electronic Payments
 and
 Outstanding Entries
 .

1. Click
 Refresh
 to populate the grid and enable the Initialize button.

1. Click Initialize. The CM Clear Initialize form displays.

1. Select the
 Use Auto-Clearing File
 checkbox.

1. In the
 Upload Date
 field, enter the upload date of the AC28 text file. This will be the date you ran IM Upload.

1. In the
 Clear Outstanding Entries On or Before
 field, enter the date through which to clear entries. The system will mark all entries dated on or before this date as cleared.

1. Click
 OK
 .

Related information

- [About the CM Clear Initialize Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-initialize-form)

- [AP Credit Service Download Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-credit-service-download-form)

- [AP FTP Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-ftp-form)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM Import Form](/en/vista/vista/administration/imports/processing/about-the-im-import-form)

- [About the IM Work Edit Form](/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form)

- [About the IM Upload Form](/en/vista/vista/administration/imports/processing/about-the-im-upload-form)
