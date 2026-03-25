---
title: "Enter Scopes for a Work Order Quote | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote/enter-scopes-for-a-work-order-quote"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote/enter-scopes-for-a-work-order-quote"
---

# Enter Scopes for a Work Order Quote

Once you save the header of a work order quote (in SM Work Order Quotes), you can add scopes to capture the work being done, as well as cost estimates and required tasks, materials, equipment, labor, and miscellaneous expenses.

1. In the scope Seq field, enter N or +. The system automatically assigns the next sequential number.

1. In the Scope field, enter the work scope for this quote sequence or press F4 to select from a list of valid work scopes.Leave this field blank if this quote scope is not associated with a work scope.

1. If there is a due date associated with this quote scope, use the Due drop-down to select the due date:

- 0-By - Select this option if the work associated with this quote sequence is due by a specific date. Then use the second date field to enter the 'due by' date.

- 1-Within - Select this option if the due date is within a specific date range. Then use both of the date fields to enter the 'due within' date range.

1. In the Call Type field, enter the call type for the quote sequence.

1.  In the Detail text box, enter a description of the service request/problem.

1. In the Division field, enter the division for the quote sequence or press F4 to select from a list of valid divisions for the service center specified above. Leave blank if not applicable.

1. In the Cust PO field, enter the customer's purchase order number. Leave blank if you do not know or do not require the customer PO number.

1. If the quote is associated with an agreement (existing customers only), use the Agreement field to enter the agreement or press F4 to select from a list of agreements for the customer. Otherwise, leave blank.

1. If this quote sequence is already approved, select the Approve Seq. checkbox. This allows you to select individual work order quote scopes to approve before approving a quote.

1. From the Price Method drop-down, select the pricing method for this quote scope:

- F-Flat Price

- 'T-Time and Material

- D-Derived Flat Price

 For information about each of these options, see the [Price Method](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form#ID-00044e34--en) F1 help.

1. If you selected the F-Flat Price price method:

1. In the Price field, enter the total price for the quote sequence.

1. Select the Split button to [enter split revenue entries](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue) (required).

1. In the Margin field, enter the expected margin percentage to apply when recognizing revenue for the work order scope generated from this quote scope. This step is required if using the 'As Costs Incurred' revenue recognition method (checkbox in SM Company Parameters).

1. If you selected the T-Time and Material or Derived Flat Price price method, use the Rate Template field to enter the rate template to use or accept the defaulted template.Note: If using the Derived Flat Price method, the Price field is disabled. The system populates this field once you [add detailed cost estimates](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/about-setting-up-required-resources-for-a-work-order-quote) to the Material, Equipment, Labor, and Misc tabs. In addition, the system automatically generates split revenue entries based on the material, equipment, labor, and miscellaneous lines.

1. For Flat Price or Time and Material price methods only, if you want budget values calculated based on the detailed cost estimates (Material, Equipment, Labor, and Misc tabs), select the the Derived checkbox.To calculate budget values using the summarized cost estimates entered in SM WO Quote Cost Detail (accessed by selecting the Detail button on the quote scope), leave the Derived checkbox unselected.Note: If you have already entered summarized cost estimates in SM WO Quote Cost Detail (accessed via the Detail button), selecting this checkbox does not affect those entries.

1. From the Tax Source drop-down, select whether to default the tax code for work completed equipment, labor, miscellaneous, or materials lines from the service center or service site.

1. From the Matl Tax Override drop-down, select the tax override option for materials. Options are:

- Blank

- N-No Tax

- S-Sales

- U-Use Tax

 For more information about these each of these options, see the F1 help for [Matl Tax Override](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form#ID-00044e84--en).

1. From the Tax Option
 Override drop-down, select select how to apply taxes for work
 order scopes generated from this quote scope.

- N - Not Taxable

- P - Taxable at Purchase Order Only

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax

 For information about each of these options and defaulting, see the [F1 help](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-sm-work-order-quotes-form#concept-vv9fxhj6--en).

1. For Flat Price or Derived Flat Price quote sequences only, enter tax information.

1. From the Tax Type drop-down, select 1-Sales or 3-VAT to identify the type of tax for this line, or accept the default (if applicable).

1. Enter the tax code in the Tax Code field.

1. For Time and Material quote sequences only, use the Not to Exceed field to enter the billable limit for this quote sequence. Leave blank if there is no billable limit for the customer/service site.

1. Save the record.

1. If applicable, [enter rate overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-rate-overrides-by-customer-service-site-or-quote) (T&M and Derived Flat Price scopes only).

1. If applicable, [enter summarized cost estimates](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/enter-summarized-cost-estimates-for-wo-quote-scopes).

1. If applicable, [set up required resources](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/about-setting-up-required-resources-for-a-work-order-quote).
