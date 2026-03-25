---
title: "Enter POs in SM Purchase Order Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-pos-in-sm-purchase-order-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-pos-in-sm-purchase-order-entry"
---

# Enter POs in SM Purchase Order Entry

You can enter purchase orders for an SM work order using the SM Purchase Order Entry form.
Note: If you are entering purchase orders for a job work order, you must assign a phase to each applicable work order scope. The system will not allow you to enter purchase order items for work order scopes without a phase.

1. Open the SM Work Orders form.

1. In the Work Order field, enter the work order for which to create a purchase order.

1. Select Create PO (bottom of form). The SM Purchase Order Entry form displays.

1. In the PO
 # field, enter a purchase order number or accept the default number (if you selected to auto-generate PO #s in PO Company Parameters).

1. In the Vendor field, enter the vendor or press F4 to select from a list of valid vendors.Note: You may leave this field blank if you do not know the vendor. The system will set the PO status to Reserved and leave the batch unposted. Once you assign a vendor, the batch will be posted and the work completed purchase line generated.

1. In the Description field, enter a description of the purchase order.

1. In the Order Date field, accept the current date default or enter the date the order was placed.

1. In the Expected
 Date field, enter or select the date that you expect to receive the items on this purchase order.

1. In the Ordered By field, enter the name of the person who placed the order.

1. In the Hold Code field, if applicable, enter the hold code that applies to this purchase order or press F4 to select from a list of valid hold codes. Leave blank if no hold code is needed.

1. In the Pay Terms field, enter the payment terms for the purchase order or accept the default payment terms (for the specified vendor). Press F4 for a list of valid payment terms.

1. In the Cmpl Group field, enter the compliance group for this purchase order or press F4 to select from a list of valid compliance groups.Note: If you leave this field blank, you will need to enter compliance codes manually for this purchase order in PO Compliance Tracking.

1. In the Ship Location field, if applicable, enter the shipping location or press F4 to select from a list of valid ship locations. The ship location address populates the address fields on the Shipping tab.

1. If you did not enter a ship location, use the Shipping tab to enter the shipping address, as well as attention information and shipping instructions.

1. [Add items to the purchase order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-po-items-in-sm-purchase-order-entry).

Once you successfully post the purchase order, the system generates a work completed purchase line for the work order (in SM Work Orders, Work Completed tab).
