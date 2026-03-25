---
title: "About Work Order Scope Services | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-work-order-scope-services"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-work-order-scope-services"
---

# About Work Order Scope Services

If you are using the Agreements feature, the Services tab in the SM Work Orders form displays all agreement services associated with a work order scope (generated work orders only)
The list of services may include a single agreement service or multiple services, depending on how you set up your agreement services.

-  If you selected the Separate Work Order checkbox for a service (in SM Service), the system will always create a separate work order/scope for that service when generating work orders.

- If you did not select the Separate Work Order checkbox for a service (in SM Service), the service will be included on the same work order scope with other services not flagged for separate work orders that have the same service site, service center, pricing method (and rate template, if applicable), call type, and schedule date.

Note: The system may add services to an existing work order scope if the work order has a status of New and meets the criteria specified above.
Work order scopes generated using SM Generate PM Work Orders will display a Maintenance flag on the scope's Info tab to indicate they were generated from an agreement. Scopes that you manually add to a work order that have an agreement specified are not associated with an agreement service; therefore, the Services tab will be blank and no Maintenance flag will display.
If there is an item group assigned to the agreement service, it will appear in the Item Group column of the Services tab.
For more information about setting up agreement services, see [Agreement Service Setup](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup).
