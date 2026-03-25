---
title: "Field Definitions: PM Project Budgets Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form/field-definitions-pm-project-budgets-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form/field-definitions-pm-project-budgets-form"
---

# Field Definitions: PM Project Budgets Form

The following is a list of field descriptions for the PM
 Project Budgets form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

 Enter the project (from PM Projects) for which to set up a budget.

Related information

- [PM Project Budgets Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)

##  Budget

 Manually enter a budget code or enter ‘+’, 'n', 'N', or 'New' if you want the system to automatically assign the new budget code the next available number.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Description

 Enter a description of this budget, up to 60 characters.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Seq

 Display only, the sequence number assigned to this budget detail line. This sequence number only represents the order in which the entry was added to the grid; it does not control the order in which detail appears on budget reports, nor is it used in subtotals or total calculations.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Group

 Required.
 Enter the group number (1-999999) for this budget sequence. Group numbers are used to group detail together and will be used to combine lines within a group for subtotaling purposes. The group number is not used in ‘Total’ calculations.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Line

 Required.
 Enter a line number (1-9999) for this budget sequence. The line number controls the order in which the detail appears on budget reports, and is used in the subtotal and total calculations.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Level

 Specify the costing level for this budget sequence. The costing level defines the level of cost or revenue detail.

- Detail – Select this option if using this budget code to breakdown cost or revenue detail.

- Subtotal – Select this option if using this budget code to provide a subtotal (with or without markup).

- Total – Select this option if using this budget code to provide a grand total (with or without markup).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

## Code

Enter a budget code (must be set up in PM Billing and Cost Rate IDs) for this budget sequence. May be left blank.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

## Description

Enter a description for this budget sequence, up to 60 characters. May be left blank. If you entered a budget code for this sequence, defaults the description defined in [PM Billing and Cost Rate IDs](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

## Phase

Enter the phase to which this budget sequence applies. May be left blank. If you entered a budget code for this sequence, defaults the phase assigned in PM Billing and Cost Rate IDs, if applicable.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

## C-T: Cost Type

Enter the cost type to which this budget sequence applies. May be left blank.
If you entered a budget code for this sequence, defaults the cost type assigned in [PM Billing and Cost Rate IDs](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Units

 Enter the number of units for this budget sequence.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

## UM

Enter a valid unit of measure for this budget
 sequence. May be left blank. If you entered a budget code for this sequence, defaults the
 UM assigned in PM Billing and Cost Rate IDs, if applicable. If no budget code is entered,
 but a phase and cost type are entered, defaults the UM assigned to the phase/cost type in
 JC Phases (Cost Types tab).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

## Hrs/Unit

Enabled only if tracking hours for the specified cost type (flag in JC Cost Types).
Enter the number of hours required to complete a single unit of the specified UM. If you entered a budget code for this sequence, defaults the hours/unit specified in [PM Billing and Cost Rate IDs](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Hours

 Enabled only if tracking hours for the specified cost type (flag in JC Cost Types).
 Enter the number of hours required to complete this sequence. Initially defaults a value based on Units x Hrs/Unit. May be overridden; however, Hrs/Unit will be recalculated.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Cost/Hour

 Enabled only if tracking hours for the specified cost type (flag in JC Cost Types).
 Enter the cost per hour for this sequence.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Unit Cost

 Enter the unit cost for this sequence. If you entered a budget code for this sequence, defaults the unit cost specified in PM Billing and Cost Rate IDs.
Note: If you are tracking hours for the specified cost type (flag in JC Cost Types) and you specified a cost per hour (in previous field), defaults the specified cost/hour value, even if you specified a unit cost for the budget code in PM Billing and Cost Rate IDs. If you then override the unit cost, the cost/hour value is not recalculated; however, the Hrs/Unit will be recalculated based on Unit Cost ÷ Cost/Hour and the Hours recalculated based on Units x Hrs/Unit.

Related information

- [PM Project Budgets Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)

## Markup

Enabled only if Level is set to ‘S-Subtotal’ or ‘T-Total’.
Enter the markup percentage for this sequence. If you entered a budget code for this sequence, defaults the percentage specified in [PM Billing and Cost Rate IDs](/en/vista/vista/project-management/setupmaintenance/pm-billing-and-cost-rate-ids-form), if applicable.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Amount

 This field is only enabled if Level is set to ‘D-Detail’.
 Enter the total amount for this sequence. If UM not ‘LS’, defaults an amount based on Units x Unit Cost.
 For sequences where Level is ‘S-Subtotal’, the amount will be a calculation of the subtotal markup percent times the sum of all sequences within the group with a line number less than the Subtotal line number.
 For sequences where the Level is ‘T-Total’, the amount will be a calculation of the total markup percent times the sum of all sequences (regardless of group) with a line number less than or equal to the Total line number.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets

##  Total

 Display only, the total amount for Subtotal and Total sequences.
 For sequences where Level is ‘S-Subtotal’, this amount will be the sum of the subtotal amount, plus the amount of all lines within the group with a line number less than the subtotal line number.
 For sequences where the Level is ‘T-Total’, this amount will be the sum of all sequences where the line number is less than or equal to the Total line number (regardless of group).

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-budgets-form)PM Project Budgets
