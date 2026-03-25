---
title: "Field Definitions: AP Initialize Payments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-initialize-payments-form/field-definitions-ap-initialize-payments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-initialize-payments-form/field-definitions-ap-initialize-payments-form"
---

# Field Definitions: AP Initialize Payments Form

The following is a list of field descriptions for the AP Initialize Payments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Acct to be Used if not Assigned in Transaction

 Specify the CM account (from CM Accounts) that will be assigned to all transactions without an assigned CM account.

## Restrict By CM Account

 Check this box if you want to initialize payable transactions by CM account.
 Do not check this box if you want to initialize payable transactions for all CM accounts.

## CM Account

 Enter the CM account to restrict by. Only payable transactions assigned this CM account will be initialized into the payment batch.

## Restrict By Vendor

 Check this box to initialize payable transactions by vendor.
 Do not check this box if you want to initialize transactions for all vendors.

## Vendor

Enter the vendor to restrict by. Only those
 payable transactions posted to this vendor will be initialized into the payment batch.

## Restrict By Job

 Check this box if you want to initialize payable transactions by job.
 Do not check this box if you want to initialize payable transactions for all jobs.

## JCCo

 Enter the Job Cost company in which the payable job transactions are located.

## Job

Enter the job to restrict by. Only those payable transactions posted to this job will be initialized into the payment batch.
Note: When restricting by Job, and an AP transaction exists
 with multiple lines referencing different jobs, only the line posted to the job specified
 for initialization is pulled in for payment.

## Restrict By Payment Control

 Check this box if you want to initialize payable transactions by payment control code.
 Do not check this box if you want to initialize payable transactions for all payment control codes.

## Payment Control

Enter the payment control code to restrict by.
 Only those payable transactions assigned this payment control code will be initialized into
 the payment batch.

## Restrict By Payable Type

Select this checkbox to initialize payable transactions by payable type. Then use the Payable Type selection box below to indicate which payable type(s) to restrict by. Only those transactions assigned the selected payable type(s) are initialized into the payment batch
Do not check this box if you want to initialize payable transactions for all payable types.

## Payment Methods

For each checkbox you select, the system will include invoices to be paid by that method.
For each checkbox you do not select, invoices to be paid by that method will not be included.
Note: By default, when you open the form, the Check and EFT boxes are selected. When processing invoices that have a credit service payment method, use a separate payment batch from invoices paid by check or EFT.

## Include Discounted Transactions Only

Check this box to initialize only those
 transactions with a discount. When checked, if any line on a transaction has a discount,
 all lines for the transaction are initialized into the batch.
Do not check this box if all transactions
 should be initialized, whether or not a discount is taken.

## Take All Discounts

Check this box if you want offered discounts
 to be taken.
Note: This box defaults as checked and will be disabled if
 the Post Discounts
 Offered to GL and Net Amounts to Subledgers and/or Using Tax
 Discounts boxes are checked in AP Company Parameters.
Do not check this box if you do not want
 offered discounts to be taken.

## Cancel if Discount Date is prior to

Cancel if Discount Date is prior to field in the AP Initialize Payments form
For those transactions offering discounts, enter the discount date to use when determining whether the discount may be taken or not. Discounts will be taken for all transactions with a discount date equal to or later than this date. If the discount date specified for a payable transaction is prior to this date, the discount will not be taken.
If you specify a date here and you have also
 selected the If
 available, use Discount Date checkbox, it will affect how canceled
 discounts are handled. For more information, see [Adding Invoices
 with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).
This field is disabled if either of the following checkboxes are selected in the AP Company Parameters form:

- PayTypes/Discounts/ICR tab: Post Discounts
 Offered to GL and Net Amounts to Subledgers

- Invoice Options tab: Using tax
 discount

## Create A Separate Payment Per Subcontract

Check this box if you want a separate check printed for each subcontract. All subcontract transactions will be grouped together by vendor and subcontract, and a separate check printed for each unique combination.
Note: Transactions with the “Separate Payment” option
 checked (in AP Transaction Entry or Unapproved Invoice Entry) are paid separately and will
 not be grouped with other transactions for the vendor/subcontract.
Do not check this box if you want a single check printed per vendor.

## Create A Separate Payment Per Job

Check this box if you want a separate check printed for each job. All job transactions will be grouped together by vendor and job, and a separate check printed for each unique combination.
Note: Transactions with the “Separate Payment” option
 checked (in AP Transaction Entry or AP Unapproved Invoice Entry) are paid separately and
 will not be grouped with other transactions for the vendor/job.
Do not check this box if you want a single check printed per vendor.

## Exclude Vendors with Credit

 Check this box to exclude vendors with a credit balance.
 When you check this box, if the sum total of all the vendor’s transactions is zero, or have a negative balance (credit), the system does not add the transactions to the batch. If you do not check this box, the system only adds transactions greater than zero into the payment batch.

## Include Transactions Due As Of

Specify the due date to use as a cutoff date when determining which transactions can be added to the payment batch.
All transactions with a due date equal to or prior than this date will be included in the batch. All transactions with a due date later than this date will be skipped.

## If Available, Use Discount Date

Check this box if you want the discount date
 to be compared to the date you specified in the Include Transactions Due As Of field when
 selecting transactions to add to the payment batch. All transactions with a discount date
 equal to or less than the cutoff date will be included in the batch. All transactions with
 a discount date later than the cutoff date will be skipped. If a transaction does not have
 a discount date indicated, the transaction’s due date will be used.
Do not check this box if you do not want to
 compare a transaction’s discount date to the cutoff date when selecting transactions to add
 to the payment batch. The due date will be used instead.
Note: If this option is checked and you enter a date in the
 Cancel if
 Discount Date is Prior To field, it will affect how canceled discounts are
 handled. For more information, see [Adding Invoices
 with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).
