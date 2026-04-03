---
title: "Inventory Count Listing Screen - Warnings and Errors | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry/inventory-count-listing-screen---warnings-and-errors"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry/inventory-count-listing-screen---warnings-and-errors"
---

# Inventory Count Listing Screen - Warnings and Errors

View the Inventory Count Listing Screen warnings and
 errors.
Message
Explanation

Warehouse is invalid
The Warehouse code included in the file is not valid.

Warehouse is missing
The Warehouse code was not included in the file.

Inventory item is invalid
The Item code included in the file is not valid.

Inventory item is not in the warehouse
The Item code is not set up in the warehouse.

Physical count is missing
The physical count of items was not included in the import file.

Physical count has already been updated
This message occurs when you have already imported and updated item counts and
 attempt to import the quantity file in again. The import process is
 cancelled and the quantities are not updated again.
This happens when the user attempts to reimport the file after it has been
 updated in the system, but before the physical inventory cycle has been
 cleared.

Warning: The count will be adjusted for this item
Multiple files have been imported using the same item + warehouse. These
 counts will be adding together, thus changing the item count.
