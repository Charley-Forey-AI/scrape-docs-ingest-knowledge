---
title: "Category File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/category-file-maintenance/category-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/category-file-maintenance/category-file-maintenance---field-descriptions"
---

# Category File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Category code
Enter the category code.
Because many users prefer alphabetic or combination alpha and numeric coding, this code is not a numeric-only field. Because of this, the code left-justifies when entered. Users preferring a strictly numeric coding scheme should be advised to use leading zeros when adding codes in order to produce desired sort results on screens and reports. Without leading zeros, '01', '10', '100' will appear before '2', '20', '200'. Instead, codes should be set up '001', '002', and so forth. If more than 1000 codes are anticipated, instead enter '0001', '0002', and so forth.

Description
Type the description of the category (for example, Lumber, Concrete, Nuts & Bolts, and so forth).

Costing method
The system defaults to the costing method set up during Inventory
 Control Installation. Press Enter to accept the
 default or enter one of the following codes for the costing method of the
 type of product being defined:

- F - First-In-First-Out

- L - Last-In-First-Out

- A - Average Cost

- S- Standard Cost
Important: Once items are on-hand the costing method should not be
 changed.

Multiplier
Enter the percentage multiplier for standard cost. This is used during the Price Update (for example, 70% of list).
Use the category multiplier for setting either the cost or the list price with the Quick-Link. The system multiplies the list price by the multiplier to calculate the cost; otherwise, it will divide the cost by the multiplier to calculate the price. The original price import load only has the option of setting the standard cost from the category multiplier list price.

G/L department
Enter the inventory General Ledger department code for this category. The
 default hierarchy is as follows: The system first looks to the
 Category File Maintenance for the G/L department
 code. If the field is blank, the software will then look to the
 Warehouse File Maintenance. If this is also blank,
 the user will be prompted to enter a valid code.

Item mask
Enter the item mask, for example, XXXX.

Next item code
Enter the next available item sequence number.
