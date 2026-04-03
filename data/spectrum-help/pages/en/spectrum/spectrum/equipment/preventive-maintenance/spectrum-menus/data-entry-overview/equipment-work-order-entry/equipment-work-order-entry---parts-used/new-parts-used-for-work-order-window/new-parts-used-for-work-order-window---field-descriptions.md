---
title: "New Parts Used for Work Order window - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/data-entry-overview/equipment-work-order-entry/equipment-work-order-entry---parts-used/new-parts-used-for-work-order-window/new-parts-used-for-work-order-window---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/preventive-maintenance/spectrum-menus/data-entry-overview/equipment-work-order-entry/equipment-work-order-entry---parts-used/new-parts-used-for-work-order-window/new-parts-used-for-work-order-window---field-descriptions"
---

# New Parts Used for Work Order window - Field Descriptions

Use the table below when completing the fields on this
 screen.
Fields
Descriptions

Equipment
The code and description associated
 with the selected piece of equipment default from the New/ Edit
 Equipment Work Order window.
Work order
The work order number associated
 with the selected piece of equipment defaults from the New/ Edit
 Equipment Work Order window.
Transaction

Item code
Enter the applicable part's item
 code, or press F4
 or use the drop-down menu to select from a list of available parts codes
 that were previously set up in the Inventory Control > Inventory Item File Maintenance screen. Entry in this field is required. If the item status
 code is set to 'Not used' entry will be disallowed.Once an inventory item's code is entered, the part's description and
 unit of measure default.
To enter non-stock
 parts, enter an exclamation mark (!) as the first
 character of the item code. When a non-stock item is entered, a unit of
 measure field displays next to the Quantity field. Use the
 Part note
 field to record the non-stock part's description.

Warehouse
Enter the warehouse code of the
 item, or use the drop-down arrow to select from a list of valid warehouse
 codes. Warehouse codes may be up to 10 characters long.
Date
Enter the part's transaction date.
 The system will confirm that the date is within the minimum/maximum
 Preventive Maintenance date range.
Quantity used
Enter a positive entry to reflect
 the quantity going out of the warehouse. Enter a
 negative entry to reflect the quantity returned to warehouse.

Unit cost
This field is skipped for positive
 quantity entries. When the quantity used is negative, this field defaults to
 the standard cost (including conversion factor), or you can enter another
 positive value.
Part note
Use this field to enter option text
 about the selected part. If this is a non-stock item, it is recommended that
 you enter a description of the part.
Distribution

Department
Select the department code for the
 part used.
G/L account
Assign a G/L account code to the
 item.
Cost category
Enter the cost category code of the
 item, or use the drop-down arrow to select from a list of valid cost
 category codes. When adding a new part used, Spectrum
 will verify that the assigned G/L account is not restricted for this cost
 category code.

- If the G/L account is authorized for this cost
 category, the part used can be added.

- If the G/L account is not authorized for this
 cost category, and error message appears and you will not be able to
 proceed.
