---
title: "Void Payments in an Open Month | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-payments-in-an-open-month"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-payments-in-an-open-month"
---

# Void Payments in an Open Month

You can void any type of payment, even if fully processed, as long as the month is still open.

If you are about to void a payment made using ePayments, you must first confirm that the payment hasn't already been remitted by Corpay. To do this, log in to your Corpay customer dashboard.
If you need to [void a payment in a closed month](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/reverse-a-prior-month-payment), use AP Prior Mth Payment Reversal. To [void payments that have not yet been posted,](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-unposted-payment-records) use the AP Payment Posting form.

1. From the main menu, select Accounts Payable > Programs > AP Void Payments.

1. From the Payment Method drop-down, select a payment method by which to filter payments to void.

- N - ePayments

- C - Check

- E - EFT

- S - Credit Service

Leave the Payment Method drop-down blank to include all payment methods.

1. In the CM Account field, enter the CM account by which to filter payments to void or press F4 to select from a list of valid accounts.If not filtering by CM account, leave this field blank.

1. In the CM Reference field, enter the CM reference number by which to filter payments to void. Press F4 to select from a list of valid CM references for the batch month.If not filtering by CM reference number, leave this field blank.

1. In the Batch # field, enter the original posting batch number by which to filter payments to void or press F4 to select from a list of valid batch numbers for the specified batch month (that is, the batch month you specified for this void payments batch).If not filtering by batch number, leave this field blank.

1. Select Fill Grid.The system populates the Eligible To Void grid with all payments meeting the filter criteria.

1. Select the Void checkbox for each payment in the grid you want to void.

1. In the Action field, specify how to handle CM Reference numbers for the voided payments.

- Void - Select to void the CM reference numbers of the selected payment transactions. When you post the void payments batch, the system records the reference numbers in both CM and AP Payment History as voided and makes them unavailable for reuse.

- Clear - Select to allow reusing the reference numbers of the selected invoices/transactions. When you post the void payments batch, the system clears the reference numbers from both CM and AP Payment History so they can be reused later.

1. In the Void Memo field, enter additional information about this void payment batch. This memo will be applied to all voided transactions in this batch.

1. Select Update Batch.A message displays indicating how many payments were added to the void batch and those payments appear in the Payment Batch grid.

1. Review all payments in the Payment Batch grid. To remove a payment from the grid, select the Remove checkbox next to that payment and select Update Batch. The selected payment is removed from the payment batch and placed back in the Eligible To Void grid.Note: You can also use the Remove option if you determine that the Action (Void or Clear) is incorrect for a transaction. Once you remove the transaction from the payment batch, you can then select that transaction in the upper grid, change the Action, and then select Update Batch.

1. When have completed your review and are ready to process the voided payments, select Post Batch.The AP Batch Process form displays.

1. Validate and process the batch.

 Once the batch process is complete, the system either flags the payment number(s) as Void (if not reusing check numbers) or removes the payment number(s) from the CM and AP Payment History files (if reusing check numbers). In either case, the previously paid transactions are then reopened and payable, and paid amounts and discounts are reinstated on vendors' totals. New transactions are automatically posted to GL to adjust the Cash, Discounts Taken, and AP accounts.
 Take any follow up action required by your circumstances. If any portion of the payment you just voided was paid by:

- ePayment (U.S. only) - Log in to your Corpay customer dashboard and cancel the payment(s) that have not already been remitted.

- Check - Contact the vendor if the check has already been mailed.

- EFT - Contact the bank if the file has already been uploaded.

- Credit Service - Contact your credit service provider if the data file has already been uploaded.
