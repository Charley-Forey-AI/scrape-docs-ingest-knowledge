---
title: "Site Material Pricing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/inquiries-overview/site-material-pricing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/inquiries-overview/site-material-pricing"
---

# Site Material Pricing

Use the Site Material Pricing screen
 to review information on the various prices offered to customers for specified inventory
 items.
Field
Description

Site
Enter a site code. This field can be
 left blank for quote purposes, but then no special pricing will be shown.
Item code
Enter an inventory item code. This
 field will permit entry of a non-stock code.
Warehouse
Enter a warehouse code.
Category
The item category displays in this
 field.
Effective date
This date will default to the current
 Work Order processing date. Change the effective date to re-calculate totals on
 this screen.
Stock quantity
If the current work order
 or specified customer/site is a non-stock code, the software will search for a
 non-stock markup code from the Site first. If not specified there, the Customer
 markup code will be applied. The Work Order Installation
 markup code will be used as a last option. If no location has a non-stock
 markup code specified, the Unit price will be set to zero. If the non-stock
 markup flag is not set to 'Yes' for the current code, this window will display
 as if no markup code is present on the work order.If the
 selected item is an inventory stock item, the software will search for a
 non-stock markup code from the Site first. If not specified there, the
 Customer markup code will be applied. The Work Order
 Installation markup code will be used as a last option. If no
 location has a non-stock markup code specified, the Unit price will be set
 to zero. If the non-stock markup flag is not set to 'Yes' for the current
 code, the following fields will be available:

- The Stock quantity field will be available to specify
 quantity value for the item.

- The Unit of measure will display the 'Sell unit of measure'
 from the Inventory master table.

- The Unit cost will default from the inventory standard cost,
 but a different cost basis can be entered as desired.

Unit of measure

Unit cost

Item summary

Quantity available
The current available quantity of this
 item at the specified warehouse displays.
Lowest price
The customer's "best" price displays.
 This is also the price per item that would be offered by the software during
 Quote Entry, Order Entry or Invoice Entry. This is the lowest price among price
 tables, special pricing and promotional prices.
Method
The method the software used to arrive
 at the lowest price is displayed, for example, LIST, PROMOTIONAL PRICE, and so
 forth.
Current quantity

On hand
The current total quantity on hand of
 the item at the specified warehouse displays.
Committed
The current total quantity of items
 committed for sale from the specified warehouse displays. This number is updated from entry in Inventory Control > Job Requisition Entry, Work Order Material Entry,
 Order Entry, Invoice Entry,
 and Inventory Control > Mix Assembly Transaction Entry.

On order
The current total quantity of items on
 order from supplier (shown in purchase units) to the specified warehouse
 displays.
Price table

Price (list)
The established price
 levels (1-5) for this customer displays, and the customer's price level will
 display below.
Price level

Quantity breaks

Quantity
The quantity at which each price break
 occurs is displayed.
Amount
The amount of each quantity discount is
 displayed.
Date range
The effective date range for the
 applicable table displays in these fields.
Material markup

Unit price
The unit price for the material markup
 item (if specified) displays in this field. The software
 will search for a non-stock markup code from the Site first. If not
 specified there, the Customer markup code will be applied. The
 Work Order Installation markup code will be used
 as a last option. If no location has a non-stock markup code specified, the
 Unit price will be set to zero.

Total price
The total price for material markup
 items (if specified) displays in this field, computed using the Unit price,
 Quantity and Unit of measure amounts.
Date range
The effective date range for any
 material markup items (if specified) display in these fields.
Special price

Amount
The special price amount for this item,
 for this customer displays, if applicable.
Date range
The first and last allowable dates for
 special pricing display in these fields.
Promotional price

Amount
The promotional price for this item
 displays, if applicable.
Date range
The first and last allowable dates for
 promotional pricing display in these fields.
