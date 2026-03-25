---
title: "AR Transaction Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-transaction-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/transaction-entry/ar-transaction-types"
---

# AR Transaction Types

When posting transactions in the AR Invoice Entry program, you
 are required to enter a transaction type. The transaction type you select determines what
 type of information is required for input.

When posting transactions in the AR Invoice Entry program, you are required to enter a transaction type. The transaction type you select determines what type of information is required for input.
There are four transaction types available:

- Invoice – This type of transaction is used to record billing/invoice amounts
 posted to customers. For each invoice line entered, you can specify
 discount, tax, and retainage amounts, depending on the setup options
 selected in the AR Company Parameters, AR Customers, and JC Contracts forms.
 Note: Invoices interfaced from Job Billing (JB),
 Material Sales (MS), or Service Management (SM) will automatically be
 entered with an Invoice transaction type. These invoices cannot be
 edited in this program; they must be edited from the modules in which
 they were created.

- Adjustment – This type of transaction is used to adjust existing invoices (such as the invoice amount, retainage, or tax information) without affecting the original transaction lines. An adjustment entry must be applied to a previous transaction. You can adjust lines that exist on the original invoice, or you can add new lines to the invoice. An adjustment amount may be either positive or negative; positive amounts will be added to the invoice (debited to AR) and negative amounts will reduce the invoice amount (credited to AR). If adjustment entries are posted to contracts, they will update Job Cost.

- Credit Memo – This transaction type is used when you need to credit all or part of an invoice or finance/service charge. Credits must be applied by line item, and the line items entered must be line items that exist on the original invoice to which the credit memo is being applied. You do not need to credit the entire amount of any selected line item, nor do you have to credit every line item that exists on the original invoice. Credit amounts for tax, retainage, and discounts, if applicable, will be calculated on the credit amount of each line item selected. Calculated amounts may be overridden, if desired and all credited amounts will be updated to Job Cost.

- Write Off – This type of transaction is used to write off all or part of an invoice, and is similar to the Credit Memo in that each line item entered in a write-off transaction must exist on the original invoice. The differences are that write-offs are not updated to Job Cost, and write-offs debit a write-off account rather than the original revenue account. Write-off amounts for tax, retainage, finance charges, and discounts, if applicable, are calculated on the write-off amount of each line item (full or partial). Cost adjustments are not updated to Job Cost. Note: Write-off transactions can be entered manually in AR Invoice Entry or automatically in AR Automatic Write-off.

When entering Adjustment, Credit Memo, or Write Off transactions, information about the invoice to which you are applying the transaction is displayed to the right of the date fields (i.e. the 'apply to' month and transaction number). You can view additional information about the invoice (i.e. original amounts) by selecting the Other Info tab in the Lines section of AR Invoice Entry.
