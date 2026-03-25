---
title: "About Adding Invoices with Discounts to a Payment Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/about-adding-invoices-with-discounts-to-a-payment-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/about-adding-invoices-with-discounts-to-a-payment-batch"
---

# About Adding Invoices with Discounts to a Payment Batch

An overview of how the system handles discounts for Accounts Payable invoices added to a payment batch.
When you add invoices to a payment batch via the AP Payment Workfile or AP Initialize Payments form, how you set the If Available, Use Discount Date and Cancel if Discount Date is Prior To fields determines whether discounts are taken or canceled.
If you select the If Available, Use Discount Date checkbox and you enter a date in

the Cancel if Discount Date is Prior To field, discounts are handled as follows:

- The discount is taken if:

- the discount amount is greater than 0.00

- the discount date is equal to or prior to the cutoff date (Include transactions due as of field)

- the discount date is greater than the cancel date (Cancel if Discount Date is Prior To field)

- The discount is canceled if:

- the discount amount is greater than 0.00

- the discount date is equal to or prior to the cutoff date

- the discount date is less than the cancel date
At this point, the system then compares the due date to the cutoff date. If the due date is equal to or less than the cutoff date, the system adds the invoice to the batch. If the due date is greater than the cutoff date, payment is not due and is not added to the batch.

-
The invoice is added to the batch if:

- the discount amount is 0.00

-  the due date is equal or prior to the cutoff date.
If the due date is greater than the cutoff date, payment is not due and is not added to the batch.

In the AP Payment Workfile form, if you select the Cancel if Discount Date is Prior To checkbox when clearing the workfile, you are given the option to update the transaction to cancel or restore the discount.
