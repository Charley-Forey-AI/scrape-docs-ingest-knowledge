---
title: "Work Order Material - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/field-tech/work-order-main/work-order-material/work-order-material---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/service/field-tech/work-order-main/work-order-material/work-order-material---field-descriptions"
---

# Work Order Material - Field Descriptions

Use the table below when completing the fields on this screen.
Field
Description

Item
Enter an inventory item code, stock or non-stock.
Note: If the item code has a status of 'Not used', entry is disallowed.

Description
For stock items, the selected item description will automatically display in this field. For non-stock items, enter a description.

Warehouse
If a Truck Warehouse code was defined in Technician Maintenance, this code will default here and auto-repeat when more lines are added.
If no Truck Warehouse code was specified, the warehouse code for the material entry transaction will default here. No changes are allowed when editing material transactions.

Quantity
 Enter a quantity for the selected inventory item. The quantity can be left blank and the material will not be billed, even if an invoice extension is entered.
If the quantity is changed, the software will automatically recalculate the unit price.

U/m
For stock items this field will be display-only. For non-stock items, enter a unit of measure.

Billed?
If the material has already been invoiced, 'Yes' will display in this field. If not, this field will remain blank. No entry is allowed.

Phase
Enter a phase code for the work order. The Phase description will display to the right of this column. The phase code will default if an existing material record is already added to this work order.
Note: This column is hidden if this is a Site work order.

Ct
Enter a cost type for the work order. Spectrum will verify that the phase + cost type are valid for the current job.
Note: This column is hidden if this is a Site work order.
