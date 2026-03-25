---
title: "Generate Credit Service Files | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/generate-credit-service-files"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/generate-credit-service-files"
---

# Generate Credit Service Files

You can generate credit service files for transmission to a credit service provider.

- [Set up Credit Service provide](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata)r

- [Add payments to a payment batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches)

 After you have set up your credit service provider and added your vendor payment to an AP payment batch, you can pay the vendor by credit card via a credit services provider. You do this by generating a credit service payment request file from AP Payment Posting. The system automatically formats the file to match your credit service provider's rules and regulations. Tip:
 Credit service transactions can exist in a payment batch along with check and EFT
 transactions, but you may find it easier to create a separate payment
 batch.

1. From the AP Payment Posting form, select Tasks > Generate Credit Service Export File.The AP Credit Service Download form displays

1. If you want the system to overwrite the CM reference number for all payment sequences in the batch, select the Reload Credit Service payments checkbox. The system will generate new numbers, starting with the number in the Beginning CM Reference # field and incrementing by one for each payment sequence, assigning only numbers that have not already been used in the system. If you do not select this checkbox, the system will enter a CM reference number only for payment sequences without one.

1. The Beginning CM Reference # field defaults to the next available number. You can override this number if necessary.

1. In the Paid Date field, enter the payment date. This is the date that you authorize the credit service provider to make payment. The field initially defaults to the current date.

1. Click Generate File.The system displays a message stating the number of payments processed.

1. Click Close.The Save Export File As window displays.

1. Save the file to the correct location.A message displays indicating the number of processed transactions.

1. Click Close.

1. If you are using Comdata as your credit service provider, a message displays asking if you want to transfer the generated file to Comdata. Click Yes to automatically transmit the file via FTP to Comdata. Click No if you prefer to transmit the file later via [AP FTP](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-ftp-form).

1. If you are using EPS as your credit service provider, send the file to EFS electronically.

Related information

- [Set up Credit Services with Comdata](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/set-up-credit-services-with-comdata)

- [About Invoice Payment Batches](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP FTP Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-ftp-form)

- [AP Payment Posting Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)
