---
title: "Field Definitions: JC Budget Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-budget-codes-form/field-definitions-jc-budget-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-budget-codes-form/field-definitions-jc-budget-codes-form"
---

# Field Definitions: JC Budget Codes Form

The following is a list of field descriptions for the JC
 Budget Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Budget Code

The Budget Code field on the JC Budget Codes form.
Enter a budget code, up to 10 characters. Examples of codes you might use:

- C1 – Carpenter Apprentice

- C2 – Carpenter Journeyman

- C3 – Carpenter Foreman

- L1 – Laborer Type 1

- L2 – Laborer Type 2

- LS – Labor Subtotal

- LT – Labor Total

## Description

The Description field on the JC Budget Codes form.
Enter a description of this budget code, up to 60
 characters.

## Costing Level

The Costing Level drop-down on the JC Budget Codes form.
Specify the costing level for this budget code. The costing level
 determines the level of cost or revenue detail that will be provided when setting up
 projection detail in JC Cost Projections or when setting up budgets in PM Project Budgets.

- Detail - Select this option if using this budget code to
 breakdown cost or revenue detail. This is the default setting for new records.

- Subtotal - Select this option if using this budget code to
 provide a subtotal (with or without markup).

- Total - Select this option if using this budget code to
 provide a grand total (with or without markup).
Which should you select?

Although you can assign any costing level to a budget code,
 generally you should select Subtotal or
 Total if the budget code will be
 assigned to a budget in PM Project Budgets. Project budgets allow assignment of multiple
 budget codes; therefore, you can set up budget codes that will be used to provide detail
 breakdowns, as well as subtotals and grand totals.

## Exclude From Lookups

The Exclude From Lookups checkbox on the JC Budget Codes form.
Check this box to exclude this budget code
 from budget code lookups (i.e., lookups accessed by pressing F4 at any budget code field).
Leave this box unchecked to include this
 budget code in budget code lookups.

## Phase Code

The Phase Code field on the JC Budget Codes form.

 This field is
 enabled only when Costing Level is ‘Detail’.
If applicable, enter the phase (from JC
 Phases) to which this budget code is associated.
Note: Phases assigned here will not be used when entering projection detail in JC Cost Projections; they are only used when the budget code is assigned to a budget in PM Project Budgets.

## Cost Type

The Cost Type field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Detail’ or ‘Subtotal’.
Enter the cost type (from JC Cost Types) to
 which this budget code is associated, if applicable.
Note: Cost types assigned here will not be used when entering projection detail in JC Cost Projections; they are only used when the budget code is assigned to a budget in PM Project Budgets.  

## Basis

The Basis drop-down on the JC Budget Codes form.
This field is enabled when you select
 Detail from the Costing Level field.
Select the basis for this budget code:

- H-Hour - This budget code will be measured in hours. Selecting this option enables the Time UM, Hrs/Time Unit, and Rate fields.

- U-Unit - This budget code will be measured in units. Selecting this option enables the Work UM and Unit Cost fields. This is the default setting for this field.

## Time UM

The Time UM field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Detail’ and Basis is ‘Hour’.
Enter a valid unit of measure (from HQ Units
 of Measure) to represent the time measurement for this budget code (e.g. HRS, DAY, WEEK,
 etc.).

## Hrs/Time Unit

The Hrs/Time Unit field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Detail’ and Basis is ‘Hour’.
Enter the number of hours in one unit of the
 Time U/M specified for this budget code. For example, if the Time UM is ‘Day’, the
 hours/time unit would be ‘8’.

## Rate

The Rate field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Detail’ and Basis is ‘Hour’.
Enter the rate for the specified time unit of
 measure.
This rate defaults as the Cost/Hour when this
 budget code is specified for a projection detail sequence in JC Cost Projections
 (Projection Detail tab) or assigned to a budget in PM Project Budgets (Budget Detail tab).

## Work UM

The Work UM field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Detail’ and Basis is ‘Unit’.
Enter a valid unit of measure (from HQ Units
 of Measure) to represent work units for this budget code.

## Unit Cost

The Unit Cost field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Detail’ and Basis is ‘Unit’.
Enter the unit cost for the specified work
 unit of measure.
This unit cost will default as the Unit Cost
 when this budget code is specified for a projection detail sequence in JC Cost Projections
 (Projection Detail tab) or assigned to a budget in PM Project Budgets (Budget Detail
 tab).

## Percentage

The Percentage field on the JC Budget Codes form.
This field is enabled only when Costing Level
 is ‘Subtotal’ or ‘Total’.
Enter the markup percentage (e.g. 5% as
 5.00.).
