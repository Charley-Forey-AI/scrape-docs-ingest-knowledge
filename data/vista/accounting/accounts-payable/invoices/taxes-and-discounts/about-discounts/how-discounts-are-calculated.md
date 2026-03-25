---
title: "How Discounts are Calculated | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts/how-discounts-are-calculated"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts/how-discounts-are-calculated"
---

# How Discounts are Calculated

An outline of the setup and processing steps to calculate
 discounts on payable invoices.
For more general information about discounts, see [About Discounts](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts).

Setup

AP Company Parameters:
If you elect to expense the full gross when
 posting the discounts amount (the common and recommended method), leave the
 Post Discounts Offered to GL and Net Amounts to Subledgers checkbox selected
 and assign a valid GL Account in the Discount Taken GL Account field.
If you elect to expense net amounts when posting
 discounts, select the Post Discounts Offered to GL and Net Amounts to
 Subledgers checkbox. You also need to assign a valid GL account to both the
 Discount Taken GL Account field and the Discount Offered GL Account
 field.
If you will be using tax discounts, select the
 Using Tax Discounts checkbox. Otherwise, leave it cleared.

HQ Payment Terms:
Set up payment term codes that define the various
 discount terms your vendors offer.

AP Vendors:
Assign a default payment term code to each vendor.


Processing

AP Transaction Entry and AP Unapproved Invoice Entry
When you enter the Invoice Date for a transaction,
 the system uses the vendor’s default pay terms code to calculate the
 Discount Date and the Due Date based on the codes set up in the HQ Payment
 Terms form. You can override the Discount Date or Due Date as needed. On the
 transaction line, a Discount amount is calculated based on the discount rate
 (from the vendor’s default pay terms) and the line’s gross amount (less
 retainage, if any). You can override the discount amount or the discount
 percentage, and the system recalculates the appropriate value.
If you are using tax discounts, the line's
 discount amount is subtracted from the gross amount to provide the 'tax
 basis.’ The tax rate is then applied to the tax basis amount to provide the
 line's discounted tax amount. The tax amount is added to the gross amount
 (total), and the line's discount amount subtracted from the resulting value
 (net payable amount).

AP Payments:
The Post Discounts Offered to GL and Net Amounts
 to Subledgers and/or Using Tax Discounts options determine whether or not
 you can change a transaction’s discount amount before payment. Changing a
 discount can be done in either the AP Payment Control Detail or AP Payment
 Workfile Detail form.

- If you did not check either of these
 options, you can change or cancel the discount as needed.

- If you did check one or both of these
 options, the discount cannot be changed. If you do not want a discount
 amount to be taken, you can either change the original transaction (if
 the month is still open) or you will have to add a new transaction to
 pay the discount amount.

Note: When the Post Discounts Offered to GL and Net Amounts to
 Subledgers or Using Tax Discounts options are in use, any discount set up
 when the transaction was posted must be taken because the net amount was
 expensed when the batch was posted. Therefore, at payment time, the system
 requires the same net amount to be posted to GL in order to balance the
 expense with the payment.
