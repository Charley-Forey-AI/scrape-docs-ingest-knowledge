---
title: "Add a Single Invoice to a Payment Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-a-single-invoice-to-a-payment-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-a-single-invoice-to-a-payment-batch"
---

# Add a Single Invoice to a Payment Batch

You can add a single invoice to a payment batch using the Initialize New Payment section of the AP Payment Posting form.
To add a single invoice
 to a batch:

1. Open the AP Payment Posting form.

1. In the Seq # field, enter a new sequence number or enter N, New, or + to have the system generate the next available sequence number.

1. In the Initialize New Payment section, use the Month field to enter the invoice expense month.

1. In the AP Trans field, enter the transaction number of the AP invoice or press F4 to select from a list of AP invoices associated with the specified month.

1. Click Initialize.

The system adds the invoice to the batch.Note: If an invoice is missing a CM account, the system displays a
 warning dialog box. Close the dialog and enter a CM account in the CM Acct is missing on the
 transaction... field. Click Re-validate and then click
 Initialize to add
 the invoice to the batch.If you are adding an invoice with
 a payment method of Credit
 Service, the system will not add the invoice if:

- the CM account does not match the entry in the
 CM Acct
 # field in the AP Company Parameters form, Credit
 Services tab.

- you did not enter the required credit service
 provider information in the AP Company Parameters form (Comdata or
 EFS sections of the Credit Services tab).

 Invoices with payment method of either check
 or EFT that reference the credit service CM account number (CM Acct field, AP Company
 Parameters form, Credit Services tab) will not be added to the batch.
 If
 the invoice is “out of compliance,” a warning displays. To add the transaction,
 click Initialize and
 the system adds the invoice to the payment batch. For more information on
 tracking compliance in AP, see [Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking).
