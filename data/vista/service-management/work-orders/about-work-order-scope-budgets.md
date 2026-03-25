---
title: "About Work Order Scope Budgets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets"
---

# About Work Order Scope Budgets

You can set up budget information for a work
 order scope by entering cost estimates in the SM Work Orders form.
There are two methods for setting up cost estimates for a work order scope:

- Summarized Cost Estimates - These are entered in the SM Work Order Cost Detail form (accessed by clicking the
 Detail button in the Budget section of SM Work Orders).

- Detailed Cost Estimates - These are entered in the SM Work Orders form using the Material, Equipment, and Labor
 tabs.

The system determines which set of cost
 estimates to use when calculating the budget totals (estimated Labor Hours, Cost Total,
 Price Total, and Profit) depending on how you set the Derived checkbox for the work order
 scope.

## Detailed Cost Estimates

If you prefer to use detailed cost
 estimates to derive the estimated budget totals, select the Derived
 checkbox. The system sums the labor hours from all entries on the Labor tab to
 determine the estimated Labor Hours for the work order scope. It then uses the detailed
 cost estimates to determine the estimated budget totals. The Pricing method defined for
 the work order scope determines how the budget totals are calculated:

- Non-Billable - For these scopes, the
 system sums the cost totals from all tabs to derive the budget Cost Total.
 However, since these scopes are not billable, no Price Total or Profit will be
 calculated.

- Flat Price - For these scopes, the
 system sums the cost totals from all tabs to derive the budget Cost Total. It then
 uses the Price entered for the work order scope as the Price Total. The Profit is
 then calculated as the Price Total less the Cost Total.

- Time and Material - For these scopes,
 the systems sums the cost totals and billable totals from all tabs to derive the
 budget Cost Total and Price Total. The Profit is then calculated as the Price
 Total less the Cost Total.

- Job Work Order, Actual Cost - For
 scopes on these work orders, the system sums the cost totals from all tabs to
 derive the budget Cost Total. However, since no pricing is defined for these
 scopes, no Price Total or Profit will be calculated.

- Job Work Order, Markup - For scopes
 on these work orders, the systems sums the cost totals and billable totals from
 all tabs to derive the budget Cost Total and Price Total. The Profit is then
 calculated as the Price Total less the Cost Total.

## Summarized Cost Estimates

If you do not select the Derive check
 box, you can use the SM Work Order Cost Detail form to enter estimated labor hours, and
 summarized cost estimates for labor, materials, equipment, subcontracts, and
 miscellaneous expenses. The system will then use the summarized cost estimates to
 determine the estimated budget totals. The Pricing method defined for the work order
 scope determines how the budget totals are calculated:

- Non-Billable - For these scopes, the
 system uses the estimated labor hours and total cost estimates to derive the
 budget Labor Hours and Cost Total, respectively. However, since these scopes are
 not billable, no Price Total or Profit will be calculated.

- Flat Price - For these scopes, the
 system uses the estimated labor hours and total cost estimates to derive the
 budget Labor Hours and Cost Total, respectively. It then uses the Price entered
 for the work order scope as the Price Total. The Profit is then calculated as the
 Price Total less the Cost Total.

- Time and Material - For these scopes,
 the SM Work Order Cost Detail form provides additional fields for entering markup
 rates for cost estimates, which are then used to calculate pricing estimates. The
 system sums the cost estimates and pricing estimates to determine the estimated
 Cost Total and Price Total (respectively) for the work order scope. The Profit is
 then calculated as the Price Total less the Cost Total.

- Job Work Order, Actual Cost - For
 scopes on these work orders, the system uses the estimated labor hours and total
 cost estimates to derive the budget Labor Hours and Cost Total, respectively.
 However, since no markups or pricing estimates are defined for these scopes, no
 Price Total or Profit will be calculated.

- Job Work Order, Markup - For scopes
 on these work orders, the SM Work Order Cost Detail form provides additional
 fields for entering markup rates for cost estimates, which are then used to
 calculate pricing estimates. The system sums the cost estimates and pricing
 estimates to determine the estimated Cost Total and Price Total (respectively) for
 the work order scope. The Profit is then calculated as the Price Total less the
 Cost Total.

Related tasks

- [Enter Summarized Cost Estimates for Customer Work Order Scopes](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/enter-summarized-cost-estimates-for-customer-work-order-scopes)

- [Enter Summarized Cost Estimates for Job Work Order Scopes](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/enter-summarized-cost-estimates-for-job-work-order-scopes)
