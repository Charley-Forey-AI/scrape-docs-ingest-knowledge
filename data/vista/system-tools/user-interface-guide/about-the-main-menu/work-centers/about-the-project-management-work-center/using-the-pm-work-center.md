---
title: "Using the PM Work Center | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-the-project-management-work-center/using-the-pm-work-center"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-the-project-management-work-center/using-the-pm-work-center"
---

# Using the PM Work Center

You can use the PM Work Center to perform a variety of tasks and functions, such as view project information, create and edit records, and review/approve purchase orders and subcontracts.

View RecordsUse the filters at the top of the PM Work Center (Company, Project Manager, Project Status, and Project), and then select a record in the menu. The grid will populate with all of the records that match the selected criteria.
For example if you want to view all of the RFIs associated with a specific project, select a Company and Project in the filter fields, and then select Document Control >  Request For Information in the menu. All of the RFIs associated with the selected company and project will display.
Using the GridOnce the PM Work Center displays records, you can manipulate and customize how this information displays.

- Keyword Search - Enter a keyword and the system will search all of the visible columns in the grid for items that contain the keyword. Columns that have been hidden will not be included in the search.

- Filter Bar - The Filter Bar allows you to filter the items in the grid by a specific column. Right-click the mouse in the grid and select Filter Bar from the menu that appears to add a filter bar to the top of the grid. Enter information into the filter bar to filter the data in the grid.Note: The Filter Bar and Keyword Search field both search and filter the data in the grid, but they function differently.The Filter Bar searches for items that begin with the keyword value. For example, if you enter "Blue" in the Filter Bar, the search results will include "Blue Red" but not "Red Blue". You cannot use wildcards in a Date column of the Filter Bar.
The Keyword Search field searches for any item that contains the keyword. For example, if you enter "Blue" in the Keyword Search field, the search results would include both "Blue Red" and "Red Blue".

- Group Bar - The Group Bar allows you to group the items in the grid by column heading. For example, you can use it to group all of the PCOs that display in the grid by PCO type. Right-click the mouse in the grid and select Group Bar from the menu that appears. Once the Group Bar displays at the top of the grid, drag a column heading into the Group Bar to group the data by that column.

- Totals - You can add a totals row to the bottom of the grid. This row displays a total of each relevant column and only includes the displayed items. For example, you can use this feature to see the total contract change amount associated with a filtered list of pending change orders. Right-click in the grid and select Totals from the menu that appears to add the Totals row to the bottom of the grid.

- Export the grid to a file - You can export the records that display in the PM Work Center to a file (for example, to an MS Excel spreadsheet or PDF file). Right-click in the grid and select Export Grid from the menu that appears.Tip: See [Using the Grid Print Preview/Print/Export Options](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids/grid-print-previewprintexport-options) for more information on exporting grids.

- Customize the columns - You can add or remove the columns that display on the grid by selecting the Column Settings icon () above the grid.

Open/Edit a recordUse the PM Work Center menu to display a list of records. Once the records display in the grid, double-click on a record to open it. For example, select Document Control Meeting Minutes in the PM Work Center menu and then double-click on a meeting in the grid. This will open the meeting using the PM Meeting Minutes form.Create New RecordsYou can create a new record by selecting the type of record to create from the Work Center menu, choosing record from the grid (middle panel), right-clicking the mouse, and selecting Actions > New Record.In some cases, you can also create new records by selecting the type of record to create from the Work Center menu, choosing a record from the grid (middle panel), selecting the Create Related Record icon (), and then from the drop-down menu, selecting the record type to create.
Note: When you create records using the Create Related Record option, the new record will automatically be linked with the original record using the Related Items feature.

View / Open Related ItemsUse the Related Items panel on the right hand side of the PM Work Center to view and open items that are related to the record selected in the grid. For example, you can highlight a project issue in the grid and the Related Items panel will display all of the PCOs, RFIs, and other items related to that issue.This panel will also display attachments associated with the selected record. For example if you highlight an RFI, the RFI documents generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature will display in a folder titled Attachments.
Note: The Create and Send feature must be set up to save the generated documents as attachments before they will display in the Attachments folder in the Related Items panel. Check the Default Create and Send Attach to Parent Form as checked box on the Info tab of the PM Create & Send Settings if you want the system to save generated documents as attachments.

Organizing the Menu ItemsYou can customize the menu in the left panel of the PM Work Center. Changes to this menu only affect how the menu displays on this PM Work Center for your user account. If you have multiple PM Work Centers, only the selected PM Work Center is affected by the changes.

- Rename Menu Items - Select a highlighted menu item and the title of it will be enabled. Enter text to change the title.

- Rename Folder Items - Highlight a folder, right-click on it, and select Rename. This enables the title of the folder. Enter text to change the title of the folder.

- Drag and Drop Menu Items - You can drag and drop the menu items into any folder in the menu. Left-click on an item and hold down the left mouse button as you pull the item to the desired folder.

- Hide Menu Items or Folders - Highlight a menu item or folder, right-click on it, and select Hide from the menu that appears. The selected folder or menu item will be removed from the menu.

- Show Hidden Menu Items or Folders - Right-click in the menu tree panel and select Show from the menu that appears. Select All to restore all menu items and folders that have been hidden, or use the menu options to locate the specific folders and items that you would like to display.

Save/Load a PM Work CenterThe save and load feature is intended to reduce the time it takes to set up work centers.
For example, your system admin can create a work center, customize it for a specific group of employees (such as project managers, payroll clerks, etc.), and then save the modified work center and make it public. You can then add the modified work center to your application window.
This feature applies to all work centers (Dashboard, Project Management, Service Management, and Accounting). You can use saved work centers in any company.
For more information about saving and loading work centers, see [Save a Work Center](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/save-a-work-center) and [Load a Saved Work Center](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/work-centers/about-work-center-setup/add-a-saved-work-center-to-the-application-window).
Review/Approve Purchase Orders and SubcontractsIf you are using the Workflow Process feature, you can use the PM Work Center to review and approve or reject purchase orders and/or subcontracts that are assigned to you for review/approval. Once a PO or subcontract is submitted for approval (in their related forms), any items assigned to you for review are displayed in the My Documents to Review query (left panel of the Work Center menu in Document Review section). You can then select a PO or subcontract, review it, and approve or reject it. For more information, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).
