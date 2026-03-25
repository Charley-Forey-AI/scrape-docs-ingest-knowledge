---
title: "Field Definitions: SM Dispatch Board Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form/field-definitions-sm-dispatch-board-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form/field-definitions-sm-dispatch-board-setup-form"
---

# Field Definitions: SM Dispatch Board Setup Form

The following is a list of field descriptions for the SM
 Dispatch Board Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Board Name

The Board Name field on the SM Dispatch Board Setup form, Info tab.
This field is only editable for custom dispatch boards. You can use this field to select the "All" dispatch board for limited modifications; however, because it is a standard board provided by Viewpoint, the board name cannot be changed.
Enter the dispatch board name. Up to 50 characters allowed.

## Service Center

The Service Center field on the SM Dispatch Board Setup form, Info tab.
This field is enabled for custom dispatch boards only.
Enter the service center to which
 this dispatch board applies or press F4 to select from a list of valid service
 centers. When using this dispatch board (in SM Dispatch Board), only work orders referencing the specified service center are displayed on the board.
Note: Entry in this field is required if you will be specifying a division for this dispatch board. If you specify a division for this dispatch board, when using the board in SM Dispatch Board, only work orders referencing both the service center and division are displayed.

Leave blank if this dispatch board is not associated with a specific center. When using this dispatch board (in SM Dispatch Board), the board displays all work orders, regardless of service center.

## Division

The Division field on the SM Dispatch Board Setup form, Info tab.
This field is enabled for custom dispatch boards only.
Entry in this field requires that you first enter a service center in the
 Service
 Center field.
Enter or select the division to which this
 dispatch board applies or press F4 to select from a list of valid divisions for the
 specified service center. When using this dispatch board (in SM Dispatch Board), only work orders referencing the specified service center and this division are displayed on the board.
Leave blank if the dispatch board is not associated with a specific division. If you leave this field blank, but entered a service center, when you use this dispatch board (in SM Dispatch Board), the board displays all work orders assigned to the specified service center. If you also leave the service center blank, the board displays all work orders.

## Refresh Interval

The Refresh Interval field on the SM Dispatch Board Setup form, Info tab.

Enter the refresh interval (in seconds) for this dispatch board. Must be equal to or greater than 10 seconds. When using this board in SM Dispatch Board, the system will automatically refresh the board based on the value entered here. For example, if you set this value to 30 seconds, the system will auto-refresh the board every 30 seconds.

## Hide Board from Board Choices

The Hide Board from Board Choices checkbox on the SM Dispatch Board Setup form.

Select this checkbox to hide this dispatch board from dispatch board selection lists in SM Dispatch Board. When selected, the dispatch board is no longer available for selection in the Dispatch Board Selector (displayed when opening the SM Dispatch Board form) or the from dispatch board drop-down (just above the calendar grid) in SM Dispatch Board.
 Leave this checkbox unselected to include this dispatch board in all board selection lists. When not selected, the specified dispatch board is available for selection in the Dispatch Board Selector and the dispatch board drop-down menu on the SM Dispatch Board form.

## Refresh Board on Work Order Save

The Refresh Board on Work Order Save checkbox on the SM Dispatch Board Setup form, Info tab.

Select this checkbox to enable updates to this dispatch board (when open) each time a work order is saved.
Leave this checkbox unselected (default) to disable updates to this dispatch board when saving work orders.
Note: If you have large amounts of data on your system and/or use custom queries on your dispatch board, it is recommended that you do not select this checkbox, as it may potentially cause performance issues when saving work orders.

## Refresh Board on Scope Save

The Refresh Board on Scope Save checkbox on the SM Dispatch Board Setup form, Info tab.

Select this checkbox to enable updates to this dispatch board (when open) each time a work order scope is saved.
Leave this checkbox unselected (default) to disable updates to this dispatch board when saving work order scopes.
Note: If you have large amounts of data on your system and/or use custom queries on your dispatch board, it is recommended that you do not select this checkbox, as it may potentially cause performance issues when saving work order scopes.

## Technician

The Technician field on the SM Dispatch Board Setup form, Technicians tab.
This field is enabled for custom dispatch boards only.
Enter or select an active SM technician for
 this dispatch board. Press F4 for a list of valid technicians.
Tip: You can set up a technician on-the-fly by
 pressing
 F5 from this field or by clicking the Setup button in the F4 lookup. For
 more information about setting up technicians, see [Setting up a Service Technician](/en/vista/vista/service-management/service-management-setup/set-up-a-service-technician).

## Technicians: Active

The Active checkbox on the SM Dispatch Board, Technicians tab.

Display only, indicating the "active" status of the selected technician as defined in SM Technicians.
If selected, this technician will be available for selection when adding technicians to a dispatch board in SM Dispatch Board Setup or when entering transactions prompting for technician (e.g. work completed on a work order, required labor on agreements, etc.).
If unselected, the technician will not be available for selection when adding technicians to a dispatch board in SM Dispatch Board Setup or when entering transactions prompting for technician.

## Custom Queries: Query Name

The Query Name field on the SM Dispatch Board Setup form, Custom Queries tab.
Enter or select the custom query to display
 when this named board is selected in SM Dispatch Board. Press F4 for a list
 of valid custom queries. The query selected here will display below the standard dispatch
 board queries (Overdue, Unassigned, In Progress, Incomplete, and On Hold).
For information about creating custom queries, see [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).

## Standard Queries: Query Name

The Query Name field on the SM Dispatch Board Setup form, Standard Queries tab.

Display only, the query name for this standard query.
Note: You cannot add or delete queries on this tab. You can only use this tab to specify whether standard query is active or inactive. If you deselect the Active checkbox, this query will not display for this dispatch board in SM Dispatch Board.

## Standard Queries: Active

The Active checkbox on the SM Dispatch Board Setup form, Standard Queries tab.

Select this checkbox (default) to activate this standard query for this dispatch board. When using this board in SM Dispatch Board, this query will display in the queries panel of the dispatch board.
Do not select this checkbox if you want to hide this standard query from this dispatch board. When using this board in SM Dispatch Board, this query will not display in the queries panel of the dispatch board.
