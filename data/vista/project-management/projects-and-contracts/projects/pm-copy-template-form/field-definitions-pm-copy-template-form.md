---
title: "Field Definitions: PM Copy Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-template-form/field-definitions-pm-copy-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-template-form/field-definitions-pm-copy-template-form"
---

# Field Definitions: PM Copy Template Form

The following is a list of field descriptions for the PM Copy
 Template form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Enter the template (from PM Template Phases) from which to copy phases/cost types to the specified project.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-template-phases-form)PM Template Phases

## Project

Enter the project into which the specified
 template will be rolled. Project must already be set up in PM Projects.
To implement the roll-in, click the Copy button. All phases, cost types, and standard item codes set up on the template will be copied into the specified project and assigned to the contract item specified on the template.
Note:Phases/cost types that no longer exist in JC Phases
 will be copied to the project; however, each cost type's UM will be set to 'LS', the
 Bill Flag set to 'C', and the Item Unit and Phase Unit flags set to N.

- If the contract item does not already exist on the contract, it will be set up automatically.

- If no contract item was specified for a phase, and no standard item code is specified, the phase will be assigned to contract item #1.

- If no contract item is specified for the phase, and a standard item code is specified that exists for the contract's region, the standard item code will become the contract item, and the standard item code's description will be used as the contract item description.

- If no contract item was specified for a phase, and standard item codes are specified but do not exist for the contract's region, and you have specified to add standard item codes to database if not on file (in JC Company Parameters), copy process will:

- add the standard item codes to JC Standard Item Codes (JCSI). The standard item code description will default from the phase, and the UM will default from the cost type having a Bill Flag of Y. If multiple phases are assigned the same standard item code, the description will default from the first phase having a cost type with a Bill Flag of Y, and will use that cost type's unit of measure. Unit of measure will default as LS if there are no cost types with a Bill Flag of Y.

- add the standard item codes and contract items to the contract, with contract item codes equal to the standard item codes. Contract item descriptions will default from the standard item codes. If multiple phases are assigned the same standard item code, description will default from the first phase. Contract item UMs will default from the phase cost type with a Bill Flag of Y. If multiple phases are assigned the same standard item code, the unit of measure will default from the first phase having a cost type with a Bill Flag of Y. If no cost types have a Bill Flag of Y, unit of measure will default as LS.

- add the phases and cost types to the project, with the standard item code assigned as the contract item.

Note: If the Add Standard Item Code to Database if Not on File flag (in JC Company Parameters) is unchecked, the standard item code is set to null and the phase is assigned to contract item #1.

[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-template-phases-form)PM Template Phases
