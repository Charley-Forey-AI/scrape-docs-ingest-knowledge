---
title: "Set Physical Inventory Status | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/set-physical-inventory-status"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/set-physical-inventory-status"
---

# Set Physical Inventory Status

At the time of a physical inventory, it is necessary to
 cease normal operations in order to accurately count all items at once.
The company must not be taking receipt of
 additional stock or removing items being sold. This update disables the Inventory
 Transaction Report and the Order Processing Invoice Register Report to ensure that changes
 cannot be made to inventory while the physical inventory is being performed. Once the
 physical inventory is complete and the [Clear Physical Inventory Status ](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/clear-physical-inventory-status) has been run, operators can resume entering inventory
 transactions.
It is not possible to backdate physical inventory adjustments to a period after which inventory activity has taken place, therefore it's vital that the Physical Inventory process be completed as close to the fiscal and count date as possible. For example, if you are counting all your inventory as of 12/31/xx, it's recommended that the Physical Inventory Status Update be performed for all warehouses after all transactions through 12/31/xx are updated; January activity should not be updated before the Physical Inventory Status Update is performed. Once the update is complete, the [Physical Inventory Count Entry](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry) should be completed to compare the current quantity on hand, which will calculate the adjustment the Physical Inventory update will make.
For example, suppose item 100 had a quantity-on-hand count of 6 at 12/31/07 and a quantity on hand count of 4 at 2/15/07. If the Physical Inventory process is not performed until February 2007, a count of 5 would produce a positive adjustment of 1 (5 count compared to 4 current quantity-on-hand). When the Physical Inventory process is performed in a timely manner shortly after 12/31, it would produce a correct negative adjustment of 1 (5 count compared to 6 quantity on hand). To make this easier, the Physical Inventory Status Update can be performed on one warehouse at a time. In our example, items in warehouse 1 can be counted and updated at the end of fiscal period 5, while warehouse 2 can be counted and updated at the end of fiscal period 7.
Be sure that both the Inventory Transaction Report and the Invoice Register Report have been updated before continuing with this update.
Once the status has been set, Physical Inventory Status Update cannot be selected again before the current physical inventory process is complete. If an attempt is made to select this option, a warning message will display.
A physical inventory can be canceled by running the Physical Inventory Clear selection on the Physical Inventory menu.
Field
Description

Warehouse
To include all warehouses in the physical inventory, press Enter. To perform a physical inventory at a particular warehouse, enter that warehouse code or double-click in this field to select from a list of valid warehouse codes. Warehouse codes may be up to 10 characters long.
