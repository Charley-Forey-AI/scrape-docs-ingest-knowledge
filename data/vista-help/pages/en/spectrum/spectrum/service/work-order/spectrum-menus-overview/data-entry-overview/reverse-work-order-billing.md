---
title: "Reverse Work Order Billing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/reverse-work-order-billing"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/reverse-work-order-billing"
---

# Reverse Work Order Billing

This update reverses entries created in Work Order and
 other modules that have already been updated to Accounts Receivable so that the work order can
 be priced again.
A reversal created using this screen will create a credit memo in Accounts Receivable > Invoice Entry, which re-opens labor, material, and other charges associated with the
 particular bill # being reversed. The reversing transactions will exactly reverse amounts
 originally updated when the work order was transferred to A/R. The new transactions will be
 assigned the G/L date on the starting screen. Once all of the necessary pricing changes
 have been entered, the work order should be posted to A/R again in order to create a new
 invoice. Any work order costs included on the original invoice will be reversed on the
 credit memo.
This update reopens entries originating in the Work Order and Payroll
 modules. This update also reverses the Inventory Control transactions if the Inventory
 Control module is present, the Work Order Installation prompt for Update inventory is selected, and stock items are contained on
 the work order. The update will return the inventory to stock using the actual unit cost
 recorded during the previous update.
When adding a new material transaction record for a work order, the current Work Order processing date will be assigned as the 'Transaction Create Date'.
