---
title: "About SM Work Order Cost Adjustments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments"
---

# About SM Work Order Cost Adjustments

You can use the Adjustments feature in SM Work Orders to move work completed lines from an existing work order to a different work order for the same company or a different company.

Adjustments are allowed for all posted work completed line types except for Purchase lines; however, certain conditions do apply:

- The adjustment work completed line must be of the same line type as the source work completed line.

- The scope associated with the source work completed line cannot be closed.

- The source work completed line must have an actual cost greater than zero.Note: Labor and Purchase work completed lines are the only line types that initially have no actual costs. For labor lines, actual costs are posted when the employee is fully processed in Payroll. For purchase lines, actual costs are posted once you invoice the PO in AP Transaction Entry.

- You cannot enter an adjustment to a work completed line that is an adjustment (that is, it has a status of Adjustment) or a work completed line that has already been fully adjusted (0.00 remaining Actual Cost).

When you create an adjustment line, the system duplicates the source work completed line, but sets the units and amounts as negative. If you want to adjust only a portion of the work completed line, you can adjust the applicable values (see table below), making sure to enter them as negative values.
 For example, say you are adjusting a Misc line with a Total Actual Cost of 5,500.00 and you only want to move 50% of the Total Actual Cost to the new work order/scope. The original transaction has a Cost Qty of 100.000, so you would enter a Cost Qty of -50.000 on the adjustment line; all remaining values are adjusted accordingly.
Once you post the adjustment (save the line), the system sets the source line's status to Adjustment and adds the work completed line to the destination work order.
Tip: You can view the GL detail for original and adjustment entries on the Posted Detail tab (in SM Work Orders). The original transaction shows as a debit and the adjustment transaction as a credit. On the destination work order, the added work completed line shows as as a debit entry.

## Cost Values vs. Bill Values

When you adjust a work completed line, the system handles the cost values differently than bill values.
The cost values on the originating work completed adjustment line are copied exactly to the destination work completed line. This includes cost tax values, regardless of whether the default tax code for the destination work order differs from the originating work order.
However, the bill values on the destination work completed line may potentially differ from those on the originating work completed line, depending on the Rate Template, Tax Option Override, and Tax Code specified for the destination work order scope.
 For example, if you adjusted a material-related work completed line and the rate template on the originating work order scope has a material markup of 10%, but the rate template for the destination work order scope has a material markup of 20%, the Bill Rate and Bill Subtotal for the work completed line will differ between the original and destination work order.

## Allowable Adjustment Changes

You can make adjustments directly in the Work Completed grid or using the related Work Completed form (Cost Adjustment Info drop-down). Changes to line amounts for an adjustment are limited to the following:
Line TypeWork Completed Grid FieldWork Completed Form Field
EquipmentTime Units or Work UnitsTime Units or Work Units
LaborHrs WorkedCost Hours
MiscCost Qty and Billable Qty (units)Actual Cost and Billable Amt (no units)
Dest JC CT (job work orders only)
Cost Quantity and Billable Quantity (units)Cost Total and Billable Total (no units)
JC Cost Type (job work orders only)

InventoryQuantityQuantity

For information about entering cost adjustments, select the link below.
[Enter Cost Adjustments for Work Completed Lines](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments/enter-cost-adjustments-for-work-completed-lines)

Related information

- [SM Work Completed Equipment Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)

- [SM Work Completed Misc Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [SM Invoice Review Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form)

- [SM Work Order Billing Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-work-order-billing-form)
