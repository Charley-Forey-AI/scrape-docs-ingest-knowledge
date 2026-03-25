---
title: "Generate Preventative Maintenance Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders"
---

# Generate Preventative Maintenance Work
 Orders

You will use the SM Generate PM Work Orders form to generate work orders for agreement services.
 Using the selection criteria, you can filter the list of
 services for maintenance and then select the items for which to create work orders.The following steps will guide you
 through this process.

1. From the Vista main
 menu, select Service Management > Programs.

1. Open the SM Generate PM Work Orders form.

1. In the Search Criteria section, use any combination of the Service Center, Customer, Service Site, and/or Agreement Type fields to filter work orders returned to the grid.

1. In the Due Within the Next __ days field, accept the default of 30 days or enter the number of days to use in determining which services are due.

1. Click Search.Note: Services with the Separate
 Work Order checkbox unselected (in SM Services) that have
 the same criteria (e.g. service site, schedule date, pricing method,etc.)
 may appear together in the Service Name column for
 the applicable agreement (e.g. "Service #1, Service #2"), indicating they
 will be grouped together on the same work order/scope.

The system populates the grid with all services that
 are due within the specified number of days and that meet all other filter
 criteria.

1.  Select the Create checkbox for applicable service or click Check All to select all items in the grid.

1. If applicable, select the Skip checkbox for services/due dates you want skipped during the work order generation process. For more information about using this checkbox, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form/field-definitions-sm-generate-pm-work-orders-form#ID-000434b1--en) help.

1. Click Process.The system displays a message indicating the number
 of work orders that will be generated and/or skipped and asking if you want to
 continue.

1. Select Yes.

The system creates a single job in SQL Agent for the selected agreements/services and opens the SM
 Generate Work Order Summary form. The process request is assigned an ID, a status of Requested, and a Requested Time. If you specified a process run time in SM Company Parameters (in the Generate Agreement WO Time field), the system will run the process at the specified time. If you did not schedule a time in SM Company Parameters, the system runs the process within a minute after it is requested. When the system begins the process run (regardless of timing), if other requests exist in the queue, the system starts with the earliest request (based on the Requested Time) and continues until all requests are processed.
Once all requests are processed, the system sets the status for each run ID to Complete.

Related information

- [Remove the Skip Status on Agreement Services](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-creatingskipping-work-orders/remove-the-skip-status-on-agreement-services)

- [SM Generate PM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form)
