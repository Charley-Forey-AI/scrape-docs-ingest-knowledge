---
title: "SM Generate Work Order Summary Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-work-order-summary-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-work-order-summary-form"
---

# SM Generate Work Order Summary Form

Use the SM Generate Work Order Summary form to view the status of work order process runs.
You can also use this form to continue a process run that was interrupted due to a power outage or system shutdown, well as clear completed runs
You can access this form in one of two ways:

- By selecting work orders to generate in [SM
 Generate PM Work Orders](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-generate-pm-work-orders-form) and clicking Process.

- From the main menu. You will typically only use this
 method when you need to continue a process run that was interrupted or to clear
 completed process runs.

The upper grid shows work order process runs that are requested,
 processing, or completed. The lower grid shows errors that may occur during a process run
 (e.g. selecting work orders for generation that have already been processed).
When you click the Process button in SM Generate PM Work Orders, the system creates a single job in SQL Agent for the selected agreement services and opens this form. The process requests are added to the upper grid and are assigned an ID, a status of Requested, and a Requested Time. The system runs the work order process either within a minute of the request or if using the scheduling feature, at the time specified in the Generate Agreement WO Time field in SM Company Parameters.
Regardless of the timing, if other requests exist in the grid, the system begins the run with the earliest request (based on the Requested Time) and continues with each request until all are completed. Once completed, the status for each ID is set to Complete.
For more information about using this form, click the link below.
[Remove, Cancel, or Complete Work Order Process Runs](/en/vista/vista/service-management/work-orders/remove-cancel-or-complete-work-order-process-runs)

Related information

- [Generate Preventative Maintenance Work Orders](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders)
