---
title: "Purchase Variance Account | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/purchase-variance-account"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/purchase-variance-account"
---

# Purchase Variance Account

The account is typically called a "variance" account
 because the value entered into Inventory Control at the time the merchandise arrives may be
 slightly different than the invoice when it arrives some days later. The balance in this
 account will always be the sum of the value of inventory received (but not yet invoiced), plus
 or minus the variance on prior receipts.
Important: This information only applies to companies
 with Order Processing that do not use Purchase Order.

Using a strictly manual account system for inventory, the inventory
 asset account would be debited and the Accounts Payable liability account would be
 credited when merchandise is received from the supplier.
Using Spectrum, the user may access information about inventory
 quantities and valuation. As soon as merchandise arrives at the loading dock from the
 supplier, the user will be able to take receipt of it. It may be several days before the
 invoice for the merchandise is received by mail from the supplier. At that time, the
 user will enter the invoice into Accounts Payable. In order to account for these two
 distinct, separate operations, the user will access a common clearing account in the
 General Ledger. This account could be named "Purchase Variance," "Inventory Variance,"
 or Pending Supplier Payable," for example. Because most businesses receive the
 merchandise before the inventory, this account is usually placed with other liabilities
 as a pending payable account.
Periodically, it will be appropriate to make a journal entry between
 the purchase variance account and cost of goods sold account in the net amount of the
 variance. This may be done monthly, quarterly or annually.
Using T-accounts, the following is an example of how this account
 will work in the General Ledger:
INVENTORY
ACCOUNTS PAYABLE

Debit
Credit

(1) 100.00
(2) 99.50

COST OF GOODS SOLD
PURCHASE VARIANCE

Credit
Debit
Credit

(3) .50
(2) 99.50
(1) 100.00

(3) .50

TRANSACTIONS

1. Items delivered to warehouse, received into inventory at $100.

1. AP invoice arrives by mail, recorded in Accounts Payable at $99.50.

1. $.50 Purchase Variance credited to Cost of Goods Sold using G/L journal
 entry.
