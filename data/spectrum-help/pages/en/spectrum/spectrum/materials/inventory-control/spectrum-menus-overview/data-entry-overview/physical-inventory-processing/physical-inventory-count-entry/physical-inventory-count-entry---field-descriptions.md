---
title: "Physical Inventory Count Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry/physical-inventory-count-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry/physical-inventory-count-entry---field-descriptions"
---

# Physical Inventory Count Entry - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Import
Click this button to open the Import Counts from Text File screen. Use this screen to import inventory counts directly from a comma delimited text file.
The file layout for the text file should be set up in the format: Item Code or Part Number, Warehouse Code, Physical Count

Warehouse
The default warehouse code displays. Press Enter to enter inventory counts for the default warehouse. To enter inventory counts for a different warehouse, enter the warehouse code. Warehouse codes may be up to 10 characters long.

Item code
Enter inventory item code for the count is being entered. If you enter the same item for the same warehouse twice, the [Physical Count Adjustment window](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry/physical-count-adjustment-window) window opens automatically so that you can revise the count.
If the item code status is 'Not used,' entry will be disallowed.

Item cost
The system automatically proceeds past this field, although you can arrow back to this field to change the item cost as needed. If no cost is entered, this field is blank. However, the fields will have a hidden value that defaults from the standard cost entered in Inventory Item File Maintenance, however this cost will not display. This cost will only become important if the quantity counted exceeds the software quantity on hand. Costs entered in this screen will override the standard cost of the item when a positive variance occurs (more stock counted in the warehouse than on-hand, per Spectrum).
Note: If the costing method is Standard cost, this field will be
 view-only. During the Physical Inventory Update if no cost was entered here,
 Spectrum will look for a warehouse-specific standard cost when recording an
 increase to inventory. If no standard cost was recorded at the warehouse
 level, the standard cost from the Item Master Table will be used
 instead.

Count
Enter the item quantity that was counted. If this item was not found in the warehouse, enter 0. The unit of measure for entry in this screen is sell units. If an item code that has already been counted is entered again, the [Physical Count Adjustment window](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/physical-inventory-processing/physical-inventory-count-entry/physical-count-adjustment-window) window opens, showing the physical count-to-date and allowing entry of either additional count or the new total quantity.
