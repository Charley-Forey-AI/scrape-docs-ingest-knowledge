---
title: "Add Invoices to a Batch Using AP Payment Workfile | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-batch-using-ap-payment-workfile"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-invoices-to-a-batch-using-ap-payment-workfile"
---

# Add Invoices to a Batch Using AP Payment Workfile

You can add invoices in a payment workfile to a payment batch for posting.
Once you add transactions to the AP Payment Workfile form, you can select the transactions that you want to add to a payment batch. For each transaction that you want to add to the batch, you must specify that the transaction is ready for payment, and release any hold codes that are preventing the transaction from being paid.Note: You can only release non-retainage holds using this form. To release retainage holds, use the AP Release Retainage form. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice#task-2209--en__task-2209).

1. In the AP Payment Workfile form, select a transaction to add to the batch.

1. Release non-retainage hold codes as needed. For more information, see [Release Hold Codes in AP Payment Workfile](/en/vista/vista/accounting/accounts-payable/payments/invoicetransaction-holds/release-hold-codes-in-ap-payment-workfile#task-6664--en__task-6664).

1. For N-Viewpoint, C-Check, and E-EFT pay methods only, if you want to generate a separate payment for this transaction, select the Separate Pay checkbox. If you do not select this checkbox, the system will group this transaction with other transactions for the vendor into one payment.Note: Invoices with a payment method of S-Credit Service for the same vendor will be grouped into a single payment sequence.

1. If you are ready to pay the transaction, select the Pay checkbox. This step may be unnecessary if you selected the Initialize to be Paid checkbox when you first added transactions to the workfile. When you select this checkbox, the system automatically selects the Pay checkbox for each associated line item. If there's a specific line item you do not want to make a payment for, clear its Pay checkbox.
Note: If there are hold codes associated with this transaction that have not been released, the system displays a warning and prevents you from selecting this checkbox.

1. Add additional transactions to the batch as needed.

1. Click Create Payment Batch.The system displays the Batch Selection form.

1. Choose to create a new batch or use an existing one and click OK.

 The system displays the AP Payment Posting form, which lists all transactions you marked for payment in the payment workfile.Note: Some things to keep in mind:

- Transactions not marked for payment are cleared from the workfile at the point that you proceed with adding your chosen invoices to a batch.

- Transactions that you marked for payment that would have resulted in a negative payment remain in the workfile. The system does not add them to the batch.

- Any credit service invoices that have a different CM account than the one specified in the AP Company Parameters form (CM Acct field, Payment Services tab) will not be added to the payment batch.

- If you are using Comdata as your credit service provider, and you have not specified an email address in the Payment Service Email field in the AP Vendors form (Payment Method tab), the system will not add invoices/transactions for the vendor to the payment batch.

- All invoices with a payment method of Credit Service for the same vendor will be grouped together into a single payment sequence, regardless of whether you selected the Separate Payment checkbox during invoice entry or their addresses differ.

- Invoices with payment method of either Check or EFT that reference the credit service CM account number (CM Acct field in the AP Company Parameters form, Payment Services tab) will not be added to the batch.
