---
title: "Create a Released Retainage Payment Workfile | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/retainage/create-a-released-retainage-payment-workfile"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/retainage/create-a-released-retainage-payment-workfile"
---

# Create a Released Retainage Payment Workfile

You can create a workfile containing only released retainage transactions that are ready for payment using the AP Payment Workfile form.

The following details how to create an 'open retainage only' workfile.
Note: This process works only for retainage released using the AP Release Retainage form.

1. Open the AP Payment Workfile form.

1. In the CM Acct to use if not assigned in the transaction field, enter the appropriate CM account or accept the default.

1.  In the Selection Criteria section, select the Open Retainage only check
 box. Then do one of the following:

- If you want to initialize all available open retainage transactions to the workfile, leave all remaining selection criteria blank.

- If you want to initialize specific open retainage transactions to the workfile, use the remaining selection criteria fields to filter transactions as needed.

1. Use the Payment Methods section to specify the payment methods to include in the workfile.Tip: For ease of use, you might consider using
 a separate workfile for each payment method; however, you can include
 multiple payment methods in the workfile if desired.

1. If applicable, use the Cutoff Date and Discounts
 sections to further restrict transactions added to the workfile.Note: The If
 Available, Use Discount Date and Cancel
 if Discount Date is Prior To fields determine whether
 the system includes or cancels discounts for the initialized
 transactions. For more information, see [Adding Invoices with Discounts to a Payment
 Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).

1. Select the Initialize to be Paid  checkbox to flag transactions as ready for payment when they display in the workfile.Note: When you select this checkbox, the
 system selects the Pay checkbox for
 each transaction in the grid as long as the transaction is in compliance.

1. Click Fill Grid.The system initializes all transactions/lines meeting the specified criteria to the header/detail
grids of the form.

1. If needed, add, [delete](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-the-payment-workfile/remove-transactions-from-the-workfile), and/or [edit](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-the-payment-workfile/edit-payment-workfile-transactions) transactions.

1. Make sure the Pay checkbox is selected for all transactions/lines that are ready for payment and deselected for any transactions/lines that you do not want added to the payment batch.

Once you are ready, create the payment batch.
