---
title: "Field Definitions: SM Work Order Billing Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-work-order-billing-form/field-definitions-sm-work-order-billing-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-work-order-billing-form/field-definitions-sm-work-order-billing-form"
---

# Field Definitions: SM Work Order Billing Form

The following is a list of field descriptions for the SM Work
 Order Billing form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Service Center

Enter the service center by which to filter work orders for billing. Only work orders referencing this service center that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave blank if not filtering by service center.

## Division

Enter the division by which to filter work orders for billing. Only work orders with work completed items referencing scopes assigned this division that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave blank if not filtering by division.

## Customer

Enter the customer by which to filter work
 orders for billing. Only work orders for this customer that have not been billed and that
 meet all other filter criteria will display in the Work Orders grid. If you enter a value
 in this field and in the Bill To field, the system will display
 only work orders where both fields match.
Leave blank if not filtering by customer.

## Bill To

Enter the bill to customer (from AR Customers) for filtering work orders for billing. Only work orders for this customer that have not been billed and that meet all other filter criteria will display in the Work Orders grid. Press F4 to see a list of valid customers.
If you enter a value in this field and in the
 Customer field, the system will only display work orders where both fields
 match.
Leave blank if not filtering by bill to customer.

## Service Site

Enter the service site by which to filter work orders for billing. Only work orders for this service site that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave blank if not filtering by service site.

## Date Provided

Enter the beginning date in a range of dates by which to filter work orders for billing. Only work orders with work completed items posted on or after this date that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave this field blank if you are filtering by
 date range but want to include all work completed items posted on or prior to the ending
 date specified in the To field (right).
Note: Leave both date fields blank if not filtering by date range.

## To

Enter the ending date in a range of dates by which to filter work orders for billing. Only work orders with work completed items posted on or prior to this date that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave this field blank if you are filtering by
 date range but want to include all work completed items posted on or after to the beginning
 date specified in the Date Provided field (left).
Note: Leave both date fields blank if not filtering by date range.

## Line Type

Select the line type by which to filter work orders for billing. Only work orders with work completed items of this type that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave blank if not filtering by line type.

## Scope Status

Select the scope status by which to filter work orders for billing. Only work orders with work completed items of this work order scope status that have not been billed and that meet all other filter criteria will display in the Work Orders grid.
Leave blank if not filtering by work order scope status.

## Reference No

Enter the reference number for auto-selecting work completed lines for billing. When you move off the field, the system selects the
 Bill
 checkbox for work completed lines on all work orders matching the current filter settings and the specified reference number. If all work completed lines for a work order match the specified reference number, the system also selects the
 Bill
 checkbox for the work order (in the Work Orders grid). If only some of the work completed lines on the work order match the reference number, the work order's
 Bill
 box will be colored blue ().
The system will then clear the reference number and return focus to this field to allow entry of another value.
Note: The
 Reference No
 field is not a filtering option; it is only used to auto-selecxt the
 Bill
 flag for applicable work completed lines. It can be entered with the filter criteria or after filtering is complete.

## Work Order: Bill

Check this box to bill this work order. The system will automatically check the Bill box in the Work Order Detail grid for all work completed lines related to this work order.
Leave this box unchecked if you do not want to bill the work order at this time or if you want to individually select which related work completed lines to bill for the work order (using the Work Order Detail grid).

## Work Order Detail: Bill

Check this box to bill this work completed line.
Note: The system will automatically check the Bill box for
 this line's work order (in the Work Order grid) when you check this box for all work
 completed lines on the work order.
Leave this box unchecked if you do not want to bill this work completed line at this time.

## Billing Amount

Enter the amount to bill for this invoice session. This can be the full flat price amount or a partial amount. The system will automatically calculate the billing percent based on the amount entered here and the flat price amount.
Leave this field blank to enter a billing percent. The system will automatically populate this field with the appropriate amount once you enter the billing percent.

## Billing Percent

This field automatically defaults a percentage based on the Billing Amount and the Flat Price. If the billing amount is 0.00 (i.e. you did not enter an amount), enter the percent (1.00% - 100.00%)of the flat price to bill for this invoice session. The system will automatically calculate the billing percent based on the amount entered here and the flat price amount.

## Is Adj

Appears in the Work Order Detail section of the Work Order Billing form.
checkbox indicates that a cost adjustment to an Equipment, Labor, Miscellaneous or Inventory Work Completed line has been created for this work order line number.

## Orig Line #

Appears in the Work Order Detail section of the Work Order Billing form.
The original work order line number appears in this field if there has been a cost adjustment made to this line.
