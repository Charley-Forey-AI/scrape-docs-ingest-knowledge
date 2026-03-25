---
title: "Field Definitions: PM Revenue Projection Options Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projection-options-form/field-definitions-pm-revenue-projection-options-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projection-options-form/field-definitions-pm-revenue-projection-options-form"
---

# Field Definitions: PM Revenue Projection Options Form

The following is a list of field descriptions for the PM
 Revenue Projection Options form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Write Over Plugged Values

 Specify how to handle plugged values when initializing projections.

- Never — Never calculate projected revenue units and dollars for a contract item that has been previously plugged.

- Always — Always calculate projected revenue units and dollars for a contract item, regardless of whether previous plugged values exist.

If you are using the ‘Units from Cost Projections’ projection method, plugged values for contract items with a LS unit of measure will be left intact, regardless of whether you specify to ‘always write over plugged values’.

Related concepts

- [About the JC Revenue Calculation Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)

## Projection Methods

Units from Cost Projections
Select this option to calculate revenue
 projections based on cost projected units from JCCD (Cost Detail).
 Calculation will include projected cost units for all phases/cost types
 assigned to a contract item where the cost type UM equals the contract
 item's UM and the cost type's Item Unit Flag is checked. If cost
 projected units are 0.00, projected revenue units will be set equal to
 the current contract. units
If the unit of measure for the Contract Item is not the same
 as the Job Phase Cost Header (JCCH) unit of measure, revenue projected
 units and dollars will be calculated as follows:

Revenue Projected Units = (Cost Projected Units \ Cost Current Estimate
 Units) * Contract Item Current Contract Units

Revenue Projected Dollars = Revenue Projected Units * Contract Item Unit
 Price

 (Cost Projected Units and Cost Current Estimate Units are based on cost
 types with the Item Unit flag checked).
You will typically only use this option for unit-based contracts where
 contract units are likely to change, and only if cost projections have
 been done and projected units modified (plugged).

Billed
 Units and Dollars
Select this option to calculate revenue
 projections based on all billing units and dollars through the month and
 date specified.

 You will typically use this option at the end of a job (i.e. job closeout)
 when you want the revenue projected units and dollars to be equal to the
 billed values.
Actual
 Cost Plus Markup Percent

Select this option to set projected
 revenue equal to the actual costs plus markup (specified below). If a
 markup percent is not specified, projection values will be set equal to
 actual costs.

 You will typically use this option for T&M projects. Since projection
 information is used on WIP reports, this will allow revenue to be set to
 cost plus the specified markup on the reports.

Projected
 Cost Plus Markup Percent
Select this option to set projected
 revenue equal to the projected costs plus markup (specified below). If a
 markup percent is not specified, projection values will be set equal to
 projected costs.

 You will typically use this option for T&M projects. Since projection
 information is used on WIP reports, this will allow revenue to be set to
 projected cost plus the specified markup on the reports.

Related concepts

- [About the PM Revenue Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Markup Percent

Enabled only for ‘Actual Cost Plus Markup Percent’ and ‘Projected Cost Plus Markup Percent’ projection methods.
Specify the percent of markup to add to actual or project cost values when calculating revenue projections, or enter 0.00 to set revenue projections equal to cost. (Example: Enter 10% as 10.00.)

Related concepts

- [About the PM Revenue Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Include Contract Item Bill Types

The Include Contract Item Bill Types radio options on the PM Revenue Projection Options form.

- All
 – Select this option to calculate projections for all contract items,
 regardless of bill type (i.e. Progress, T&M, Both, and None).

- Progress
 – Select this option to calculate projections for only those contract
 items with a 'Progress' bill type.

- T&M
 and Both – Select this option to calculate projections for only those
 contract items with a 'T&M' or 'Both' bill type. You will
 typically select this option if you are using the 'actual cost plus
 markup' projection method.

Related concepts

- [About the JC Revenue Calculation Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)

## Beginning Item

 Specify the beginning and ending item in a range of contract items for
 which to initialize revenue projections.

 If you specified a range of departments above, the calculation
 process will only include contract items within this range that are
 assigned a department within the range of departments specified above.


Related concepts

- [About the JC Revenue Calculation Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)

- [About the PM Revenue Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Ending Item

Specify the beginning and ending item in a range of contract items for
 which to initialize revenue projections.

 If you specified a range of departments above, the calculation
 process will only include contract items within this range that are
 assigned a department within the range of departments specified above.


Related concepts

- [About the JC Revenue Calculation Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)

- [About the PM Revenue Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Beginning Department

Specify the beginning and ending department in a range of departments for
 which to calculate revenue projections. The calculation process will
 include only those contracts/contract items within the specified
 contract/contract item range that are assigned a department within this
 range.

Related concepts

- [About the JC Revenue Calculation Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)

- [About the PM Revenue Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Ending Department

Specify the beginning and ending department in a range of departments for
 which to calculate revenue projections. The calculation process will
 include only those contracts/contract items within the specified
 contract/contract item range that are assigned a department within this
 range.

Related concepts

- [About the JC Revenue Calculation Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form)

- [About the PM Revenue Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projections-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)
