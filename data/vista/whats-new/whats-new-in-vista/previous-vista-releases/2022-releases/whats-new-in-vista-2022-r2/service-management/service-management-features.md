---
title: "Service Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/service-management/service-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r2/service-management/service-management-features"
---

# Service Management Features

Vista 2022 R2 delivers on user-requested Service Management enhancements, fixes, and other improvements.

## Relocated Margin Field for Flat Price Scopes

The Margin field that displays (in SM Work Orders) for Flat Price work order scopes was moved below the Price field for improved workflow. Previously, the Margin field was located before the Price Method field and was only visible after selecting Flat Price as the price method, resulting in a poor workflow. Now when you enter the flat price amount, the cursor moves directly to the Margin field.

## Performance Tuning the SM Dispatch Board

You now have the ability to set the refresh interval for Dispatch Boards. The refresh interval determines how often the dispatch board is refreshed when it is being used in SM Dispatch Board.
Additionally, you also have the ability to hide standard queries so that they do not display for a selected Dispatch Board, as well as hide standard queries that you are not using.
The following changes were made in SM Dispatch Board Setup to implement these features:

- Added a Refresh Interval field to the Info tab. The value entered in this field determines how often the system refreshes the selected board when it is in use in SM Dispatch Board. For more information, see [Refresh Interval](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form/field-definitions-sm-dispatch-board-setup-form#concept-9899--en).

- Added a Hide Board from Board Choices checkbox to the Info tab. When this checkbox is selected for any dispatch board, including the standard "All" board, that board is no longer available in the Dispatch Board Selector (displayed when opening the SM Dispatch Board form) or from the dispatch board drop-down (just above the calendar grid) in SM Dispatch Board. This allows you to hide boards that you do not want to delete, but are not currently using. It is also useful if you just want to limit the number of boards displayed in the selection lists. For more information, see [Hide Board from Board Choices](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form/field-definitions-sm-dispatch-board-setup-form#concept-771--en).

- Added a new Standard Queries tab. This tab displays the five standard queries automatically assigned to each dispatch board, including the standard "All" board. You cannot add or remove queries from this tab; however, you can use the Active checkbox to specify whether the query will display for that board in the SM Dispatch Board. For more information, see [Standard Queries: Active](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form/field-definitions-sm-dispatch-board-setup-form#concept-3341--en).

- In conjunction with adding a new Standard Queries tab, changed the label of the Queries tab to Custom Queries for better clarity.

For more information about dispatch board setup, see [SM Dispatch Board Setup Form](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-dispatch-board-setup-form).

## Access to the Service Manager Dashboard in Field Service

 If you have Field Service and have integrated your Vista Web account (that is, you have designated the appropriate Vista Web URL in VA Site Settings), you can now access the Service Manager Dashboard from Vista as follows:

- From the Vista Main Menu, select Service ManagementPrograms and double-click the SM Dashboard link.

- From the SM Work Orders form, click the Send Work Orders to Technicians Instantly button (just below the Work Completed drop-down in the toolbar).

- From the SM Dispatch Board form, click the Send Work Orders to Technicians Instantly button (just below the Alerts button).

If you do not have Field Service, clicking any of the links indicated above takes you to the Trimble Viewpoint website for information about Service Management Dashboard.

## New Refresh Option in SM Batches

If you post a batch in a related batch processing form while the SM Batches form is open, you can now use the new Refresh button to update the Batches grid.
 Some batches listed in the grid cannot be posted using SM Batches, but rather must be posted using the related batch processing form. For example, batches with an 'SM Invoice' source must be posted directly in AR Batch Process. If you post the AR batch while SM Batches is open, clicking the Refresh button updates the grid, removing the batch you just posted.

## Separate SM Work Order Close and Reopen Functions

The SM Work Order Close and Work Order Reopen functionalities are now handled in separate forms to allow setting security individually for each function.
To accommodate this change, a new SM Work Order Open form was added, with access via SM Work Orders at the scope level (Reopen option in the Scope Status drop-down) and at the work order level (Reopen WO button at the bottom of the SM Work Orders form.
When you close a scope or work order, the system uses the SM Work Order Close form. Then, when you select to reopen a scope or work order, the system uses the new SM Work Order Reopen form. The actual close and reopen functionalities remain the same.

##  Change to Handling of Negative Agreement Billings

When entering a billing schedule in SM Agreements (Billing Schedule tab) or modifying a billing schedule in SM Billing Schedule Mod, you must now enter a billing amount that is equal to or greater than 0.00.
 Previously, if you entered a negative amount on a billing schedule to generate a negative billing, processed the billing (via SM Agreement Billings Due), and then amended the agreement, it would potentially result in amortization not balancing with the total billing amount, and would require manually entering a journal entry in GL Journal Entry to correct the amount.
 Now, if you need to enter a negative billing, you must do so by entering a negative adjustment billing in SM Agreement Adjustments. This allows for proper updates to GL and ensures balance between amortization and total billing amounts.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
