---
title: "PM Project Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form"
---

# PM Project Phases Form

Use this form to assign phases/cost types to projects and enter/modify original estimates for those phases/cost types.
Phases entered here update the Job Phases (JCJP) and Job Cost Header (JCCH) tables. These are the same tables that are updated by the JC Job Phases and JC Original Estimates programs in the Job Cost modules. However, data entered in this program is considered "pending" and will not be accessible in Job Cost until you interface the project. At the time of interface, the Job Cost by Period (JCCP) and Job Cost Detail (JCCD) tables are updated with the original estimates using the start month of the contract.
There are three ways to enter phases and cost types to a project:

- Manual entry

- Initialization

- Imports

For more information, see [About Adding Phases and Cost Types to a PM Project](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project).

## Roles

Use the Roles tab to assign roles to project phases. Roles are set up in [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) and represent the different functions performed by users on a project (e.g. project manager, concrete coordinator, electrician, etc.). Assigning roles at the project phase level will allow users to filter the phases they work on by role when entering progress and cost projections in JC Progress Entry and JC Cost Projections (once project is interfaced to Job Cost).

- Roles must be assigned at the job level (in PM Projects) before they can be assigned at the phase level.

- Users not assigned a role will be able to access all phases in both JC Progress Entry and JC Cost Projections.

For each role you assign to a phase, you must specify the process (Progress Entry or Cost Projections) to which the role is associated. For example, if the role only posts job progress, you would assign a process of Progress Entry for each applicable phase. The user assigned to that role will be able to access the specified phases in JC Progress Entry, but not in JC Cost Projections. For roles that post in both Progress Entry and Cost Projections, you will need to set up an entry for each process per phase.
Note: You can also initialize phases to users/roles using [JC Job Phase Roles Initialize](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form) (accessed by selecting File > Job Phase Roles Initialize).

## Subcontract / Material Detail

You can enter subcontract detail for phases on a project using the Subcontract Detail button. All phases set up for the project that are assigned either of the cost types designated for subcontracts in PM Company Parameters (SL Params tab) are automatically set up in [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form). You can add, modify, or delete the detail as necessary.
You can also enter material detail for phases on a project using the Material Detail button. All phases set up for the project that are assigned either of the cost types designated for materials in PM Company Parameters (Material Parameters tab) are automatically set up in [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form) (with a Material Type ofP-Purchase Order). You can add, modify, or delete the detail as necessary.

## Update Status

The Update field shows the update status for each phase/cost type set up for the job. This field corresponds to the Source field JC Original Estimates. The system updates these fields automatically each time you enter and save a phase/cost type combination in either form.
When entering phases/cost types in this form, the update status defaults to Y-Ready to Update. You can manually change the flag to N-Not Ready to Update if needed to prevent the phase/cost type from being interfaced to Job Cost. However, once you interface the phase/cost type to Job Cost, the systems sets status to I-Interfaced status and you cannot change the status or any of the values.The J-Job Cost status is applied to all phase/cost type added directly in Job Cost. If you make any changes to the phase/cost type values (units, hrs/unit, hours, cost/hour, unit cost, and amount), the system automatically sets the status to Y-Ready to Update.
The following table shows the status options used in this form versus the corresponding options used in the Source field in JC Original Estimates.
PM Project PhasesJC Original Estimates
J-Job CostJ-Entered in Job Cost
Y-Ready to UpdateY-Entered in Project Management and yet to be interfaced to Job Cost
N-Not ready to UpdateN-Entered in Project Management and flagged not to be interfaced to Job Cost
I-InterfacedI-Interfaced from Project Management

For more information, select the links below.
[About Deleting Phases and Cost Types from a Project](/en/vista/vista/project-management/projects-and-contracts/projects/about-deleting-phases-and-cost-types-from-a-project)
