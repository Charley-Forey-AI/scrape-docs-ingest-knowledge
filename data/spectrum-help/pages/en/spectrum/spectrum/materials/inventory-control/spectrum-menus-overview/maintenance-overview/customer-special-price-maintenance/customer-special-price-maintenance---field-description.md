---
title: "Customer Special Price Maintenance - Field Description | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/customer-special-price-maintenance/customer-special-price-maintenance---field-description"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/customer-special-price-maintenance/customer-special-price-maintenance---field-description"
---

# Customer Special Price Maintenance - Field Description

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Customer code
Enter the customer code. Entry in this field is required, and is prevented if the customer status is 'Not used'. A warning is provided when the status is 'Inactive'.

Customer's job
Enter the customer's job number in this field.

Item/category code

- If a new item code is being added, click the New Item button and specify the inventory item code in this field. This code must have been previously defined in Inventory Item File Maintenance. If the item status is set to 'Not used', entry will be disallowed.

- If a new category code is being added, click the New Category button and enter the category code in this field. This code must have been previously defined in Category File Maintenance.
Note: Category codes are automatically stored with an exclamation
 point (!) as the first character. This character does not need to be
 added.

Pricing method
To enter a special price, select Price. To enter a special discount multiplier, select Discount. To enter a price table code (from 1 to 5), select Price table code.
Categories may have a discount multiplier or a price table code, not a special price.

Amount / Multiplier / Price level
If the selected pricing method is Price, the Amount field displays. Enter the amount for the specified item. When the special price is computed as a price, then the software sets the Sell price to the price specified here.
If the selected pricing method is Discount, the Multiplier field displays. Enter the discount multiplier for the specified item or category. When the special price is computed as a percent discount, then the software computes the Sell price by reducing the Inventory Item Master table price for the applicable price level (1-5) by the multiplier entered here. Example of a 0.9000 multiplier for an item with a regular price of $6: $6 x 0.9000
 If the selected pricing method is Code, the Price level field displays. Enter the price table level number from 1 to 5 for this item or category. When the special price is computed as a price level code, then the software computes the Sell price by referring to the alternate price level (1-5) in the Inventory Item Master table instead of the price level specified in the work order header.

Effective dates
Enter the date the special price begins and ends for the specified customer. The special price will be applied if the transaction date is on or between these dates. Entry in these fields is required.

Message
Enter the message relating to this special pricing entry, if desired.
