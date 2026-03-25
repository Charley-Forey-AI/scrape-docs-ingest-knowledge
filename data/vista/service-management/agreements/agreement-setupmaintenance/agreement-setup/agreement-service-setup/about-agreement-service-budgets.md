---
title: "About Agreement Service Budgets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-agreement-service-budgets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-agreement-service-budgets"
---

# About Agreement Service Budgets

You can set up budget information for an agreement service by entering summarized or detailed cost estimates.
There are two methods for setting up budget information for an agreement service.

- Summarized Cost Estimates - These are entered in SM Service Detail (accessed
 by clicking the Detail button in the Budget section of SM Service).

- Detailed Cost Estimates - These are entered in SM Service using the
 Material, Equipment, Labor, and Misc tabs.

The system determines which set of cost estimates to
 use when calculating the budget totals (estimated Labor Hours, Cost Total, Price Total,
 and Profit) depending on how you set the Derive checkbox for the agreement
 service (in the Budget section of SM Service, Info tab).

## Detailed Cost Estimates

If you prefer to use detailed cost estimates to derive the estimated budget totals,
 select the Derive checkbox. The system will sum the labor hours from all
 entries on the Labor tab to determine the estimated Labor Hours for the agreement
 service. It will then sum the detailed cost estimates to determine the estimated
 budget totals. The Pricing method defined for the agreement service determines how
 the budget totals are calculated:

- Included in Agreement - For these services, the system sums the cost
 totals from all tabs to derive the budget Cost Total. However, since these
 services are included in the agreement price, no Price Total or Profit will be
 calculated.

- Time of Service, Flat Price and Periodic - For these services, the
 system sums the cost totals from all tabs to derive the budget Cost Total. It
 then uses the Price entered for the agreement service as the Price Total. The
 Profit is then calculated as the Price Total less the Cost Total.

- Time of Service, Rate Template - For these services, the systems sums the
 cost totals and billable totals from all tabs to derive the budget Cost Total
 and Price Total. The Profit is then calculated as the Price Total less the Cost
 Total.

## Summarized Cost Estimates

If you do not select the Derive checkbox, you can use the SM Service Detail
 form to enter estimated labor hours, and summarized cost estimates for labor,
 materials, equipment, subcontracts, and miscellaneous expenses. The system will then
 use the summarized cost estimates to determine the estimated budget totals. The
 Pricing method defined for the agreement services determines how the budget totals
 are calculated:

- Included in Agreement - For these services, the system uses the estimated
 labor hours and total cost estimates to derive the budget Labor Hours and Cost
 Total, respectively. However, since these services are included in the agreement
 price, no Price Total or Profit will be calculated.

- Time of Service, Flat Rate and Periodic - For these services, the
 system uses the estimated labor hours and total cost estimates to derive the
 budget Labor Hours and Cost Total, respectively. It then uses the Price entered
 for the agreement service as the Price Total. The Profit is then calculated as
 the Price Total less the Cost Total.

- Time of Service, Rate Template - For these services, the SM Service
 Detail form provides additional fields for entering markup rates for cost
 estimates, which are then used to calculate pricing estimates. The system sums
 the cost estimates and pricing estimates to determine the estimated Cost Total
 and Price Total (respectively) for the agreement service. The Profit is then
 calculated as the Price Total less the Cost Total.

Note: When you create a work order from the agreement service (via SM Generate PM Work
 Orders), the system updates the budget totals for the work order from the agreement
 service. If you selected the Derived checkbox on the agreement service, but
 also entered summarized cost estimates, the system will populate the summarized cost
 estimates on the work order scope using the detailed cost estimates. The summarized
 cost estimates on the agreement service will be left intact.
Once you enter your service budgets, the system sums the cost estimates for
 all services and displays them by call type and call type category in the Service
 Budget column of the Budget tab in SM Agreements. Additionally, the system will sum
 all pricing estimates and display the total value in the Est. Service Revenue field
 for the agreement (next to the agreement price).

Related concepts

- [SM Service Detail Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-detail-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)
