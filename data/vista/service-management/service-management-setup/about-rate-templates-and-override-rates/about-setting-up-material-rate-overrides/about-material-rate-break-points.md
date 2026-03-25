---
title: "About Material Rate Break Points | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/about-material-rate-break-points"
---

# About Material Rate Break Points

Rate break points allow you to define one or more levels of discount or markup rates for materials used on work orders.
You can set up material rate break points in one of two places:

- SM Rate Override Material - You will set up rate break points here if you need differing levels of overrides to the standard markup/discount rate specified on the rate template for materials.

- SM Override Category Material - You will set up rate break points here if you override markup/discount rates by category or material, and you need differing levels of overrides to the standard markup/discount rate specified for selected categories or materials.

When setting up rate break points, you must first
 specify whether to override rates based on a material's total cost or unit cost using
 the Break Points
 By field in the Material Rates section of the setup form (SM Rate
 Templates, SM Rate Template Effect Dates, SM Override Category Material, or SM Rate
 Override Base). This rate basis determines what the break point values represent as
 follows:

- If you select Total Cost, the break point values represent the total dollar
 amount levels used to determine a discount or markup rate (depending on the rate
 type).

- If you selected Unit Cost, the break point values represent the unit cost levels
 used to determine a discount or markup rate

When entering work completed material lines
 (Inventory or Purchase), the system applies the discount or markup rate based on the
 material's total cost or unit cost. If the total cost or unit cost is less than the
 first level of rate break points, the system uses the standard rate defined in the
 Material Rates section. If the total cost or unit cost equals or exceeds the first level
 of rate break points, the system applies the discount or markup rate accordingly.
For example, you set up the material rate options as follows:Type: Markup
Basis: Actual Cost
Break Points By: T-Total Cost
You set up your break points as
 follows:
Table 1. Break Point ValuePercent
2.000003.00000
2.500003.50000
3.000004.00000
3.500004.50000

You then enter a material work
 completed line with a unit cost of $2.60 and a quantity of 100 (for a Total Cost of
 $260.00). The system compares the material's actual unit cost to the Break Points
 table and determines that it falls between the 2.50000 and 3.00000 break point
 values. Therefore, it uses the rate of 3.5% when calculating the billable rate for
 the material:
$260.00 + (260.00 x
 .035) = 269.10
269.10 ÷ 100 =
 2.6910 (billable rate)
The
 calculation will differ slightly depending on the basis you selected for material
 rates. For example, if you select Last Cost as the rate basis and your Last Unit
 Cost for the material was $2.45, the system compares the last unit cost to the Break
 Points table to determine the rate to use. In this case, since $2.45 falls between
 the 2.00000 and 2.50000 break points, the system uses the rate of 3.0% when
 calculating the billable rate for the material as follows:
(2.45 x 100) + (245.00 x .030) =
 252.35
252.35 ÷ 100 = 2.5235
 (billable rate)
Note: Due to the differing
 levels of material rate overrides that can be set up, the system uses a specific
 hierarchy to determine which markup/discount rates to use when calculating billable
 rates for work completed inventory or work completed purchase lines. For more
 information, see [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).
