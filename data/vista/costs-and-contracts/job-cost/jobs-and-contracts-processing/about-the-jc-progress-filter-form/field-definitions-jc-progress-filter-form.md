---
title: "Field Definitions: JC Progress Filter Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-filter-form/field-definitions-jc-progress-filter-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-filter-form/field-definitions-jc-progress-filter-form"
---

# Field Definitions: JC Progress Filter Form

The following is a list of field descriptions for the JC
 Progress Filter form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Job

 Specify the job for which to select phases/cost types for display. Defaults the job specified in JC Progress Entry.
Note: If you enter a soft- or hard-closed job and you do not allow posting to closed jobs (flags in JC Company Parameters), a message displays indicating the job’s status and entry is not allowed.

## Phase Options

Indicate which phases to display for progress posting.

- All Phases – Select this option to display all phases in the progress entry grid. Useful if you will be posting progress for all phases on the job.

Note: If you are using the job roles functionality and are assigned a role for this job, selecting this option will not restrict display to job role phases; the progress entry grid will display all phases, regardless of job phase role assignment. To restrict grid to only those phases assigned to your job role, use the Select Phases option.

- Select Phases – Select this option to display selected phases. Useful if you will be posting progress for specific phases on a job. Once selected, the phase selection box (below) is enabled. Phases are initially sorted by phase code, but can be sorted by contract item (by clicking on the Contract Item column) to allow selecting phases based on contract item. Select the desired phases (using the Shift key for consecutive selection or the Ctrl key for random selection) and check the box for any of the selected phases. This will automatically check the box for all highlighted phases.

Note: If you are using the job roles functionality and are assigned a role for this job, the phase selection grid will show only those phases to which your role is assigned.

- No Phases – Select this option if you do not want any phases displayed. Useful if you prefer to enter phases manually.

Note: If you are using the job roles functionality and are assigned a role for this job, you will only be able to enter phases to which your role is assigned.

## Cost Type Options

 Indicate which cost types to display for progress posting.

- All Cost Types - Select this option to display all cost types for each phase. Useful if you will be posting progress to all cost types on a phase.

- Select Cost Types - Select this option to display selected cost types. Useful if you will be posting progress to specific cost types (e.g. labor and equipment). Once selected, the cost type selection box (below) is enabled.   Select the desired cost types (using the Shift key for consecutive selection or the Ctrl key for random selection) and check the box for any of the selected cost types. This will automatically check the box for all highlighted cost types.

- Item Units Only - Select this option to display only those cost types with the Item Unit Flag checked in JC Job Phases. Useful if you will be posting progress to cost types designated for accumulating units complete for the related contract.

- Phase Units Only – Select this option to display only those cost types with the Phase Unit flag checked in JC Job Phases. Useful if you will be posting progress to cost types designated for accumulating units complete for the related phase.

Note: If you are using linked cost types, they will only display in the grid if the primary cost type is not used on the phase and you specified to include the cost type in the grid. For example, if you specify to show labor and equipment cost types, but the equipment cost type is linked to the labor cost type, only the labor cost type will display in the grid. Progress posted for the labor cost type will be posted to the equipment cost type automatically. However, if the labor cost type is not used on the phase, the equipment cost type will display to allow for posting progress.
