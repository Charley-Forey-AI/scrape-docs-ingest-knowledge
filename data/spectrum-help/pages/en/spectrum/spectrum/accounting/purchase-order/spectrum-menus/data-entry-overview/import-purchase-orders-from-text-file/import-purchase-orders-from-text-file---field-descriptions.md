---
title: "Import Purchase Orders from Text File - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/import-purchase-orders-from-text-file---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/import-purchase-orders-from-text-file/import-purchase-orders-from-text-file---field-descriptions"
---

# Import Purchase Orders from Text File - Field Descriptions

Use the table below for assistance when completing the fields on this screen.
Field/Button
Description

Batch
Enter the purchase order batch code.
 The default is the Operator ID.
G/L account
Enter the G/L account code.
Include transactions for P.O. numbers that already exist?
Select this checkbox to allow for
 duplicate purchase order numbers.
Warehouse
Enter the warehouse code for inventory
 items.
Set up inventory items?
Select this checkbox to allow set up
 of non-stock items as inventory items. If you select this checkbox, you should
 NOT use an exclamation point in front of your (currently) non-stock item. If
 you do, the item will be entered into inventory while including the exclamation
 point. If the Inventory Control module is not present,
 then the following conditions apply:

- Price-per-factor is not supported.

- The Inventory Item Master Table is not validated.

- All imported lines are treated as non-stock items.
 However, no exclamation point should be inserted into the beginning of
 the code.

- The import update does not use any information
 stored in the Item Code Maintenance screen.

Default item category
If the Set up inventory items checkbox
 is selected, enter a valid category code for the new inventory item.
