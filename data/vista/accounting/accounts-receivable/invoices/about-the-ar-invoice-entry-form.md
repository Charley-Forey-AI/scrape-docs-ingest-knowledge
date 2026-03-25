---
title: "About the AR Invoice Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-invoice-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-invoice-entry-form"
---

# About the AR Invoice Entry Form

You can use the AR Invoice Entry form to enter invoices and to
 make amendments to existing invoices in the form of Adjustments, Credit Memos, and/or
 Write-offs.
 The transaction type determines the information
 required for each transaction. In addition, the various setup options selected in AR
 Company, AR Customers, and JC Contracts determine what defaults display on the screen,
 as well as what fields may or may not be accessed.
The transaction header (upper section) is used to enter information about the invoice, adjustment, credit memo, or write-off (depending on transaction type). This includes the customer, invoice number or if an adjustment, credit memo, or write-off, the invoice to which you are applying the transaction, contract (if applicable) and invoice, due, and discount dates.
Transaction lines are set up in the lower section of the form. Although much of the information entered for invoice lines is the same for all line types (e.g. description, GL account, amount, retainage, tax basis, etc.), some information will depend on the line type. For example, contract line types require a contract item and contract units and material lines (non-contract invoices) require a material code, UM, units, and unit price.
If you are entering adjustments, you can either specify an existing invoice line to work with or enter a new one. For credit memos and write-offs, you must specify an existing invoice line; new lines can only be added to the original invoice.
Note: It is important to note that once line detail has been entered, there is certain header data that cannot be changed (e.g. customer number, transaction type, invoice, etc.).

## Invoice Numbers

If you are using the Automatically Number Invoices feature, the invoice number is assigned automatically, but may be overridden. If you manually enter invoice numbers, the validation process will automatically check to see if the invoice number already exists. It will check both posted and non-posted invoices (in AR) to see if the number exists for the specified customer or any other customer in the current AR company. It then checks in Job Billing to see if any active, changed, or deleted billings (that have not yet been interfaced) exist in any JB/JC companies using the current AR company. If a duplicate number is found in any of these areas, a warning displays (showing the batch month, ID, and Seq #), but the entry is allowed.

## Receivable Type

If you do not allow overriding receivable types (option in AR Company Parameters), the Rec Type field will be disabled, but will default the receivable type as follows:

- If a non-contract invoice, defaults the receivable type assigned to the customer in AR Customers.

- If a contract invoice, defaults the receivable type
 assigned to the contract in JC Contracts (JB Info tab) or JB Contract Info.
 If no receivable type is assigned to the contract, defaults the receivable
 type assigned to the customer.

- If no receivable type is assigned to the customer, defaults the receivable type assigned in AR Company Parameters.

Note: Once lines exist for an invoice, the Rec Type field is disabled, regardless of whether you allow overrides to the receivable type. If you need to change the receivable type, you must first delete all invoice lines. Once you change the receivable type, you can then re-enter the invoice lines. This is also true of transactions that are added back into an invoice batch. The Rec Type is also disabled for all Adjustment, Credit Memo, or Write-off transactions, regardless of whether overrides to the receivable type are allowed.

## Misc Distributions

This tab is used to distribute any amount of the invoice that requires separate accounting by your company (e.g. commissions, city business tax, etc.). You can enter, modify, or delete miscellaneous distributions directly in the grid or via the related form (accessed by double-clicking in a grid line or by selecting the Open Related Record in Form option on the Records menu).

## Other Info / Contract Item Info

The Other Info tab is used in conjunction with adjustment, credit memo, and write-off transactions, and displays information about the original invoice to which you are applying the transaction. In addition to the original invoice number, month, transaction, and line number, this tab shows the original amount, tax, retainage, and finance charges, as well as the total amount, tax, retainage, and finance charges, including payments.
The Contract Item Info tab shows original, current, and billed units and amounts for the contract to which the invoice, adjustment, credit memo, or write-off transaction applies.

## Automatic Write-offs

The Auto WriteOff Process option (File menu) allows you to generate write-offs for account balances, invoice balances, and finance charges based on a set of criteria. Once write-off transactions are generated, you are returned to this form so that you can review/edit the transactions as necessary.

Related information

- [About the AR Automatic Write-Off Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-automatic-write-off-form)

- [About the AR Miscellaneous Distributions Form](/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-miscellaneous-distributions-form)

- [About Invoices Interfaced from JB, MS, and SM](/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/about-invoices-interfaced-from-jb-ms-and-sm)

- [About Payment and Tax Discounts](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/discounts/about-payment-and-tax-discounts)

- [About Applying Taxes to Invoices](/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/about-applying-taxes-to-invoices)

- [About Offset GL Accounts](/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/about-offset-gl-accounts)

- [AR Transaction Types](/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-transaction-types)

- [Setup Options (AR and JC)](/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-invoices/setup-options-ar-and-jc)
