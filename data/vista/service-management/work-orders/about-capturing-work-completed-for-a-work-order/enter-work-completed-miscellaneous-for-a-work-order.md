---
title: "Enter Work Completed Miscellaneous for a Work Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-miscellaneous-for-a-work-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-miscellaneous-for-a-work-order"
---

# Enter Work Completed Miscellaneous for a Work Order

Enter work completed miscellaneous lines to capture miscellaneous expenses for job and customer work orders (including those auto-generated from a customer agreement).
You can use the Work Completed tab in SM Work Orders or the SM Work Completed Misc form to enter work completed lines for miscellaneous expenses, such as trip charges, fuel surcharges, and so forth.The instructions below describe entry of work completed miscellaneous lines using the Work Completed grid in SM Work Orders.

1. Open the SM Work Orders form (Service Management > Programs > SM Work Orders).

1. In the Work Order field, enter the work order to which you are adding a work completed entry.

1. Select the Work Completed tab.

1. From the Line Type drop-down, select 3 - Misc.

1. In the Scope Seq field, enter the work order scope or press F4 to select from a list of valid scopes for the work order.

1. In the Date field, enter the date the work was completed or accept the current date default.

1. For Customer work orders only:

1. If the work complete line is not billable, select the the Non-Billable checkbox. For information about the defaulting and enabling/disabling behavior for this checkbox, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form/field-definitions-sm-work-completed-misc-form#ID-000457d8--en) help.

1. If the miscellaneous expense for work you completed is associated with an agreement, use the Agreement and Agreement Rates fields to enter agreement information. For information about each field, see the F1 help.Note: If the work order scope is associated with an agreement, the agreement fields will default the agreement information and be disabled.

1. In the Post Month field, enter the posting month or accept the default. This will become the batch month when costs are updated to GL.

1. If applicable, use the  Reference No field to enter the reference number for this work completed line.  This field may default a reference number from existing work completed entries. For more information, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045836--en) help.

1. In the Serviceable Item field, enter the serviceable item to which this work completed line applies or press F4 to select from a list of valid serviceable items for the service site.Leave blank if the work completed line does not apply to a serviceable item.

1. If applicable, use the Technician field to enter the technician that performed the work associated with this work completed line.

1. In the Standard Item field, enter the standard item for the work completed line or press F4 to select from a list of valid standard items.Leave this field blank if this line does not apply to a standard item.Note: The standard item is used to derive the Cost Rate and Billable Rate for the line. If you leave this field blank, you will need to enter the Cost Rate and Billable Rate manually.

1. The Description field defaults a value from the standard item entered in the Item field; you may override the default if applicable. If you did not enter an item in the Item field, enter a description of the miscellaneous charge.

1. In the SM Cost Type field, enter the SM cost type that applies to this work completed line. You may enter any cost type, regardless of the cost type category.  The SM Cost Type, along with the Material Tax Override (material-related cost types only) and Tax Option Override options selected for the specified work order scope are used to determine taxability and tax defaults. For more information, see the F1 Help.

1. For Job work orders only, use the JC Cost Type field to enter the JC cost type for this miscellaneous line or accept the default cost type. Press F4 for a list of valid JC cost types. For information about the defaulting for this field, see the F1 help for [JC Cost Type.](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045858--en)

1. In the Cost Qty and Cost UC fields, enter the quantity and unit cost for this work completed line.

1. The Cost Subtotal field automatically defaults a calculation of Cost Qty x Cost UC. Accept the default or enter the cost subtotal.Note: If you override the Cost Subtotal value, the system recalculates the Cost UC.

1. If applicable, enter the cost tax values (Cost Tax Type, Cost Tax Code, and Cost Tax Basis). For more information about the cost tax fields, see the F1 Help.Note: Cost Tax Type 3-VAT is not allowed for miscellaneous lines entered in SM; it is only allowed for miscellaneous lines generated from an AP invoice line.

1. Enter or adjust the billable values (Bill Qty, Bill Rate or Bill Subtotal) as applicable.For Job work orders, you can only adjust the bill values if the Costing Method for the work order is Markup. If the Costing Method is Actual Cost, all bill fields are disabled. For information about the bill fields and their default behavior, see the F1 help.

1. For Customer work orders only:

1. If applicable, enter or adjust the bill tax values (Bill Tax Type, Bill Tax Code, Bill Tax Basis, Bill Tax Amt). For more information about these fields and their default behavior, see the F1 Help.

1. If you will not be charging the customer or the work associated with this work complete line, select the No Charge checkbox.

For more information about the billable tax fields, see the F1 help.

1. Save the record.

Related information

- [SM Work Completed Misc Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Completed Equipment Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices)
