---
title: "Enter Work Completed Inventory for Stocked Materials on a Work Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-stocked-materials-on-a-work-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-stocked-materials-on-a-work-order"
---

# Enter Work Completed Inventory for Stocked Materials on a Work Order

Enter work completed inventory lines to capture stocked material expenses for job and customer work orders (including those auto-generated from a customer agreement).

You can use the Work Completed tab in SM Work Orders or the SM Work Completed Inventory form to enter work completed lines.The instructions below describe entry of work completed inventory lines for stocked materials using the Work Completed grid in SM Work Orders.
Note: If you enter work completed for a job work order and the job is hard or soft-closed, you can only save the record if you allow posting to closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs boxes are checked in JC Company Parameters).

1. Open the SM Work Orders form (Service Management > Programs > SM Work Orders).

1. In the Work Order field, enter the work order to which you are adding the work completed entry.

1. Select the Work Completed tab.

1. From the Line Type drop-down, select 4-Inventory.

1.  In the Scope Seq field, enter the work order scope fro this line or press F4  to select from a list of valid scopes for the work order.

1. In the Date field, enter the date the work was completed or accept the current date default.

1. For Customer work orders only:

1. If the work complete line is not billable, select the Non-Billable checkbox. For information about the defaulting and enabling/disabling behavior for this checkbox, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form/field-definitions-sm-work-completed-misc-form#ID-000457d8--en) help.

1. If the stocked material usage for work you completed is associated with an agreement, use the Agreement and Agreement Rates fields to enter agreement information. For information about each field, see the F1 help.Note: If the work order scope is associated with an agreement, the agreement fields will default the agreement information and be disabled.

1. In the Post Month field, enter the posting month or accept the default. The system uses this as the batch month when creating and posting the material use batch.

1. If a reference number applies to this line, use the  Reference No field to enter the reference number.  This field may default a reference number from existing work completed entries. For more information, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045836--en) help.

1. In the Serviceable Item field, enter the serviceable item to which this work completed line applies or press F4 for a list of valid serviceable items for the service site. Leave blank if the work completed line does not apply to a serviceable item.

1. In the Technician field, enter the technician that performed the work associated with this work completed line.

1. In the SM Cost Type field, enter the SM cost type (with a Material cost type category) that applies to this work completed line. Leave blank if an SM cost type is not applicable for this line. The SM Cost Type, along with the Material Tax Override and Tax Option Override options selected on the work order scope are used to determine taxability and tax defaults. For more information about these fields, see the F1 Help.

1. In the IN Co and IN Location fields, enter the IN company and inventory location from which the material was pulled.

1. In the Material field, enter the material used to complete the work order scope or press F4 to select from a list of valid materials for the specified location.

1. For Job work orders only, use the JC Cost Type field to enter the JC cost type for the work completed line or accept the default cost type. Press F4 for a list of valid JC cost types.For information about the defaulting for this field, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045858--en) help.

1. Enter or adjust the cost values (Cost UM, Cost Qty, Cost UC, and Cost Subtotal) for the material as needed. For information about the default behavior for these fields, see the F1 Help.

1. If applicable, enter or adjust the cost tax values (Cost Tax Type, Cost Tax Code, Cost Tax Basis, Cost Tax Amt). For information about these fields and their default behavior, see the F1 Help.

1. Enter or adjust the billable values (Bill Qty, Bill Rate, Bill ECM, Bill Subtotal) as applicable.For Job work orders, you can only adjust the bill values if the Costing Method for the work order is Markup. If the Costing Method is Actual Cost, all bill fields are disabled. For information about the bill fields and their default behavior, see the F1 help.

1. For Customer work orders only:

1. If applicable, enter or adjust the bill tax values (Bill Tax Type, Bill Tax Code, Bill Tax Basis, Bill Tax Amt). For more information about these fields and their default behavior, see the F1 Help.

1. If you are not charging the customer for the specified material, select the No Charge checkbox.

1. Save the record.

Related information

- [Enter Work Completed Inventory for Non-Stocked Materials on a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-non-stocked-materials-on-a-work-order)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
