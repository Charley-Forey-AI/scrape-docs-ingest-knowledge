---
title: "Enter Cost Adjustments for Work Completed Lines | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments/enter-cost-adjustments-for-work-completed-lines"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments/enter-cost-adjustments-for-work-completed-lines"
---

# Enter Cost Adjustments for Work Completed Lines

You can enter cost adjustments for SM Work Orders to move work completed lines from one work order to another work order in the same company or a different company.
You can enter cost adjustments directly in the Work Completed grid or using the related work completed form (for example, SM Work Completed Equip).The following describes how to enter a cost adjustment for a work completed line using both methods.

1. Open the SM Work Orders form.

1. Choose the method for entering the cost adjustment:

- If making the adjustment directly in the work completed grid, select the Work Completed tab.

- If making the adjustment via the work completed form, open the applicable form by either double-clicking the source line in the Work Completed grid or by selecting Work Completed from the toolbar and then selecting the appropriate form from the drop-down list.

1. Add a new work completed line:

- If using the work completed grid, add a new line and in the Line Type field, enter the line type for the cost adjustment. Must be the same line type as the work completed line you are adjusting.

- If using the work completed form, select New Record () from the toolbar and then expand the Cost Adjustments Info drop-down.

1. Flag the line as a cost adjustment:

- If using the work completed grid, select the Adj checkbox.

- If using the work completed form, select the Create Adjustment checkbox.

1. In the Orig Line # field, enter the Work Completed line you are adjusting. Press F4 to select from a list of work completed lines of the specified line type.The system automatically populates the record with data from the original work completed line, but with negative quantity, rate, and amount values.

1. In the Dest SM Co# field, enter the destination company for the cost adjustment. Press F4 to select from a list of valid SM companies.

1. In the Dest Work Order field, enter the destination work order. Press F4 to select from a list of valid SM work orders.

1. In the Dest Scope field, enter the destination scope sequence. Press F4 to select from a list of valid scope sequences for the destination work order.

1. If applicable, adjust the defaulted line amounts.Adjustments allowed are based on the line type. For more information, see [About SM Work Order Cost Adjustments](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments).

1. Save the record.

Once you save the cost adjustment line, the system selects the Has Adj checkbox for the source work completed line and sets the status of the adjustment line to Adjustment. For the destination work completed line, the system sets the Adj checkbox to selected and displays information from the source work order (Orig Line #, Src Co#, Src Work Order, and Src Line #).Note: You can view the GL update for both the originating work order and the destination work order using the Posted Detail tab. For more information, see [About Posted Detail: Work
 Completed](/en/vista/vista/service-management/work-orders/updates-to-gl/about-posted-detail-work-completed).
