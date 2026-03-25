---
title: "About Adding Template Phases to a Project | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup_1/about-adding-template-phases-to-a-project"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup_1/about-adding-template-phases-to-a-project"
---

# About Adding Template Phases to a Project

You can add the phases set up on a template to a project using
 the PM Copy Template form.
When you copy template phases to a project, the following occurs:

- All phases and cost types defined on the template are set up for the
 destination project in PM Project Phases. Note: Phases/cost types that no longer exist in JC Phases
 will still be copied to the project; however, the UM for each cost type will
 be set to 'LS', the Bill Flag set to 'C', and the Item Unit and Phase Unit
 flags set to 'N'.

- Phases will be assigned to the contract item specified for them on the
 template. If the assigned contract item does not exist on the contract, it will
 automatically be set up for the contract in PM Contracts as follows:

- If no standard item code is assigned, the contract item description will
 default from the phase description and the UM will default as LS. If
 multiple phases are assigned the same contract item, the contract item
 description will default from the first phase assigned to the contract
 item.

- If a standard item code is assigned, the contract item description will
 default from the item code description and the UM will be the standard
 item code's UM (as assigned in JC Standard Item Codes). Note: This only
 applies if the contract is assigned a region code. If no region code
 exists, the contract item description defaults from the phase and
 the UM will default as LS. The standard item code is not
 used.

- If a phase is assigned to an existing contract item and a standard item code is specified, the item code will not be copied to the contract; however, the phase and cost types will be added to the project.

- If a phase is not assigned a contract item, but is assigned a standard item
 code that exists for the contract's region, the standard item code will become
 the contract item, the contract item description will default from the standard
 item code description, and the UM will be the standard item code's UM (as
 assigned in JC Standard Item Codes). If the standard item code does not exist
 for the contract's region, and you have specified to 'add standard item codes to
 database if not on file' (in JC Company Parameters), roll-in will:

- add the standard item codes to JC Standard Item Codes (JCSI). The
 standard item code description will default from the phase and the UM
 will default from the cost type having a Bill Flag of Y. If multiple
 phases are assigned the same standard item code, the description will
 default from the first phase having a cost type with a Bill Flag of Y,
 and will use that cost type's unit of measure. Unit of measure will
 default as LS if there are no cost types with a Bill Flag of Y.

- add the standard item codes and contract items to the contract, with
 contract item codes equal to the standard item codes. Contract item
 descriptions will default from the standard item codes. If multiple
 phases are assigned the same standard item code, description will
 default from the first phase. Contract item UM's will default from the
 phase cost type with a Bill Flag of Y. If multiple phases are assigned
 the same standard item code, the unit of measure will default from the
 first phase having a cost type with a Bill Flag of Y. If no cost types
 have a Bill Flag of Y, unit of measure will default as LS.

- add the phases and cost types to the project with the standard item code
 assigned as the contract item.Note: If the "Add Standard Item Code to
 Database if Not on File" flag is N, standard item code is set to
 null, and phase is assigned to contract item #1.

- Phases not assigned a contract item or standard item code will automatically be assigned to contract item #1. The contract item description will be the project description and the UM will be LS.

- If the template includes the subcontract cost type on any phases, a record will be added to the PM Subcontract Detail form for assignment of subcontracts.
