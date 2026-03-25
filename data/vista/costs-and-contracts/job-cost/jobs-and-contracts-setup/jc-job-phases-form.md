---
title: "JC Job Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form"
---

# JC Job Phases Form

Use this form to assign phases/cost types to jobs.
Once you add a phase, all cost types assigned to the phase in the [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) form are automatically added to the phase. Using the Cost Types tab, you can delete cost types that do not apply, as well as add non-standard cost types for the phase (i.e. cost types not assigned to the phase in JC Phases).
Note: If you use the JC Original Estimates form to enter phase estimates, it should not be necessary to use this program unless you need to change a phase’s description, standard cost types, or contract item, or if you want to add notes about the phase.
Other things you can do in this form:

- Change the status of a phase - Estimates, commitments, and costs can only be posted to active phases (Info tab, Active Phase field).

- Quickly change the status of multiple phases - Select File >  Phase Status Change to quickly change the status of several phases at once.

- Delete a phase - If you want to delete the assignment of a phase to a job in this program, you must first delete all cost types assigned to the phase. However, only cost types with zero balances in every month may be deleted. Only when all cost types for the phase are deleted, can you use the delete option to delete the phase assignment.

- Enter Estimates - The Estimates tab allows you to create original estimates for each phase/cost type on a job. You can set them up directly in the grid or using the JC Original Estimates form, which you can access by double-clicking on any cost type in the grid or by placing focus in the grid and selecting the ‘Open Related Record in Form’ option from the Records menu.

- All cost types for a phase will automatically display in this grid. You can only modify the information for a cost type or delete a cost type using this tab; if you want to add a cost type, you must use the Cost Types tab.

- The informational display above the grid (Job Total and Phase Total) provides a running total of estimated costs (for the job and phase) as they are entered for each cost type on a phase.

- Roles - Use this tab to assign roles to job phases. This is an optional feature that allow users to filter the phases they work on by role when entering progress and cost projections (JC Progress Entry and JC Cost Projections). This feature has not been implemented in the enhanced cost projections process (PM Cost Projections).

- Assign a role to a user - Roles are set up in HQ Roles and represent the different functions performed by users on a job (e.g. project manager, concrete coordinator, electrician, etc.).

- Roles must be assigned at the job level (in JC Jobs) before they can be assigned at the phase level.

- Users not assigned a role will be able to access all phases in both JC Progress Entry and JC Cost Projections.For each role you assign to a phase, you must specify the process (Progress Entry or Cost Projections) to which the role is associated. For example, if the role only posts job progress, you would assign a process of Progress Entry for each applicable phase. The user assigned to that role will be able to access the specified phases in JC Progress Entry, but not in JC Cost Projections. For roles that post in both Progress Entry and Cost Projections, you will need to set up an entry for each process per phase.Note: You can also initialize phases to users/roles using JC Job Phase Roles Initialize (accessed by selecting File > Job Phase Roles Initialize).

- Assign a Contract Item - When you add a phase to the job, you must assign a contract item. You will typically assign a contract item that already exists for the job; however, if you have checked the Auto-Add Contract Item and Update Contract Item Amount box for the job in JC Jobs, you can add a contract item 'on the fly'. Just enter the new contract item number and it will be added to the contract automatically. Any estimated costs entered for the phase's cost types will be added to the contract item's original amounts. If the Auto-Add Contract Item and Update Contract Item Amount box is unchecked, contract items must exist for the contract before they can be assigned to a phase.

Note: There are several fields that are on both the JC Job Phases and PM Project Phases forms. When a change is made to one of these fields, the other form is automatically updated.

For additional information, click the links below.
[About Changing a Unit of Measure](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-changing-a-unit-of-measure)
[JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)
[Change the Status of Phases on a Job](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/change-the-status-of-phases-on-a-job)
[JC Original Estimates Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)
[JC Job Phase Roles Initialize](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form)
[About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)
