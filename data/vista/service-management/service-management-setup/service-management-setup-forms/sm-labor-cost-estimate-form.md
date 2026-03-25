---
title: "SM Labor Cost Estimate Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-cost-estimate-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-cost-estimate-form"
---

# SM Labor Cost Estimate Form

Use the SM Labor Cost Estimate form to set up labor cost rate estimates by technician, craft, class and/or effective date.
The system uses the rates defined here
 to determine the cost rate for the following:

-  Labor requirements entered manually
 for a quote or auto-added to the quote from standard tasks associated with
 required tasks on the quote.

- Labor requirements entered manually
 for a work order or auto-added to the work order from an agreement service or
 from standard tasks associated with required tasks on the work order.

- When calculating Allocated amounts
 for labor allocations entered for an agreement (in SM Agreement Labor
 Allocation).

Note: Setting up labor cost estimates here is not
 necessary unless you want to override the standard employee/technician or craft/class
 rates.

## Effective
 Dates

Use this tab to set up cost rates for labor by
 effective date. When setting up labor requirements for a work order quote or work
 order, the system will check for an effective date cost rate based on the
 information entered for the labor requirement (e.g. technician, craft, and/or class)
 and the current date.
For example, assume you have defined a cost rate of $65.00
 for Craft A/Class 1. You then set up the following Effective Date schedule:Effective DateCost Rate
06/01/1970.00
12/01/1975.00
06/01/2080.00

If you enter a labor requirement for Craft A/Class 1 prior
 to 06/01/19, the cost rate defaults as 65.00. If you enter a labor requirement on or
 after 06/01/19, but prior to 12/01/19, the cost rate will default as 70.00, and so
 forth.

## Labor Cost Rate Hierarchy

When you enter labor requirements
 (quotes/work orders) or labor allocations (agreements), the system searches the
 labor cost estimate records to determine which cost rate to use. Using the hierarchy
 shown below, the system looks for the closest match based on the current date and
 the information on the labor requirement or labor allocation entry. If no match is
 found on all fields, the system will continue to check each level until a match is
 found.
Note: The system also uses this hierarchy for labor
 requirements auto-added to a work order from agreement services or standard tasks
 associated with an agreement, work order, or work order quote.
PR Co
Technician
Craft
Class
Effective Date

X
X
X
X
X

X
X
X
X

X
X
X

X

X
X
X

X
X

X

X
X

X

X
X
X

X

X
X

X

X

X

X

X

X

X

X

Related tasks

- [Set Up Labor Cost Estimates](/en/vista/vista/service-management/service-management-setup/set-up-labor-cost-estimates)
