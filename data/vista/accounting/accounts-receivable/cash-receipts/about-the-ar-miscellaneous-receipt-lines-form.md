---
title: "About the AR Miscellaneous Receipt Lines Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-miscellaneous-receipt-lines-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-miscellaneous-receipt-lines-form"
---

# About the AR Miscellaneous Receipt Lines Form

You can use the AR Miscellaneous Receipt Lines form to post payments received from sources other than a customer.
Access this
 form by clicking the Misc Receipts button in [AR Cash Receipts](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form).
There are
 several major differences between posting
 miscellaneous receipts and customer payments.
 These differences include the following:

- Miscellaneous receipts do not post to customer
 accounts. Instead of assigning customers, the
 system prompts you to enter a description of the
 payment.

- Transactions are not invoice-related, so the
 payment application options used for customer
 payments (in [AR Initialize
 Receipt](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-initialize-receipt-form)) are not available. Instead, the
 system applies payments to lines that you set up
 in the lower section of this form.

- You can post transactions to a specific job/phase
 or equipment/cost code.

- Discounts and retainage are not applicable.

## Entering Transaction Lines

When entering transaction lines, you must specify
 the type of receipt being entered. There are three
 types of miscellaneous receipts available:

- O-Other – Use this type for non-job,
 non-equipment cash receipts, such as
 over-the-counter sales, plan deposits, or any
 other miscellaneous cash receipt in which only a
 GL account is credited.

- J-Job – Use this type for job-related
 miscellaneous receipts; typically used to post
 refunds that will reduce the job’s costs.

- E-Equip – Use this type for equipment-related
 miscellaneous receipts; typically used to post
 refunds that will reduce the equipment’s costs.

- S-SM Work Order - Use this type for SM work order-related miscellaneous receipts, such as posting refunds that reduce work order costs.

Line amounts should be entered as positive values
 to balance with the check amount specified in the
 receipt header. However, job and equipment lines
 will post to their respective systems as negative
 costs.

 If a miscellaneous cash receipt transaction line
 is intended to process the refund of a purchase
 amount previously paid to a vendor, and not to
 record a new sale, in the GL
 Acct field, enter a GL account whose
 Account Type is E-Expense (set in [GL Chart of
 Accounts](/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-form)).

## Posting Taxes

When posting taxes for a receipt transaction, do
 not enter the check amount in the Check
 Amount field if the check’s amount
 includes the tax amount. Instead, enter the
 pre-tax amount. The system automatically
 calculates the tax amount based on the specified
 tax code (Tax
 Code field in the line detail), and
 the Total
 Amount field will reflect the true
 check amount.

## Changing Previously Posted Miscellaneous
 Receipts

You can make changes to a previously posted
 miscellaneous receipt by adding the transaction to
 the current batch (using File > Add Transaction
 in AR Cash Receipts). If the transaction’s deposit
 number has been cleared in CM, a message displays
 in the receipt header indicating the deposit has
 been reconciled; all CM-related inputs (check
 amount, company, account, and deposit) will be
 disabled, along with amount inputs.
Note: When you
 use F4 to find the transaction, look for
 transactions with a Transaction Type of ‘M’
 (Miscellaneous Receipts). For more information
 about adding transactions to a batch, see [AR Add Transaction to
 Batch](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-add-transaction-to-batch-form).

## Miscellaneous Distributions

The Misc Distributions tab allows you to
 distribute any amount of a miscellaneous cash
 receipt that requires separate accounting by your
 company. For more information, see [AR Miscellaneous
 Distributions](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-miscellaneous-distributions-form).

## Show All Type Columns

Access this option from the Options menu. It is
 available only when focus is on Grid tab in the
 Lines section of the form. When this option is
 selected, the grid will display all of the columns
 associated with each of the different line types
 (Other, Job, and Equip), regardless of the current
 line type.
Note: The use of
 this option was intended for viewing purposes
 only. Displaying all line type columns increases
 the size of the grid, which can make data entry
 more cumbersome. Additionally, once you close the
 form, the grid automatically resets to the default
 (unchecked).

Related information

- [About the AR Cash Receipts Form](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form)

- [About the AR Add Transaction to Batch Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-add-transaction-to-batch-form)

- [About the AR Miscellaneous Distributions Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-miscellaneous-distributions-form)
