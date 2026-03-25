---
title: "Reverse a Prior-Month Payment | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/reverse-a-prior-month-payment"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/reverse-a-prior-month-payment"
---

# Reverse a Prior-Month Payment

You can void a payment in a closed month by reversing the payment in the AP Prior Mth Payment Reversal form.

To reverse a prior-month payment:

1. In the respective fields, for the record you want to reverse, specify the payment method, CM account, check/e-pay number (must be 'outstanding'), and sequence (typically zero).

1. If necessary, in the Pre-Paid Date field, override the default value.

1. If you selected the ePayment or EFT payment method, do one of the following:

- To reverse all payment sequences on the EFT / ePayment transmission, select the Reverse all Seqs checkbox.

- To reverse a single payment sequence on the EFT / ePayment transmission, leave the Reverse all Seqs checkbox unselected and use the EFT Seq # field to enter the payment sequence to reverse (required).

1. If you want the invoice to be payable again, select the Create Open Transaction(s) in Batch Month checkbox. When you post this batch, the system creates a new unpaid transaction.

1. Select Update to pull the transaction into the batch and display the information in the Payment Info section.Note: If you did not select the Create Open Transaction(s) in Batch Month checkbox, the system displays a warning that a reversal batch will be created without open transactions and asks if you want to continue. Only select Yes if you are sure you don't want open transactions created in the reversal batch.

1. Select Post. The AP Batch Process form appears. Proceed with posting as normal. For instructions, see [AP Batch Process Form](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form).

1. If you opted not to immediately repay any portion of what you just reversed, you must determine what followup action you need to take. If the payment you reversed was paid by:

- Check - contact the vendor if the check has already been mailed

- EFT - contact the bank if the file has already been uploaded

- Credit Service - contact your credit service provider if the data file has already uploaded

- ePayments (U.S. only) - log in to your Corpay customer dashboard and cancel the payment(s) that have not already been remitted

Note: Selecting Cancel closes the form but does not remove the selected transaction(s) from the batch. If you want to remove the transaction(s) from the batch, first select Post to open the AP Batch Process form (or open the form from the main menu), and then select File > Clear Batch.

This process only reverses amounts; it does not reverse units. If you did not select the Create Open Transaction(s) in Batch Month checkbox, you may need to edit the reversing transaction and add units or post an adjusting entry in the appropriate subledger.
