---
title: "Material Markup File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/material-markup-file-maintenance/material-markup-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/material-markup-file-maintenance/material-markup-file-maintenance---field-descriptions"
---

# Material Markup File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Description

Material markup
Enter a material markup code here. The
 markup code entered here will be used when the software calculates the unit
 price from the cost of a material item when added into Material
 Entry or the detail windows of Purchase Order
 Entry or Accounts Payable > Invoice/Credit Memo Entry.
Description
Enter a description for the markup
 item.
Type
Select a markup type: Amount or Percent
Effective date
Enter a from/to effective date range
 for the markup item. These dates do not need to be restricted based on
 processing dates or the fiscal calendar.
Mark up non-stock material? Mark up stock (inventory) material?
Select the checkbox to mark up
 non-stock and/or stock (inventory) materials.
Properties

Minimum unit cost basis
This column will be read only. The
 first entry will always be 0.00, and additional line entries will be one penny
 more than the maximum cost basis from the previous line.
Maximum unit cost basis
Enter a maximum cost basis for the
 markup item in this field. Subsequent line entries must be larger than the
 previous line. The operator is permitted to leave the
 last cost basis line blank or enter 99,999,999 to allow 'unlimited' range
 during the price calculation.

Non-stock markup Stock markup (inventory)
Enter a markup amount for each maximum
 cost basis line entry for non-stock and/or stock (inventory) items. These
 fields permits the operator to enter a zero or negative markup value. The format of these fields is determined by the
 Type selected
 above:

- When "Amount" type is selected, the operator will
 enter a dollar amount to add to the cost.

- When "Percent" type is selected, the operator will
 enter a percentage to add to the cost basis.
