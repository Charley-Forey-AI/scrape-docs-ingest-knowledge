---
title: "Quantity Breaks File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/quantity-breaks-file-maintenance/quantity-breaks-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/quantity-breaks-file-maintenance/quantity-breaks-file-maintenance---field-descriptions"
---

# Quantity Breaks File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Code type
Select the type of quantity break information: specific inventory Item or product Category.

Item/category code
If Item was selected in the Break record type field, enter the item code. If Category was selected in the Break record type field, enter the product category code. The item/category code must have been previously defined in either Inventory Item File Maintenance for items, and Category File Maintenance for category codes.

Description
Enter a description for the inventory item or product category.

Effective from
Enter the date on which this quantity break takes effect. The quantity break will be applied if the transaction date is on or after this date. Entry in this field is required.

Effective to
Enter the date this quantity break ends. The quantity break will be applied if the transaction date is on or before this date. Entry in this field is required.

Quantity break type
Select the type of quantity break: Discount % or Price.

Quantity
Enter the sell quantity at which the price changes. Up to 10 different quantities may be entered.

Break value
Enter the discount percentage (100% or less) or the price associated with each quantity break point. When the quantity of items ordered reaches the quantity shown, prices will be affected by the associated break value.
Examples:
 If "Discount" percent break value increases with a greater percentage discount, then:
10 qty 1.00 %
 20 qty 5.00 %
30 qty 7.00 %
 If "Price" discount break value diminishes with smaller prices, then:
 10 qty $5.00
20 qty $4.85
30 qty $4.60
