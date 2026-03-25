---
title: "SM Dispatch Board | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board"
---

# SM Dispatch Board

With the Service Management Dispatch Board, you can manage the scheduling of work orders, technicians, and trip progress, all in one place.
The Dispatch Board is an interactive tool that allows you to perform drag-and-drop scheduling of service and small job work orders, track the status of trips and technician availability, and monitor unassigned, overdue, and incomplete work orders. You can also create new work orders and purchase orders, as well as access existing work order, trip, customer, and site information.
Note: Each technician assigned to a dispatch board must have a work schedule defined in SM Technicians. When working with a dispatch board, you can see at a glance, which technicians are working (white background) and which ones are not (gray background). If a technician is scheduled to work, but is unavailable for part or all of that day, you can set up their "unavailable" time using the SM Technician Unavailable Time form, and that time will display in pink on the dispatch board. For more information, see [SM Technician Unavailable Time](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-technician-unavailable-time-form).

There are five standard queries associated with each dispatch board that are used to filter work orders based on their status/progress.

- Overdue - This query will only display if one or more work orders exist that are overdue (i.e. have exceeded the Due Date specified for one or more scopes on the work order), and have not yet been scheduled.

- Unassigned - Work order has not been scheduled and either has not exceeded its specified Due Date or has no Due Date specified. All new work orders automatically display here.

- In Progress - One or more trips exist for the work order that are currently scheduled and assigned to a technician, but not yet completed.

-  Incomplete - All scheduled trips for the work order are completed, but the work order scopes are still Open. Once all work order scopes are closed and the work order is billed, it is removed from this list.

- On Hold - This query will only display if one or more work orders have been placed 'on hold'. For more information, see [Placing a Work Order on Hold](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board/place-a-work-order-scope-on-hold).

If you wish to filter work orders using different or additional criteria than what is provided by the standard queries, you can set up custom queries in VA Inquiries and then assign them to dispatch boards in SM Dispatch Board Setup. Custom queries will display below the standard queries for each applicable dispatch board. For information about setting up custom queries, see [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).

## Access to Service Manager Dashboard in Field Service

 If you have Field Service and have integrated your Vista Web account (that is, you have designated the appropriate Vista Web URL in VA Site Settings), you can access the Service Manager Dashboard from any dispatch board by clicking the Send Work Orders to Technicians Instantly button (just below the Alerts button).
You can also access the Service Manager Dashboard as follows:

- From the Vista Main Menu, select Service ManagementPrograms and double-click the SM Dashboard link.

- From the SM Work Orders form, click the Send Work Orders to Technicians Instantly button (just below the Work Completed drop-down in the toolbar).

If you do not have Field Service, clicking any of these links takes you to the Trimble Viewpoint website for information about Service Management Dashboard.

For more information about the Dispatch Board, click the links below.
[Set up a Custom Dispatch Board](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/set-up-a-custom-dispatch-board)
[About Using the Dispatch Board](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board)
