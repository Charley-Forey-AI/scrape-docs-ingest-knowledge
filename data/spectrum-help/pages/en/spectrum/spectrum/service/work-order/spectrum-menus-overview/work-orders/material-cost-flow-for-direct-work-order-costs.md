---
title: "Material Cost Flow for Direct Work Order Costs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/material-cost-flow-for-direct-work-order-costs"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/material-cost-flow-for-direct-work-order-costs"
---

# Material Cost Flow for Direct Work Order Costs

Material details are added to the following tables when using a Direct WO Cost G/L account.

## Purchase Order

- PO Entry

- PO_PURCHASE_ORDER_DETAIL_MC

- PO Received and AP Invoice created

- VN_INVOICE_TRAN_DETAIL_MC or VN_INVOICE_APPROVAL_DET_MC

- AP Invoice Updated

- WO_COST_HISTORY_MC

## Work Order

- WO Billing Entry (entered directly or selected from Cost History)

- WO_MATERIAL_DETAIL_MC

- AR Invoice created from WO Entry or Transferred to AR

- WO_MATERIAL_DETAIL_HIST_MC

- WO_COST_HISTORY_MC

- WO_BILLING_HISTORY_MC

The Work Order Cost History table should only include items that have already been updated to G/L.
The Detail History table should only have items that are already billed.
You do not have to bill the customer for materials, but the invoice update should still be performed.
