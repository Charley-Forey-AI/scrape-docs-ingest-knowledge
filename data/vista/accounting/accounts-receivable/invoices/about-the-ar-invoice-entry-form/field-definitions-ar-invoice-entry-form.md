---
title: "Field Definitions: AR Invoice Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-invoice-entry-form/field-definitions-ar-invoice-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-invoice-entry-form/field-definitions-ar-invoice-entry-form"
---

# Field Definitions: AR Invoice Entry Form

The following is a list of field descriptions for the AR Invoice Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

##  Customer

 Enter the number of the customer to which this transaction applies. (Use F4 to display a list of valid customers).

## Trans Type

Specify the transaction type for this transaction:

- Invoice – Use this type when entering invoices.

- Adjustment – Use this type to post an amendment to an existing invoice.

- Credit Memo – Use this type to credit amounts of an existing invoice.

- Write Off – Use this type to write-off amounts of an invoice for which payment cannot be collected.

For Adjustment, Credit Memo, or Write Off transaction types, once you tab off this field, the screen displays the ‘apply to’ lookup window so that you may select the invoice to which the Adjustment, Credit Memo, or Write Off applies. You must select an 'apply to' invoice in order to save the record.

- If you do not select an 'apply to' invoice (i.e. you cancel out of the 'apply to' lookup window), attempts to save the record will display a message indicating that the invoice number is required. Upon closing the message, focus will return to this field. You will need to tab off the field to redisplay the 'apply to' invoice lookup, and then select the applicable invoice.

- You can review information about the ‘apply to’ invoice using the Other Info tab (Lines section). Information includes the original invoice number and posting month, transaction number, and line number, as well as the original and current due invoice, tax, retainage, and finance charge amounts.

## Invoice #

Required.
If you are using the Automatically Number Invoices option (AR Company Parameters), this field defaults the next sequential invoice number available. May be overridden; however, the override value will not be updated to the Last Invoice Number in AR Company Parameters.
If you are assigning invoice numbers manually, enter the invoice number, up to 10 characters. (Note: Invoice number will be checked against existing invoice numbers in AR and JB. If the number already exists for any posted or non-posted invoice for any customer in the current AR company, or for any active, changed, or deleted billing (not yet interfaced) in any JB/JC company using the current AR company, a warning is displayed; however, the entry will be allowed.
If this is an adjustment, credit memo, or write-off transaction, this field is disabled and no invoice number is assigned. However, you will need to select the invoice to which the adjustment, credit memo, or write-off applies via the invoice lookup window (displayed automatically for Adjustment, Credit Memo, or Write-off transactions). Once you select the 'apply to' invoice, that invoice number displays in this field.

##  Description

 Enter a description of this invoice, up to 30 characters. If this is an Adjustment, Credit Memo, or Write-Off transaction, the description defaults from the original invoice, but can be changed without affecting the original invoice.

##  Customer Reference

 Enter the customer reference for this invoice, up to 20 characters. For example, if a purchase order or material order is associated with this invoice, you might use the PO/MO number as the customer reference.

## Rec Type

Enabled only if allowing overrides to receivable type (option in AR Company Parameters).
Initially defaults the receivable type specified for the customer in AR Customers. If no receivable type was specified for the customer, then the receivable type specified in AR Company Parameters is used.
If a contract is entered, default will be receivable type specified for the contract (in JB Contract Info). If no receivable type is specified for the contract, default will be the receivable type for the customer or company (if none exists for the customer).
Note: Regardless of whether you allow overrides to the receivable type, once lines exist for an invoice, you can no longer access this field. If you need to change the receivable type, you must first delete all invoice lines. Once you change the receivable type, you can then re-enter the invoice lines.  This is also true of transactions that are added back into an invoice batch.
You cannot change the receivable type for Adjustment, Credit Memo, or Write-Off transactions. Field will always be disabled, regardless of how you set the 'Allow Override of Receivable Type' flag.

##  JC Co

 Enter the Job Cost company to use for contract information, and to which this transaction will be updated. If you are not applying this invoice to a contract, leave this field blank.

##  Contract

 Enter the contract to which this invoice is being applied. If you are not applying this invoice to a contract, leave this field blank.
Note: If you enter a soft- or hard-closed contract, the status displays in red above the tab page. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

##  Invoice Date

 Enter the date for this invoice. Initially defaults the current date.

## Due Date

Enabled for ‘Invoice’ transactions only.
Specify the due date for this invoice. Initially defaults a due date as follows:

- Contract Invoice – Due date defaults based on the contract's payment terms. If the contract's payment terms are null, default will be based on the customer's payment terms. If the customer's payment terms are null, due date will be the same as the invoice date.

- Non-Contract Invoice – Due date defaults based on the customer's payment terms. If the customer's payment terms are null, due date will be the same as the invoice date.

##  Disc Date

 Enabled for ‘Invoice’ transactions only.
 Enter the discount date for this invoice.
 Initially defaults a discount date based on the payment terms assigned to the contract (JC
 Contracts) to which this invoice applies. If this is a non-contract invoice, the discount
 date is based on the payment terms assigned to the customer (AR Customers).

##  Reason

 Enter the reason code (from HQ Reason Codes) that identifies why this invoice, adjustment, credit memo, or write-off is being entered, changed, or deleted.

##  Line #

 Enter the line number or N, New, or + to add a new line. The system will automatically assign the next available sequential number.
 If this is a Credit Memo or Write-off transaction, you must enter the line number from the original invoice to which the transaction applies.

## Type

For non-contract invoices, adjustments, or credit memos only, identify the item type for this line. The type entered here determines what fields will display on this section of the screen.

- Material – Use this type to enter information about materials you have sold.

- Other – Use this type to enter detail for all other non-contract type invoices.

When entering adjustments or credit memos, the type will default from the invoice item to which the adjustment or credit memo is being applied. Although the type can be overridden for these types of transactions, it is not recommended.
Note: For non-contract write-offs and contract-related transactions, this field is disabled. If a non-contract write-off, it will default the type from the 'applied to' invoice item. For contract-related transactions, it will default as 'Contract'.

##  Contract Item

 For contract-related transactions only.
 Enter the number of the contract item to which this invoice line applies.
 If this is an Adjustment transaction and you are entering a new line, enter the contract item to which the line applies.

## Material

For non-contract invoices, adjustments, or credit memos with Type of 'Material'.
Enter the material for this line.
Note: If entering a non-contract write-off transaction, field is disabled, but will default the material from the 'applied to' invoice item.

##  Description

 Enter a description of this item, up to 30 characters. If a contract-related item, defaults the contract item's description. If a non-contract item with a Type of 'Material', defaults the material description. If a non-contract item with a Type of 'Other', defaults the invoice header description.

## GL Account

Specify the GL account to credit or debit for this transaction, or accept the displayed default:

- Non-Contract– Defaults the Revenue account defined for the receivable type assigned to the specified customer.

- Contract – Defaults the Open Revenue Acct or Closed Revenue Acct (if job/contract closed and you allow posting to closed jobs) specified for the department assigned to the contract item (in JC Contract Items). This default may only be overridden if the “Allow GL Account Override” option is checked on the GL Revenue tab of JC Company Parameters. Otherwise, this field is disabled.

Note: If this is a previously posted transaction and the
 posted job is closed, this field may default the Open Revenue Acct; however, the batch
 process will correctly post the line's amount to the Closed Revenue Acct.

- Credit Memo – Defaults the Revenue
 account from the original invoice item to which the credit memo is being applied.
 If a contract-related transaction, this default may only be overridden if the
 “Allow GL Account Override” option is checked on the GL Revenue tab of JC Company
 Parameters. Otherwise, this field is disabled.

- Write-Off – Defaults the WriteOff
 account specified for the receivable type assigned to this AR company (AR Company
 Parameters). If a contract-related transaction, this default may only be
 overridden if the “Allow GL Account Override” option is checked on the GL Revenue
 tab of JC Company Parameters. Otherwise, this field is disabled.

Note: If you are writing off finance charges (manually or using the 'auto write-off' feature), this field will default the WriteOff account assigned to the line's receivable type (in AR Receivable Types). However, the account that is actually debited for the write-off amount will be the FC WriteOff account specified for the receivable type. This 'switch' occurs during batch processing. Once you validate the batch, if you review the audit lists, you will note that the "AR Invoice Audit List" will show the 'Write Off' account specified in the transaction line. However, the "AR GL Invoice Distribution List" will show the actual account being debited as the 'FC WriteOff' account.

## Tax Code

This field is enabled only when the Post Taxes on
 Invoices checkbox is selected in AR Company Parameters.
Enter the tax code by which taxes will be calculated
 for this invoice. Initially defaults the tax code specified for the customer in AR
 Customers (if non-contract invoice) or the contract item in JC Contract Items (if
 contract invoice).
Adjustment Transactions
If adjusting an existing transaction line, this field is disabled. If the adjustment is being entered to correct the tax code, use the following procedure:

1. Apply equal negative values to the existing line. This will zero out the line to cancel it.

1. Add new line with the appropriate amounts. The Tax Code field will now be enabled, allowing you to enter the correct Tax Code. This will assure that tax amounts will be distributed to the correct tax code.
If adding a new invoice line, this field is enabled and will remain enabled until you post the batch.
Credit Memo / Write-Off Transactions
This field will always be disabled, as credits or write-offs must always ‘credit’ the same tax code as specified on the original invoice. You will however, be able to enter a credit amount and credit tax basis, which will then calculate the correct amount of tax to credit or write off.

## Contract Units

For contract invoices only.
If this is an Invoice transaction, specify the number of units being billed for this item.
If this is an Adjustment transaction, specify the number of units to bill or credit for this item. If the adjustment is negative, you must enter the units as a negative (–) amount.
If this is a Credit Memo or Write-Off transaction, specify the number of units to credit for this item. The system automatically assumes the amount to be negative, so do not enter as a negative value.
Note: Units are posted against original contract units. If using the Job Billing (JB) module, units posted in this program may affect progress posting in JB.

##  U/M

 For non-contract items with a Type of 'Material' only.
 Specify the material unit of measure for this non-contract invoice item.

##  Units

 For non-contract items with a Type of 'Material' only.
 Specify the number of material units being billed for this invoice item.

##  Unit Price

 For non-contract items with a Type of 'Material' only.
 Specify the unit price for the material.

##  ECM

 For non-contract items with a Type of 'Material' only.
 Indicate which quantity the unit price represents:
E = Unit price is per each unit.
C = Unit price is per 100 units.
M = Unit price is per 1000 units.

## Amount

For Invoice/Adjustment transactions, enter the amount of this line item. This amount is used to calculate tax, retainage, and discounts, if applicable. If entering a negative adjustment, enter the amount as negative; otherwise, the system will assume the amount to be positive.
For Credit Memo/Write-Off transactions, enter the amount of the original invoice item you wish to credit. Since the system automatically assumes the amount to be negative, you do not need to enter the amount as negative. This amount is used to calculate the tax, retainage, and discount amounts to be credited, if applicable.
Note: For all transaction types, taxes are normally calculated on the amount in this field. However, you can calculate taxes on an amount other than this item’s amount. If you are calculating taxes on an amount other than this amount, enter that amount in the Tax Basis field.

## Tax Basis

This field is enabled only if the Post Taxes on Invoices option is checked in AR Company Parameters.
Enter the amount on which taxes are to be calculated for this invoice line. Defaults an amount as follows:

- If the Calculate Tax on Retainage option is unchecked (in AR Company Parameters), defaults the line amount less retainage (taxes will not be calculated on the retainage portion).

- If the Calculate Tax on Retainage option is checked, defaults the line amount including retainage.

- If the Calculate Tax on Retainage option is checked, but you also checked the Distribute Tax to Retainage option, defaults the line amount less retainage (tax will be calculated on the retainage separately).

Note: Amounts entered here do not affect the line amounts, nor do they affect retainage or discount calculations.

##  Tax

 This field is enabled only if the Post Taxes on Invoices option is checked in AR Company Parameters.
For Invoices and Adjustments, taxes are calculated automatically, and default an amount based on the tax code specified for the line and the tax basis. If the item’s amount is negative (–), the default calculation in this field will also be negative.You may override default calculations if necessary.
For Credit Memos and Write-Offs, taxes are calculated based on the actual credit or write-off amount, not the original amount. For write-offs, credit tax cannot exceed tax due.
Note: The system automatically assumes the credit or write-off amount to be negative, so do not enter the amount as negative.

##  Retainage Tax

 This field is enabled only if both the Post Taxes on Invoices and Distribute Tax to Retainage options are checked in AR Company Parameters.
 The retainage tax amount is calculated automatically based on the tax code and the retainage amount specified for the line. You may override this amount if necessary.

## Total Amount

Display only, the total amount for the line, including sales tax and, if applicable, retainage tax. For Adjustment transactions with negative line, tax, and retainage tax amounts, this amount will also be negative.
Note: For negative adjustments, credit memos, and write-offs, if this amount is greater than the line’s amount due, the following warning displays when you save the line:
“Warning – The line Credit is more than the line AmtDue! It is recommended that you credit this amount against multiple lines. See Other Info tab for line values.”
Although it is recommended that you credit only the amount due for the line, credit amounts exceeding the amount due will be accepted.

##  Retg %

 Enter the percent by which retainage will be calculated for this customer.
 If this transaction is being posted to a contract, this field defaults to the retainage percent you specified for the selected contract item in JC Contract Items. This default may be overridden, if desired.

## Retainage

Enter the retainage amount for this invoice line. Defaults an amount based on the line amount and the retainage percent specified for the line.
If this is an Adjustment transaction and you entered a negative (–) value in the Amount field, the retainage amount will automatically default to a negative amount.
If this is a Credit Memo or Write-Off transaction, and you are crediting or writing off only part of the original invoice, the retainage will be calculated on the credit amount. For write-offs, credit retainage cannot exceed retainage due.
Note: Credit retainage is automatically assumed a negative amount by the system..

## Discount

This field displays only if allowing discounts on invoices (option in AR Company Parameters).
If this is an Invoice or Adjustment transaction, enter the discount amount for this invoice line. Defaults an amount based on the discount rate specified for the contract’s payment terms (contract invoice) or customer’s payment terms (non-contract invoice). You may override as necessary.
If this is a Credit Memo or Write-Off transaction, and you are crediting or writing off only part of the original invoice, the discount will be based on the credit amount.

- Do not enter negative amounts in this field. If the line’s amount is negative, the discount amount should be positive.

- Also, if retainage is used, discounts will not be calculated on the Retainage portion of the transaction.

##  Finance Chg

 Displays for Write-Off transactions only.
 If you used the AR Automatic Write-Off program to automatically write off finance charges, this field will default the total finance charge for this customer/invoice.
 If you used the AR Automatic Write-Off program to automatically write off minimum balances, this field will default a finance charge only if finance charges were assessed on the invoice meeting the minimum balance requirement.
 If this is a manual write-off transaction, this field defaults as 0.00 and you must specify the amount of finance charges for this customer/invoice that you want to write off.
Note: Whether you are entering finance charge amounts manually or overriding default finance charge amounts, the amount entered here cannot exceed the finance charge due for the line. In addition, this amount, combined with the credit tax and retainage amounts, cannot exceed the Total Amount.

##  Tax Disc

 Displays only if allowing discounts on invoices and tax discounts are in use (options in AR Company Parameters).
 Specify the tax discount offered for this invoice line. Initially defaults an amount based on the line's tax rate and payment discount amount. For example, if the invoice amount is 100.00, the tax amount is 5.00 (rate of 5%), and the discount amount is 3.00, this field will default a tax discount of 0.15 (5% x 3.00).
