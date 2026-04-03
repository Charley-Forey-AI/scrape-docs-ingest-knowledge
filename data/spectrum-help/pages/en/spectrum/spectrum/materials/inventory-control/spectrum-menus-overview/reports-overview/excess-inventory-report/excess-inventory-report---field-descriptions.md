---
title: "Excess Inventory Report - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/reports-overview/excess-inventory-report/excess-inventory-report---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/reports-overview/excess-inventory-report/excess-inventory-report---field-descriptions"
---

# Excess Inventory Report - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Warehouse
Enter a valid warehouse code, or press Enter to print inventory for all warehouses. Warehouse codes may be up to 10 characters long.

Item code
Enter an item code, or press Enter to print ALL codes.

Item category
Enter the number of the category to be included on the report, use the SuperSelect options, double-click in this field to select from a list of valid category codes, or press Enter to include ALL.

Through date
Enter the date through which to print, or press Enter to accept the current Inventory Control processing date.

Months to use
Enter the number of months (1-24) to be included on this report. This is the number of previous months that the report uses to determine sales volume. Complete, full months are used to determine the volume of sales; the report pulls the specified number of months preceding the date specified as the "through date."
Example 1: Number of Months specified: 6 Through Date: 9/15/04 The report will include all sales activity from 3/1/04-8/31/04
Example 2: Number of Months specified: 12 Through Date: 12/31/04 The report will include all sales activity from 12/1/03-11/30/04

Months of excess
Enter the number of months of average usage for excess inventory. This is the Total Cost (Number of Months of Excess multiplied by Average Monthly Use multiplied by Standard Cost). The 'Standard Cost' is the number entered in Inventory Item File Maintenance as the approximation of the current cost. The 'Excess' is the dollar amount of the Total Cost that exceeds the value needed to cover the 'Number of Months of Excess' specified for the report.

Sort by
Select the order in which the report is to be sorted: by Item code, by Category code, or in Descending order of number of months in stock.

Status
Select whether to print Active,
 Discontinued, and/or Not used items.
Note: Items are designated as "discontinued" in the Inventory Item Maintenance
 screen. The Discontinued checkbox only affects Order Processing orders
 and invoices, and if an operator attempts to use a discontinued item, a
 warning message will display in the Order Processing > Invoice Entry, Order Entry, and Quote
 Entry screens (Work Order, Purchase Order, and Inventory
 Control job requisitions are not impacted).

Quantities to print
Select the report type to be printed. This indicates the quantities that will be included:

-  Positive/negative (exclude zero quantities)

- Positive quantities only

-  Negative quantities only

- Zero quantities only

- All quantities (positive, negative, and zero)
