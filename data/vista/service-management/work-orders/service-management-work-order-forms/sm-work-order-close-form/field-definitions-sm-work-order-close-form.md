---
title: "Field Definitions: SM Work Order Close Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-close-form/field-definitions-sm-work-order-close-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-close-form/field-definitions-sm-work-order-close-form"
---

# Field Definitions: SM Work Order Close Form

The following is a list of field descriptions for the SM Work
 Order Close form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Customer

Customer field in the header of the SM Work Order Close form.
Enter the customer to filter on, or press F4 for the SM Customer Info Lookup and select one.

Leave blank if not filtering work orders by customer.

## Service Site

Service Site field in the header of the SM Work Order Close form.
Enter the service site to filter on, or press F4 for the SM Service Sites Lookup and select one.

Leave blank if not filtering work orders by service site

## Service Center

Service Center field in the header of the SM Work Order Close form.
Enter the service center to filter on, or press F4 for the SM Customer Info Lookup and select one.

Leave blank if not filtering work orders by service center.

## Division

Division field in the header of the SM Work Order Close form.
Enter the division to filter on, or press F4 for the SM Division Lookup and select one.

Leave blank if not filtering work orders by division.

## Call Type

Call Type field in the header of the SM Work Order Close form.
Enter the call type to filter on, or press F4 for the SM Call Types Lookup and select one.

Leave blank if not filtering work orders by call type

## SM Cost Type

SM Cost Type field in the header of the SM Work Order Close form.
Enter the SM cost type to filter on, or press F4 for the SM Cost Types Lookup and select one.

## Scope Status

Scope Status drop-down list in the header of the SM Work Order Close form.
Select the scope status by which to filter work orders for closure.

Leave blank if not filtering by work order scope status.

## Price Method

Price Method drop-down list in the header of the SM Work Order Close form.
Select the price method by which to filter work orders for closure.
Leave blank if not filtering by work order price method.

## Cost Status

Cost Status drop-down list in the header of the SM Work Order Close form.
Select the cost status by which to filter work orders for closure.

- P - Projected Cost Exists - for labor that has not been run through Payroll, or purchase order lines that have not been invoiced.

- A - All Costs Actual - for all lines that have been invoiced and run through Payroll

Leave blank if not filtering work orders by cost status.

## Last Activity

Last Activity calendar field in the header of the SM Work Order Close form.
Enter the last activity date (MM/DD/YYYY) on the work order (either the latest Work Completed line entered, or trip performed by a technician). The date you enter is up until that date.

Leave blank if not filtering work orders by last activity date.

## Last Labor Activity

Last Labor Activity calendar field in the header of the SM Work Order Close form.
Enter the last labor-specif activity date (MM/DD/YYYY) on the work order (the latest Work Completed Labor line entered). The date you enter is up until that date.

Leave blank if not filtering work orders by last labor activity date.

## Aging Date

Aging Date calendar field in the header of the SM Work Order Close form.
Enter the date the work order was created (MM/DD/YYYY). Click the Calendar icon to select a date.
Leave blank if not filtering work orders by aging date

## Work Order is Fully Billed

Work Order Is Fully Billed checkbox in the header of the SM Work Order Close form.
Select this checkbox to filter on work orders that have been fully billed.

## All POs Closed

All POs Closed checkbox in the header of the SM Work Order Close form.
Select this checkbox to filter on work orders whose POs have all been closed.

## All Trips Completed

All Trips Completed checkbox in the header of the SM Work Order Close form.
Select this checkbox to filter on work orders whose final scheduled trip has been completed.

If open trips exist (those with a status of Open), a warning is displayed. If you select to close the work order, the open trips will be deleted. If you do not want the trips deleted, change applicable trips to a status other than Open. Trips with a status other than Open will be set to Completed

## All Costs Posted

All Costs Posted checkbox in the header of the SM Work Order Close form.
Select this checkbox to filter on work orders whose costs have all been posted.

## Auto Delete Open Trips

Auto Delete Open Trips checkbox in the Processing Settings section in the header section of the SM Work Order Close form.

Select this checkbox if you want to delete open trips on the work order. (If you do not selected this option, and trips are still open on the work order, you will receive an error. However, you can then either delete the trip manually or mark it complete.)

## Use Closest Open Month

Use Closest Open Month checkbox in the Processing Settings section in the header section of the SM Work Order Close form.
Select this checkbox to filter on the next-closest open month than the current month (assuming the current month is still open).

## Advanced Grid Options

Advanced Grid Options checkbox in the Processing Settings section in the header section of the SM Work Order Close form.
Select this checkbox to add Billable Remaining and Unclosed PO's data to the grid, for sorting purposes.
