---
title: "About the IN Monthly Reconciliation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-monthly-reconciliation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-monthly-reconciliation-form"
---

# About the IN Monthly Reconciliation Form

Use this form to capture beginning and ending Inventory levels, accumulate activity, and calculate ending values for the month.
Based on
 the Valuation Method specified in IN Company Parameters (Average Cost,
 FIFO, LIFO, Standard Cost), adjustments will be generated automatically to correct
 Inventory GL balances.
Run this
 form only after all activity has been posted for the month (i.e. purchases, sales,
 transfers, production, and adjustments). Inventory will be checked to make sure no
 current batches are open for the specified month; however, PO Receipts, AP Expense,
 JC, EM, MS, or SM will not be checked.
Each month must be reconciled separately and should be run in
 consecutive order. It is important that months are not skipped as “beginning” values
 for the current month are initialized from the “ending” values of the previous
 month.
If necessary, you can run
 this process for a month that has been previously reconciled. Generally, this would
 only be required if additional activity was posted to the month after the initial
 reconciliation. If you re-reconcile a month, a message displays warning that monthly
 activity entries exist and that they will be removed. Once the month is reconciled,
 you will need to rerun the process for each successive month that was previously
 reconciled.
[Start the Reconciliation Process](/en/vista/vista/job-resources/inventory/monthly-reconciliation/start-the-reconciliation-process#task-4615--en__task-4615)

Related information

- [How the Reconciliation Process Works](/en/vista/vista/job-resources/inventory/monthly-reconciliation/how-the-reconciliation-process-works)
