---
title: "Determining the Best Material Price | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-hierarchies/determining-the-best-material-price"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-hierarchies/determining-the-best-material-price"
---

# Determining the Best Material Price

This flowchart depicts the process to determine the best
 material price for Work Order materials.
This calculation will determine the best material price based on the type of item (stock or
 non-stock), whether the work order is setup for flat rate or Time & Material pricing,
 whether the Inventory Control module is present, and which screen the operator is currently
 using.

## Method 1 - Non-Stock Material Pricing

The software will first determine the non-stock markup code to use for the price calculation, using the [Non-Stock Markup Hierarchy](/en/spectrum/spectrum/service/work-order/spectrum-hierarchies/non-stock-markup-hierarchy). The software will then calculate the non-stock price based on 'unit cost' (before sales tax). The cost basis of the material transaction is computed by multiplying the Quantity times the Unit cost. The cost basis is then used to determine which break point to use from the non-stock markup table. If the markup type is 'Amount', the Unit cost is added to break point value from the non-stock markup table to determine the Unit price. If the markup type is 'Percent', the Unit cost is added to the cost basis of one unit multiplied by the break point value stored in the non-stock markup table and divided by 100 to determine the Unit price.

## Method 2 - Inventory Stock Item Pricing

The software will search for the lowest stock price from the following five sources. The software does not combine discount pricing, but rather looks for the lowest price among these sources to use for Unit price.
Item Price
Price level (1-5)
Lowest Price

Quantity Discount Price

1. Quantity discount for item

1. If not found, then find quantity discount for
 category

Special Price

1. 'Customer's Job' special price for item

1. If not found, then find 'Customer's Job' category
 special price

1. If not found, then find special price for item

1. If not found, then find special price for
 Category

Promo Price
Promotional discount

Markup Price
Material markup

## Method 3 - Work Order Item Pricing

When the Inventory Control module is not present, the Unit price will default
 from the stored price in System Administration > Materials.
