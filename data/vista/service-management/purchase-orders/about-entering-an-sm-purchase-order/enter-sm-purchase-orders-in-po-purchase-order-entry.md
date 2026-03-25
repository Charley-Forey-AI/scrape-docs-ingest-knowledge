---
title: "Enter SM Purchase Orders in PO Purchase Order Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-sm-purchase-orders-in-po-purchase-order-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-sm-purchase-orders-in-po-purchase-order-entry"
---

# Enter SM Purchase Orders in PO Purchase Order Entry

You can enter purchase orders for an SM work order using the PO Purchase Order Entry form.

1. From the main menu, select Purchase Orders > Programs > PO Purchase Order Entry. This is a batch form, so the Batch Selection form displays.

1. Select Create a new batch or Use an existing batch.

1. If you selected to open a new batch, enter the batch month in the Batch Month field and click OK. If you select to open an existing batch, use the Unposted Batches grid to select the desired batch and click OK.
The PO Purchase Order Entry form displays.

1. In the Seq # field, enter New, N, or + . The system automatically generates the next available sequence number.

1. In the PO # field, accept the default PO number (if auto-generating numbers) or enter a purchase order number (if not auto-generating numbers).

1. In the Vendor field, enter the vendor number or press F4 to select from a list of valid vendors. Note: If you selected the Check compliance on transaction entry, warning only checkbox for Purchase Orders in AP Company Parameters (Audit Options tab), the system will display a warning (in red) if the vendor is out of compliance, but will allow the entry.

1. In the Description field, enter a description for the purchase order.

1. In the Expected Date field, enter the date that the order is expected to arrive.

1. In the Order Date and Ordered By fields, enter the date the materials were ordered and by whom, respectively.

1. In the Pay Terms field, accept the defaulted pay term or override as necessary.

1. In the Cmpl Group field, enter the compliance group for this purchase order or press F4 to select from a list of valid compliance groups.Leave this field blank to enter compliance codes manually for this purchase order in PO Compliance Tracking.

1. If applicable, in the Ship Location field, enter the shipping location or press F4 to select from a list of valid ship locations. The ship location address populates the address fields on the Shipping tab.

1. If you did not enter a ship location, use the Shipping tab to enter the shipping address, as well as attention information and shipping instructions.

1. [Add items to the purchase order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-po-items-in-sm-purchase-order-entry).

Once you successfully post the purchase order, the system generates a work completed purchase line for the work order (in SM Work Orders, Work Completed tab).
