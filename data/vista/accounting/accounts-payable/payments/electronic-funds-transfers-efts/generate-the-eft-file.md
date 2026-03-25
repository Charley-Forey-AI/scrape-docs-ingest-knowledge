---
title: "Generate the EFT File | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/generate-the-eft-file"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/generate-the-eft-file"
---

# Generate the EFT File

To pay a vendor via EFT, you must generate the EFT file and then transmit the data file to your bank.

You must set up the information the system will use to generate EFT files. If you haven't already, see [Set up the EFT Process](/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/set-up-the-eft-process).
Vista generates EFT data files that are formatted based on the rules and regulations of the destination payment association:

- United States - Automated Clearing House (ACH)Note:Vista also adheres to the International ACH Transactions (IAT) form for paying international vendors. For more information, see [Set up Vendors for International Electronic Payments (United States)](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-up-vendors-for-international-electronic-payments-united-states). EFT file features include the use of CCD (Cash Concentration or Disbursement) and CTX (Corporate Text Exchange) standard entry class codes to ensure NACHA (National Automated Clearing House Association) compliance.

- Australia - Australian Payments Clearing Association (APCA)

- Canada - Canadian Payments Association (CPA)

This topic only covers the steps to generate and save the EFT data file and is part of a larger process which is described in [About Adding Invoices with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/about-adding-invoices-with-discounts-to-a-payment-batch).
Note: For the United States only: If you use ePayments to generate and send your AP payment files, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

1. In the AP Payment Posting form, select Tasks > Download EFTs.The AP EFT Download form opens.

1. In the CM Account, CM Reference #, and Effective Date fields, enter the correct information.

1. Optional: In each of the Description and Download Filename fields, press F1 to view important information about changing the default entries.

1. (Australia only) In the File Creation Number field, enter a number that uniquely identifies this file for the bank.

1. Select Initialize.The system updates the records in the batch with the information you specified and provides an opportunity to preview a report of the information downloaded to the data file.Note: If you select No, you will not have another chance to view the download unless you cancel and start over with the file creation process.

1. Select Download.One of two things occurs:

- If you are not using the Secure File Path feature, the Save Export File As window displays and you must choose a location to save the file. You can opt to change the default filename.

- If you are using the Secure File Path function, no Save As window appears, as Vista saves your file directly to the location specified in the AP Company Parameters form.

Note: If you close the AP EFT Download form before selecting Download (for example, changes need to be made to a transaction), you must reload the transactions. To do this, select the Overwrite Existing CM Reference# and Seq# checkbox, choose Initialize again, and proceed as described above.

The EFT file is generated in the background and saved.
You must post the payment batch in the AP Payment Posting form (to move transactions from 'payables' to 'paid') and you must transmit the data file to your bank so the vendor can be paid.

Related concepts

- [Payment Reporting Information](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

Related tasks

- [Send Vendor Payment Information by Email](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/send-vendor-payment-information-by-email)
