---
title: "Enter Non-Billable Work Order Scopes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-non-billable-work-order-scopes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-non-billable-work-order-scopes"
---

# Enter Non-Billable Work Order Scopes

You can enter non-billable work order scopes for work that you need to track, but for which you will not bill the customer.
The system automatically adds a single work order sequence (scope) for you once you save the header, and defaults values where applicable. You can either fill out the remainder of the information at the time the scope is added or at a later time.

1.  In the Seq field:

-  If you are entering information for an auto-added work order scope, skip to the next step.

-  If manually adding a work order scope, enter N or +.

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

 Entry here determines the Cost Tax Type default for material-related work completed lines. For information about each of these options, see the F1 help for [Material Tax Override](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000455bc--en).

1. From the Tax Option Override drop-down, select how to apply taxes for applicable work completed lines referencing this work order scope or accept the defaulted value.

- N - Not Taxable

- P - Taxable at Purchase Order Only (applies to sales and use tax)

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax

If you leave this field blank, the system uses the Tax Option specified for the scope's Call Type to determine taxability.
Note: This option applies to cost taxes only, since work completed lines are non-billable and default all billing fields as blank and disabled. For information about each of these options and defaulting, see the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-nef25hfx--en).

1. In the Assignment field, enter an assignment number, or press F4 to select from a list of valid assignment numbers.

1. If this work order scope is related to an agreement, enter the agreement number in the Agreement field or press F4 to select from a list of valid agreements for the customer/service site.If this work order scope is not related to an agreement, leave the agreement field blank.
Note: This field may or may not default an agreement number depending on how you set the Default Agreement number on Work Order Scopes checkbox in SM Company Parameters. For information about the default behavior, see the [Agreement](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000455f3--en) F1 help.

1. From the Price Method drop-down, select N - Non-Billable.

1. If applicable, enter the customer's PO number In the Customer PO field. If you leave this field blank and the service site or customer requires a customer PO, the system displays a warning, but allows you to save the record.

1. In the Insurance Code field, enter the insurance code.  If you selected the Insurance Based on Phase or SM Work Order Scope (in PR Company Parameters), timecards posted to this work order scope will default the insurance code specified here.

1. In the Bill To field, enter the AR customer to bill for the work completed on this order or accept the default (alternate bill to customer or service site customer). See the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000456f5--en) help for more information.

1. In the Tax Source field select whether to default the tax code for work completed lines from the 0 - Service Center or 1 - Service Site.  For more information about this field, see the [Tax Source](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-00045746--en) F1 help.

1. If applicable, [enter summarized cost estimates](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/enter-summarized-cost-estimates-for-customer-work-order-scopes) for the scope.

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
