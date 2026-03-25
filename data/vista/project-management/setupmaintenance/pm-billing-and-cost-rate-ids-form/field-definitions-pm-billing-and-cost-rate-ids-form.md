---
title: "Field Definitions: PM Billing and Cost Rate IDs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form/field-definitions-pm-billing-and-cost-rate-ids-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form/field-definitions-pm-billing-and-cost-rate-ids-form"
---

# Field Definitions: PM Billing and Cost Rate IDs Form

The following is a list of field descriptions for the PM
 Biling and Cost Rate IDs form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Budget Code

 Enter a budget code, up to 10 characters. Examples of codes you might use:
 C1 – Carpenter Apprentice
 C2 – Carpenter Journeyman
 C3 – Carpenter Foreman
 L1 – Laborer Type 1
 L2 – Laborer Type 2
 LS – Labor Subtotal
 LT – Labor Total

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Description

 Enter a description of this budget code, up to 60 characters.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

## Costing Level

Specify the costing level for this budget code. The costing level determines the level of cost or revenue detail that will be provided when setting up budgets in PM Project Budgets or projection detail in JC Cost Projections.

- Detail – Select this option if using this budget code to breakdown cost or revenue detail.

- Subtotal – Select this option if using this budget code to provide a subtotal (with or without markup).

- Total – Select this option if using this budget code to provide a grand total (with or without markup).

Note: You will typically only use the Subtotal and Total costing levels if you will be assigning the budget code to budgets in PM Project Budgets.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Exclude From Lookups

 Check this box to exclude this budget code from budget code lookups (i.e., lookups accessed by pressing F4 at any budget code field).
 Leave this box unchecked to include this budget code in budget code lookups.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

## Phase Code

This field is enabled only when Costing Level
 is ‘Detail’.
If applicable, enter the phase (from JC
 Phases) to which this budget code is associated.
Note:Phases assigned here will not be used when entering projection detail in JC Cost Projections; they are only used when the budget code is assigned to a budget in PM Project Budgets.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

## Cost Type

This field is enabled only when Costing Level is ‘Detail’.
Enter the cost type (from JC Cost Types) to which this budget code is associated, if applicable.
Note: Cost types assigned here will not be used when entering projection detail in JC Cost Projections; they are only used when the budget code is assigned to a budget in PM Project Budgets.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

## Basis

This field is enabled only when Costing Level is ‘Detail’.
Select the basis for this budget code.

- H-Hour – This budget code will be measured in hours. Selecting this option enables the Time UM, Hrs/Time Unit, and Rate fields.

- U-Unit – This budget code will be measured in units. Selecting this option enables the Work UM and Unit Cost fields.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Time UM

 This field is enabled only when Costing Level is ‘Detail’ and Basis is ‘Hour’.
 Enter a valid unit of measure (from HQ Units of Measure) to represent the time measurement for this budget code (e.g. HRS, DAY, WEEK, etc.).

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Unit Cost

 This field is enabled only when Costing Level is ‘Detail’ and Basis is ‘Unit’.
 Enter the unit cost for the specified work unit of measure.
 This unit cost will default as the Unit Cost when this budget code is assigned to a budget in PM Project Budgets (Budget Detail tab) or specified for a projection detail sequence in JC Cost Projections (Projection Detail tab).

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Hrs/Time Unit

 This field is enabled only when Costing Level is ‘Detail’ and Basis is ‘Hour’.
 Enter the number of hours in one unit of the Time U/M specified for this budget code. For example, if the Time UM is ‘Day’, the hours/time unit would be ‘8’.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Rate

 This field is enabled only when Costing Level is ‘Detail’ and Basis is ‘Hour’.
 Enter the rate for the specified time unit of measure.
 This rate will default as the Cost/Hour when this budget code is assigned to a budget in PM Project Budgets (Budget Detail tab) or specified for a projection detail sequence in JC Cost Projections (Projection Detail tab).

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Work UM

 This field is enabled only when Costing Level is ‘Detail’ and Basis is ‘Unit’.
 Enter a valid unit of measure (from HQ Units of Measure) to represent work units for this budget code.

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs

##  Percentage

 This field is enabled only when Costing Level is ‘Subtotal’ or ‘Total’.
 Enter the markup percentage (e.g. 5% as 5.00.).

[](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form)PM Billing and Cost Rate IDs
