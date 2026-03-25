---
title: "PO Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-purge-form"
---

# PO Purge Form

Use this form to purge all of the purchase orders and requisitions that were closed in or prior to a given month.

## Purging Purchase Orders

When you purge closed purchase orders, the system removes the following:

- header and detail records

-
all related submittal, change order, compliance tracking, and receipt detail records

Consider the following as you proceed:

- The purge process does not update PM Subcontract Detail or the item detail in the PM Material Detail form

-
The system uses the date(s) you enter to when determining whether to delete any PM PO Change Order records

-
If you want to purge AP invoices related to purchase orders, you must first purge purchase orders

- POs which have remaining units or remaining cost are not purged

- POs with received costs or units not equal to invoiced costs or units are not purged

For more information, see [Purge Purchase Orders](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/purge-purchase-orders).

## Purging Requisitions

Purging requisitions removes header records from the system. The purge process also removes all requisitions lines with a status of Complete. If any requisition lines are not complete, the system will not purge the header record. The purge process does not update PM Subcontract Detail.
For more information, see [Purge Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/purge-requisitions).
