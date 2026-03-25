---
title: "About the PM Revenue Projection Options Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projection-options-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-revenue-projection-options-form"
---

# About the PM Revenue Projection Options Form

 Use this form (accessed by selecting the Calculate
 Projections option from the Options menu in PM Revenue Projections) to initialize revenue
 projections.
 The projection method determines how projected revenue values will be
 calculated. Available methods are as follows:

- Units from Cost Projections - If you select this method, calculation will project revenue units based on projected cost units from JCCD (Cost Detail). Calculation will include projected cost units for all phases/cost types assigned to as a contact item where the cost type UM, and the cost type Item Unit Flag is checked. If cost projected units are 0.00, projected revenue units will be set equal to the current contract units. This method is typically used for unit-based contracts where the contract units are likely to change, and cost projections have been done and projected units modified (plugged).
If the unit of measure for the Contract Item is not the same as the Job
 Phase Cost Header (JCCH) unit of measure, revenue projected units and dollars will be
 calculated as follows:
Revenue Projected Units = (Cost Projected Units \ Cost Current Estimate
 Units) * Contract Item Current Contract Units
Revenue Projected Dollars = Revenue Projected Units * Contact Item Unit
 Price
Cost Projected Units and Cost Current Estimate Units are based on cost
 types with the Item Unit flag checked.

- Billed Units and Dollars - If this method is selected, calculation will project revenue units and dollars based on units and dollars billed through the month and date specified. This method is typically used at the end of a job (i.e. job closeout) when you want the revenue projected units and dollars to be equal to the billed values.

- Actual Cost plus Markup Percent - If this method is selected, projected revenue values will be set equal to actual costs plus a specified markup percent. If you do not specify a markup, projection values will be set equal to actual costs. You will typically use this method for T&M projects. Since WIP reports use projection information, this will allow revenue to be set to cost plus the specified markup on the reports.

- Projected Cost plus Markup Percent - If this method is selected, projected revenue values will be set equal to projected costs plus a specified markup percent. If you do not specify a markup percent, projection values will be set equal to projected costs. You will typically use this method for T&M projects. Since WIP reports us projection information, this will allow revenue to be set to projected cost plus the specified markup on the reports.
