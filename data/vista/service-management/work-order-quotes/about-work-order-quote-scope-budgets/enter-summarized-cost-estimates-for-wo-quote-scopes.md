---
title: "Enter Summarized Cost Estimates for WO Quote Scopes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/enter-summarized-cost-estimates-for-wo-quote-scopes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/enter-summarized-cost-estimates-for-wo-quote-scopes"
---

# Enter Summarized Cost Estimates for WO Quote Scopes

You can enter summarized cost estimates for labor, material, equipment, subcontract, and other costs associated with a work order quote scope.
Before setting up cost estimates, you must have already set up your work order quote and added at least one quote sequence. For more information, see [Enter an SM Work Order Quote](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote).
The system uses the cost estimates to determine the total estimated cost for the quote scope. For quote scopes using the Time and Materials price method, you can also enter markup rates for cost estimates to derive pricing estimates. The system will use the cost estimates and pricing estimates to determine the estimated profit for the quote scope.

1. Open the SM Work Order Quotes form.

1. In the Quote ID field, enter the work order quote or press F4 to select from a list of work order quotes. Quote must have a Status of New.

1. In the scope Seq field, enter the quote sequence for which to set up cost estimates or use the /  buttons in the toolbar to select the desired quote sequence.

1. In the Budget section, make sure the Derived checkbox is unselected.

1. Click Details.  The SM WO Quote Cost Detail form displays.

1. In the Labor Hours field, enter the estimated labor hours.

1. In the Craft and Class fields, enter the craft and class to which the budget hours for this quote scope apply.

1. In the Cost Estimates fields, enter the estimated cost amounts for labor, materials, equipment, subcontracts, and other expenses.

1. For Time and Material quote scopes only, enter the markup rates / price estimates using one of the following methods:

- To use a common markup rate, select the Common Markup Rate checkbox and then enter a markup rate in the Markup field of any cost estimate. The system will set the markup rate for the remaining cost estimates equal to the value you entered and calculate the price estimate for each cost estimate accordingly.

- To set individual markup rates, leave the Common Markup Rate checkbox unselected and then enter a markup rate in the Markup field for each cost estimate. The system will automatically calculate the price estimates accordingly.

- If you do not know the markup rates, you can enter pricing estimates and have the system calculate the markup rates for you. To do this, leave the Common Markup Rate checkbox unselected and then enter the appropriate value in the Pricing Estimates field for each cost estimate.

1. For Time and Material quote scopes only, enter sales tax amounts using one of the following methods:

- To automatically default sales tax for all cost estimates, select the Default All checkbox. The system auto-selects the Default Tax Amount? checkbox (unlabeled) for each of the cost estimates and defaults the appropriate tax amount in the Sales Tax Amount field.

- To automatically default the sales tax for individual cost estimates, leave the Default All checkbox unselected and manually select the Default Tax Amount? checkbox for each applicable cost estimate. The system will default the appropriate tax amount in the Sales Tax Amount field for the selected cost estimates.

- To manually enter sales tax amounts, leave the Default All and individual Default Tax Amount? checkboxes unselected. Then, use the Sales Tax Amount fields to enter the sales tax amount for each applicable cost estimate.

1. Save the record.

Related information

- [SM WO Quote Cost Detail Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-wo-quote-cost-detail-form)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)
