---
title: "Enter Work Completed Labor for a Work Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-labor-for-a-work-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-labor-for-a-work-order"
---

# Enter Work Completed Labor for a Work Order

Enter work completed labor lines to capture labor expenses for job and customer work orders (including those auto-generated from a customer agreement).

You must be set up in VA User Profile with a PR Co and Employee designation, as well as the appropriate My Timesheet Permissions setting. If this is not done, you will be unable to enter labor lines, regardless of whether you are entering them for work you completed. For more information, see [Setting Timesheet Permissions for Users](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions) in the online help
You can use the Work Completed tab in SM Work Orders or the SM Work Completed Labor form to enter work completed labor lines. You can also capture labor hours for a work order in PR My Timesheet or PR Timecard Entry. Labor hours entered with a timesheet or timecard will generate a labor work completed line for the work order.Note: If you enter work completed for a job that is hard or soft-closed, you can only save the record if you allow posting to closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs checkboxes are selected in JC Company Parameters).

The instructions below describe entry of work completed labor lines using the Work Completed grid in SM Work Orders.

1. Open the SM Work Orders form (Service Management > Programs > SM Work Orders).

1. In the Work Order field, enter the work order to which you are adding a work completed entry.

1. Select the Work Completed tab to access the Work Completed grid.

1. From the Line Type drop-down, select 2 - Labor.

1. Tab through the Line # and Status fields. The system automatically defaults values in these fields.

1. In the Scope field, enter the work order sequence associated with this work completed labor line or press F4 for a list of valid scopes (sequences) for the work order.

1. In the Date field, enter the date the work was completed or accept the current date default.

1. For Customer work orders only:

1. If the work complete line is not billable, select the the Non-Billable checkbox. For information about the defaulting and enabling/disabling behavior for this checkbox, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form/field-definitions-sm-work-completed-misc-form#ID-000457d8--en) help.

1. If the labor for work you completed is associated with an agreement, use the Agreement and Agreement Rates fields to enter agreement information. For information about each field, see the F1 help.Note: If the work order scope is associated with an agreement, the agreement fields automatically default the agreement information and are disabled.

1. In the  Reference No field, enter the reference number associated with this work completed labor line, if applicable.

1. In the Serviceable Item field, enter the serviceable item to which this work completed line applies or press F4 to select from a list of valid serviceable items for the service site.Leave blank if the work completed line does not apply to a serviceable item.

1. In the Technician field, enter the technician that performed the work associated with this work completed line or press F4 to select from a list of valid technicians.

1. In the Labor Code field, enter the labor code that identifies the repair or resolution associated with the work completed line.

1. In the Description field, enter a description of the labor performed for the work order sequence.

1. In the SM Cost Type field, enter the SM cost type that applies to this work completed line. Must be a cost type with a Cost Type Category of L-Labor.The SM Cost Type, along with the Tax Option Override option selected for the specified work order scope are used to determine taxability and tax defaults. For more information, see the F1 Help.

1. For Job work orders only, use the JC Cost Type field to enter the JC cost type for this labor line or accept the default cost type (see [F1 Help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045858--en) for information about how this field defaults the JC cost type).

1. In the Pay Type field, enter the pay type or press F4 for a list of valid pay types.The system uses the pay rate to determine the cost rate for the labor line. See the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form/field-definitions-sm-work-completed-labor-form#ID-00045901--en) for more information about how the pay type determines the pay rate.

1. The Craft and Class fields automatically default the employee's assigned craft/class (from PR Employees), if applicable. Accept the defaults or enter the craft and class under which the technician performed the service work.

1. The Shift field automatically defaults the employee's assigned shift (from PR Employees), if applicable. Accept the default or enter the shift worked by the technician.

1. In the Hrs Worked field, enter the number of hours worked by the technician to complete the work order sequence. This will be the number of hours for which the technician will be paid.

1. Tab through the Cost Rate, Proj Cost, and Actual Cost fields; these values default automatically and cannot be changed. For information about how the system defaults the Cost Rate, see the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045a01--en) for this field.

1. Enter or adjust the billable values (Bill Hrs, Bill Rate or Bill Subtotal) as applicable.For Job work orders, you can only adjust the bill values if the Costing Method for the work order is Markup. If the Costing Method is Actual Cost, all bill fields are disabled. For information about the bill fields and their default behavior, see the F1 help.

1. For Customer work orders only:

1. If applicable, use the Tax fields to enter or adjust tax values. For more information about the tax fields, see the F1 help.

1. If you will not be charging the customer or the work associated with this work complete line, select the No Charge checkbox.

1. Save the record.

Related information

- [Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices)

- [Enter Work Completed Equipment for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-equipment-for-a-work-order)

- [Enter Work Completed Inventory for Stocked Materials on a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-inventory-for-stocked-materials-on-a-work-order)

- [Enter Work Completed Miscellaneous for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-miscellaneous-for-a-work-order)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
