---
title: "Payment Receipt Overrides | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/payment-receipt-overrides"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/payment-receipt-overrides"
---

# Payment Receipt Overrides

You can apply more of a payment to
 Tax, Retainage, Finance Charges, or Discounts than is available or due for the invoice.
 By default, the system does apply discount amounts
 greater than 'offered' amounts. Note: 'Disc Offered' (and 'Avail
 TaxDisc') values are always 0.00 when not entered at the same time as the invoice
 was posted.
If you need to adjust the 'available' or 'due' amounts, enter an
 adjustment transaction in the AR Invoice Entry form to allow for proper updates and GL
 accounting.
However, you can apply overrides without creating an adjustment by selecting the Remove Input Restriction checkbox in the AR Payment Detail form

 (AR Cash Receipts > Payment Detail button).
For example, if you want to
 apply a larger discount for an invoice than was originally offered, select this checkbox and then enter the desired discount amount for each line on the invoice. Once you
 click OK, the system adjusts the total paid amount accordingly.Note: Before you apply any overrides, it is strongly recommended that you have a complete understanding of how
 data is tracked within the detail and distribution tables.
