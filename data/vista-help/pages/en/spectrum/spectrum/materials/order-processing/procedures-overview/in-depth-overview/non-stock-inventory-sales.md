---
title: "Non-Stock Inventory Sales | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/non-stock-inventory-sales"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/procedures-overview/in-depth-overview/non-stock-inventory-sales"
---

# Non-Stock Inventory Sales

Non-stock items are pieces of merchandise that are not standard items in your warehouse and therefore do not have associated item codes. Since this merchandise is never received into inventory, different procedures are required to ensure the proper recording of the sales and receipts transactions.
The procedure utilized in Spectrum will vary depending upon whether the Purchase Order module is in use or not.
Two options are presented below for each condition. The user's decision needs to be based on a review of current personnel and procedures. Regardless of the option selected for non-stock transactions, it is necessary to enter the cost of the non-stock item during Order Entry and Invoice Entry in order to correctly track amounts in the General Ledger and Order Processing.
If Purchase Order IS installed on the system:
Option 1 Enter an inventory category code followed by an exclamation point (!). This must be a valid category in The Inventory G/L Department File Maintenance screen and must refer to a G/L department which "sells" out of a non-stock clearing account rather than the inventory valuation account. This will be the default G/L department for that line item. Purchase Order Entry should have the Non-Stock Clearing Account when adding the P/O.
advantages Ability to track non-stock sales by category in Sales Analysis and properly records in the General Ledger. The G/L account titled "Inventory" will contain only stock item transactions; therefore, it will be easier to balance the General Ledger with the subsidiary ledger.
disadvantages Requires entry of the non-stock G/L department code during Order Entry and Invoice Entry.
Option 2 Sales/Invoice entry procedure is the same as Option 1 above, except the regular G/L department is used. The Purchase Order clerk will record the regular Inventory G/L account when adding the Purchase Order.
advantages Requires no change in Order Entry, Invoice Entry or Purchase Order Entry.
disadvantages The General Ledger account titled "Inventory" will represent both stock and non-stock assets, and the G/L will not balance with the subsidiary ledger without reconcilement of non-stock amounts.
The Inventory G/L Department File Maintenance screen should be completed based on the drop-ship option selected:
Option 1
Option 2

G/L department code
ZZZ
ABC

Description
Non-Stock Category
Standard Sales

G/L Accounts:
Sales
Cost of sales
Inventory (non-stock)
Adjustments
Credit returns
Receipts
JC markup
JC direct cost
Mix usage
Equipment cost
Sales
Cost of Goods Sold
Non-Stock Clearing
Cost of Goods Sold
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Sales
Cost of Goods Sold
Inventory
Cost of Goods Sold
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Not Applicable
Not Applicable

If Purchase Order is NOT installed on the system:
Option 1 Enter an inventory category code followed by an exclamation point (!). This must be a valid category in The Inventory G/L Department File Maintenance screen and must refer to a G/L department which "sells" out of the purchase variance account rather than the inventory valuation account. This will be the default G/L department for that line item. (For additional information about Purchase Variance accounts, refer to the discussion of this topic in this chapter.)
advantages Ability to track non-stock sales by category in Sales Analysis and properly records in the General Ledger.
disadvantages Requires entry of the non-stock G/L department code during Order Entry and Invoice Entry.
Option 2 Sales/Invoice entry procedure is the same as Option 1 above, except the regular G/L department is used. The A/P clerk will post the invoice to the inventory G/L account when the invoice is recorded in A/P, since it was never received in inventory (through IC receipts transactions).
advantages Requires no change in Order Entry and Invoice Entry.
disadvantages Accounts Payable clerk will need to isolate non-stock items from stock items during A/P invoice processing.
The Inventory G/L Department File Maintenance screen should be completed based on the drop-ship option selected:
Option 1
Option 2

G/L department code
ZZZ
ABC

Description
Non-Stock Category
Standard Sales

G/L Accounts:
Sales
Cost of sales
Inventory (non-stock)
adjustments
Credit returns
Receipts
JC markup
JC direct cost
Mix usage
Equipment cost
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
