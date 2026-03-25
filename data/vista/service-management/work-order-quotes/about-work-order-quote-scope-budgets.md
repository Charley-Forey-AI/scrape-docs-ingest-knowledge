---
title: "About Work Order Quote Scope Budgets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets"
---

# About Work Order Quote Scope Budgets

You can set up budget information for a work
 order quote scope by entering cost estimates in the SM Work Order Quotes form.
There are two methods for setting up cost estimates for a work order quote scope:

- Summarized Cost Estimates - These are entered in SM
 WO Quote Cost Detail (accessed by clicking the Detail button in the Budget
 section of SM Work Order Quotes).

- Detailed Cost Estimates - These are entered in SM
 Work Order Quotes using the Material, Equipment, Labor, and Misc tabs.

The system determines which set of cost estimates to
 use when calculating the budget totals (estimated Labor Hours, Cost Total, Price Total,
 and Profit) based on how you set the Derived checkbox, as detailed below.

## Detailed Cost Estimates

If you prefer to use detailed cost
 estimates to derive the estimated budget totals, select the Derived
 checkbox for the selected quote scope. The system will sum the labor hours from all
 entries on the Labor tab to determine the estimated Labor Hours for the quote scope.
 It then uses the detailed cost estimates to determine the estimated budget totals.
 The Pricing method defined for the quote scope determines how the budget totals are
 calculated:

- Flat Price - For these scopes, the system sums the cost
 totals from all tabs to derive the budget Cost Total. It then uses the Price
 entered for the quote scope as the Price Total. The Est Profit is then
 calculated as the Price Total less the Cost Total.

- Time and Material - For these scopes, the systems sums the
 cost totals and billable totals from all tabs to derive the budget Cost Total
 and Price Total. The Est Profit is then calculated as the Price Total less the
 Cost Total.

## Summarized Cost Estimates

If you do not select the Derive
 checkbox, you can use the SM WO Quote Cost Detail form to enter estimated labor
 hours and summarized cost estimates for labor, materials, equipment, subcontracts,
 and miscellaneous expenses. The system uses the summarized cost estimates to
 determine the estimated budget totals. The Pricing method defined for the quote
 scope determines how the budget totals are calculated:

- Flat Price - For these scopes, the system uses the estimated
 labor hours and total cost estimates to derive the budget Labor Hours and Cost
 Total, respectively. It then uses the Price entered for the quote scope as the
 Price Total. The Profit is then calculated as the Price Total less the Cost
 Total.

- Time and Material - For these scopes, the SM WO Quote Cost
 Detail form provides additional fields for entering markup rates for cost
 estimates, which are then used to calculate pricing estimates. The system sums
 the cost estimates and pricing estimates to determine the estimated Cost Total
 and Price Total (respectively) for the quote scope. The Profit is then
 calculated as the Price Total less the Cost Total.

Note: When you create a work order from the quote,
 the system updates the budget totals for the work order from the quote scope. If you
 selected the Derived checkbox on the quote scope, but also entered summarized
 cost estimates, the system will populate the summarized cost estimates on the work
 order scope using the detailed cost estimates. The summarized cost estimates on the
 quote scope are left intact.
For information about entering detailed
 cost estimates (required resources) and summarized cost estimates, click on the
 links below.

- [About Setting up Required Resources for a Work Order Quote](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/about-setting-up-required-resources-for-a-work-order-quote)

- [Enter Summarized Cost Estimates for WO Quote Scopes](/en/vista/vista/service-management/work-order-quotes/about-work-order-quote-scope-budgets/enter-summarized-cost-estimates-for-wo-quote-scopes)
