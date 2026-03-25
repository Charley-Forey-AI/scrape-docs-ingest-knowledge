---
title: "Field Definitions: AP Void Payments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-void-payments-form/field-definitions-ap-void-payments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-void-payments-form/field-definitions-ap-void-payments-form"
---

# Field Definitions: AP Void Payments Form

The following is a list of field descriptions for the AP Void Payments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Payment Method

Payment Method drop down in the AP Void Payments form.

From the drop-down, select the payment method by which to filter invoices/transactions to void. Only invoices/transactions with this payment method that are eligible to void are added to the Eligible To Void grid.
Leave blank to include all eligible invoices/transactions, regardless of payment method.

- N-ePayments (U.S. only)

- C-Check

- E-EFT

- S-Credit Service

## CM Account

The CM Account field on the AP Void Payments form.
Enter the CM account by which to filter payments eligible for voiding. Leave blank to include all eligible payments meeting other filter criteria, regardless of the CM account.

## CM Reference

The CM Reference field the AP Void Payment form, Filter Payments section.
Enter the CM reference number (assigned to the invoice during payment posting) by which to filter payments for voiding. When you click Fill Grid, the grid populates with only those payment transactions assigned this CM reference number that meet all other filter criteria.
Leave this field blank if not filtering payment transactions by CM reference number. When you click Fill Grid, the grid populates with all payments meeting the filter criteria, regardless of CM reference number.

## Batch #

The Batch # field on the AP Void Payments form.
Enter the number of the original posting batch by which to filter invoices/transactions to void. Press F4 to select from a list of batches within the specified batch month (that is, the AP Void Payments batch month). Only eligible invoices/transactions within the specified batch are added to the Eligible To Void grid.
Leave this field blank if you are not restricting by batch number.

## Action

The Action field on the AP Void Payments form, Batch Control section.

Specify how to treat CM reference numbers for voided payment transactions.

- Void - Select this option to record the CM reference numbers of selected invoices/transactions as voided. When you post the void payments batch, the system records the reference numbers in both CM and AP Payment History as voided and makes them unavailable for reuse.

- Clear - Select this option to allow reusing the reference numbers of the selected invoices/transactions. When you post the void payments batch, the system clears the reference numbers from both CM and AP Payment History so they can be reused later.

Note: If you select the wrong option for payments added to the void batch, you must select the Remove checkbox in the Payment Batch grid for the applicable payment transactions and then click Update Batch. This removes the payment transaction(s) from the lower grid only. You can then select the transaction(s) in the Eligible to Void grid, select the correct Action option, and then click Update Batch to add the transactions back to the void batch.

## Void Memo

The Void Memo field on the AP Void Payments form.
Enter information about the voided payment(s), up to 255 characters. The memo entered here will be applied to all payment transactions in the void payments batch.

## Void

The Void checkbox on the AP Void Payments form, Eligible To Void grid.
Select this checkbox for each invoice/transaction you want to void. You can also click the Check All button (above the grid) to select all invoices/transactions.
Once you have finished selecting invoices/transactions to void, click the Update Batch button to add the transactions to the payment batch. Transactions will then appear in the Payment Batch grid.

## Remove

The Remove checkbox on the AP Void Payments form, Payment Batch grid.
Select this checkbox for each invoice/transaction you want to remove from the Payment Batch grid.
Once you have finished selecting invoices/transactions to remove, click the Update Batch button. The invoice/transaction is added back to the Eligible To Void grid.
