---
title: "Item Warehouse Details - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/item-warehouse-details/item-warehouse-details---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/maintenance-overview/item-warehouse-details/item-warehouse-details---field-descriptions"
---

# Item Warehouse Details - Field Descriptions

Use the table below for reference when completing the
 fields on this screen.
Field/Button
Description

Item code
The selected inventory item code will display in this
 field.

Warehouse
Enter the warehouse code in which this inventory item is
 stored, or press Enter to accept the default from the Inventory
 Control Installation screen. The warehouse code must have
 already been defined using Warehouse File Maintenance,
 and it may be up to 10 characters long.
An item may be stored in multiple warehouses. After entry
 in this screen is complete, the screen clears and the cursor returns to the
 item code prompt, allowing for entry of this same item into a different
 warehouse.

On hand valuation
The sum of the amounts shown in the Valuation $ column
 for the current warehouse displays in this field.

Properties

Item location
Enter a description of where in this warehouse the item
 is located. For example, if the item is stored in bin 12, aisle A, the item
 location might be A12. The location entered here may be useful on an
 on-going basis to find items in the warehouse. The location will also be
 useful at the time of physical inventory, since the Physical Count Sheet
 Printing is done in location sequence within the warehouse.
If the Validate item location checkbox is selected in
 Inventory Control Installation, you must enter a
 valid item location code as previously set up in Location File
 Maintenance.

Standard cost
Use this field to enter a standard cost for the inventory
 item. Entry in this field will be contingent on the costing method selected
 in Category File Maintenance.

- If the costing method is standard cost and there is
 no stock on-hand for the inventory item, entry in this field is
 optional. If there is quantity on-hand, this field will be display
 only.

- If the costing method is LIFO, FIFO or Average
 cost, entry in this field is optional.

Reorder point
Enter the quantity at which this item is to be reordered.
 When the available quantity reaches the reorder quantity, the item will
 appear on the Reorder Report. This is the reorder point for stock only in
 the specified warehouse.

Suggested quantity
Enter the typical quantity of this item that would be
 ordered when a reorder is placed.

Lead time (days)
Enter the number of days required to receive the item
 once a purchase order has been placed.

Last received
The most recent date for any Purchase Order receiving,
 Inventory Control receipt, or Inventory Control credit displays.

Last adj./transfer
The most recent date for any Inventory Control
 adjustment, transfer, mix usage, equipment adjustment, or cost adjustment
 displays.

Last shipped
The most recent date for any Inventory Control sales
 adjustment or job requisition, Order Processing invoice or credit memo, or
 work order displays.

Current quantities

On hand
The total quantity of this item on hand within the
 warehouse displays.
 If LIFO or FIFO is in use, this number is the sum of all
 20 quantity on hand fields. If Average is in use, it is the same as the
 first quantity on hand. This quantity is calculated by the software.

Committed
The quantity of this item that has been committed
 displays.
This number is updated from entry in Job Requisition
 Entry, Work Order Material Entry, Order Processing Order Entry and Invoice
 Entry, and Mix Processing.

Available
The quantity of this item that is available displays. No
 entry is allowed. The computer system calculates the quantity available by
 subtracting the quantity committed from the quantity on hand.

On order
The on order quantity is calculated from purchase orders
 being received into inventory for this warehouse. This number does NOT
 include packing list updates or purchase orders entered for a specific job,
 work order, or piece of equipment. Quantity is shown in purchase units. No
 entry is required, but is allowed if the Purchase Order module is not
 present.

Quantity on hand
 layers

Quantity
Quantities on hand displayed here represent item
 quantities with different costs. The quantities (in sell units) are
 organized with the most recent activity in field one, the next most recent
 in field two, and more.

Cost basis
The cost associated with each quantity displays.
