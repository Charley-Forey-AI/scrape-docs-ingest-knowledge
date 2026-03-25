---
title: "Field Definitions: JC Job Phase Roles Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form/initializing-phases-to-job-roles/field-definitions-jc-job-phase-roles-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form/initializing-phases-to-job-roles/field-definitions-jc-job-phase-roles-initialize-form"
---

# Field Definitions: JC Job Phase Roles Initialize Form

The following is a list of field descriptions for the JC Job
 Phase Roles Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Job

This field is enabled only if a job was not specified in the calling form.
Enter the job for which to initialize job role phases.
Note: Roles must have already been established for the job in order to initialize job phases to roles in this form. 
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form)JC Job Phase Roles Initialize

## User Name

This field is disabled if you accessed this form from any of the following forms:

- JC Change Orders

- JC Cost Projections

- JC Progress Entry

- PM Approved Change Orders

- PM Change Orders

- PM Pending Change Orders

Enter the user name for which you are initializing job role phases. Initially defaults the user currently logged in.
Note: User must be currently assigned a role on this job/project. Press F4 for a list of valid user names.  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form)JC Job Phase Roles Initialize

## Role

This field is enabled only if the user
 specified in the User Name field is assigned to more than one role on the specified job.
Enter the role for which to initialize job phases. Must be a valid role for the specified user. Press F4 for a list of valid roles for the specified user name.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form)JC Job Phase Roles Initialize

## Process

This field is disabled if you accessed this form from JC Cost Projections or JC Progress Entry, and defaults based on the calling form.
Select the process to assign to phases selected for this user name/role.

- JC Cost Projections — Select this option if this role will post cost projections only to the selected phases (in JC Cost Projections). Role will be unable to access phases for progress posting.

- JC Progress Entry — Select this option if this role will post progress only to the selected phases (in JC Progress Entry). Role will be unable to access phases for cost projections.

- Both — Select this option if this role will be posting both progress and cost projections to the selected phases.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form)JC Job Phase Roles Initialize

## Show All Phases in Available List

Specify how phases should be displayed in the Available Job Phases list.
Check this box to show all phases for this job, regardless of whether the phases have already been assigned to a role.
Uncheck this box to show only those phases for the job that have not already been assigned to a role.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phase-roles-initialize-form)JC Job Phase Roles Initialize
