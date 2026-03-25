---
title: "About Invoice Payment Batches | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches"
---

# About Invoice Payment Batches

There are multiple ways to add invoices to a payment batch:

- Using the initialization feature in the AP Initialize
 Payments form.

- Using the Initialize New Payment feature in the AP Payment
 Posting form.

- Manually using the AP Payment Posting form.

- From a payment workfile in the AP Payment Workfile
 form.

Payments in a batch may contain references to multiple bank accounts;
 specifically, invoices in the batch may all be assigned for payment from different CM
 accounts. (CM accounts are assigned to invoices by the user when entering invoices using
 either the AP Transaction Entry or AP Recurring Invoices form.) Although a payment batch
 can contain multiple transactions with different bank accounts, payments can only be
 processed (using either the AP Check Print or AP EFT Download form) for one CM account
 at a time.

## Compliance

You can prevent non-compliant subcontract, purchase order, and/or vendor
 invoices/transactions from being added to payment batches by selecting the appropriate
 options in the AP Company Parameters form. For subcontracts and purchase orders, select
 the Don't add to Payments batch if "out of compliance" checkbox
 in the Audit Options tab. For vendors, select the Don't add vendor to payment
 batch if "out of compliance" checkbox in the Invoice Options tab.
If you normally check compliance, but allow payments to be processed, do not select the
 above options. Use the AP Payment Preview with Compliance report to identify any
 invoices that are out of compliance, along with the related compliance codes. This
 allows you to determine if you want to remove the transaction from the payment batch or
 print a check (perhaps holding the check until compliance is met).

Related concepts

- [About Adding Invoices with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/about-adding-invoices-with-discounts-to-a-payment-batch)

Related tasks

- [Add Multiple Invoices to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-multiple-invoices-to-a-payment-batch)

- [Add a Single Invoice to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-a-single-invoice-to-a-payment-batch)

- [Add Invoices to a Payment Batch Manually](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-payment-batch-manually)

- [Add Invoices to a Batch Using AP Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-batch-using-ap-payment-workfile)

Related information

- [AP Payment Posting Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)

- [AP Payment Workfile Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form)
