---
title: "About the JC Revenue Calculation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form"
---

# About the JC Revenue Calculation Form

Use the JC Revenue Calculation form (accessed by selecting the Calculate Projections option from the Options menu in JC Revenue Projections) to initialize revenue projections.

## Write Over Plugged Values

The Write Over Plugged Values option determines how the sytem handles plugged
 (overridden) values during initialization.
You can specify to 'Never' calculate
 projected revenue units and dollars for a contract item that has been previously
 plugged, or to ‘Always’ calculate projected revenue units and dollars for a contract
 item, regardless of whether previous plugged values exist.
Note: If you are using the Units from Cost Projections
 projection method, plugged values for contract items with a LS unit of measure will
 be left intact, regardless of whether you specify to ‘always write over plugged
 values’.

## Projection Methods

When initializing revenue projections, the projection method determines how
 the system calculates projected revenue values. Available methods are as follows:

- Units from
 Cost Projections – If you select this method, calculation
 will project revenue units based on projected cost units from JCCD (Cost
 Detail). Calculation will include projected cost units for all phases/cost
 types assigned to a contract item where the cost type UM equals the contract
 item UM, and the cost type Item Unit Flag is checked. If cost projected
 units are 0.00, projected revenue units will be set equal to the current
 contract units. This method is typically used for unit-based contracts where
 the contract units are likely to change, and cost projections have been done
 and projected units modified (plugged).If the unit of
 measure for the Contract Item is not the same as the Job Phase Cost
 Header (JCCH) unit of measure, revenue projected units and dollars will
 be calculated as follows:
Revenue Projected
 Units = (Cost Projected Units \ Cost Current Estimate Units) * Contract
 Item Current Contract Units
Revenue Projected
 Dollars = Revenue Projected Units * Contract Item Unit Price
Note: Cost Projected Units and Cost Current
 Estimate Units are based on cost types with the Item Unit flag
 checked.

- Billed
 Units and Dollars - If this method is selected, calculation
 will project revenue units and dollars based on units and dollars billed
 through the month and date specified. This method is typically used at the
 end of a job (i.e. job closeout) when you want the revenue projected units
 and dollars to be equal to the billed values.

- Actual
 Cost plus Markup Percent – If this method is selected,
 projected revenue values will be set equal to actual costs plus a specified
 markup percent. If you do not specify a markup, projection values will be
 set equal to actual costs. You will typically use this method for T&M
 projects. Since WIP reports use projection information, this will allow
 revenue to be set to cost plus the specified markup on the reports.

- Projected
 Cost plus Markup Percent – If this method is selected,
 projected revenue values will be set equal to projected costs plus a
 specified markup percent. If you do not specify a markup percent, projection
 values will be set equal to projected costs. You will typically use this
 method for T&M projects. Since WIP reports use projection information,
 this will allow revenue to be set to projected cost plus the specified
 markup on the reports.

## Include Contract Item Bill Types

This section allows you to specify which contract items (within the specified
 contract item range) will be included in projection calculations based on bill type.
 There are three options available:

- All – Use this option to calculate projections for all
 contract items, regardless of their assigned bill type.

- Progress – Use this option to calculate projections for only
 those contract items with a bill type of 'Progress'.

- T&M and Both – Use this option to calculate projections
 for contract items having either a 'T&M' or 'Both' bill type. You will
 typically select this option if you are using the 'actual cost plus markup'
 projection method.

After you set up the projection options,
 specify the contract and contract item range to initialize. Then click OK to begin
 calculations. Once complete, a message displays indicating how many projections were
 initialized. Click the Close button to exit the calculation form and return to the
 revenue projections grid.
Note: If you included pending/potential change order
 amounts in projection calculations (the Projections Option field is set
 to Display & Calculate in Projections for the PCO’s status code‘), the
 projection calculation will include all pending changing order item amounts meeting
 the criteria.
[About the JC Revenue Projections Form](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)
