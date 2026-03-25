---
title: "About the Work Order Status | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-the-work-order-status"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-the-work-order-status"
---

# About the Work Order Status

The work order header displays the status of the work order so that it can be tracked throughout the work order's life cycle.
 The display-only WO Status field shows available statuses as follows:

- New - This status is applied to each work order when it is first entered. Work orders will retain this status until you begin to add trips, work completed, invoices, and so forth.Note: Work orders with work completed lines that were auto-added from miscellaneous requirements, standard charges, or the import process will also be set with a status of New. Once you process the auto-added lines (via SM Work Order Cost Posting), the status will change to Open.

- Open - This status is applied to work orders once you begin to manually enter work completed, add trips, and create invoices and purchase orders.

- Completed - Work orders with this status indicate that all work is done and no more trips are needed, but not all costs have been captured. A work order will only receive this status when you set the status for all scopes on the work order to Complete or if there is a mix of Closed and Complete scopes

- Closed - This status is applied to a work order using the SM Work Order Close form (which you can access by selecting Close from the Scope Status drop-down or by clicking the Close WO button). Work orders with this status indicate that all costs have been entered and the only changes to costs will be work completed Purchase lines that have not been invoiced yet (via AP Transaction Entry) or work completed Labor lines that have not been posted via PR Ledger Update

Note: You cannot enter new trips or work completed lines on a closed work order. If you need to enter new trips or work completed, you must re-open the work order.
