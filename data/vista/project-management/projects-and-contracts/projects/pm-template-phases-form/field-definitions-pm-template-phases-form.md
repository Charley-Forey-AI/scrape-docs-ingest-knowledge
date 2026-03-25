---
title: "Field Definitions: PM Template Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-template-phases-form/field-definitions-pm-template-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-template-phases-form/field-definitions-pm-template-phases-form"
---

# Field Definitions: PM Template Phases Form

The following is a list of field descriptions for the PM
 Template Phases form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Template

Enter a name, up to 10 characters, that uniquely identifies this template. This name should represent the group of commonly used or standard phases/cost types used for similar jobs (e.g. HOUSING, OFFICE, BRIDGE, etc.).

## Description

Enter a description of the template. The description can be up to 30 characters long.

## Phase

Enter a phase or press F4 to select one from a
 list. Phases that you assign to this template should be standard to jobs using this
 template.
Phases are created and maintained using [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form).

## Description

The description of the phase. This field
 defaults with the description of the phase set up in [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form), but it can be changed.
The description can be up to 30 characters long.

##  Contract Item

 Enter the contract item, up to 16 digits, to which this phase will be linked when the template is rolled into a project.
 If the contract item does not already exist on the destination contract, it will be set up for the contract automatically during the roll-in, with the contract item description defaulting from the phase description. If multiple phases are assigned to this contract item, the contract item description will default from the first phase to which the contract item is assigned.
Note: If no contract item is assigned, phase will automatically be assigned to contract item #1 unless a standard item code is specified; in which case, the standard item code will become the contract item.

## Std Item Code

Enter the standard item code. Standard item codes are created and maintained in [JC Std Item Codes ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form).
Note: If no contract item is specified in the Contract
 Item field but there is a standard item code, the standard item code will
 become the contract item, and the standard item code's description will be used as the
 contract item description. If neither a contract item or standard item code is
 specified, phase will be assigned to contract item #1.

## Cost Type

All cost types for the selected phase (as
 defined in JC Phases Maintenance) will automatically display in this field.
To delete the cost type, select the line and press the Delete key (or click the Delete button in toolbar).
To add a previously deleted cost type, enter the cost type number.
Note:Cost types that have not already been set up for the
 phase in JC Phases must be added in that program before they can be added to the phase
 here.
