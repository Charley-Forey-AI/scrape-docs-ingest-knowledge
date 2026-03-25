---
title: "SM Dispatch Board Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form"
---

# SM Dispatch Board Setup Form

Use the SM Dispatch Board Setup form to set up the dispatch boards needed for tracking and scheduling work order trips.

Viewpoint provides a default dispatch board titled "All". This board displays automatically if you open the SM Dispatch Board form prior to setting up your custom dispatch boards. The default board displays all technicians and all work orders for the active SM company. Customization of this board is limited to the refresh interval, adding/removing custom queries, and controlling which standard queries are shown on the board. You cannot customize the technicians or work orders displayed.
With custom boards, you can control the technicians and work orders displayed on the board, add/remove custom queries, and control which standard queries are shown on the board. Using the Technicians tab, you can assign the technicians you want associated with each board. These are the technicians to which you will assign work orders/trips. There is no limit to the number of technicians you can assign, but a minimum of one technician is required in order to use the board in SM Dispatch Board.
If you schedule and track work orders by service center, you can set up a separate dispatch board for each applicable service center. You can also associate each board to a division within the specified service center. When you select the dispatch board in SM Dispatch Board, only work orders assigned the specified service center or service center/division will display in the work order query pane.
Note: Trips placed in the Unscheduled or Scheduled/Unassigned
 columns of the Dispatch Board will show on every dispatch board, regardless of their
 assigned division and/or service center.

## 'Refresh Board' Options

The Refresh Board on Work Order Save and Refresh Board on Scope Save checkboxes control whether the dispatch board is updated (when open) each time a work order and/or work order scope is saved. If you have large amounts of data on your system and/or use custom queries on your dispatch board, it is recommended that you do not select either checkbox, as doing so may potentially cause performance issues when saving work orders and work order scopes.

## Custom Queries

The Custom Queries tab allows you to assign custom queries to a dispatch board.
 You will typically only use this tab if you will be filtering work
 orders using different criteria than is provided with the standard
 dispatch board queries (Overdue, Unassigned, In Progress, and
 Completed). For information about setting up custom queries, see
 [VA Inquiries Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).

## Standard Queries

The Standard Queries tab displays the standard queries assigned to each dispatch board. Although you cannot add or delete queries on this tab, you can designate which queries are active for each dispatch board. If you deactivate a query (deselect the Active checkbox for the query), that query does not display for that board.
There are five standard queries associated with each dispatch board:

- Overdue - Only displays if one or more work orders exist that are overdue and have not yet been scheduled.

- Unassigned - Work order has not been scheduled and either has not exceeded its specified Due Date or has no Due Date specified. All new work orders automatically display here.

- In Progress - One or more trips exist for the work order that are currently scheduled and assigned to a technician, but not yet completed.

-  Incomplete - All scheduled trips for the work order are completed, but the work order scopes are still Open. Once all work order scopes are closed and the work order is billed, it is removed from this list.

- On Hold - Only displays if one or more work orders have been placed 'on hold'.

## Hiding a Dispatch Board

If you do not want to delete a dispatch board, but you don't want it used in SM Dispatch Board, you can hide it by selecting the Hide Board from Board Choices checkbox. When you hide a board, it no longer shows in the Dispatch Board Selector (displayed when opening the SM Dispatch Board form) or in the dispatch board drop-down (just above the calendar grid) in SM Dispatch Board. Hiding a dispatch board does not change the board's setup; it only prevents it from being selected for display in SM Dispatch Board.

## Deleting a Dispatch Board

You can delete any dispatch board (other than the All dashboard), regardless of whether you are using it
 in SM Dispatch Board. Because the Dispatch Board is basically a
 "snapshot" of information stored in Service Management, deleting a
 board does not delete the technicians or queries assigned to the
 board, nor does it delete any trips you created and tracked using
 the board.

Select the following link for more information about using this form.
[Set up a Custom Dispatch Board](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/set-up-a-custom-dispatch-board)

Related concepts

- [SM Dispatch Board](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board)
