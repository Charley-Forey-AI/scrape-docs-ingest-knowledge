---
title: "Inventory Items - Add new inventory item | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/inventory-items/inventory-items---add-new-inventory-item"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/inventory-items/inventory-items---add-new-inventory-item"
---

# Inventory Items - Add new inventory item

Use the table below for reference when completing the
 fields on this screen.
Field/Button
Description

Category
Enter the category code to which this item belongs. The
 product category must be previously defined in Category File
 Maintenance. A pull-down list is available for viewing valid
 inventory categories.

Item code
Enter the item code. The code may be any combination of
 letters and numbers.
Note Regarding Numeric Coding
Because many Spectrum users prefer alphabetic or
 combination alpha and numeric coding, the Item code field is not a
 numeric-only field and automatically aligns to the left. If you prefer a
 strictly numeric coding scheme, use leading zeros when adding codes in order
 to achieve a uniform format. Without leading zeros, 1, 10, or 100 will
 appear before 2, 20, or 200. Instead, set up the codes as 001, 002, and so
 forth. If more than 1000 codes are anticipated, enter each code as 0001,
 0002, and so forth.

Description
Enter a description of the item. This description will
 print on purchase orders, sales orders and invoices. It will also be
 displayed on the screen whenever the item code is referenced.

Set up this item in all
 warehouses?
Select this checkbox to add items to all warehouses.

Purchase

Standard cost
Enter the usual cost of this item from the vendor. This
 is the cost used throughout the software for default purposes and when the
 standard costing method is specified.
The date this field was last changed is saved, but is
 updated with the current processing dateany time the standard cost is
 amended using a related screen (such as Inventory Transaction Update,
 Purchase Order Receiving, and so forth). In addition, if changes are made to
 the Price-per-factor field, the standard cost is automatically
 reset to $0.00.

U/m conversion
The conversion factor is used to convert the purchase
 unit of measure into the sell unit of measure:
Purchase
 unit of measure ÷ sell unit of measure = conversion
 factor
Examples:

-  Items that are purchased by the dozen and sold in
 singles have a conversion factor of twelve (12 ÷ 1 = 12).

- Nails might be purchased by the case, with 10 boxes
 per case and 500 nails in each box, then sold by the box. The u/m prch
 would be CS, the u/m-sell would be BX, the conversion would be 10, and
 the price per factor would be 500 (sales price per 500).

Unit of measure
Enter an abbreviation for the unit of measure used when
 this item was purchased. For example, PR for pairs, DZ for dozen, SL for
 sling, or EA for each.

Sell

List price
You may assign up to five prices to each inventory item.
 Customers are assigned a price level (1-5) in the mat level field of the
 Customer File Maintenance screen for use with the
 Work Order, Order Processing Materials Management, or Time + Material
 modules; this amount defaults when the customer price level is 1 or is
 blank. The item discount in the discount code field is applied only to the
 first item price, which is considered the list price.

Price per factor
Price per factor represents the total number of items
 being sold at price level 1-5. For example, for an item with a price per
 factor of 100 and a list price of $35, when 100 units are sold to a
 customer, the price will be $35. When entering the quantity sold, 100 units
 are recorded. The unit price is $35. The extension is $35 for the 100 units,
 and is determined by this formula:
Units sold ÷ price per factor X unit price =
 extension
Example #1: sell 100 units ÷ 100 X 35 = $35.00
Example #2: sell 1 unit ÷ 100 X 35 = $00.35
Example #3 sell 250 units ÷ 100 X 35 = $87.50
The price per factor also applies identically to standard
 cost, and computation of the actual costs during processing.
The default for this field is 1.0000. Other typical
 entries are 100.0000 and 1000.0000. You may enter another factor when
 appropriate, but whenever a change is made to this field, a warning message
 will display to remind you that any transactions currently recorded for this
 item will be affected by changes made here. Furthermore, if changes are
 made, the Standard
 cost field and Price fields will automatically be reset to $0.00 for this
 item.

Unit of measure
Enter an abbreviation for the unit of measure used when
 this item was sold. For example, PR for pairs, DZ for dozen, SL for sling,
 or EA for each.
