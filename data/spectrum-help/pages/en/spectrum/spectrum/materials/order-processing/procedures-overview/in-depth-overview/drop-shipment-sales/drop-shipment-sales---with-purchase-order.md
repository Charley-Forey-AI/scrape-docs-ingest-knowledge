---
title: "Drop Shipment Sales - With Purchase Order | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/drop-shipment-sales/drop-shipment-sales---with-purchase-order"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/drop-shipment-sales/drop-shipment-sales---with-purchase-order"
---

# Drop Shipment Sales - With Purchase Order

If Purchase Order is installed on the system, one of the following drop shipment recording methods should be implemented, based on your company's procedures and personnel.
Important: The Purchase Order Receiving will update the inventory on hand quantities. It
 is recommended to use a separate warehouse code for Drop Shipment Purchases so that the
 quantities can be periodically cleared. The Inventory Control > Utilities > Delete Items in Warehouse will allow for easily clearing all items in a designated warehouse
 code.Option 1 Enter
 orders and invoices (make sure the Drop
 Ship checkbox is selected in the Order Entry > Order Details window). Enter a G/L department code that sells out of the Drop Ship
 Clearing Account rather than the inventory valuation account.Advantages: The General Ledger account titled Inventory will contain any amount
 actually stored in the warehouse; therefore, it will be easier to balance the General
 Ledger with the subsidiary ledger.Disadvantages: It requires a change in procedure for the Sales and
 Order Entry staff. It also requires a special G/L department code entry during Invoice
 Entry and Order Entry. The Purchase Order clerk must use/enter the Drop Shipment
 Clearing Account when adding the Purchase Order.Option 2 Use the same order/invoice entry as in procedure as Option 1, except use the regular G/L department code. The Purchase Order clerk will record the regular Inventory G/L account when adding a Purchase Order.Advantages: It requires no change in Order Entry, Invoice Entry or
 Purchase Order Entry procedures. Disadvantages: The General Ledger account titled Inventory will represent both
 Warehouse and Drop Ship assets, and the General Ledger will not balance with the
 subsidiary ledger without reconcilement of Drop Ship amounts.The Inventory Control G/L Department File Maintenance
 screen should be completed based on the drop ship option selected:
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
Drop Ship Clearing
Cost of Goods Sold
Not applicable
Not applicable
Not applicable
Not applicable
Not applicable
Not applicable
Sales
Cost of Goods Sold
Inventory
Cost of Goods Sold
Not applicable
Not applicable
Not applicable
Not applicable
Not applicable
Not applicable
