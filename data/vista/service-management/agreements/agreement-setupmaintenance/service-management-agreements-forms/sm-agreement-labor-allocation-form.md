---
title: "SM Agreement Labor Allocation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-labor-allocation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-labor-allocation-form"
---

# SM Agreement Labor Allocation Form

Use the SM Agreement Labor Allocation form to set up labor allocations for agreement quotes.
Access this form by clicking the Labor Allocation button in SM Agreements.
 Labor allocations are defined by call type and craft/class and are used to specify how many labor hours to allocate to each applicable month in a calendar year. If your agreement term spans multiple years, you can enter labor hours for each applicable month in each year of the agreement term. Although you will typically used this feature in conjunction with agreement budgets, you can set up labor allocations without a budget.

## Budget Labor Summary

The Budget Labor Summary grid displays in the upper right corner of the form and shows the budget amounts defined for an agreement (on the Budget tab of [SM Agreements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)). The Budget Total column displays the Budget Amount specified for each call type with a labor cost type category. As you enter hours for each month in the labor allocation grid, the system calculates the Allocated amount (hours x cost rate) and then subtracts the amount from the Budget Total to determine the Remaining amount. If you did not set up a budget, the Budget Labor Summary grid will initially display as blank. As you enter labor allocations, the grid is updated with each call type entered. The Budget Total will be 0.00 for each call type, but the Remaining amount will be updated as the sum of all entries for the call type (hours x cost rate). In this case, since there is no budget amount, remaining amounts will show as a negative amount.Note: The Budget Total and Remaining amount represents all months for all years of the agreement. This also applies to the Hours and Allocated amounts shown for each call type in the allocation grid.

## Yearly Commitments by Labor Type

 The yearly Commitments by Labor Type grid displayed at the bottom of the form shows the total allocation for each craft or craft/class combination by month for the given year. These totals encompass all allocations defined for the craft/class across all active agreements for the SM company. The labor hours include agreements that are scheduled to be renewed, based on the Auto-Renewal Period on the agreement, projecting the labor hours by month as they will be adjusted on the renewal. Allocations entered for the current agreement will be updated to this grid once you "activate" the agreement.

## Amendments and Renewals

When you amend or renew an agreement, the system copies all labor allocations to the new agreement revision and adjusts the months accordingly. Entries for a month that do not apply to the new agreement term are deleted. For more information about amendments and renewals, see [Amend an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement) and [About Agreement Renewals](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-renewals).

The following is a related task:
[Set up Labor Allocations](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-labor-allocations)
