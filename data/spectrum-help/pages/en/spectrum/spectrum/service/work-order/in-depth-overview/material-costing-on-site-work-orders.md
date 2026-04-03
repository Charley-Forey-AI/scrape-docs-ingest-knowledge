---
title: "Material Costing on Site Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/in-depth-overview/material-costing-on-site-work-orders"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/in-depth-overview/material-costing-on-site-work-orders"
---

# Material Costing on Site Work Orders

The following is a discussion on the methodology Spectrum uses when costing material on a site work order.
Completed Work Orders When a work order is updated to the Accounts Receivable module, it is considered complete. Materials are costed using each item's FIFO/LIFO/Average inventory cost from the Inventory Control module. Exception: Spectrum uses the standard cost on a complete work order only when there are no items in the bin.
Work Orders in Process Spectrum uses the item's actual purchase price when calculating the costs of material until the work order status is set to Complete. Complete work orders show actual material costs on a FIFO/LIFO/Average inventory cost basis at the time the work order was updated to the Accounts Receivable module.
Note: Once the update occurs, this cost becomes the actual material
 cost and does not change with further activity on this work order.
Why two methods to cost materials? You can use standard costs while processing a work order so you can create invoices quickly. As long as the work order revenue covers the standard cost of the material, you don't have to wait for the actual costs (via the material invoice) to arrive before you can issue the invoice to the customer. Creating invoices faster for work completed can lead to improved cash flow.
The Work Order Profitability Report uses the true inventory cost of the material and not the standard cost. Of course, if there were no items in the bin at the time the work order was updated, the material will be costed at standard cost.
