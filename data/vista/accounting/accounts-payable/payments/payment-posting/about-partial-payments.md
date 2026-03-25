---
title: "About Partial Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments"
---

# About Partial Payments

An overview of partial payments.
Partial payments are payments of anything less than the total invoice. This is typically done when you want to either pay the two sequences at separate times (one now, one at a later date), or pay the two sequences on separate checks (one to the vendor and supplier, one to the vendor only.)
A partial payment is implemented by splitting the transaction into two sequence numbers. You can create partial payments for either the entire transaction, or at the
 line/sequence level.
Transactions that have retainage applied are automatically split
 into two sequences, one for the current amount, and one for the retainage portion, which
 is placed on hold. If you split a transaction that has retainage, a third sequence is
 created, which can also be placed on hold (non-retainage holds only).
You can also split released retainage into partial payments and put a
 portion of the retainage back on hold. If you are an Australian or Canadian customer,
 see the following article for best practices when splitting retainage with tax: [About Partial Payments for Split Released Retention / Holdback with
 Tax (AU and CA)](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/about-partial-payments-for-split-released-retention--holdback-with-tax-au-and-ca).
See the examples and breakdown of the transactions for partial payments in the tables
 below.
For example, you have a transaction with a single Job line totaling
 $1000, with $100 retainage. You want to create a partial payment of $600.00. The
 diagrams below show what the split transaction would look like.
Before creating the partial payment:
Seq #
Pay Type
Amount

1
Job
$900.00

2
Retg
$100.00

After creating the partial payment of
 $600.00:
Seq #
Pay Type
Amount

1
Job
$300.00

2
Retg
$100.00

3
Job
$600.00

You can optionally assign a supplier to the
 split portion if being paid by a 2-party check, and/or place the amount on a
 non-retainage hold so that it can be paid at a later date.
If you use discounts, and you select the
 Distribute
 Discounts checkbox, the discount amounts on the split detail are adjusted
 proportionately for each sequence number. For example, if the transaction shown above
 had an original discount of $30, the discount distribution would be as follows:
Seq #
Amount
Discount
Calculation

1
$300.00
10%
30 x 300 / 900

2
$100.00
---
---

3
$600.00
20%
30 x 600 / 900

Related tasks

- [Create a Partial Payment](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-partial-payments/create-a-partial-payment)
