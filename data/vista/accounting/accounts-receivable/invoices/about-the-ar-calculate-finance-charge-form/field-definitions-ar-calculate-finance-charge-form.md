---
title: "Field Definitions: AR Calculate Finance Charge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-calculate-finance-charge-form/field-definitions-ar-calculate-finance-charge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-calculate-finance-charge-form/field-definitions-ar-calculate-finance-charge-form"
---

# Field Definitions: AR Calculate Finance Charge Form

The following is a list of field descriptions for the AR Calculate Finance Charge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Set for DueDate to be Same as TransDate

 Select this checkbox to have the due date for all finance charges set to the transaction date (specified in the Transaction Date field).
 Leave this checkbox cleared to have the payment terms specified for the customer (non-contract invoices) or contract (contract invoices) determine the due date for each transaction.

##  Transaction Date

 Enter the date to use as the transaction date for each finance/service charge.

##  Due Date Cutoff

 Enter the due date cutoff for unpaid invoices. Unpaid invoices with a due date less than or equal to the date specified here will be included in finance/service charge calculations. Unpaid invoices with a due date greater than this date will not be subject to finance/service charges and the system will exclude it from calculations. Also applies to invoices for 'on account' customers.

##  Paid Date Cutoff

 Enter the cutoff date for paid invoices. Payments must have been received and posted by this date to avoid charges. The system assesses finance charges on unpaid invoices after this date.

##  Customer

 Enter the specific customer for finance/service charge calculation. If you leave this field blank during processing, a message displays indicating that you did not enter a customer value and asks if you want to continue. Click Yes to have the system calculate finance charges for all customers with invoices meeting the criteria. Click No to return to the form and specify a customer.

##  RecType

 Enter the specific receivable type for finance/service charge assessment. The system includes only invoices with this receivable type when calculating finance charges.

## Recalculate Each Customer

Select one of the following radio buttons:

- Skip Customers already in batch - Select this option to have the calculation process skip any customers that are already in the batch.

- Recalculate charges for Customers already in batch - Select this option to recalculate finance/service charges for customers already in the batch.
