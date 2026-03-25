---
title: "Enter Job Work Order Scopes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-job-sm-work-orders/enter-job-work-order-scopes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-job-sm-work-orders/enter-job-work-order-scopes"
---

# Enter Job Work Order Scopes

Once you have entered the work order header information (in SM Work Orders), you can then enter work order scopes.
The system automatically adds a single work order
 sequence (scope) for you once you save the header. You can either fill out the remainder
 of the information at the time the scope is added or at a later time.

1.  In the Scope section of the form, use the Seq field to do one of the following:

- If you are entering information for an auto-added work order scope, skip to the next step.

- If manually adding a work order scope, enter N or +.

1. In the Scope field, enter the work scope that represents the work requested by the service call or press F4 to select from a list of valid work scopes.

1. In the Priority field, enter Low , Med , or High to indicate the priority of the work order or press F4 to select the priority.If you entered a scope in the previous field, this field defaults the priority assigned to the scope in SM Work Scopes. You may override as necessary.

1.  In the Scope Detail text box, enter a description of the service request / problem.

1. From the Due drop-down, do one of the following:

- Select 0-By if this work order sequence is due by a specify date.

- Select 1-Within - if this work order is due within a given date range.

- Leave blank if not specifying a due date.

1. If you selected 0-By in Step 5, use the second date box to enter the due date. If you selected 1-Within in Step 5, use the first and second date boxes to enter the due date range.

1. In the Division field, enter the division of the service center that is responsible for completing the work to be done.

1. In the Call Type field, enter the call type.

1. In the Serviceable Item field, enter the item being serviced or press F4 to select from a list valid serviceable items for the service site.

1. From the Matl Tax Override drop-down, select the tax override option for materials. For more information about each of these options, see the [F1 help](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form#ID-00044e84--en).

- Blank – Select this option to use the standard tax type defaulting behavior.

- N - No Tax – Select this option to default the tax type as "blank".

- S-Sales Tax Only – Select this option to default the tax type as Sales.

- U-Use Tax Only (US companies only) – Select to default the tax type as Use.

1. From the Tax Option
 Override drop-down, select how to apply taxes for
 material-related work completed referencing this work order scope or accept the
 defaulted option:

- N - Not Taxable

- P - Taxable at Purchase Order Only (applies to sales and use tax)

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax

 For information about each of these options and defaulting, see the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-nef25hfx--en).

1. In the Assignment field, enter an assignment number, or press F4 to select from a list of valid assignment numbers.

1. For job work orders with a Markup cost method, use the Revenue Recognition drop-down to select the revenue recognition method:

- B-As Billed - Select to have revenue recognized as it is billed.

- C-As Costs Incurred - Select to have revenue recognized as costs are incurred.

Note: The Revenue Recognition field is disabled for job work orders with a Cost Method of Actual Cost.

1. In the Phase field, enter the phase number or press F4 to select from a list of valid phases for the job.

1. In the Not to Exceed field, enter the billable limit for this work order scope.

1. If applicable, [enter summarized cost estimates](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/enter-summarized-cost-estimates-for-job-work-order-scopes) for the scope.

1. For job work orders with a In the Rate Template field, enter the rate template (from SM Rate Templates) for this work order scope.

1. For job work orders with a Markup cost method, use the Tax Source drop-down to select the tax code default source:

- 0-Service Center - Select to default the tax code for work completed lines referencing this scope from the work order's service center.

- 1-Service Site - Select to default the tax code for work completed lines referencing this scope from the work order's service site.

Note: The Tax Source field is disabled for job work orders with a Cost Method of Actual Cost.

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
