---
title: "About Adding Phases and Cost Types to a PM Project | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project"
---

# About Adding Phases and Cost Types to a PM Project

You can add phases and cost types to a project manually or by initializing or importing them.
You can add phases to a project manually in the PM Project Phases grid, initialize them using the [PM Project Phase Copy](/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-project-phases-form) form, or import them using [PM Import Estimates](/en/vista/vista/project-management/import-project-estimates/pm-import-estimates-form).
Each phase you add to the project must be linked to a contract item. Initialized phases are automatically assigned to contract item ‘1’, which may be overridden.
Note: If you selected the Auto-Add Contract Item and Update Contract Item Amount checkbox in PM Company Parameters and you assign a contract item that does not exist for the contract, the system adds it automatically (in PM Contracts). Estimate amounts entered for the phase/cost types are updated to the contract item's original amounts. If you did not select the Auto-Add Contract Item and Update Contract Item Amount checkbox, contract items must exist for the contract before you can assign them to a phase.
You may also override the projection minimum percent (defaulted for each phase from JC Phase Maser), which determines the minimum percent completed needed before cost projections can be calculated for the phase in Job Cost. If left at zero, the percentage specified for the job or in JC Company Parameters will be used.
Estimate totals (by cost type) are displayed in the informational section at the bottom of the Info tab (or at the end of the Grid tab). Totals displayed will depend on which cost types you selected for display in PM Company Parameters (CT Display tab). You can have up to ten cost types displayed; however, you might consider showing only those cost types for which you standardly enter estimate information. The Phase Total column displays the total estimate amount for all cost types defined for the phase (including those not displayed).

## Manually Adding Phases/Cost Types

You can enter phases and cost types manually or by initialization. Manual entry is typically useful when you are only adding one or two phases to a project or one or two cost types to a phase.
You can add phases manually using the Grid tab or the Info tab in PM Project Phases. If adding a phase on the Info tab, you'll need to use the Phase field above the tabs.
 When manually adding cost types, you'll use the Cost Types tab (in PM Project Phases) to assign cost types to project phases and enter estimate detail. The system automatically updates [JC Original Estimates](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form) with the information you enter, but it will not be accessible in Job Cost until you interface the project. Once interfaced, new phase/cost types entered in either PM Project Phases or JC Original Estimates will automatically update the other.
Note: If the Auto-Add Contract Item and Update Contract Item Amount checkbox is selected in PM Company Parameters), any estimated costs entered for a phase's cost types will be added to the original amounts of the contract item assigned to the phase.

## Initializing Phase/Cost Types

You can initialize phases to a project using the [PM Copy Project Phases](/en/vista/vista/project-management/projects-and-contracts/projects/pm-copy-project-phases-form) form. This method is most useful when you have a large number of phases to add to your project. For more information on initializing phases to your project, see [Copy Phases to a Project](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/copy-phases-to-a-project).
If you use the Initialization feature to add cost types (by selecting the Initialize Cost Types button), the grid is populated with all cost types set up for the phase in JC Phases, along with the assigned unit of measure and Bill Flag, Item Unit Flag, and Phase Unit Flag settings. The system sets all values (units, hrs/unit, hours, cost/hour, unit cost, and amount) to 0.00, and sets the Update field to Y (Ready to Update). You can delete any cost types you do not need, modify flag settings, and enter estimate detail as necessary. If you are not ready to interface estimate data to Job Cost, you will need to change the Update field to N (Not Ready to Update). Once you interface phase/cost type detail to Job Cost, the Update field is set to I (Interfaced) and cannot be changed, nor can you change the estimate detail here. You can, however, change the detail as necessary in JC Original Estimates, and the changes will automatically be updated here.
Note: Phase/cost type detail entered in JC Original Estimates is updated for the project in this form. The Update flag is set to J (Job Cost) to indicate the information was set up in Job Cost. If changes or modifications are made, the Update field is set to Y and you will need to interface the detail for it to be updated to Job Cost.

## Importing Phases/Cost Types

You can import phase/cost type estimates using the PM Import Estimates form. Estimates may be imported from several standard estimating packages using specific import routines. Others may be formatted to fit a generic text, comma separated value import.
During the import process, the system validates all phases against JC Phases. If they do not exist, you will receive a warning; however, the phases will still be added. You can modify the phase detail as needed, but you will be unable to add sub-phases until you add the phase to JC Phases.
Phases not added to JC Phases will not affect the PM to JC interface; the system will add all phases for the project to the JC Job Phase file during the interface, regardless of whether they exist in the JC Phases or not.
For more information about importing phase/cost type estimates, see [PM Import Estimates Form](/en/vista/vista/project-management/import-project-estimates/pm-import-estimates-form).
