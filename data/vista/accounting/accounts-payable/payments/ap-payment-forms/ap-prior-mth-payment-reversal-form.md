---
title: "AP Prior Mth Payment Reversal Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-prior-mth-payment-reversal-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-prior-mth-payment-reversal-form"
---

# AP Prior Mth Payment Reversal Form

Use the AP Prior Mth Payment Reversal form to reverse a payment posted in month that is now closed or to reverse a payment in the current month, even though the original posting month for the payment is still open.
Reversing a payment also reverses any tax amounts (sales, use, or VAT) for invoices and retainage.
Important: If reversing an ePayments payment, you must also cancel the payment on the Corpay website.

Note: You can still use the AP Void Payments form to void payments posted in a month that is still open; however, the paid month and batch month must be the same.

When you reverse a payment:

- the system automatically generates a prepaid reversing transaction in the batch month indicated in the posting form, not the month the payment was originally posted.

- the reversing transaction is identical to the original transaction, except that a negative amount is posted.

- if you are reversing any retainage amounts, the reversing transaction includes them.

- if the original payment covered multiple transactions, a reversing entry is created for each original transaction.

- the reversing transactions are posted to the batch month indicated in the batch posting form. The system assigns the same payment reference number as the original, but with a new sequence.

- and you post the 'payment' of the negative amount (via AP Prepaid Process), the system updates the necessary CM module tables, as well as the AP Payment History tables (APPH, APPD).

-  the positive- and negative-amount sequences of the check net to zero, and you may clear them during the next check reconciliation. Nothing is marked as void.

For example:
Original Transaction:
Exp MonthTrans #JobGross
1/XX2001000$500.00

Original Payment:
Paid MonthCM AccountCheck #Check Seq #Paid Amount
2/XX1031000$500.00

Reversing Transaction:
Exp MonthTrans #JobGrossPrepaid Chk #Prepaid Seq #
4/XX4001000-$500.0031001

Reversing Prepaid:
Paid MonthCM AccountCheck #Check Seq #Paid Amount
4/XX1031001-$500.00

If you want to reinstate the invoice so that it is available again for payment, select the Create Open Transaction(s) in Batch Month checkbox. Once all the reversing entries are made, a new payable transaction matching the original transaction is generated and posted to your chosen batch month, as shown below.
New Transaction:
Exp MonthTrans #JobGross
4/XX4011000$500.00

The system updates the subledgers and GL when the expense batch is posted. The transaction is then available for payment like any other transaction.

Related tasks

- [Reverse a Prior-Month Payment](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/reverse-a-prior-month-payment#task-3956--en__task-3956)

Related information

- [AP Void Payments Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-void-payments-form)

- [AP Batch Process Form](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form)
