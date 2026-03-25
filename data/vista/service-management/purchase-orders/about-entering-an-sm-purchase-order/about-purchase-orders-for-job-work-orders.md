---
title: "About Purchase Orders for Job Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/about-purchase-orders-for-job-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/about-purchase-orders-for-job-work-orders"
---

# About Purchase Orders for Job Work Orders

You can enter purchase orders for job-related work orders using the SM Purchase Order Entry or PO Purchase Order Entry forms.
If you will be entering purchase orders for a job-related SM work order, you must first assign a phase to each scope on the work order that will be associated with items on a purchase order. If you specify a scope on a PO item that is not assigned a phase, you will receive a message indicating that the scope phase is missing, and you will be unable to proceed until you assign a phase to the scope (which you can do without exiting the purchase order). Each PO item will automatically default the phase from the work order scope; this cannot be changed. You must then assign a JC cost type to the item, making sure the cost type is valid for the phase in either JC Job Phases (locked jobs) or JC Phases (non-locked jobs).
Note: If the job associated with the work order is soft or hard-closed, you will only be able to create a purchase order if you allow posting to closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs checkboxes are selected in JC Company Parameters).

## Committed Costs

Committed costs for job-related SM work orders are handled in the same manner as they are when posting job purchase orders (type 1-Job) in PO Purchase Order Entry.
When you create a purchase order for a job work order (in SM Purchase Order Entry or PO Purchase Order Entry), the system updates the costs to JC as committed costs. Once the purchase order is received and invoiced (in AP), the system will update the remaining committed based on the actual costs posted to the invoice.
For more information about committed costs related to purchase orders, see [PO Purchase Order Entry](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form).
