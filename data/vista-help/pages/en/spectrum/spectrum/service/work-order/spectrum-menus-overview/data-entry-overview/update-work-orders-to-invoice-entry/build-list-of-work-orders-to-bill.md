---
title: "Build List of Work Orders to Bill | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-work-orders-to-invoice-entry/build-list-of-work-orders-to-bill"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-work-orders-to-invoice-entry/build-list-of-work-orders-to-bill"
---

# Build List of Work Orders to Bill

Use this window to specify which work orders to update to A/R invoice entry.
FieldDescription
Work orderEnter the work order number, or press Enter to transfer all work order numbers.
WO typeEnter the work order type, or press Enter to transfer all types of work orders.
CustomerEnter the customer, or press Enter to transfer work orders for all customers.
JobEnter the job to transfer, or press Enter to transfer work orders for all jobs.
This field will be hidden if the Allow job work orders? option is not selected in Work Order Installation.

Dispatch statusChoose a status as a filter, or press Enter to include work orders of any status in the transfer.
From/To requested datesEnter the first and last dates to be included in the transfer, or press Enter to begin with the first record on file and end with the current Work Order processing date.
From/To finish dates
Bill through dateBy default, the update will include transactions through the maximum Work Order processing date, but you can enter a different date in this field to shift the most recent transactions onto future billings. During the update, Spectrum selects labor transactions based on the work order date, and material transactions based on the date added to the work order.
Require Finished Work Order Form to be printed prior to update?Select to omit all work orders which haven't had their Finished Work Order Form printed already.
Set site work orders to complete?Select if you want to close out all work orders included in the transfer.
Assign A/R invoice batchEnter the batch code, or press Enter to accept the current operator as the batch code assigned to the data that transfers to A/R.
Assign VAT code?Select if you want to assign the same VAT code to all work orders being updated to Invoice Entry.
Tax codeEnabled if Assign VAT code is selected. Choose which tax code to assign.
