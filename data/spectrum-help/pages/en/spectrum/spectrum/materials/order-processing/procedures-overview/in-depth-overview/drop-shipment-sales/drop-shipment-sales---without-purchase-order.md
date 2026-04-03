---
title: "Drop Shipment Sales - Without Purchase Order | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/drop-shipment-sales/drop-shipment-sales---without-purchase-order"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/drop-shipment-sales/drop-shipment-sales---without-purchase-order"
---

# Drop Shipment Sales - Without Purchase Order

If Purchase Order is not installed on the system,
 one of the following drop shipment recording methods should be implemented, based on your
 company's procedures and personnel.
Option 1 Enter
 orders and invoices (make sure the Drop
 Ship checkbox is selected in the Order Entry > Order Details window). Enter a G/L department code that sells out of the purchase variance
 account rather than the inventory valuation account. (For additional information about
 Purchase Variance accounts, click [Purchase Variance Account](/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/purchase-variance-account).)
Advantages: It allows for proper recording of drop shipment
 transactions in Inventory Control and the General Ledger. Accounts Payable is the same as
 in stock shipments (paid to the Purchase Variance).
Disadvantages: It requires a change in procedure for the Sales
 and Order Entry staff. It also requires a special G/L department code entry during
 Order/Invoice entry and a special cost entry, either during Order/Invoice Entry or as a
 separate function.
Option 2 Use the same Order/Invoice procedure as Option 1, except you should use the regular G/L department code. You will still need to enter cost either during Order Entry and Invoice Entry or as a separate transaction. The A/P clerk will post the invoice to the Inventory G/L account, since it was never received to inventory.
Advantages: It requires no change in Order Entry, Invoice Entry
 or Purchase Order Entry.
Disadvantages: The Accounts Payable (or Purchase Order Receiving)
 clerk will need to isolate drop ship invoices and post to Inventory instead of purchase
 variance.
The Inventory Control G/L Department File
 Maintenance screen should be completed based on the drop ship option
 selected:
Option 1
Option 2

Department code:
XYZ
ABC

Description:
Drop-Ship Sales
Standard Sale

G/L Accounts
Sales:
Cost of sales:
Inventory value (non-stock):
Adjustments:
Credit returns:
Receipts:
JC markup:
JC direct cost:
Mix usage:
Equipment cost:
Sales
Cost of Goods Sold
Purchase Variance
Cost of Goods Sold
Purchase Variance
Purchase Variance
Not applicable
Not applicable
Not applicable
Not applicable
Sales
Cost of Goods Sold
Inventory
Cost of Goods Sold
Purchase Variance
Purchase Variance
Not applicable
Not applicable
Not applicable
Not applicable
