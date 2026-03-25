---
title: "SM Work Order Close Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-close-form_1"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-close-form_1"
---

# SM Work Order Close Form

Use the SM Work Order Close form to close a work order scope or work order.
You can access this form from SM Work Orders by either selecting the Close option from the status drop-down for an Open or Completed work order scope or by clicking Close WO (at the bottom of the form).
Important: This form has its own security, so in order to use this feature, make sure you set up access to the form (SMWorkOrderClose) using [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form).
When you close a work order scope, the behavior differs slightly depending on whether the work order has a single scope or multiple scopes. If multiple scopes exist, the system closes only the scope you select. If only one scope exists for the work order, the system closes both the scope and the work order. Once closed, you can no longer add work completed or purchase orders to the work order scope. However, you can bill the scope (if Flat Price) or existing work completed lines associated with the scope.
If you close a work order with open scopes, the system displays all open scopes on the work order and provides the option to close all of the scopes. Selecting Yes closes the work order and all of its open scopes. Once closed, you can no longer add new scopes or trips, enter purchase orders, or capture work completed. However, you can bill for existing work completed or flat price scopes. Additionally, limited edits are allowed.Note: You can open reopen a work order if needed via the SM Work Order Reopen form by clicking the Reopen WO button in SM Work Orders. The system changes the WO Status to Complete, but leaves the work order scopes Closed. If you reopen all the work order scopes, the system sets the work order status to Open. For more information, see [SM Work Order Reopen Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-reopen-form).

## Close Criteria

When you close a work order or a work order scope, the system checks for the following criteria:

- Provisional Miscellaneous Work Completed – Miscellaneous work completed lines with this status are auto-added to a work order from standard charges or miscellaneous requirements. Before you can close the scope/work order, you must process these using SM Batches.

- Pending Invoices – If pending invoices exist, you will be unable to close the scope or the work order until you process the work completed lines in SM Batches. The system also checks for pending invoices associated with the work order/scope. If any exist, you will need to either process the invoices or cancel them.

- Open Trips – If open trips exist (those with a status of Open), a warning is displayed. If you select to close the work order, the open trips will be deleted. If you do not want the trips deleted, change applicable trips to a status other than Open. Trips with a status other than Open will be set to Completed.

Related information

- [About Editing Closed Scopes/Work Orders](/en/vista/vista/service-management/work-orders/close-multiple-work-orders--work-order-scopes/about-editing-closed-scopeswork-orders)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
