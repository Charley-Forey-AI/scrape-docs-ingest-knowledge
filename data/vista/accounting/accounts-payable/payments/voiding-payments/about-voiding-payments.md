---
title: "About Voiding Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/about-voiding-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/about-voiding-payments"
---

# About Voiding Payments

You can void payments that you have already posted, as well as those that you have not yet posted.

There are a couple of methods for voiding payments. The method you use depends on the following:

- which form was used to post the payment

- whether the payment batch is posted or unposted

- whether the payment was posted in a prior month (open or closed).

Voiding a payment is a process of registering a specific CM reference number as "used and voided" in the both the AP payment record and the CM module's record.
If you are removing a payment in a current batch or a current month, you may indicate whether the check is to be "voided" or made available to reuse. If flagged as available to reuse, it will not be recorded as void in the Payment files or CM module.

## Prepaid Transactions

Prepaid transactions that have not been posted through the AP prepaid process may have the CM reference number removed and made available for reuse. If the prepaid has been updated, but not posted in the AP Prepaid Process program, it must first be removed from the payment batch. The AP transaction may then be added to an AP transaction batch and the prepaid payment removed.

## Manual/Computer Checks, EFTs, ePayments, and Credit Service Payments

If the payment batch is not yet postedIf a payment is in an unposted batch, you may remove or void the CM reference numbers using the AP Payment Posting form.When you select the Void Payment button on the AP Payment Posting form, you are presented with two options:

- Click Yes to record the CM reference number as voided, in which case it is recorded as void in the AP payment files and in CM and will not be reusable.

- Click No to remove the CM reference number and the CM Sequence number from the payment sequence, in which case it is not recorded as void in the AP Payment files or CM, and will be available for reuse.

In either case, the invoice/transaction is rendered open for payment, allowing you to either remove the invoice/transaction from the batch for later payment or run the payment process again using a different payment method and/or CM reference number.
For instructions on voiding unposted payments, see [Void Unposted Payment Records](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-unposted-payment-records).
If the batch has been postedIf you have fully processed a payment, you may void it using one of two forms:

- If the month in which the payment was processed is still open, you can use the AP Void Payments form to void the payment, as long as the paid month is the same as the batch month. If you select the Record CM Reference as Void - number cannot be reused checkbox, the CM references for selected payments are recorded as void in the AP payment files and CM, and cannot be reused. If you leave the checkbox unselected, the CM references are removed from the payment transactions and are available for reuse. For EFT payments, you may void all EFT sequence or only specific sequences. Because any of these options reverse payments previously processed, the update includes a GL distribution to reverse the payment. The selected transactions are reopened for later payment. For instructions, see [Void Payments in an Open Month](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/void-payments-in-an-open-month).

- If the payment was processed in a month that is now closed, or you want to reverse a payment that was posted in a prior, open month, you must use the AP Prior Mth Payment Reversal program. This program reverses the check rather than flagging it as void. The process creates an invoice batch in the current month and posts transactions to offset the original ones paid. Transactions are posted as “prepaid” and assigned the same check / EPay# number as the original, but with a new sequence number. For instructions, see [Reverse a Prior-Month Payment](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/reverse-a-prior-month-payment).

Note: You also have an option to reinstate the transactions as open, which creates additional, positive, unpaid AP transactions. When the offsetting prepaid is processed, it updates CM with a negative check under the same CM Reference number. Both the positive and negative checks may be cleared on the next check reconciliation. EFT payments may not be voided and checks may not be flagged for reuse after the payment month is closed.
