---
title: "Add Multiple Invoices to the Payment Workfile | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-the-payment-workfile/add-multiple-invoices-to-the-payment-workfile"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-the-payment-workfile/add-multiple-invoices-to-the-payment-workfile"
---

# Add Multiple Invoices to the Payment Workfile

You can add invoices to the payment workfile by initializing a group of invoices at one time.
When using AP Payment Workfile to add multiple invoices to the workfile, you can add as many payable transactions as you want, or you can tailor the process so that the system only selects a few, specific transactions for initialization. You can restrict by CM account, vendor, AP reference number, job, payment control code, and/or payable type. You can also restrict initialization to include/exclude transactions that are on hold, transactions to be paid by check and/or EFT, and transactions with a due date equal to or less than the cut-off date you specify.

1. In the Payment Selection Criteria section of the form, use any combination of the fields to create a transaction filter. Refer to the F1 help for more information on how each field functions.

1. Select the Initialize to be Paid  checkbox to flag transactions as ready for payment when they display in the workfile.Note: When you select this checkbox, the system selects
 the Pay checkbox for each transaction as long as the transaction’s due
 date is equal to or less than the cut-off date that you specified in the
 Cutoff Date fields, and that the transaction is in compliance.
 For more information, refer to the [F1 help](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-workfile-form/field-definitions-ap-payment-workfile-form#ID-00006823--en).

1. Select Fill Grid.The system initializes all transactions and lines to the workfile grids
 in the header/detail section of the form.
Note: The If Available, Use Discount
 Date and Cancel if Discount Date is Prior
 To fields determine whether the system includes or cancels
 discounts for the initialized transactions. For more information, see [Adding Invoices with Discounts to a Payment
 Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).

You can now add transactions one at a time to the grid (as necessary), and/or edit transaction and line information.
Once you're ready, create a payment batch.

Related information

- [Create a Released Retainage Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/retainage/create-a-released-retainage-payment-workfile)
