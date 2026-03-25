---
title: "Field Definitions: PM Project Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form/field-definitions-pm-project-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form/field-definitions-pm-project-phases-form"
---

# Field Definitions: PM Project Phases Form

The following is a list of field descriptions for the PM
 Project Phases form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter the project number to set up the
 phase/estimate detail or press F4 to select a project from a list.
Note: If you enter a soft- or hard-closed project (status
 will display in red to the right of the job description), you will be allowed to add a
 phase, even if you do not allow posting to soft- or hard-closed jobs (flags in JC Company
 Parameters). However, you will not be able to add cost type detail unless you have
 specified to allow posting to closed jobs.
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Phase

Enter the phase (from JC Phases Maintenance)
 you want to add to this project.
Phases imported from a third-party estimating software package or initialized via PM Copy Project Phases will be displayed on the Grid tab.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Description

 Enter the description for this phase, up to 60
 characters. Initially defaults the description defined for this phase in JC Phases
 Maintenance.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Contract

 Display only, the contract assigned to the specified project.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Contract Item

Enter the contract item associated with this
 phase or press F4
 to select one from a list.
Adding a new phase or changing the contract item on an existing phase
If you are adding a new phase or changing the
 contract item for an existing phase, and you enter a contract item that has not been set up
 for the contract, it will only be added if the Auto-Add Contract Item and Update Contract Item
 Amount box is checked for the project in PM Projects. Estimate detail added
 for cost types on the phase will be updated to the contract item's original amount once you
 save the record.
 If the Auto-Add Contract Item and Update Contract Item
 Amount box is unchecked, you must assign an existing contract item or press
 F5 (to access PM Contract Items) and manually set up the contract item before assigning it
 to the phase.
If you need to create a new contract item,
 press F5. This will open [PM Contract Items](/en/vista/vista/project-management/projects-and-contracts/contracts/pm-contract-items-form), which can be used to create new contract
 items.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Projection Minimum %

 Enter the minimum percent complete needed to
 calculate a cost projection in PM Cost Projections. If the percent complete is below this
 minimum, estimated amounts will be used.
If there is no entry in this field, the system
 will use the minimum percent specified at the phase level (JC Phases).
Projection minimum percentage is set up in several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a projection minimum percentage has not been set up on the project/job or phases.

- [PM
 Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) - This value is only used if a projection
 minimum percentage has not been set up on the phases.

- [PM Project
 Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) / [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This field defaults based on the
 projection minimum percentage set up using the JC Phases form.

- [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is the default value of the
 projection minimum percentage when new phases are added to a project/job.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Insurance Code

Enter an insurance code or press F4 to select
 one from a list. Insurance codes are created and maintained using the [HQ Insurance Codes ](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-insurance-codes-form) form.
When entering timecards (PR Timecard Entry), the system defaults the insurance code set up on the phase.
 If an insurance code isn't set up on the phase, the insurance code will default from the job’s insurance template or from the employee master.
Using insurance templates
If you have standard phases (each job has the same phases), you should use insurance templates ([JC Insurance Template ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-insurance-template-form)) to assign insurance codes to project phases.
If you use non-standard phases (e.g. different phases for each job), use this field to assign insurance codes to the non-standard phases.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.
[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Cost Type

Enter a valid cost type for this phase. If the
 cost type has been set up for the phase in JC Phases Maintenance, the U/M, Bill Flag, Item
 Unit Flag, and Phase Unit Flag will all default as defined for the phase.  If an
 estimate was imported, all cost types previously assigned to the selected phase will
 display. If adding a cost type that is not set up for the phase in the JC Phases, the unit
 of measure defaults to LS (lump sum) and the Bill Flag to C (costs only). Defaults may be
 overridden.
Initialize
To initialize cost types to the phase, click
 the Initialize button. The grid is automatically populated with all cost types set up for
 the phase in JC Phases Maintenance, along with the assigned unit of measure and Bill, Item
 Unit, and Phase Unit flag settings. Values (units, hrs/unit, hours, cost/hour, unit cost,
 and amount) are set to 0.00, and the Update flag set to Y. You can delete or modify cost
 types as necessary.

- If you do not allow posting to hard- or soft-closed jobs (flags in JC Company Parameters unchecked), you cannot add or modify cost types for a phase.

- Subcontract cost types defined here will automatically generate a subcontract detail record in PM Subcontract Detail, with one exception; if the UM is not LS and you enter 0.00 Units and Unit Cost, but Amount is not 0.00, no subcontract record will be created.

Note:If you manually enter or initialize a cost type that matches one of the two material cost types specified in PM Company Parameters (Material Parameters tab), the system will automatically create a single material detail line for the phase/cost type in PM Material Detail with a Material Type of P-Purchase Order

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Units

 Enter the estimated units for this cost type.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  U/M

 Enter the unit of measure for this cost type. If LS (lump sum), units may be entered to allow posting of progress in JC Progress Entry (recommended 1 or 100). For labor, the unit of measure should not be HRS (hours) in most circumstances. Units are separate from hours, and actual units will not be updated with hours from Payroll. The UM should be the quantity to be completed. If you are not tracking the quantity (units), the UM may be set up as LS (lump sum).

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Hrs/Unit

If applicable for the specified cost type, indicate the number of hours required to complete a single unit.
Note:In order to track hours for a cost type, you must have checked the Track Hours option in JC Cost Types.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Hours

Initially defaults the number of hours based on the Units x the Hrs/Unit. Accept the default, or indicate the total number of hours for this cost type. If you change the default, the Hrs/Unit will automatically be recalculated.
Note:In order to track hours for a cost type, you must have checked the Track Hours option in JC Cost Types.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Cost/Hour

Enter the cost per hour for this cost type.
Note:In order to track hours for a cost type, you must have checked the Track Hours option in JC Cost Types.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Unit Cost

 Enter the unit cost for this cost type.
 If you entered hours (Hrs/Unit, Hours, Cost/Hour), this field defaults a unit cost based on the calculation of Hours x Cost/Hour / Units. If you change the unit cost, the Hrs/Unit and Amount are recalculated.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Amount

 Initially defaults an amount based on units x unit cost. Accept the default, or enter the amount for this cost type.
 If you change the default, and you are tracking hours, both the hours and unit cost will be recalculated. If not tracking hours, only the unit cost is recalculated.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Bill Flag

 Specify whether units and/or costs for this cost type on this phase are to be used in calculating progress complete. Used only for Job Billing.
 Y = Both units and dollars posted to this cost type will be used to calculate progress complete.
 C = Only dollars will be used in calculating percent complete for this phase/cost type.
 N = Neither units nor dollars posted to this cost type will be used when calculating progress complete.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Item Unit Flag

Specify whether this cost type will be used to accumulate units complete for the contract item.
Check this box if this cost type on this phase will be used to accumulate units complete for the related contract item. When summarizing job costs, the costs are all totaled, but only the units posted to the specified phase/cost type are counted.
Leave this box unchecked if this cost type will not be used to accumulate units complete for the related contract item.
Note:Generally, this flag is set to Y for only one cost type on one phase, and the phase selected would be the one most closely related to the contract item.
JC Job Phases and PM Project Phases

This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Phase Unit Flag

 Specify whether this cost type will be used to accumulate units complete for this phase.
 Check this box if this cost type will be used to accumulate units complete for this phase. Typically, this flag is set to Y for the main cost type, and only units posted to that cost type for that phase would be accumulated.
 Leave this box unchecked if this cost type will not be used to accumulate units complete for this phase.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Update

This option is used to determine whether the data for each cost type is ready to be interfaced to accounting.
Y-Ready to Update.  Data is ready to be updated to accounting during the next interface.
N-Not Ready to Update.  Data is not ready to be interfaced to accounting.
Note:If the selected cost type was set up in JC Job Phases or JC Original Estimates, this flag defaults to ‘J-Job Cost’ to indicate that the information was set up in Job Cost. Data can be changed or modified, which will cause the flag to change to Y.

If the line has already been interfaced, this field will default to ‘I-Interfaced’. The flag and/or detail cannot be changed here; any necessary changes will have to be made in JC Original Estimates.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Role

Enter the role for this phase. Must be a role
 assigned to the project in PM Projects (pending projects) or JC Jobs (interfaced jobs or
 jobs set up directly in Job Cost).
Note:You will only need to assign roles here if you want to filter job phases by role when entering progress and/or cost projections.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Process

Select the process applicable to this role for this phase.

- C - Cost Projections — Select this option if this role will only be posting cost projections to this phase (in JC Cost Projections). Role will be unable to access this phase for progress posting.

- P - Progress Entry — Select this option if this role will only be posting progress to this phase (in JC Progress Entry). Role will be unable to access this phase for cost projections.

Note:If a role needs access to this phase in both cost projections and progress entry, you will need to set up an entry for each process.

[](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup/about-adding-phases-and-cost-types-to-a-pm-project/set-up-phases-for-the-project)Setting up a project - Phase Setup Step
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases
