---
title: "Reverse Work Order Billing - Update Details | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/reverse-work-order-billing/reverse-work-order-billing---update-details"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/reverse-work-order-billing/reverse-work-order-billing---update-details"
---

# Reverse Work Order Billing - Update Details

When the reversal update is initiated, the status of the
 selected work order will be changed from Completed to Finished, and the Dispatch status, Priority and Markup code entries will be reset from the
 starting screen entries.
All dates, including the finished date, will be retained, but the print
 status for the invoice will be reset to Unprinted. Detail lines will be created in summary
 or detail formats based on the original invoice (rather than the current settings in
 Work Order Installation). The credit memo will be assigned the
 work order number if the A/R invoice option for Accounts Receivable invoice is set to Work
 order on the Work Order Installation > Properties tab, unless that credit memo number already exists. In other words, Spectrum
 will use the invoice number that was previously assigned when the work order was
 transferred; however, if the credit memo is already used, then the new invoice number will
 be assigned based on the Next invoice number designated on the Accounts Receivable Installation > Properties tab.
For job work orders the update will re-open all history transactions, since multi-billing is not supported for this type of work order.
If the selected work order has any inventory entries assigned to a warehouse conducting a physical inventory, the software will provide the following error message "ERROR: Physical inventory in progress at all warehouses - Transfer not allowed".
The assigned labor billing code will be transferred from the Labor Transaction History record to the Work Order Labor Transaction Detail Table.
Note: Labor entries are already flagged when transferred to Payroll >  Pre-Time Card Entry regardless of work order status. This process will be unaffected by this
 update.
