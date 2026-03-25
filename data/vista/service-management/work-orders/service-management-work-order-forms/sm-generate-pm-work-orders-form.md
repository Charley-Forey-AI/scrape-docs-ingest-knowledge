---
title: "SM Generate PM Work Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form"
---

# SM Generate PM Work Orders Form

Use the SM Generate PM Work Orders form to create preventative maintenance work orders for services defined on an agreement.
When you search for services due in SM Generate PM Work Orders, you can enter any combination of criteria to filter services due for maintenance. Once you click the Search button, the system populates the grid with all active agreements that are due within the specified number of days that meet the filter criteria.
The grid does not include services that already exist on a work order for a due date that falls within the specified Due Within the Next __ days; however, because multiple due dates can exist for a service based on the recurring pattern, the grid will include each frequency due date for that service that falls with the specified number of days.

For example, Service A has a recurring pattern of Monthly, on Day 10 of every 1 month(s). You run the work order generation process on 4/1/22 and enter 90 in the Due Within the Next __ days field. The grid will display three entries for Service A: one for 4/10/22, one for 5/10/22, and one for 6/10/22. However, if you had already created a work order for the 4/10/22 due date, the grid would show only the entries for 5/10/22 and 6/10/22.
Note: The system does not save selected services to allow for changing filter criteria for additional selections. Once you enter your criteria and make your selections, you must generate the work orders. Changing the filter criteria before generating work orders will clear the Create checkbox for all previously selected services.
Once the grid is populated, you must then select to create a work order for applicable agreements/services in the grid. When you click the Process button, the system creates a single job in SQL Agent for the selected agreements/services and adds the requested process run to the SM Generate Work Order Summary grid. The system runs the work order process either within a minute after the request or if using the scheduling feature, based on the Generate Agreement WO Time specified in SM Company Parameters.
Note: You can also select to Skip an agreement/service to make it unavailable for work order generation or leave both the Create and Skip checkboxes unselected to exclude it from the current work order generation session, but make it available for a future session.

Click on the following links for more information about using this form.
[Generate Preventative Maintenance Work
 Orders](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders)
[Remove the Skip Status on Agreement
 Services](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-creatingskipping-work-orders/remove-the-skip-status-on-agreement-services)
[About Creating/Skipping Work Orders](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-creatingskipping-work-orders)
[About the Work Order Generation Process](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process)

Related information

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
