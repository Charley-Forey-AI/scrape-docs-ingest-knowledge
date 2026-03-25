---
title: "About Payment and Tax Discounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/discounts/about-payment-and-tax-discounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/discounts/about-payment-and-tax-discounts"
---

# About Payment and Tax Discounts

If you have opted to allow entering discounts on invoices (in the AR Company Parameters form), the system calculates payment discounts automatically for each invoice line entered.
The discount rate and amount is based on the line amount and the type of invoice:

- Contract invoice - the contract's payment terms

- Non-contract invoice - the customer's payment terms

The system does not subtract the discount amount (that is, discount 'offered') from the total due when you enter the invoice. Instead it applies the discount if the payment is posted in the AR Cash Receipts form prior to the discount date.

## Tax Discounts

If you have specified to allow tax discounts (option in AR Company Parameters), and you allow entering discounts with invoices, a tax discount will be calculated once the discount amount is calculated. The tax discount is a calculation of the discount amount times the tax rate (specified for the line's tax code). So, for example, if you have an invoice for $100, with $5 tax (5%) and a discount of $3 (3%), the calculated tax discount would be $.15 (5% x $3).
For more information about payment discounts
 and tax discounts, see [Discounts](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/discounts).
