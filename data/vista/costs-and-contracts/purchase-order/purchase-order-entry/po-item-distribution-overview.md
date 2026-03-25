---
title: "PO Item Distribution Overview | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview"
---

# PO Item Distribution Overview

You can distribute PO items into multiple lines using the PO Item Distribution feature.

The PO Item Distribution feature allows you to redirect the costs on a PO item to a different job, phase, or cost type when it is received in the PO module or invoiced in the AP module. You can also use it when you purchase a material for multiple allocations (for example, a material that will be used on a JC job and an SM work order).
When you create a new PO item, the system automatically creates a distribution line that is identical to the PO item. You can view this distribution line using the PO Item Distribution form, which is used to create and maintain PO item distribution lines. The system generated PO item distribution line is display only.

Type
Job
Phase
Units
Unit Cost
Amount

PO Item
Job
1-8000
00150-100
100
$5
$500

PO Item Line #1
Job
1-8000
00150-100
100
$5
$500

You can also add distribution lines manually via the PO Item Distribution form. When you create a new distribution line, the system automatically updates PO item line #1. For example, if you create PO item line #2 to receive 40 units to a different job and phase, PO item line #1 is automatically reduced by the 40 units.

Type
Job
Phase
Units
Unit Cost
Amount

PO Item
Job
1-8000
00150-100
100
$5
$500

PO Item Line #1
Job
1-8000
00150-100
60
$5
$300

PO Item Line #2Job1-800100200-30040$5$200

Once you have created PO item lines, you can enter receipts for them using PO Initialize Receipts or PO Receipts Entry. For more information, see [About Receiving Purchase Orders](/en/vista/vista/costs-and-contracts/purchase-order/receiving/about-receiving-purchase-orders).
 You can also skip the receiving process and invoice POs in the AP module. Once you enter a PO, you can invoice it via AP Transaction Entry or AP Unapproved Invoice Entry. From these forms you can launch the PO Item Distribution form, create new distribution lines, and then invoice them. Once you have invoiced all of the units on the PO, you can close it using the PO Close form.
 When you close a PO, if the PO has item lines and backordered amounts, the system automatically generates a change order to zero out the remaining backordered units/amounts. This change order will only impact PO item line #1.

## Standing/Blanket POs

Standing or blanket POs are open PO items that you can post receipts to indefinitely. Since standing POs do not have any costs or units associated with them, you cannot open them using the PO Item Distribution form; you can only distribute PO items into lines if there are units or cost associated with them. If you want to distribute PO items into lines on a standing/blanket PO, you have to add units or amounts to it.
For more information about standing/blanket POs, see [About Standing Purchase Orders](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/about-standing-purchase-orders).

## Change Orders and PO Item Lines

Purchase order change orders (POCOs) are created and edited using the PO Change Order Entry form. POCOs always impact PO item line 1.
 For example, when creating or editing a PO change order, changes to the units and total cost on the PO item will impact line 1 of the PO item distribution. If you delete a PO change order, the system updates line 1 of the PO item distribution.
 If you create a new PO item using a change order, the system automatically creates a PO item line 1 that is identical to the PO item. You can then view this line or create new lines using the PO Item Distribution form.

## SM Work Orders

Distribution lines associated with an SM work order will automatically generate work completed purchase lines (type 5-Purchase) for the specified work order in SM Work Orders (Work Completed tab and the SM Work Completed Purchase form).
Edits to the PO information cannot be made from the work completed purchase line; they must be made directly in SM Purchase Order Entry, PO Purchase Order Entry, or PO Item Distribution (as applicable). Changes are updated to the corresponding work completed purchase line accordingly.
