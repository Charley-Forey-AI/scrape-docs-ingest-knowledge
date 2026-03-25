---
title: "About Capturing Work Completed for a Work Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order"
---

# About Capturing Work Completed for a Work Order

When you complete a service call, entering work completed lines on the associated work order allows you to capture the costs and enable billing the customer.
Once a technician has completed the work requested by a service site, entering work completed lines allows you to capture all of the components related to that service call; that is, the equipment used, labor hours, miscellaneous expenses, and material usage (stocked and purchased). You can use the Work Completed tab in SM Work Orders to capture work completed on a work order or enter records directly in the work completed forms (SM Work Completed Equipment, SM Work Completed Labor, SM Work Completed Misc, or SM Work Completed Inventory). You can access the work completed forms via the Work Completed menu in the SM Work Orders toolbar.
To capture work completed for purchased materials, you must enter a purchase order (via SM Purchase Order Entry or PO Purchase Order Entry) or by distributing an existing PO item to an SM work order (via PO Item Distribution). See [About Entering an SM Purchase Order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order) and/or [SM Work Completed Purchase Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form)for more information.
Before you begin entering work completed, you must set up at least one work order sequence (scope). The work order sequence must be assigned a call type and rate template, as well as a 'bill to' customer (if a customer work order) or phase (if a job work order). Once you enter work completed for that sequence, these fields are disabled and cannot be changed.

## Changing Work Completed Lines

You can make changes to work completed lines that you have previously posted, but there are some limitations.
For work completed lines posted to a Time and Materials scope, changes are allowed at any time prior to billing. Once you have billed the work completed line, edits are no longer allowed unless the work completed line was generated via AP or through entry of a purchase order (in SM Purchase Order Entry or PO Purchase Order Entry). For these lines, you can edit the related AP or PO transaction line and the costs for the resulting work completed line are updated; however, bill amounts are not updated.
For Flat Price scopes, billing can occur as long as the amount already billed is less that the total Flat Price amount. Work completed lines posted to the Flat Price scope are not billable and have no effect on the scope's billable amount. Therefore, you can add, delete, or change any work completed line posted to the Flat Price scope at any time, even if the scope is fully billed.
Once you close a work order scope, you can no longer edit, add, or delete work completed lines for that scope. If you have not billed the work order, you can do so even if the scope is closed. For unbilled T&M scopes, you can edit the billing fields for related work completed lines until they are invoiced.

## Adjustments

If you determine you need to move a work completed line to a different work order, you can do so using the Adjustments feature. When you enter an adjustment, the system 'backs out' the adjusted line/amounts and adds the line/amounts to the specified destination work order/scope. For more information, see [About SM Work Order Cost Adjustments](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments).

Select the following links for information about entering work completed.
[Enter Work Completed Equipment for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-equipment-for-a-work-order)
[Enter Work Completed Labor for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-labor-for-a-work-order)
[Enter Work Completed Miscellaneous for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-miscellaneous-for-a-work-order)
[Enter Work Completed Inventory for Stocked Materials on a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-stocked-materials-on-a-work-order)

Related information

- [SM Work Completed Equipment Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)

- [SM Work Completed Misc Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)
