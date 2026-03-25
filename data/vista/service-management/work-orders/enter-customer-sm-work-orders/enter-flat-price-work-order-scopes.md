---
title: "Enter Flat Price Work Order Scopes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-flat-price-work-order-scopes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-flat-price-work-order-scopes"
---

# Enter Flat Price Work Order Scopes

If you do not bill work orders based on time and materials, you can set up flat price work order scopes that allow you to specify a set price.
The system automatically adds a single work order sequence (scope) for you once you save the header, and defaults values where applicable. You can either fill out the remainder of the information at the time the scope is added or at a later time.

1.  In the Seq field:

- If you are entering information for an auto-added work order scope, skip to the next step

- If manually adding a work order scope, enter N or +.

1. (Optional) If you have set up work scopes (in SM Work Scopes), use the Scope field to enter the work scope that represents the work requested by the service call. Press F4 to select from a list of valid work scopes.

1. In the Priority field, enter Low , Med , or High to indicate the priority of the work order or press F4 to select the priority.Note: If you entered a scope in the previous field, this field defaults the priority assigned to the scope in SM Work Scopes. You may override as necessary.

1.  In the Scope Detail text box, enter a description of the service request / problem.

1. Specify the due date for this work order scope as follows:

1. If due by a specific date, select 0-By from the Due drop-down. Then use the second date box (to the right) to enter the 'due by date'.

1. If due within a specific date range, select 1-Within from the Due drop-down. Then use both the date boxes (to the right) to enter the beginning and ending dates (respectively) in the desired 'within' date range.

1. In the Division field, enter the division of the service center that is responsible for completing the work to be done.

1. In the Call Type field, enter the call type.

1. If the service associated with this scope is for a specific serviceable item, use the Serviceable Item field to enter the item or press F4 to select from a list valid serviceable items for the service site.

1. From the Material Tax Override drop-down, select the tax override option for material-related work completed lines or accept the defaulted value. Options are:

- Blank

- N-No Tax

- S-Sales Tax

- U-Use Tax

 Entry here determines the Cost Tax Type default for material-related work completed lines. For information about each of these options, see the F1 help for [Material Tax Override](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000455bc--en).

1. From the Tax Option Override drop-down, select how to apply taxes for work completed lines referencing this work order scope or accept the defaulted value.

- N - Not Taxable

- P - Taxable at Purchase Order Only (applies to sales and use tax)

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax

 If you leave this field blank, the system uses the Tax Option specified for the scope's Call Type to determine taxability.
Note: This option applies to cost taxes only, since work completed lines are non-billable and default all billing fields as blank and disabled. For information about each of these options and defaulting, see the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-nef25hfx--en).

1. In the Assignment field, enter an assignment number, or press F4 to select from a list of valid assignment numbers.

1. If this work order scope is related to an agreement, enter the agreement number in the Agreement field or press F4 to select from a list of valid agreements for the customer/service site. May be left blank.Note: This field may or may not default an agreement number depending on how you set the Default Agreement number on Work Order Scopes checkbox in SM Company Parameters. For information about the default behavior, see the [Agreement](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000455f3--en) F1 help.

1. From the Price Method drop-down, select F - Flat Price.

1. In the Price field, enter the total amount to charge for all work covered by this work order scope.

1. In the Margin field, enter the expected margin percentage to apply when recognizing revenue for this flat price scope.  If you created this work order from a work order quote (via SM Work Order Quotes), this field defaults the margin specified for the quote scope, but may be overridden.
Note: Entry in this field is required, so if no margin applies, enter 0.00.

1. Select Split button to [enter flat price revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue) entries.Note: This step is required; however, only a minimum of one entry is needed.

1. If the scope is ready to bill:

1. Select the Ready To Bill checkbox.

1. If billing only a portion of the flat price amount, select the Partial Bill checkbox. Then use the Amount text boxes to enter either the amount or percentage to bill.

Note: If you select Partial Bill and enter an amount or percentage, the system automatically sets the Ready To Bill checkbox to an "indeterminate" state (meaning that it is neither selected nor unselected), indicating the full amount is not billable.

1. If applicable, enter the customer's PO number In the Customer PO field.If you leave this field blank and the service site or customer requires a customer PO, the system displays a warning, but allows you to save the record.

1. In the Insurance Code field, enter the insurance code.  If you selected the Insurance Based on Phase or SM Work Order Scope checkbox (in PR Company Parameters), timecards posted to this work order scope will default the insurance code specified here.

1. In the Bill To field, enter the AR customer to bill for the work completed on this order or accept the default (alternate bill to customer or service site customer). See the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000456f5--en) help for more information.

1. Use the tax fields (Tax Type, Tax Code, and Tax Source) to enter tax information for this work order scope. For more information about each field, see the F1 help.

1. If applicable, [enter summarized cost estimates](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/enter-summarized-cost-estimates-for-customer-work-order-scopes) for the scope.

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
