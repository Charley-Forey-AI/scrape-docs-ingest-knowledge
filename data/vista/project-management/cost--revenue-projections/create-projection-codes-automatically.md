---
title: "Create Projection Codes Automatically | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/create-projection-codes-automatically"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/create-projection-codes-automatically"
---

# Create Projection Codes Automatically

 You can create projection codes automatically based on the phases, cost types, phases and cost types, or contract items on the job.This can save you time and reduce data entry when creating projection codes
Projection codes allow you to control what level of detail you want when creating cost projections in the PM Cost Projections form.When generating projection codes, the system will skip codes that meet the following criteria:

- Any phase/cost type that is already been assigned to a projection code on the job

- Any phase that is already associated with a projection code

- Any phase on the job that is not associated with a cost type - This can occur if there are no cost types associated with the phase in the JC Phases form (Cost Types tab), and no cost types were added to the phase once it was associated with the job (JC Job Phases, Cost Types tab).

Note: You can copy projection codes from one project to another; typically useful when projection codes are similar between projects. For more information, see [Copy Projection Codes](/en/vista/vista/project-management/cost--revenue-projections/copy-projection-codes).

To auto-create projection codes:

1. Open the PM Projection Codes form.

1. In the Project field, enter the source project or press F4 to select from a list of valid projects.

1. From the toolbar, select Tasks and then select one of the following:Menu OptionDescription
Create Projection Codes from PhasesCreates a projection code for each phase on the job. If a phase is associated with multiple cost types (in JC Job Phases), those cost types are added to the Phase/Cost Type tab on the PM Projection Codes form. If the PhaseUnitFlag checkbox is selected for a phase cost type, that UM defaults as the projection code's unit of measure.
Note: The Proj Code Units checkbox is automatically selected for all cost types on the phase where the UM matches the UM of the cost type with the PhaseUnitFlag​ checkbox selected.

Note: If you have linked cost types associated with a projection code, and want their units updated automatically when posting units to the associated primary cost type, you must select the Proj Code Units checkbox for each applicable linked cost type. Otherwise, no updates will occur for the linked cost types.

Create Projection Codes from Cost TypesCreates a projection code for each cost type on the job. If a cost type is associated with multiple phases, those phases are added to the Phase/Cost Type tab on the PM Projection Codes form.
Create Projection Codes from Phases and Cost TypesCreates a projection code for each unique phase and cost type combination on the job.

- The ID number of each generated projection code will be a combination of the phase code and the cost type. For example, if phase is 03110- - and the cost type is 3, the projection code will be 03110- - - 3.

- The description of each projection code will be a combination of the the phase and cost type descriptions. For example, if the phase description is F&S Footings/Foundations and the cost type description is Labor, the projection code description will be F&S Footings/Foundation - Labor

- The projection code UM will be automatically set with the cost type UM.

 Cost types are associated with the phases of a job using the Cost Types tab on the JC Job Phases form.

Create Projection Codes from Contract ItemsCreate a projection code for each contract item on the job.

- The contract item must be associated with a phase on the job. The system will not create projection codes for contract items that have been created using the JC Contracts form but not associated with a phase on the JC Jobs form.

- If a contract item is associated with multiple phases, those phases are added to the Phase/Cost Type tab on the PM Projection Codes form.

- The system will also create a record on the Phase/Cost Type tab for each cost type associated with a phase on the contract item.

- If the Item Unit Flag is set for a phase’s cost type, that UM will default as the projection code's UM.

The screen displays a form that corresponds to the option you selected. For example, if you selected Create Projection Codes from Phases, the Create ProjCodes from Phase form displays.

1. Select Start.A message displays indicating how many projection codes were created. In addition, it will also specify how many codes were not created.

1. Select Close.

The generated projection codes display in the PM Projection Codes form.

Related concepts

- [PM Projection Codes Form](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form)

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

Related tasks

- [Copy Projection Codes](/en/vista/vista/project-management/cost--revenue-projections/copy-projection-codes)
