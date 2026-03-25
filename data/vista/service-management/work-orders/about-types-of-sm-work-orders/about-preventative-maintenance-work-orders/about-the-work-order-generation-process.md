---
title: "About the Work Order Generation Process | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process"
---

# About the Work Order Generation Process

When you generate work orders in SM Generate PM Work Orders, the system follows a specific process to determine whether a work order is needed for an agreement service.
Once you select the Process button to initiate the work order generation process, the following occurs:

- The system creates a single job in SQL Agent for the agreement services selected for work order generation. One job is created per SM company, so additional work order processes requested in the same SM company are included in the same SQL Agent job.

- The PM Generate Work Order Summary form opens and an entry appears in the grid for the requested process. The requested process is assigned an ID, a Status of Requested, and a Requested Time.

-  If you designated a specific time to run the work order process in the Generate Agreement WO Time field in SM Company Parameters, the system holds the requested work orders in a queue and processes them at the specified time. If you did not enter a value in the Generate Agreement WO Time field, the system begins the work order process run within a minute after the requested time. The SQL Agent Job Schedule field at the bottom of the form indicates the date and time the process is scheduled to run.

- If there are multiple requests, the system runs the work order process for each request in the order they were requested. This is determined by the Requested Time indicated for each request ID.

During the work order process run, the system looks at the Separate Scope Per Service Item checkbox on the agreement. If selected, the system generates a separate work order scope for each serviceable item associated with class maintenance tasks on the agreement. If not selected, service items with matching criteria (call type, price method, service site, etc.) are grouped together on one scope.
The system also checks the Separate Work Order checkbox for each agreement service to determine whether a separate work order is needed for that service. If selected, the system generates a separate work order with a single work order scope. If not selected, services will be added to existing work orders with matching criteria, as long as the status is New. If an existing work order is not found, a new work order is generated and will include all applicable services.
Note: If you select the Separate Scope Per Service Item checkbox for an agreement and one or more services on that agreement also have the Separate Work Order checkbox selected, the system generates a separate work order for each agreement service flagged for a separate work order. Remaining services are set up on one work order with separate scopes per service item.

If you designated an Assigned Tech to the agreement service in SM Service and the technician is Active in SM Technicians and PR Employees, the system automatically creates a single trip on work orders generated from the agreement service, with this technician designated. In addition, this technician is assigned as the Lead Tech on the work order. No description, details, date, time, or duration are defined for the trip.
Work order numbers are assigned based on the value specified in the Next Work Order Number field in SM Company Parameters. The due type and date for work order scopes are based on the scheduling information defined for the service (in SM Work Schedule, Schedule tab) as follows:

- Due On - Sets the Due type to 0-By and the 'due on' date based on the recurring pattern specified for the service. For example, if today's date is 4/1/12 and the service has a recurring pattern of Monthly, on Day 10 of every 1 month(s), the system will set the due date to 4/10/12.

- Due By - Sets the Due type to 0-By and the 'due by' date based on the recurring pattern specified for the service. For example, if today's date is 4/1/12 and the service has a recurring pattern of Monthly, on Day 10 of every 1 month(s), the system will set the due date to 4/10/12.

- Due Within - Sets the Due type to 1-Within and the 'due within' date range based on the 'due within' days and the recurring pattern specified for the service. For example, if today's date is 4/1/12 and the service specifies a 'due within days' of 30 and a recurring pattern of Monthly, on Day 10 of every 1 month(s), the system will set the due within date range to "4/10/12 - 5/10/12".

Note: The system does not generate work orders for a service out of sequence unless the prior due date for a sequence is flagged as 'Skipped'.

Related information

- [Generate Preventative Maintenance Work Orders](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders)

- [SM Generate PM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form)
