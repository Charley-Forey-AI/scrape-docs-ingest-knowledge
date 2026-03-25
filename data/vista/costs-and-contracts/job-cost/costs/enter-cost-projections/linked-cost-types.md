---
title: "Linked Cost Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/linked-cost-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/linked-cost-types"
---

# Linked Cost Types

If you are using linked cost types, when projections are
 entered in JC Cost Projections for the primary cost type, the linked cost type(s) will be updated as well based on
 the primary cost type's percent complete for units, hours, and costs.
If no actual values exist, the projected
 values are calculated as follows:
For the primary cost type, projected values
 will be equal to the Current Estimated values. For example:

Current Est
Actual
Proj Final

Units
1,000.00
0.00
1,000.00

Hours
80.00
0.00
80.00

Costs
25,000.00
0.00
25,000.00

Typically, projected values for linked cost
 type(s) are calculated based on the percent complete values for the primary cost type.
 However, because no actual values exist, the percent complete for the primary cost type
 will be the Projected Final / Current Estimate. Example: 1000.00/1000.00 = 1.0 (i.e.
 100%).
Projected values for the linked cost types
 are then calculated based on this percent complete (100%) and the estimated values for
 the linked cost types. Example:
Linked CT:
Curr Est Units
=
0.00
x
100%
=
0.00
(Proj Final Units)

Curr Est Hours
=
0.00
x
100%
=
0.00
(Proj Final Hours)

Curr Est Costs
=
3,750.00
x
100%
=
3,750.00
(Proj Final Costs)

If the main cost type has estimated units,
 but no estimated hours or cost, and the linked cost types have estimated units, hours,
 and cost, percent complete values for linked cost types will be set equal to the main
 cost type's percent complete for units. If the primary cost type has no estimated values
 or actual costs, linked cost types will be treated as individual cost types.
