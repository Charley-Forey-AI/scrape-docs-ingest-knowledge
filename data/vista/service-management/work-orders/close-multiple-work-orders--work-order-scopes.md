---
title: "Close Multiple Work Orders / Work Order Scopes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/close-multiple-work-orders--work-order-scopes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/close-multiple-work-orders--work-order-scopes"
---

# Close Multiple Work Orders / Work Order Scopes

You can close multiple work orders or work order scopes at one time using the SM Work Order Close form.
Using selection criteria, you can filter work orders displayed in the grid and then select the work orders or scope you want to close.

1. From the main menu, select Service Management > Programs > SM Work Order Close.

1. Under the Filter Options section, enter data into appropriate fields (or press F4 for lookups), select from relevant pull-down lists, enter dates, and /or select checkboxes to narrow down your work order search.

1. Under Processing Settings, check any of the following boxes:

- Auto Delete Open Trips - Select this checkbox to delete open trips on the work order. (If you do not select this option, and trips are still open on the work order, you will receive an error. However, you can then either delete the trip manually or mark it complete.)

- Use Closest Open Month - Select this checkbox to filter on the next-closest open month than the current month (assuming the current month is still open)

- Advanced Grid Options - Select this checkbox to add Billable Remaining and Unclosed PO's data to the grid, for sorting purposes

1. Click Search.Filtered results appear in the grid.

1. Select Check All to select all filtered work orders for closure or select the checkbox next to any individual work order you want to close.

Selected work order scopes or work orders are closed. Errors relating to any attempted closures appear (per Vista session), indicating why a particular work order was not successfully closed.

Related information

- [SM Work Order Reopen Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-reopen-form)
