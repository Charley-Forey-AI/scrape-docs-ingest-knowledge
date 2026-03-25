---
title: "About Preventative Maintenance Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders"
---

# About Preventative Maintenance Work Orders

Preventative maintenance work orders are generated automatically using the SM Generate PM Work Orders form, and apply only to those customers with which you have one or more active agreements (in SM Agreements).
 During work order generation, the system uses a combination of filtering criteria to determine which services are due. Based on the services you select, the system generates work orders accordingly.
 If several services are assigned the same same service site, service center, pricing method (and rate template, if applicable), call type, and schedule date, the system will group them together on the same work order/scope. However, there are two exceptions to this:

- Separate Scope Per Service Item - If you are using the [Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling) feature to generate agreement services and you selected the Separate Scope Per Service Item checkbox for the agreement, the system generates a separate work order scope for each service item rather than grouping them on the same work order scope.

- Separate Work Order - If you select the Separate Work Order checkbox for one or more agreement services (in SM Service), the system always creates a separate work order for those services. If you also selected the Separate Scope Per Service Item checkbox for the agreement, the system generates a separate work order for each agreement service flagged for a separate work order and then sets up the remaining services on one work order with separate scopes per service item.

The scopes for preventative maintenance work orders display the agreement and service information, as well as the pricing method and if applicable, the service price. If the agreement has a task schedule (set up in SM Agreement Task Schedule), the work order scope also displays the Task Group assigned to the maintenance task during task scheduling. These values cannot be edited, as they are based on what you defined for the agreement.
If you manually add a work order scope, the agreement-related fields are enabled, allowing you to associate the work order scope with the appropriate agreement. However, these work order scopes will be considered "add-ons" and cannot be associated with a specific service on the agreement.

- If you manually add a work order scope and do not associate it with an agreement, the agreement-related fields are enabled for work completed lines, allowing you to enter agreement information as applicable for each line. Work completed lines not associated with an agreement will use the scope's rate template for pricing calculations.

- Add-ons are billed separately from the agreement. Once you enter work completed lines for the work order scope, the Bill WO button is enabled, allowing you to generate and process an invoice.

 For more information about generating PM work orders, see [SM Generate PM Work Orders](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form).
