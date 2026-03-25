---
title: "About Using the Spread Option for Cost Projections | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-using-the-spread-option-for-cost-projections"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-using-the-spread-option-for-cost-projections"
---

# About Using the Spread Option for Cost Projections

When entering projections in the PM Cost Projections form, the
 spread determines how plugged values entered on the projection code are distributed to the
 phases/cost types.
When you set a spread option for projections in PM Company Parameters,
 the selection is applied to all of the projections made in that company. The following
 describes each of the options.

## Prorated

If you select Prorated, the plugged amount is distributed based on a weighted
 average of the percent complete units on the phases/cost types associated with the
 selected projection code (in PM Projection Codes).
For example, assume a projection code is
 associated with three phases and each phase is associated with the same cost type.
Table 1. Projection Code 1Phase
Cost Type

1000-
6

1001-
6

1002-
6

When a projection is then entered on the
 projection code in PM Cost Projections, assume the Phase/Cost Type tab contains the
 following information.
Phase
Cost Type
Percent Complete Units

1000-
6
30

1001-
6
40

1002-
6
80

Total units
150

If 200 units is entered in the
 Percent
 Complete Units field on the Grid tab of the PM Cost Projections
 form, the 200 units will be distributed to the Phase/Cost Types tab in the following
 way.
Phase
Cost Type
Calculation
Percent Complete Units

1000-
6
( 30 / 150 ) * 200
40

1001-
6
( 40 / 150 ) * 200
53.33333333333333

1002-
6
( 80 /150 ) * 200
106.6666666666667

Total units
200

Note: When spreading adjustments for units on a
 projection code only those phase/cost types that are flagged as ‘Proj Code Unit’
 will receive the adjustment either prorated or user-defined as specified.

## Defined at projection code

If you select Defined at
 projection code, the plugged amount is distributed to the
 phases/cost types based on the spread percentage set up on the projection code (PM
 Projection CodesPhase/Cost Type tab, Spread % field).
For example, assume a projection code is
 set up with the following phases/cost types.
Phase
Cost Type
Spread %

1000-
6
20

1001-
6
30

1002-
6
50

If you enter 200 units in the Percent Complete
 Units field on the Grid tab of the PM Cost Projections form, the
 system will A distribute the 200 units in the following way.
Phase
Cost Type
Calculation
Percent Complete Units

1000-
6
20% * 200
40

1001-
6
30% * 200
60

1002-
6
50% * 200
100

Total units
200

Note: When using this option, you must manually set up the spread on each
 phase/cost type on every projection code on the project. This means more data
 entry and additional set up time. Use the Spread % field on the
 Phase/Cost Type tab of the PM Projection Codes form to define the spread on each
 phase/cost type.

Note: When entering projections in PMCost Projections form, you can modify how the
 plugged values are distributed using the PM Adjust Cost Projection form. This
 only applies to the Defined at projection code
 option.

## Modify How Plugged Values are Distributed

When you enter a plugged amount on the projection code, the plugged values are
 distributed to the phases/cost types based on how you configured the spread.
 However, you can also change how plugged values are distributed, for example, if you
 need to change how a variance is spread to the phase/cost types when the projections
 are being entered.
For instructions about modifying the distribution for plugged values, see [Modify Plugged Amount Distributions for a Projection Code](/en/vista/vista/project-management/cost--revenue-projections/modify-plugged-amount-distributions-for-a-projection-code).

Related concepts

- [PM Projection Codes Form](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form)

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
