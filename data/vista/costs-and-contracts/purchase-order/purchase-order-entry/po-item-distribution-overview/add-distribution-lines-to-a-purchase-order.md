---
title: "Add Distribution Lines to a Purchase Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview/add-distribution-lines-to-a-purchase-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview/add-distribution-lines-to-a-purchase-order"
---

# Add Distribution Lines to a Purchase Order

You can distribute PO items into multiple lines via the PO Item Distribution form, enabling you to redirect the costs on a PO item to a different job, phase, or cost type when it is received.

Follow the steps below to add a new distribution line to a PO item.

1. Open the PO Item Distribution form (Purchase Order > Programs > PO Item Distribution.

1. In the JC Month field, enter the month to which the PO item distribution should be posted.For more information about this field, see [JC Month](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-item-distribution-form/field-definitions-po-item-distribution-form#ID-0003008d--en).

1. In the PO and PO Item fields, select the PO and PO item.The Grid tab in the lower portion of the form displays the lines already added to the PO item. The system automatically creates Line 1 when the PO item is created. This line is display only and is updated automatically by the system when you add a new distribution line or a change order.

1. To enter a new item distribution, enter a "+" in the Line field.

1. From the Type drop-down, select the line type.

- 1-Job

- 2-Inventory

- 3-Expense

- 4-Equipment

- 5-EM Work Order

- 6-SM Work Order

Note: Lines distributed to an SM work order automatically generate a work completed purchase line (type 5-Purchase) for the specified work order (in SM Work Orders, Work Completed tab).

1. Enter the remaining information for the selected line type.

1. Select Save.

The system updates PO item line 1 based on the line that you just created. For example if line 1 had 100 units and you just created a new line that redistributes 25 of those units to a different job, line 1 will now have 75 units that are still associated with the original job
