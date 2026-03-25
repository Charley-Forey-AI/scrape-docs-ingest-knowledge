---
title: "Payment Discounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/payment-discounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/payment-discounts"
---

# Payment Discounts

You can have discounts applied automatically or apply them manually.
If you elected to offer discounts when applying payments (that is, you selected
 the Apply Discounts checkbox in the AR Initialize Receipt form), the system automatically applies
 the payment discount (and tax discount if allowing tax discounts) for each item as long
 as:

- a discount 'offered' exists (that is, the
 discounts were specified during invoice entry);

- payment is applied before the discount
 date specified on the invoice;

- the amount of the payment covers the
 entire balance.

If you are applying a payment after the
 discount date, you can still enter discount amounts manually.
If discounts were
 not offered on the invoice or if you are using the Allow Discounts Taken on Receipts
 option (AR Company Parameters form), you can only enter discounts by selecting the Remove Input Restrictions checkbox. See [Payment Receipt Overrides](/en/vista/vista/accounting/accounts-receivable/cash-receipts/payment-receipt-overrides).
Note: You can have the system automatically set the Disc
 Taken for each line by placing focus in the Apply Amount column and pressing Ctrl +
 W.

## Applying Tax Discounts

If you selected the Allow TaxDisc on Invoices
 & Receipts checkbox in AR Company Parameters), the system calculates the tax discount amount during invoice entry. When applying payments, if you elected to
 apply discounts, the system automatically takes the tax discount along with the
 payment discount, as long as the discount date is within the period specified by the
 customer's payment terms and the amount of payment covers the entire balance. If these
 conditions are not met, or you are applying payments manually, you must enter tax
 discounts manually.
 If payment and tax discounts were not
 offered, or you selected the Allow Discounts Taken on Receipts checkbox (which prevents
 the calculation of payment and tax discounts during invoice entry), you can still
 manually take the discounts. However, because Cash Receipts restrictions disallow the
 entry of payment and tax discounts greater than the 'offered' discounts, you will need
 to override the input restrictions in order to enter the discount amounts. This is done
 by selecting the Remove Input Restrictions option, and then manually entering the
 payment and tax discount amounts.
