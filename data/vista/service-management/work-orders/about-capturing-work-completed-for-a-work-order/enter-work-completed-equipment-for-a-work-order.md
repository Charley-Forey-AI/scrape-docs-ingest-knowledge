---
title: "Enter Work Completed Equipment for a Work Order | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-equipment-for-a-work-order"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-equipment-for-a-work-order"
---

# Enter Work Completed Equipment for a Work Order

Enter work completed equipment lines to capture equipment expenses for job and customer work orders (including those auto-generated from a customer agreement).
You can use the Work Completed tab in SM Work Orders or the SM Work Completed Equipment form (accessed via the toolbar in SM Work Orders by selecting Work Completed > Equipment) to enter work completed lines.You can also capture equipment usage when entering service timecards in PR Timecard Entry if you selected both the Enter Equipment Usage With Time Cards checkbox in PR Company Parameters and the Post Equipment Usage option in PR Timecard Entry (Options menu). Equipment usage entered with a timecard will generate an equipment work completed line for the work order. However, work completed equipment lines entered in SM will not update labor entries in Payroll.
Note: If you enter work completed for a job work order and the job is hard or soft-closed, you can only save the record if you allow posting to closed jobs (that is, you selected the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs checkboxes in JC Company Parameters).

The instructions below describe entry of work completed equipment lines using the Work Completed grid in SM Work Orders.

1. Open the SM Work Orders form Service Management > Programs > SM Work Orders.

1. In the Work Order field, enter the work order to which you are adding a work completed entry.

1. Select the Work Completed tab.

1. From the Line Type drop-down, select 1 - Equip.

1. Tab through the Line # and Status fields. The system automatically defaults values in these fields.

1. In the Scope Seq field, enter the work order scope (sequence) associated with this equipment line or press F4 to select from a list of valid work order scopes.Note: If you enter a scope that is closed, a message displays indicating the scope is closed and you will be unable to save the line. You must either reopen the scope or enter a different (open) scope.

1. In the Date field, enter the date the work was completed or accept the current date default.

1. For Customer work orders only:

1. If the work complete line is not billable, select the the Non-Billable checkbox. For information about the defaulting and enabling/disabling behavior for this checkbox, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form/field-definitions-sm-work-completed-misc-form#ID-000457d8--en) help.

1. If the equipment usage for work you completed is associated with an agreement, use the Agreement and Agreement Rates fields to enter agreement information. For information about each field, see the F1 help.Note: If the work order scope is associated with an agreement, the agreement fields automatically default the agreement information and are disabled.

1. In the Post Month field, enter the posting month for this work completed line or accept the default. This becomes the batch month when creating and posting the equipment usage batch for this work completed equipment line.

1. If applicable, use the Reference No field to enter the reference number associated with this work completed equipment line.Note: This field defaults a reference number from existing work completed entries where the work order scope and date match (if a reference number was assigned). You can override the default if desired.

1. In the Serviceable Item field, enter the serviceable item to which this work completed line applies or press F4 to select from a list of valid serviceable items for the service site.Leave blank if the work completed line does not apply to a serviceable item.

1. In the Technician field, enter the technician that performed the work associated with this work completed equipment line.

1. In the SM Cost Type field, enter the SM cost type that applies to this work completed line. Must be a cost type with a cost type category of E-Equipment.The SM Cost Type, along with the Tax Option Override option selected for the specified work order scope are used to determine taxability and tax defaults. For more information, see the F1 Help.

1. In the EM Co field, enter the EM company for the equipment used to complete the work associated with this line or accept the default (from SM Company Parameters).

1. In the Equipment field, enter the equipment used to perform the work. Equipment must be flagged as Active or Down in EM Equipment.

1. For Job work orders only, use the JC Cost Type field to enter the JC cost type for this equipment line or accept the default cost type (see [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045858--en) help for information about how this field defaults the JC cost type).Note: If you are capturing work completed for a locked job (i.e., the Phases on this job are locked box is checked in JC Jobs), the cost type entered here must be valid for the job/phase. If job is not locked, the cost type must be valid for the phase. For more information, see the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045858--en) help.

1. In the Rev Code field, enter the revenue code that applies to this line or accept the default (the revenue code assigned to the equipment in EM Equipment).Note: The system derives the Cost Rate for the line based on this revenue code and rate defined for the equipment (in EM Revenue Rates by Equipment) or equipment category (in EM Revenue Rates by Category). For more information about equipment usage rates, see [About the EM Revenue Rates by Equipment Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form) and [About the EM Revenue Rates by Category Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form).

1. In the Time Units field, enter the number of time units (based on the Time UM) for this work completed equipment line. For hour-based revenue codes and unit-based revenue codes that are flagged to update hour meter, use the Time Units field to enter the number of time units (based on the Time UM) for this work completed equipment line. Note: Entry in this field applies only to hour-based revenue codes and to unit-based revenue codes with the Update Hour Meter checkbox selected in EM Revenue Rates by Category or EM Revenue Rates by Equipment.

1. For unit-based revenue codes only, use the Work Units field to enter the number of work units (based on the Work UM) for this work completed equipment entry.

1. Tab through the Cost Rate and Total Actual Cost fields. These values default automatically and cannot be changed.Note: The Cost Rate defaults the override rate defined for the equipment in EM Revenue Rates by Equipment (if one is defined) or the rate defined for the equipment's category (in EM Revenue Rates by Category).

1. Enter or adjust the billable values (Bill Rate or Bill Subtotal) as applicable.For Job work orders, you can only adjust the bill values if the Costing Method for the work order is Markup. If the Costing Method is Actual Cost, all bill fields are disabled. For information about the bill fields and their default behavior, see the F1 help.

1. For Customer work orders only:

1. If applicable, enter or adjust the billable tax values (Bill Tax Type, Bill Tax Code, or Bill Tax Basis). For more information about the tax fields, see the F1 help.

1. If you will not be charging the customer or the work associated with this work complete line, select the No Charge checkbox.

1. Save the record.

Related information

- [SM Work Completed Equipment Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)

- [SM Work Completed Misc Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices)
