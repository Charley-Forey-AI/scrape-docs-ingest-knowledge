---
title: "SM Work Completed Inventory Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form"
---

# SM Work Completed Inventory Form

Use the SM Work Completed Inventory form to add, edit, or review work completed Inventory lines for a work order.
Access this form from SM Work Orders by:

- selecting the Work Completed tab and double-clicking an Inventory line

- selecting the Work Completed drop-down in the toolbar and selecting Inventory

Note: In order to enter and edit work completed inventory lines, you must have the Inventory (IN) module.

Work completed inventory lines are used to capture stocked materials, non-stocked materials (those in HQ Materials only), and non-standard materials (not in IN or HQ) used on a work order. The system uses the information entered for each line to determine the costs incurred, as well as the charge to the customer or job. If the material is pulled from Inventory, the system updates the on-hand quantities for the specified Inventory location. If the work order is for a job, the system also updates the costs to the job in Job Cost.
Note: To capture materials pulled from an inventory location, you must have the Inventory (IN) module. To capture materials purchased from a vendor, you must enter an SM purchase order. For more information, see [SM Work Completed Purchase Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form).

For customer work orders, you will use work completed inventory lines to generate invoices. You can generate work orders one at a time using the Bill WO button at the bottom of the form or create multiple work orders at one time using SM Work Order Billing. Job work orders cannot be billed in Service Management. Instead, you must bill them using the Job Billing or Accounts Receivable modules. For more information about billing work orders, see Related Topics below.

## Batch Processing

When you enter and save a work completed inventory line, the system automatically creates a batch behind the scenes. The batch created depends on whether the material specified on the work completed line is stocked (from IN), non-stocked (from HQ Materials), or non-standard (not in IN or HQ).

- Stocked Materials — For these work completed inventory lines, the system creates an Inventory batch with a Source of SM Inv.

- Non-Stocked / Non-Standard Materials — For these work competed inventory lines, the system creates a miscellaneous batch with a Source of SMLedgerUpdate.

Once you post the batch (whether manually or automatically), the system makes the appropriate updates based on the material type. If the material is stocked and you specified to interface material use to IN (in SM Company Parameters), the system updates the on-hand quantities for the inventory location and makes the appropriate GL entries. If you did not select to interface to IN, only GL updates will occur. For non-stocked and non-standard materials, the system makes the appropriated GL entries; however, no module update will occur.

The following are related tasks:
[Enter Work Completed Inventory for Stocked Materials on a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-stocked-materials-on-a-work-order)
[Enter Work Completed Inventory for Non-Stocked Materials on a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-non-stocked-materials-on-a-work-order)

Related information

- [About Editing Work Completed Purchase Lines](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/about-editing-work-completed-purchase-lines)

- [Enter Cost Adjustments for Work Completed Lines](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments/enter-cost-adjustments-for-work-completed-lines)

- [GL Updates: Work Completed Inventory for Non-Stocked Materials](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-non-stocked-materials)

- [GL Updates: Work Completed Inventory for Stocked Materials](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-inventory-for-stocked-materials)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [GL Updates: Work Completed](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed)
