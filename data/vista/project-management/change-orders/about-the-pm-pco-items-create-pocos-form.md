---
title: "About the PM PCO Items Create POCOs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-pocos-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-pocos-form"
---

# About the PM PCO Items Create POCOs Form

Use this form to create PO change orders (POCOs)
 using the detail items on a PCO. Access this form by selecting Create > Purchase
 Order Change Order on the PM Pending Change Orders form.
The following must be true to create POCOs from PCO detail items:

- A detail item on the PCO must be associated with a purchase order and
 purchase order line item - PCO detail items are entered using the Estimate/Purchase
 Details tab on PM Pending Change Orders, and they are associated with a PO and PO
 item using the PO and PO/SL
 Item fields.

- The PO item cannot already be associated with a PO change order - each PO
 item can only be associated with a single PO change order.

- The PO associated with the PCO detail item must be approved, or interfaced -
 purchase orders are approved using the Approved checkbox on the Info tab
 of [PM
 Purchase Orders](/en/vista/vista/project-management/materials/pm-purchase-orders-form) and they are interfaced using [PM Interface.](/en/vista/vista/project-management/setupmaintenance/pm-interface-form)

Key Features:
This form has the following key features:

- You can create one or many POCOs -
 A separate POCO will be created for each PCO detail item associated with a unique
 purchase order. This is because a POCO can only be associated with a single purchase
 order. PCO detail items associated with the same purchase order will be grouped
 together onto a single POCO.

- You can add items to an existing
 POCO - If all of the PCO detail items are associated with the same
 purchase order, you can add these items to an existing POCO on that purchase order.

- Created POCOs will be linked to the
 PCO - When you create POCOs using this form, the created PO change
 orders will be linked to the PCO using the [Related Items](/en/vista/vista/project-management/about-related-items) feature.

- The purchase orders do not have to be
 interfaced with accounting - You can create PO change orders for
 purchase orders that have been approved, or approved and interfaced with the
 accounting modules using PM Interface.

Create POCOs using PCO Detail Items
Follow the steps below to create PO change orders (POCOs) using PCO item detail.

1. In [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form), select a pending change order that contains detail items that meet the conditions outlined at the top of this document.

1. Select Create > PO Change
 Orders in PM Pending Change Orders. This will open PM PCO Items Create POCOs.


1. All of the PCO detail items that meet the conditions outlined at the top of this document will display in the grid.

1. Use the Keyword
 field to locate the PCO detail items that should be added to PO change orders.

1. Check the box next to each PCO detail item that should be added to a PO change order. Note: You can also use the Select All and Deselect
 All buttons to check or uncheck all of the boxes that display in
 the grid. These buttons only affect the items that display in the grid.

1. If you are adding the
 selected PCO detail items to an existing PO change order, press F4 in the Add to POCO
 Number field to select it from a list. If you leave this field blank,
 a new POCO will be created. This field will be disabled if you selected PCO detail
 items that are associated with more than one PO. You can see the PO associated with
 each PCO detail item using the PO column.Note: You can run this process multiple times if
 you have several PCO detail items that should be grouped onto a single POCO, and
 you also have PCO detail items that should be added to new POCOs.

1. Click the Create
 POCOsbutton when complete.

1. A message will appear. Click
 Yes you would like to open the created POCO using [PM PO Change Orders ](/en/vista/vista/project-management/change-orders/pm-po-change-orders-form).

1. For each PCO item added to a
 POCO, the PO change order number and sequence will populate in the PO Change
 Order and PO Change Order Seq fields on the
 Estimates/Purchasing Details tab in the lower portion of [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form).

Related Items
The PO change order and the pending change order(PCO) will automatically be related using Related Items feature. Click [here](/en/vista/vista/project-management/about-related-items) for general information on the Related Items feature.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.
Change Orders - Overview
