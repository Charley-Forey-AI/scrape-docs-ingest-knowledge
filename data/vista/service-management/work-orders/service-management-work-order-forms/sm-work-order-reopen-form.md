---
title: "SM Work Order Reopen Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-reopen-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-reopen-form"
---

# SM Work Order Reopen Form

Use the SM Work Order Reopen form to reopen a work order that was previously closed.

You can access this form from SM Work Orders by either selecting the Reopen option from the Scope Status drop-down or by clicking the Reopen WO button at the bottom of form.
Important: This form has its own security, so in order to use this feature, make sure you set up access to the form (SMWorkOrderReopen) in VA Form Security.

## Reopen a Scope

When you select to reopen a work order scope in SM Work Orders (using the Reopen option in the Scope Status drop-down), this form opens and displays a Reopen Scope? prompt. Clicking OK sets the scope's status to Complete. If the associated work order is closed, the system also sets the work order status to Complete.
If you want to set the scope's status to Open, reselect the Reopen option in SM Work Orders. The system sets the scope status to Open. If the scope is the only scope for the work order, the system then sets the work order status to Open or New (if no trips or work complete lines exist). If multiple scopes exist for the work order, the work order status remains at Complete and the status of all other scopes on the work order remain intact.

## Reopen a Work Order

When you select to reopen a work order in SM Work Orders (using the Reopen WO button at the bottom of the screen), this form opens and displays a Reopen Work Order? prompt. Clicking OK sets the work order status to Completed, but leaves all scopes on the work order Closed. If you want to set the work order status to Open, you must reopen all work order scopes.
Note: If there are no trips or work completed on a work order, reopening all scopes sets the work order status to New, rather than Open.

Related information

- [SM Work Order Close Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-close-form)
