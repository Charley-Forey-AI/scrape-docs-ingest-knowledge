---
title: "Inventory Transaction Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-entry/inventory-transaction-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-entry/inventory-transaction-entry---field-descriptions"
---

# Inventory Transaction Entry - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Batch code
Enter the unposted inventory batch code in this field. The current operator code will default in this field, but can be changed. It is OK to assign the same batch code across entry screens.

Reference
Enter a unique transaction reference number, up to seven characters in length. If this field is left blank, the software will auto-assign the next requisition number.

Transfer Freight/Misc
Click this button to open the [Transfer Freight Misc. Charges](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-entry/transfer-freight-misc.-charges) window to allocate transfer costs across all lines in the grid with a transaction type of 'Transfer'. If there are no lines with this transaction type specified, this button will be unavailable.

Receipt Freight/Misc
Click this button to open the [Transfer Freight Misc. Charges](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-entry/transfer-freight-misc.-charges) window to allocate transfer costs across all lines in the grid with a transaction type of 'Receipt'. If there are no lines with this transaction type specified, this button will be unavailable.

Details

Item code
Enter the item code.

- If an invalid item is entered, the Search Inventory Items
 window will open to allow you to build a non-stock item code.

- If the item code status is 'Not used,' entry will be disallowed.

Description
The item code description displays in this field.

Tran type
Select a transaction type for this entry:

- Adjustment

- Transfer

- Cost adjustment

- Receipt

The transaction type selected in this field will determine the behavior of the rest of the fields in this screen. Refer to the table below for specific transaction behavior types.

Warehouse
Enter the warehouse code for the item. The warehouse code will default when adding multiple rows on this screen.

Date
Press Enter to accept the Inventory Control Processing Date as the transaction date. Otherwise, a different date may be entered. The date entered here will default when adding multiple rows on this screen.

U/m
The sale unit of measure displays in this field.

Quantity
Enter the quantity by which the current quantity-on-hand is to be adjusted. A positive entry means the quantity is in the warehouse; and a negative entry means the quantity is out of the warehouse.
Note: No entry will be allowed for cost adjustment transaction
 types.

Unit cost
For receipts and adjustments, if the quantity is not zero, the warehouse-specific standard cost will default, but allow entry of a new value. If the quantity amount is zero or blank, the cost will be read from Item Main Properties.
If the costing method is 'Standard cost,' the standard cost will display in this field by default.

Message
Enter a message related to the inventory transaction, if desired.

Department
Enter the department from which to transfer inventory. The department will default as follows:

- Category table

- Warehouse table

- Previous row, if the transaction type is not a transfer

The department code will default from the previous row when adding multiple rows at the same time.
Note: For transfer transaction types, this field will be
 display-only and the department will not be saved to the database.

G/L account
Enter the G/L account to be credited. The G/L account code will default when adding multiple rows on this screen. If this is a 'Transfer' entry, this field will be skipped.
If this is a 'Cost adjustment' entry, the G/L account will default from the G/L Department table.

Cost adjustment
If this is a 'Cost adjustment' entry, enter a non-zero value in this field to add a fixed dollar amount to the value of a specific inventory item and therefore increasing the unit cost of that item.
Click the lookup icon to open the Cost Adjustment Inquiry
 window.

- If the costing method is 'Standard cost,' the Price Variance Entry version of this window will open allowing you to enter a standard cost amount.

- For all other costing methods, the inquiry window will allow you to enter an average cost.

Source code
If this is a 'Cost adjustment' entry, enter the source code for cost
 adjustment. Source codes must have been previously defined in Cost
 Adjustment Source Maintenance.

Transfer to WH
If this is a 'Transfer' entry, enter the code of the warehouse to which the inventory is being transferred.

Transfer to dept.
If this is a 'Transfer' entry, enter the code of the department to which the inventory is being transferred.
The department code will default as follows:

- Category table

- Warehouse table, based on the warehouse code entered in the Transfer to WH field above

- Blank

Qty in extension
The quantity times unit cost amount displays in this field.
