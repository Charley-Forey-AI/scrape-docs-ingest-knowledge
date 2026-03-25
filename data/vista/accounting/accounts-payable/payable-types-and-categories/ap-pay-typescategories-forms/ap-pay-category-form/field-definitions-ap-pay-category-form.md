---
title: "Field Definitions: AP Pay Category Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-pay-category-form/field-definitions-ap-pay-category-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payable-types-and-categories/ap-pay-typescategories-forms/ap-pay-category-form/field-definitions-ap-pay-category-form"
---

# Field Definitions: AP Pay Category Form

The following is a list of field descriptions for the AP Pay Category form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Pay Type Category

 For use with Pay Category feature only (flag in AP Company Parameters).
 Enter a pay type category (0-9999), or enter 'N', 'New', or '+' for the next sequential pay category. This pay category should represent a division, location, region, branch, etc. that requires separate GL accounts for expense, job, subcontract, and retainage payables, as well as discounts.

## Description

 Enter a description of this pay category, up to 30 characters, to identify the division (e.g., location, region, branch, etc.) the pay category represents.

## Expense

 For use with Pay Category feature only (flag in AP Company Parameters).
 Specify a valid payable type for non-job transactions. This pay type defaults when posting non-job transactions referencing this pay category. Pay type may be overridden during transaction entry if the Allow Pay Type Override flag is checked (in AP Company Parameters).
 This payable type determines the AP GL Account to credit when the invoice batch is posted and to debit when it is paid.

## Job

 For use with Pay Category feature only (flag in AP Company Parameters).
 Specify a valid payable type for job transactions. This pay type defaults when posting job transactions referencing this pay category. Pay type may be overridden during transaction entry if the Allow Pay Type Override flag is checked (in AP Company Parameters).
 This payable type determines the AP GL Account to credit when the invoice batch is posted and to debit when it is paid.

## Subcontract

 For use with Pay Category feature only (flag in AP Company Parameters).
 Specify a valid payable type for subcontract transactions. This pay type defaults when posting subcontract transactions referencing this pay category. Pay type may be overridden during transaction entry if the Allow Pay Type Override flag is checked (in AP Company Parameters).
 This payable type determines the AP GL Account to credit when the invoice batch is posted and to debit when it is paid.

## Retainage

For use with Pay Category feature only (flag in AP Company Parameters).
Specify the payable type for retainage. This pay type is assigned to any retainage amount entered for a transaction referencing this pay category.
This payable type must be different from any of the other payable types assigned for Expense, Job, and Subcontract transactions and is used to determine the AP GL Account to credit when the expense batch is posted and to debit when it is paid.
Note:If a transaction line has retainage, this payable type is automatically assigned to the retainage portion of the line. It not display on the screen, and cannot be overridden.

## SM Work Order

For use with Pay Category feature only (flag
 in AP Company Parameters).
Specify a valid payable type for SM Work Order
 transactions. This pay type defaults when posting SM work order transactions referencing
 this pay category (in AP Transaction Entry and AP Unapproved Invoice Entry). Pay type may
 be overridden during transaction entry if the Allow Pay Type Override box is checked
 (in AP Company Parameters).
This payable type determines the AP GL Account to credit when the invoice batch is posted and to debit when it is paid.

## Discount Offered GL Acct

For use with Pay Category feature only (flag in AP Company Parameters).
This field is only enabled if the Post Discounts Offered to GL and Net Amounts
 to Subledgers checkbox is selected in AP Company Parameters.
Specify the GL account to debit with discounts
 posted to any transaction (AP Transaction Entry, AP Recurring Invoices, and AP Unapproved
 Invoices) referencing this pay category.
Note: Do not leave this field blank. Although a 'discount
 offered' account is specified at the company level, it is not used as a default when the
 entry here is null. As this account is required when processing payments that include a
 discount, an error occurs when you try to post the payment batch.

## Discount Taken GL Acct

For use with Pay Category feature only (flag in AP Company Parameters).
Specify the GL account (from GL Accounts) to credit with discounts actually taken with a payment. This account is used whenever a transaction referencing this pay category includes a discount, regardless of whether posting net or full amounts to subledgers.
Note: If you are using discounts, do not leave this field
 blank. Although a 'discount taken' account is specified at the company level, it is not
 used as a default when the entry here is null. As this account is required when processing
 transactions that include a discount, an error occurs when you try to post the batch.
