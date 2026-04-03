---
title: "Mix Processing - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/mix-processing/mix-processing---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/mix-processing/mix-processing---field-descriptions"
---

# Mix Processing - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Batch code
Enter the unposted inventory batch code in this field. The current operator
 code will default in this field, but can be changed. It is
 OK to assign the same batch code across entry
 screens.

Reference
Enter the mix transaction number, or press Enter for the next sequential transaction number.

Item code
Enter the mix item code previously set up in Mix Maintenance for this transaction.

- If an invalid item is entered, the Search Inventory Items window will open to allow you to build a non-stock item code.

- If the item code status is Not used, entry will be
 disallowed.

To warehouse
Enter the warehouse where the item code will be updated, or press Enter to accept the default warehouse. Warehouse codes may be up to 10 characters long.

Quantity
Enter the quantity of desired assembly mixes.

Date
Enter the date of the transaction, or press Enter to accept the current Inventory Control processing date.

Details

Line
Line numbers are assigned and maintained by the software. No entry is allowed.

Component item
The component item codes display. Entry in this field is allowed; however, if
 the number of components entered exceeds the number of components available,
 this warning message will display: QUANTITY USED IS MORE THAN THE
 QUANTITY AVAILABLE.
Another warning message will display if any components in the normal mix have a zero standard cost.

- If an invalid item is entered, the Search Inventory Items window will open to allow you to build a non-stock item code.

- If the item code status is Not used, entry will be
 disallowed.

Description
The component description displays.

From warehouse
The warehouse from which this item is to be taken displays, once a line is created this field may not be changed. The line must be deleted, and a new one added.
More info
 If the item in the Component field is not stored in the warehouse selected in
 the Whs field, the following warning displays: WARNING – Item
 Does Not Exist In Warehouse. To correct this warning, select
 a different warehouse or set up the item in an alternate warehouse in
 Item Detail File Maintenance.

U/m
The unit of measure displays in this field.

Qty per mix
The quantity needed per mix displays, but may be changed, if desired.

Total qty used
The total quantity used displays (quantity per multiplied by the quantity to be mixed).

"Before" qty available
The quantity available before the mix is produced displays.

"After" qty available
The quantity available after the mix is produced displays.

Alert
If the quantity is negative, a message will display in this field.
