---
title: "Enter Time and Material Work Order Scopes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-time-and-material-work-order-scopes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-time-and-material-work-order-scopes"
---

# Enter Time and Material Work Order Scopes

If you are billing for work on a T&M basis, you can enter Time and Material work order scopes using the SM Work Orders form.
The system automatically adds a single work order sequence (scope) for you once you save the header, and defaults values where applicable. You can either fill out the remainder of the information at the time the scope is added or at a later time.

1.  In the Seq field:

- If you are entering information for an auto-added work order scope, skip to the next step.

- If you are adding the work order scope manually, enter N or +. The system assigns the next sequential number.

1. In the Scope field, enter the work scope that represents the work requested by the service call or press F4 to select from a list of valid work scopes.

1. In the Priority field, enter Low , Med , or High to indicate the priority of the work order or press F4 to select the priority.If you entered a scope in the previous field, this field defaults the priority assigned to the scope in SM Work Scopes. You may override as necessary.

1.  In the Scope Detail text box, enter a description of the service request / problem.

1. From the Due drop-down, select 0-By if this work order sequence is due by a specify date or 1-Within if due within a given date range. Leave blank if not specifying a due date.

1. If you selected 0-By from the Due drop-down, enter the 'due by' date in the second date box. If you selected 1-Within from the Due drop-down, enter the beginning date in the first date box and the ending date in the second date box.

1. In the Division field, enter the division of the service center that is responsible for completing the work to be done.

1. In the Call Type field, enter the call type.

1. In the Serviceable Item field, enter the item being serviced or press F4 to select from a list valid serviceable items for the service site.

1. From the Material Tax Override drop-down, select the tax override option for material-related work completed lines or accept the defaulted value. Options are:

- Blank

- N-No Tax

- S-Sales Tax

- U-Use Tax

 Entry here determines the Cost Tax type default for material-related work completed lines. For more information about these options, see the F1 help for [Material Tax Override](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000455bc--en).

1. From the Tax Option
 Override drop-down, select how to apply taxes for
 applicable work completed lines referencing this work order scope or accept the defaulted value.


- N - Not Taxable

- P - Taxable at Purchase Order Only (applies to sales and use tax)

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax

 If you leave this field blank, the system uses the Tax Option specified for the scope's Call Type to determine taxability. For information about each of these options and defaulting, see the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-nef25hfx--en).

1. In the Assignment field, enter an assignment number, or press F4 to select from a list of valid assignments.

1. From the Revenue Recognition drop-down, select how to recognize revenue for this work order:

- A-As Billed

- C-As Cost Incurred

For information about each of these options, see the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-125--en).

1. If this work order scope is related to an agreement, enter the agreement number in the Agreement field or press F4 to select from a list of valid agreements for the customer/service site.Note: For information about the defaulting behavior for this field, see the [Agreement](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000455f3--en) F1 help.

1. From the Price Method drop-down, select T - Time and Material.

1. If the scope is ready to bill, select Ready To Bill. Note: If the Ready To Bill checkbox is in an "indeterminate" state for Time and Material (meaning that it is neither selected nor unselected), this means at least one work item line (but fewer than all) is marked as Ready to Bill.

1. If applicable, enter the customer's PO number In the Customer PO field.If you leave this field blank and the service site or customer requires a customer PO, the system displays a warning, but allows you to save the record.

1. In the Insurance Code field, enter the insurance code.  If you selected the Insurance Based on Phase or SM Work Order Scope checkbox (in PR Company Parameters), timecards posted to this work order scope will default the insurance code specified here.

1. In the Bill To field, enter the AR customer to bill for the work completed on this order or accept the default (alternate bill to customer or service site customer). See [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000456f5--en) help for more information.

1. In the Rate Template field, enter the rate template to use for determining billable rates for work completed lines. Press  F4 to select from a list of valid rate templates.

1. In the Tax Source field select tax source for defaulting tax codes on work completed. Options are:

- 0-Service Center

- 1-Service Site

 For more information about this field, see the [Tax Source](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-00045746--en) F1 help.

1. In the Not to Exceed field, enter the billable limit for this work order scope.

1. If applicable, [enter summarized cost estimates](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/enter-summarized-cost-estimates-for-customer-work-order-scopes) for the scope.

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
