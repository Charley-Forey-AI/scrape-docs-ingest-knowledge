---
title: "Generate and Upload an ePayments Data File | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/generate-and-upload-an-epayments-data-file"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/generate-and-upload-an-epayments-data-file"
---

# Generate and Upload an ePayments Data File

Generate the ePayments data file and upload it to Corpay.
Before generating and uploading the ePayments file, you must do the following:

- Enroll with Corpay, who receives each of your file uploads.

- Set up the credentials provided by Corpay in the AP Company Parameters form (Payment Services tab).

- Set up URLs provided by Corpay in the the VA Site Settings form.

Note: If you are not set up correctly for ePayments, when you try to upload/export payments, the system displays a message that it cannot upload because the ePayments setup may not be correct, and indicating that you may need to contact Corpay Support for assistance.

For more information, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

This task only covers the steps to generate the ePayments data file and upload it to Corpay. These steps are only a part of the larger payment process, which is described in [Post and Process Payments](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/post-and-process-payments).Watch how to set up and use ePayments.
Note: You must use a browser on your local computer to view this video, and not a browser in the cloud. If you are currently using a cloud-based browser, copy this page's URL and paste it into a web browser on your local computer.

Note: Nvoicepay changed its name to Corpay; therefore, any mention of Nvoicepay in this video refers to Corpay.

1. In the AP Payment Posting form, select Tasks > Generate ePayments Export.

1. Enter the information as needed in the CM Account, CM Reference #, Date, Time, and Effective Date fields.If you want separate CM reference numbers assigned to each payment in the file, select the Use multiple CM Reference #s checkbox. This toggles the CM Reference # field to Starting CM Reference # so that you can enter a starting reference number. For more information, see the F1 help for these fields.

1. (Optional) In each of the Description and Download Filename fields, press F1 for information about changing the default entries.

1. Select Initialize to generate the data file.Important: The system provides the option to preview a report of the information contained in the file. If you select No, you will not have another chance to view the report unless you either add more transactions or cancel and start over with the data file creation process.

1. (Optional) In the CM Account field, enter a different account and select Initialize again. Repeat as needed for each CM account you want invoices to be included for in this ePayments data file.Important: If at any point your entry in the CM Account field happens to be a credit service CM account, the system enables the Credit Service CM Account Overwrite field as an option to pay from a different CM account than what was originally intended. If you take this option, your accounts may require a journal entry to account for the difference. In most cases, you should not take this option and simply re-enter the same CM account as is in the CM Account field.

1. Select Upload.The system automatically uploads your file to Corpay and displays a confirmation message.

1. Select Close.If you are using the Secure File Path option (in AP Company Parameters), the system automatically saves your file to the specified secure location.If you are not using the Secure File Path option in AP Company Parameters, the "Save Export File As" window displays.

1. From the "Save Export File As" window, select the location where you want the XML file saved and select OK.Note: If desired, you can change the default file name.

A message displays indicating the file was saved successfully and prompting you to process the payment batch.

1. Proceed with posting the batch.Important:You must proceed with the posting process.  You have created and sent the electronic data file, and Corpay pays your vendors without a delay. You must move these transactions from 'payables' to 'paid', and to do this, you must post the payment batch. If needed, see [AP Payment Posting](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form).

At any time after one or more vendor payments from this ePayments file have been completed, Corpay will begin making payment information available to you. See the [ePayments](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-history-form/field-definitions-ap-payment-history-form#ID-000062ba--en__ID-000062ba) Help from the AP Payment History form for details.
