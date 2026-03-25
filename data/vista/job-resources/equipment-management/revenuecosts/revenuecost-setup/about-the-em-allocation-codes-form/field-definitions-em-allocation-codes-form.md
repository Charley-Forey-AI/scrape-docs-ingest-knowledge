---
title: "Field Definitions: EM Allocation Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-allocation-codes-form/field-definitions-em-allocation-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-allocation-codes-form/field-definitions-em-allocation-codes-form"
---

# Field Definitions: EM Allocation Codes Form

The following is a list of field descriptions for the EM
 Allocation Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Allocation Code

 Enter a number (0–255) that will identify this allocation.

##  Description

 Enter a description of this allocation, up to 30 characters.

## Basis

The Basis field on the EM Allocation Codes form, Info tab.
Indicate which of the following methods to use for calculating costs when processing cost allocations.

- Costs - Calculate costs based on the total dollars posted to the basis cost types (defined on the Allocation Cost Type tab).

- Hours - Base this allocation on the number of revenue/usage hours.Note: The system calculates the hours based on the time or work units x the hours per unit defined for each revenue code specified on the Allocation Rev Codes tab.

- Revenue - Calculate costs based on the total revenue/usage dollars posted to the basis revenue codes (defined on the Allocation Rev Codes tab).

- Variable - Base this allocation on a specific variable in the EM Equipment form. Specify the variable to use in the Equipment Basis Column below. You can use of the pre-defined variables provided or a custom variable (created in the VA Custom Fields Wizard form).

Note: The accumulated dollars, hours, or revenue/usage on which costs are calculated for an allocation (in EM Process Cost Allocations) are determined by whether you specify By Month or By Date Range in the Date Options section.

Related information

- [VA Custom Fields Wizard Form](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form)

##  Equipment Basis Column

 This field is only accessible if the Basis is ‘Variable’.
 Specify the standard or custom variable to use when calculating an amount for this allocation in EM Process Cost Allocations. Available standard variables are:

- EMEM.PurchasePrice

- EMEM.CurrentAppraisal

- EMEM.ReplCost

- EMEM.LeasePayment

 For a list of available custom variables, click on the arrow at the end of this field. (For information on creating custom variables, see [VA Custom Fields Wizard](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/va-custom-fields-wizard-form).)

##  Date Options

 Specify how to calculate this allocation.

- By Month - Select this option to calculate allocation costs based on the total dollars, hours, or revenue for a specific month.

- By Date - Select this option to calculate allocation costs based on the total dollars, hours, or revenue for a specific date range.

## Allocate Amount/Rate

- Allocation Amount - Select this option to allocate a fixed amount. Fixed amount is specified to the right or when processing the allocation in EM Process Cost Allocations.

- Equipment Amount Column – Select this option to allocate a fixed amount on a ‘per equipment’ basis. Use the drop-down field to the right to specify the variable (in EM Equipment) from which the allocation amount will be pulled when processing this allocation (in EM Process Cost Allocations).

- Allocation Rate - Select this option to calculate the allocation on a rate. If the allocation basis is Hours, the rate represents the dollar amount per hour. Use the field to the right to enter the allocation rate.

Note: If left blank, you must specify the rate when processing the allocation in EM Process Cost Allocations.

- Equipment Rate Column – Select this option to calculate the allocation on a rate defined on a per equipment basis. Use the combo box to the right to specify the variable (in EM Equipment) from which the allocation rate will be pulled when processing this allocation (in EM Process Cost Allocations).

## Allocation Amount

This field is only accessible if you selected
 Allocation
 Amount allocation option.
Specify the dollar amount (positive or negative) for this allocation. If set to 0.00, you will need to specify the allocation amount at the time of processing (in EM Process Cost Allocations).

Related information

- [About Defining The Allocation Amount/Rate](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-defining-the-allocation-amountrate)

## Equipment Amount Column

This field is only accessible if you selected
 the Equipment
 Amount Columnallocation option.
Using the predefined list (accessed by clicking the arrow at the end of this field), indicate the custom variable (in EM Equipment) from which to pull the amount for this allocation.
Note: In order to use this feature, you must have created
 at least one custom field (in VA Custom Fields Wizard) in which to designate an allocation
 amount. If no custom fields exist, the list will be blank.

##  Allocation Rate

 This field is only accessible if you selected ‘Allocation Rate’ allocation option.
 Specify the rate (positive or negative) for this allocation. If set to .000000, you will need to specify the allocation rate at the time of processing (in EM Process Cost Allocations).
Note: If this is an ‘hour-based’ allocation, this rate represents the dollar amount per hour.

Related information

- [About Defining The Allocation Amount/Rate](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-defining-the-allocation-amountrate)

## Equipment Rate Column

This field is only accessible if you selected
 Equipment Rate
 Columnallocation option.
Using the predefined list (accessed by clicking the arrow at the end of this field), indicate the custom variable (in EM Equipment) from which to pull the rate for this allocation.
Note: In order to use this feature, you must have created
 at least one custom field (in VA Custom Fields Wizard) in which to designate an allocation
 rate. If no custom fields exist, the list will be blank.
Note: You will typically want to specify a custom field that
 uses the ‘bRate’ datatype. However, if you specify a custom field that uses the ‘bDollar’
 datatype, it will be converted to a rate and multiplied by the basis.
For example:
udField (bDollar) = 250.00
Allocation Basis = Hours
Hours = 100
Calculation: 250.00 ¸ 100 = 2.5 (rate) x 100 (hours) = 250.00 (allocation).

##  Equipment to Allocate

 Indicate which of the following options to use when processing cost allocations to equipment.

- All Equipment - Select this option to have this allocation based on and applied to all equipment.

- Assigned Equipment - Select this option to have this allocation based on and applied to specific equipment. Use the Allocation Equipment tab to select the equipment to allocate.

- Prompt for Equipment - Select this option to have this allocation based on and applied to a specific piece of equipment designated during processing. When running EM Process Cost Allocations, you will be prompted to enter the equipment to which the allocation applies.

## Departments to Allocate

 Indicate which of the following department options to use when processing cost allocations.

- All Departments - Select this option to have this allocation based on and applied to all departments.

- Assigned Departments - Select this option to have this allocation based on and applied to specific departments. Use the Allocation Departments tab to select the departments to allocate.

- Prompt for Department - Select this option to have this allocation based on and applied to a specific department designated during processing. When running EM Process Cost Allocations, you will be prompted to enter the department to which the allocation applies.

##  Categories to Allocate

 Indicate which of the following category options to use when processing cost allocations.

- All Categories - Select this option to have this allocation based on and applied to all categories.

- Assigned Categories - Select this option to have this allocation based on and applied to specific categories. Use the Allocation Categories tab to select the categories to allocate.

- Prompt for Categories - Select this option to have this allocation based on and applied to a specific category designated during processing. When running EM Process Cost Allocations, you will be prompted to enter the category to which the allocation applies.

##  Cost Code

 Entry is required for allocations with a basis of ‘Hours’, ‘Revenue’, or ‘Variable’.
 Enter the cost code for posting allocated costs.
 If the allocation basis is ‘Cost’ and you leave this field blank, allocated amounts will be posted to the same cost code as the basis (e.g. if cost detail is posted to cost code ‘4’, allocated amounts will be based on and applied to cost code ‘4’).

##  Cost Type

 Entry is required for allocations with a basis of ‘Hours’, ‘Revenue’, or ‘Variable’.
 Enter the cost type for posting allocated costs.
 If the allocation basis is ‘Cost’ and you leave this field blank, allocated amounts will be charged to the same cost type as the basis.
Note: Basis cost type must be included on the Allocated Cost Types tab.

##  Debit Account

 Enter a valid GL account to debit for this allocation. If left blank, uses the GL account from the EM department based on cost code and cost type.

##  Credit Account

 Required.
 Enter a valid GL account to credit for this allocation.

##  Allocation Cost Type: Cost Type

 This field is only accessible for allocations having a basis of ‘Cost’.
 Enter a valid cost type (from EM Cost Types) to include in the basis of this allocation.
Note: Automatically displays all cost types added for this allocation during initialization (in EM Allocation Initialize), if applicable.

##  Allocation Rev Codes: Revenue Code

 This field is only accessible for allocations with a basis of ‘Hours’ or ‘Revenue’.
 Enter a revenue code (from EM Revenue Codes) to include in the basis of this allocation.
Note: Automatically displays all revenue codes added for this allocation during initialization (in EM Allocation Initialize), if applicable.

##  Allocation Equipment: Equipment

 This field is only accessible if the ‘Equipment to Allocate’ option is set to ‘Assigned Equipment’.
 Enter the equipment (from EM Equipment) to use when processing this allocation. Allocation will be based on and applied to this equipment.
Note: Automatically displays all equipment added for this allocation during initialization (in EM Allocation Initialize), if applicable.

##  Allocation Departments: Department

 This field is only accessible if the ‘Departments to Allocate’ option is set to ‘Assigned Departments’.
 Enter the department (from EM Departments) to use when processing this allocation. Allocation will be based on and applied to this department.
Note: Automatically displays all departments added for this allocation during initialization (in EM Allocation Initialize), if applicable.

## Allocation Categories: Category

This field is only accessible if the ‘Categories to Allocate’ option is set to ‘Assigned Categories’.
 Enter the category (from EM Categories) to use when processing this allocation. Allocation will be based on and applied to this category.
Note: Automatically displays all categories added for this allocation during initialization (in EM Allocation Initialize), if applicable.
