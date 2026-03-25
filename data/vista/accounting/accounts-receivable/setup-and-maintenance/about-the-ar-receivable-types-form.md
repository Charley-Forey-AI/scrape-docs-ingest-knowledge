---
title: "About the AR Receivable Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-receivable-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-receivable-types-form"
---

# About the AR Receivable Types Form

Use the AR Receivable Types form to set up the receivable
 types that define the various GL accounts affected when posting transactions
 in the AR module.
 For each receivable type, you may define a different GL account for each of the following:

- Accounts Receivable - for all transactions that apply to a customer’s account.

- Revenue - for non-contract related invoices.

- Retainage – the AR account for the retainage portion.

- Discount - for discounts taken when posting cash
 receipts. If using the MS module and you are
 posting cash receipts for MS invoices where an IN
 location was specified, this account will only be
 used when there is no ‘AR Discount’ account
 specified for the location (in IN Locations).

- Write Off - for write-off transactions.

- Finance Charge Revenue – the revenue account for finance charge transactions if using the invoice’s receivable type for the finance charge.

- Finance Charge Receivable – the receivables account for finance/service charges. This is the account that will be debited when finance/service charges are calculated in AR Finance Charge, or credited when writing off finance/service charges.

- Finance Charge Write-off – the account for finance charge write-offs. This is the account that will be debited when finance/service charges are written off in AR Automatic Write-Off.

If you only have one GL account set up for each of these types of transactions, then you may only need to set up one receivable type.

## Aging Reports

You can use the AR Aging reports to report by receivable type. You may choose to set up separate receivable types even though they are
 using the same GL account, in order to obtain a separate aging or other report by some
 grouping (such as by profit center, project manager, or sales type).

Related information

- [Receivable Types Assignment](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-receivable-types-form/field-definitions-ar-receivable-types-form#ID-00008231--en)

- [How Finance/Service Charges are Credited to GL](/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used/how-financeservice-charges-are-credited-to-gl)
