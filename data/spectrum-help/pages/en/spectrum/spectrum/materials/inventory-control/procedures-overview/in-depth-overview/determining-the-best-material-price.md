---
title: "Determining the Best Material Price | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/procedures-overview/in-depth-overview/determining-the-best-material-price"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/procedures-overview/in-depth-overview/determining-the-best-material-price"
---

# Determining the Best Material Price

This flowchart depicts the process to determine the best material price for Work Order materials. This calculation will determine the best material price based on the type of item (stock or non-stock), whether the work order is setup for flat rate or Time & Material pricing, whether the Inventory Control module is present, and which screen the Operator is currently using.

Method 1 - Non-Stock Material Pricing
The software will first determine the non-stock markup code to use for the price calculation. The software will then calculate the non-stock unit price. The cost basis of the material transaction is computed by multiplying the Quantity times the Unit cost. The cost basis is then used to determine which break point to use from the non-stock markup table. If the markup type is 'Amount', the Unit cost is added to break point value from the non-stock markup table to determine the Unit price. If the markup type is 'Percent', the Unit cost is added to the cost basis of one unit multiplied by the break point value stored in the non-stock markup table and divided by 100 to determine the Unit price.
Method 2 - Inventory Stock Item Pricing
The software will search for the lowest price from the material level stored in the Work Order header, quantity discount codes for the specified item, customer special pricing codes for the specified item and Customer's job, and discount code for the specified item. The software does not combine discount pricing, but rather looks for the lowest price among these sources to use for Unit price.
Method 3 - Work Order Item Pricing
When the Inventory Control module is not present, the Unit price will default from the stored price in the Work Order material item table.
