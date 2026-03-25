---
title: "Creating Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/creating-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/creating-work-orders"
---

# Creating Work Orders

When you are ready to create work orders for equipment due for maintenance, you can use the EM Work Order Initialize form to easily search for and select equipment due for maintenance, and then generate the work orders.
The system uses the criteria you select to determine
 the maintenance groups to initialize. In addition, it uses the [Standard Maintenance Group Options](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-standard-maintenance-group-options) in EM Company
 Parameters to determine which maintenance items and linked maintenance groups to
 include during initialization. The system automatically sets the
 Create
 checkbox to selected for each group in the grid. The
 Items
 Due
 and
 Items
 Not Due
 columns display the number of items due/not due (respectively) for
 each maintenance group. To view those items, select either the Items Due or Items
 Not Due tabs.
Maintenance items shown on the Items Due tab will automatically have the Initializecheckbox selected. You will need to review all items and deselect the Initialize checkbox for those that you do not want initialized to a work order.
Note: Selecting or deselecting the Create checkbox for a maintenance group (in the Std Maint Groups Matching Criteria grid) will automatically select or deselect the Initialize checkbox for all related maintenance items on this grid.
To select equipment due for maintenance and create work orders:

1. Open the SM Work Order
 Initialize form.

1. In the
 WO
 Date
 field, enter the date to use as the creation date for all
 generated work orders.

1. In the Days in Advance field, enter the number of days in advance for scheduled items to be included on work order (e.g. if you have items due for maintenance in 30 days, you would enter a number equal to or greater than 30).

1. In the Variances in Advance field, enter the number of variances in advance for scheduled items to be included on work order (e.g. if you have items with a warning interval of 200 miles/kilometres that are due for maintenance in 300 miles/kilometres or less, enter a number equal to or greater than 2 in this field).

1. In the Select Equipment Matching Following Criteria section, enter the appropriate filter values.

1. Click Refresh. The system populates the grid based on the search criteria and auto-selects the Create checkbox for all maintenance groups in the grid and the Initialize checkbox for all items in the Items Due grid.

1. In the Std Maint Groups Matching Criteria grid, deselect the Create checkbox for any maintenance groups that you want excluded when generating work orders.

1. In the Items Due grid, deselect the Initialize checkbox for any maintenance items you want excluded when generating work orders.

1. In the Create Work Orders section (below the grid), enter the appropriate default values as needed.

1.  If you are not auto-generating work order numbers, use the Beginning WO field to enter the number with which to work order numbering.

1. Click the Create WOs button. The system will generate work orders and display them on the Work Orders Created tab.

Related information

- [About the EM Work Order Initialize Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-initialize-form)
