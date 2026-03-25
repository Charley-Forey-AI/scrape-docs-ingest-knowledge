---
title: "Discounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/discounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/discounts"
---

# Discounts

The Accounts Receivable system allows you to use discounts when posting invoices and/or payments for customers.
If you elect to use discounts, the system will
 automatically calculate discount amounts and dates based on data stored in the HQ Payment
 Terms form. The AR Company Parameters program provides three discount options that
 determine if and where discounts can be posted:

- Discounts Not Used – No discounts are used.

- Allow Discounts on Invoices & Receipts – Discounts may be posted in both the Invoice Entry and Cash Receipts programs.

- Allow Discounts Taken on Receipts – Discounts may be posted only when posting payments in Cash Receipts.

## Taking Discounts

If you are calculating discounts at the time of
 invoice entry, the calculation is considered an 'offered' discount. The discount amount
 is not subtracted from the total due at this time because it cannot actually be taken
 until the payment is posted.
When posting the payment, the offered
 discount does not automatically default into the Disc Taken field unless the payment is
 made before the specified discount date and the amount of the payment covers the entire
 balance due. If payment is not made before the discount date, the discount can still be
 taken, but you will need to enter the amount manually. Although the discount offered is
 typically the discount amount taken at the time of payment posting, you are not required
 to use the same amount; default can be overridden if desired.

## Tax Discounts

The Allow TaxDisc on Invoices & Receipts option (in
 AR Company Parameters) allows you to designate whether you can take tax discounts when
 posting invoices and/or cash receipts. However, you can only use this feature if you
 allow discounts on invoices and/or receipts.
If you are using the Allow Discounts on Invoices &
 Receipts option (also in AR Company Parameters), tax discounts can be
 calculated during invoice entry, then applied when posting cash receipts. When entering
 invoice transactions (AR Invoice Entry), the Tax Disc will
 default based on the line's tax rate (determined by tax code) times the discount
 offered. For example, a $100 invoice with $5 tax (5%) and a discount of $3 (3%) would
 also have a Tax Disc of $.15 (5% x $3).
The tax discount is offered in the same manner as the payment discount. It is
 only actually applied when posting the cash receipt in AR Cash Receipts. If you
 initialize the payment (in AR Initialize Receipt) and check the Apply
 Discounts (if applicable) option, the system will automatically take the
 tax discount along with the payment discount, as long as the discount date is within the
 period specified by the customer's payment terms. If you are entering payments manually,
 you can apply the tax discount by accessing the invoice line, entering the payment
 amount in the Amount Applied column, then pressing Ctrl + E to
 apply the tax discount. Typically, you will want to take the tax discount when a payment
 discount has been offered; however, it is possible to take a tax discount even if
 payment and tax discounts were not offered on the invoice.
