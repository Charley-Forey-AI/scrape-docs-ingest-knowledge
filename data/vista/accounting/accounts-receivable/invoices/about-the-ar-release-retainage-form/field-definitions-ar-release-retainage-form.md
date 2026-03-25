---
title: "Field Definitions: AR Release Retainage Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-release-retainage-form/field-definitions-ar-release-retainage-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-release-retainage-form/field-definitions-ar-release-retainage-form"
---

# Field Definitions: AR Release Retainage Form

The following is a list of field descriptions for the AR Release Retainage form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 If this is a new batch, enter “New”, “N” or “+.” The system assigns sequence numbers, so you must accept the default.
 If this is an existing batch, enter the sequence number to work on, or enter New to add a new sequence to the batch.

##  Customer

 Enter the customer for releasing retainage.

##  JC Co

 Enter the Job Cost company for the contract that the release retainage transaction applies to. If a JC company is not specified, all invoices (contract and non-contract) with open retainage posted to this customer will display in the grid below.

##  Contract

 Specify the contract for which you are releasing retainage. If a contract is not specified, all invoices (contract and non-contract) with open retainage posted to this customer will display in the grid below.

##  Auto Calculate Release Retainage

 Select this checkbox to have the system automatically calculate release retainage.

##  Rec Type

 Enter the receivable type for this transaction. The receivable type is used to determine which Retainage Receivable account to credit and which Accounts Receivable account to debit with this release retainage transaction.

##  Invoice #

 Enter an invoice number for this release retainage transaction, up to 10 characters.
 If you selected the Automatically Number Invoices checkbox (AR Company Parameters), this field is unavailable and defaults to the next sequential invoice number available.

##  Trans Date

 Initially defaults to current date. Enter the release date or accept the default.

##  Due Date

 Initially defaults a due date based on the specified payment terms. Enter the date this transaction is due for payment, or accept the default.
 When releasing retainage, the system creates an invoice for the released amount. The invoice is subject to payment the same as a regular invoice; therefore, you must specify a due date. If you select the Release Retainage to Current A/R checkbox in AR Company Parameters, the system also uses the due date to age the retainage invoice.
 Enter the due date manually or have the system calculate it. The system uses the specified release date and the Payment Terms you assigned to the selected customer in AR Customers to determine the due date. Override the default if desired.

## Release PCT

If you had the system automatically calculate the retainage, this field defaults the retainage percent specified in the Percentage field. If you specified a fixed amount, this field defaults a percentage based on the fixed amount. The system allows overrides to this field.
If you are releasing retainage manually, this field defaults to 0.00. Enter the percent of the retainage amount to release. For example, if the full amount of retainage is $1000, but you only want to release 1/3 of that amount, enter 33.33%.
Note: If you want to enter a fixed dollar amount for release, leave this at 0.00, and enter the fixed amount in the Release Amt field. The system will calculate the percentage once you enter and save the fixed amount.

##  Release Amt

 If you specify a percentage in the Release PCT field, this field defaults the release amount calculated by the system.
 If you did not specify a percentage, enter the amount of retainage to release. The system automatically calculates a percentage and displays it in the Release PCT field.

##  Release Retainage Billed Through

 Enter the date through which all billed retainage for the specified invoice is to be released.

## Release By:

- Percentage – Select this option to release a percentage of the total retainage. Specify the release percentage in the Percentage field to the right of this field.

- Amount – Select this option to specify a fixed amount of retainage to release. Specify the release amount in the Amount field to the right of this field.

##  Percentage

 Enter the percent of the retainage amount that you want to release. For example, if the full amount of retainage is $1000.00, but you only want to release 1/3 of that amount, enter 33.33%. The system automatically calculates the release amount and display it in the Release Amt field once you exit this window.

##  Amount

 Enter the amount of retainage to release. The system applies the total amount to the first invoice in the grid. If the amount exceeds the open retainage for the first invoice, the system applies it to each subsequent invoice in the same manner, until the amount is full distributed.
