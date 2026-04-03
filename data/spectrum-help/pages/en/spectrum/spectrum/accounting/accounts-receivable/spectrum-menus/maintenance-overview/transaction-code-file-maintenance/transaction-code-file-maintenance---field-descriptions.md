---
title: "Transaction Code File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/transaction-code-file-maintenance/transaction-code-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/transaction-code-file-maintenance/transaction-code-file-maintenance---field-descriptions"
---

# Transaction Code File Maintenance - Field Descriptions

The New/Edit Transaction Code window is used to add or edit transaction codes.
 These codes are used when recording cash receipts and adjustments during Cash Receipts/Adjustment Entry to indicate the type of payment or adjustment being made by the customer.
Before setting up transaction codes, decide how customer accounts should be updated when a transaction is entered, and which General Ledger accounts should be updated when this transaction is entered. For example: if there are two cash accounts, two transaction codes could be set up which would have the same effect on customers but which would update different General Ledger cash accounts. Another example might be a situation where bad debts write-offs are to more than one General Ledger account.
Transaction codes may be added at any time, but should not be deleted if there is a chance that transactions with the code in question are still in use within the software. The transaction code specified in this screen determines which cash account the A/R cash receipt transaction will post to. The Post to Cash Management checkbox must be selected in order for this deposit to appear on the Cash Management Bank Reconciliation Entry screen.
FieldDescription
Transaction codeEnter a unique code to designate this transaction, up to 10 characters.
The transaction code is the key field for the Transaction Code File Maintenance. This code will be used to distinguish each transaction record from all other transaction records in the file.

DescriptionEnter the description for this transaction. Examples include cash payment, write-off bad debt, and so forth.
TypeSelect the type of transaction.
General ledger
G/L account codeEnter the account number to be updated for this type of transaction.
For example, if this is a payment transaction to be entered in the cash account, enter the account number of the cash account; if this transaction code is to write-off bad debts, enter the bad debt expense account. If the G/L status code you select has a status of Not used, you cannot proceed using this code. If the G/L status code you select has a status of Inactive, a warning will display.
When the Cash Management module is present this transaction code will be posted to Cash Management. The G/L account code specified must match the G/L account code for the bank account in Bank Account Maintenance in Cash Management.

G/L discount taken codeEnter the General Ledger account for discount taken with this transaction. A lookup window is available for viewing valid General Ledger account codes. If the G/L code's status is set to Not used, then no entry is allowed.
This field typically only applies to payment transactions and not to adjustments.

A/R G/L account codeEnter the General Ledger account for Accounts Receivable to be updated with this transaction. If only one Accounts Receivable account exists, this would be the same for all transaction codes. If more than one Accounts Receivable account exists in the General Ledger, enter the appropriate account for this transaction. If the G/L code's status is set to Not used, then no entry is allowed.
This G/L account will be used during the Cash Receipts Journal update for unapplied payments and adjustment. When payments are applied to open items during Cash Receipts/Adjustments Entry, the Accounts Receivable G/L account code recorded on the invoice being applied will be credited during the update, instead of this account.

Bank
Exclude from finance charges?Select this checkbox to exclude this transaction code from finance charges. Otherwise, clear this checkbox. This is only relevant if Finance Charge Calculation is used. For example, finance charges themselves are generally excluded from future charge calculations.
Post to Cash Management?This checkbox must be selected in order for this deposit to appear on the Cash Management Bank Reconciliation Entry screen. Clear this checkbox if you don't want to update amounts associated with this transaction code to Cash Management.
Bank account codeIf the Post to Cash Management checkbox is selected, enter the bank account code to use with updating this transaction code in Cash Management.
Bank account #If this is a payment transaction code, enter the bank account number for the bank account corresponding to this transaction code. This will be used when printing deposit slips.
If this is an adjustment transaction code, the bank account number is not needed but may be entered, if desired.
Note: Entry of credit card accounts is not allowed.
