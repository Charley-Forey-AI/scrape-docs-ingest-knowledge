---
title: "Set up the EFT Process | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/set-up-the-eft-process"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/set-up-the-eft-process"
---

# Set up the EFT Process

An overview of the EFT setup process.
 The electronic funds transfer (EFT) feature provides
 the ability to transmit payments from your bank directly to your vendor’s bank. Vista
 generates EFT data files that are formatted based on the rules and regulations of the
 destination payment association:

- United States - Automated Clearing House (ACH)

- Australia - Australian Payments Clearing Association
 (APCA)

- Canada - Canadian Payments Association (CPA)

The following instructions provide an overview of setting up the EFT
 process.

1. Establish as agreement with your bank on its rules, specifications, and method for transferring the payment electronically. Expect them to require a file and possibly a test file. They must also define whether they automatically debit your bank account or require both the debit and credit account data in the download file.

1. In the CM Accounts form, enter bank and EFT information as applicable.Note: The fields provided for entering EFT information
 will differ depending on the country. For the United
 States only: If your bank requires both debit and credit account
 information for each EFT, enter information in the following fields:
 Routing Transit #,
 Bank Account #, and
 Account
 Type.

1. The Service
 Class field determines the download
 file format.

- If the file contains a mix of debit and
 credit account data, enter 200 and enter the routing transit number,
 account number, and account type for the bank
 account that will be debited for the amount of the
 EFT.

- If the file contains transmission of credits only, enter 220.

1. In AP Company
 Parameters, [set payment report information](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information) for EFT
 remittances. Optionally, you can also set up information in this form to attach
 payment information to payment history records. If you want EFT data files stored in a secure network location, you can also
 specify a secure file path in this form. For more information, see [Secure EFT Data Files](/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/set-up-the-eft-process/secure-eft-data-files).

1. Set the vendor for the
 EFT payment method. See [Setting the Vendor's Payment Method: US and
 Canada](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-the-vendors-payment-method-u.s.-and-canada) or [Setting the Vendor's Payment Method: Australia](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-the-vendors-payment-method-australia#ID-00051bf6--en__ID-00051bf6) for more information.


1. Vendors who agree to
 receive EFT payments may have to go through a prenote process for your bank in
 order to validate their bank account information. If this is the case, see [Process EFT Prenotes](/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/process-eft-prenotes).

You are now ready to process EFTs. See [Generate the EFT File](/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts/generate-the-eft-file) for more information.
