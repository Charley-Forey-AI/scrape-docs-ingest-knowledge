---
title: "Set up a Custom Dispatch Board | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/set-up-a-custom-dispatch-board"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/set-up-a-custom-dispatch-board"
---

# Set up a Custom Dispatch Board

You can set up one or more custom dispatch boards to meet your dispatch needs using the SM Dispatch Board Setup form.
Vista provides a default dispatch board titled All. This dispatch board shows all technicians and all work orders. Although you can add custom queries to this board, you cannot filter the technicians or work orders displayed on this board.In order to customize what technicians and work orders you want displayed on the dispatch board, you must create a custom dispatch board.
The following steps will guide you through setting up a custom dispatch board.

1. From the Main Menu, select Service Management >  Programs > SM Dispatch Board Setup.

1. In the Board Name field, enter a name for your dispatch board.

1. If you want this dispatch board to include only work orders for a specific service center, enter the applicable service center in the Service Center field or press F4 to select from a list of valid service centers.Note: Entry of a service center is required if you are designating a division for this board.

Leave this field blank if this dispatch board is not associated with a specific service center.

1. If you want this dispatch board to include only work orders for a specific division, enter the division in the Division field or press F4 to select from a list of valid divisions for the specified service center.Leave blank if the dispatch board is not associated with a specific division.

1. If you want to change the default refresh interval (180 seconds), use the Refresh Interval field to enter the new refresh interval. Must be equal to or greater than 10 seconds.

1. If you are not ready for this board to be available for selection in SM Dispatch Board, select the Hide Board from Board Choices checkbox. Otherwise, leave the checkbox unselected.

1. If you want the dispatch board updated (when open) each time a work order and/or work order scope is saved, select the Refresh Board on Work Order Save and/or Refresh Board on Scope Save checkboxes (respectively). Otherwise, leave checkboxes unselected.Note: If you have large amounts of data on your system and/or use custom queries on your dispatch board, it is recommended that you leave both checkboxes unselected. Selecting them may potentially cause performance issues when saving work orders and work order scopes.

1. Add technicians to board.

1. Select the Technicians tab.

1. In the Technician field, enter the technician to assign to this board or press F4 to select from a list of active technicians.

1. Save the record.

1. Repeat the process for each technician you want to add.

1. Add custom queries to board.Note: You can only assign custom queries to a dispatch board if you have already created them using [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form).

1. Select the Custom Queries tab.

1. In the Query Name field, enter the custom query to add or press F4 to select from a list of valid custom queries.

1. Save the record.

1. Repeat the process for each custom query you want to add.

1. Deactivate a Standard Query.By default, standard queries are automatically set to Active, so if you do not want the query showing on the dispatch board, you can deactivate it to hide it.

1. Select the Standard Queries tab.

1. In the grid, select the standard query you want to hide for this board.

1. Deselect the Active checkbox.

1. Save the record.

1. Repeat the process to deactivate any other queries.

If this dispatch board is active (that is, you did not select the Hide Board from Board Choices checkbox), your dispatch board is ready to use and is available for selection in SM Dispatch Board. For more information about the SM Dispatch Board, see [SM Dispatch Board](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board) and [Using the Dispatch Board](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board).
