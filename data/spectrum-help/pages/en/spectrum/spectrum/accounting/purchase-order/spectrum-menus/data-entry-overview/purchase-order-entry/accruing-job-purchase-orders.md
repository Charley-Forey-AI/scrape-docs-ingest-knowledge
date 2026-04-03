---
title: "Accruing Job Purchase Orders | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/accruing-job-purchase-orders"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/accruing-job-purchase-orders"
---

# Accruing Job Purchase Orders

There are situations where it is important to accrue the
 costs of materials that have been received on a purchase order, but not yet invoiced.
Spectrum uses the two-step method of receiving to track materials received and the
 processing of the eventual invoice. The received state (step one) is performed in Packing
 List Entry. The invoiced state (step two) is performed in Vendor Invoice Entry.
Overview of the two-step receiving process:
Step One: Materials are received and recorded in Packing List Entry. The costs of the material are accrued to the job when the Packing List Update is performed.
Step Two: Invoice is matched up against the packing lists. The material cost is 'trued up' on the job during the A/P Transaction Register / Update step.

## Definitions

True-up An adjustment that brings the estimate up to the actual amount. Items ordered on a purchase order may be thought of as an 'estimate'. When the vendor invoice comes in, the true cost of the items may be different, thus necessitating a true-up transaction.
Accrued Job PO Costs The estimated cost from the purchase order charged to the job. In Spectrum, these are determined in step one of the two-step process. It is calculated as: (PO Cost X Quantity Received) X (1 + Sales/Use Tax)

## Assumptions

- When a true-up exists, job purchase orders will have two or more
 transactions in Job Cost History to account for the accrued cost amount and the true
 up.

- It is acceptable to have different workflow patterns for
 accruing different types of purchase orders.

- Warehouse (indirect costing): We are not changing the way
 Spectrum currently works for materials (Warehouses) as the items have already
 gone into inventory at the PO rate and already impacted the FIFO/LIFO/Average
 cost layers. We are not going to adjust for this as this will increase the
 complexity for very little benefit. This is an acceptable limitation.

- Equipment and Work Order: These two direct cost PO types
 do not currently support accruals.
