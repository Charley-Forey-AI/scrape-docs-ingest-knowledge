---
title: "Field Definitions: JC Job Phases Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form/field-definitions-jc-job-phases-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form/field-definitions-jc-job-phases-form"
---

# Field Definitions: JC Job Phases Form

The following is a list of field descriptions for the JC Job
 Phases form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Job

 Enter
 a valid job number or press F4 to select a job from a list.
Soft / Final Closed Jobs
If you enter a soft- or hard-closed job (status will display in red to the right of the job description), you will be allowed to add a phase, even if you do not allow posting to soft- or hard-closed jobs (flags in JC Company Parameters). However, you will not be able to add cost type detail unless you have specified to allow posting to closed jobs.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Phase

 Enter the phase you want to
 associate with the job or press F4 to select one from a list. Once you
 have entered the phase code, the phase description displays to the right of this field.
You can only select a phase that has already
 been created using the [JC Phases](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) form.
Cost types associated with the selected phase are automatically added to the job
Cost types are associated with phases using
 the Cost Types tab on the [JC Phases](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) form. When a phase is associated with a job, any cost types on that
 phase are automatically assigned to the job. You can see the cost types added to the job
 using the Cost Types tab on the JC Job Phases form.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Description

Enter a description for this job phase, up to 60
 characters. Initially defaults the description assigned to this phase in JC Phases.
Changing the description for a phase here does
 not affect the original description in JC Phases.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Contract

 Display only, the contract assigned to this job (in JC Jobs).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Contract Item

Enter the contract item (as defined in JC Contracts) to which this phase is
 linked.
If you are adding a new phase or changing the
 contract item for an existing phase, and you enter contract item that has not been set up
 for the contract, it will only be added if the Auto-Add Contract Item and Update Contract Item
 Amount box is checked for the job in JC Jobs. Estimate detail added for cost
 types on the phase will be updated to the contract item's original amount once you save the
 record.
 If the Auto-Add Contract Item and Update Contract Item
 Amount box is unchecked, you must assign an existing contract item or press
 F5 (to access JC Contract Items) and manually set up the contract item before assigning it
 to the phase.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Minimum Projection %

 Enter the
 minimum percent complete needed to calculate a cost projection in JC Cost
 Projections. If the percent complete is below this minimum, then the
 projected costs will be calculated at the higher of estimated or actual
 costs.
Projection minimum percentage is set up in several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a projection minimum percentage has not been set up on the project/job or phases.

- [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) - This value is only used if a
 projection minimum percentage has not been set up on the phases.

- [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) /
 [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This
 field defaults based on the projection minimum percentage
 set up using the JC Phases form.

- [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is
 the default value of the projection minimum percentage when
 new phases are added to a project/job.
What if you leave this field blank?

If there is no entry in this field, the system will use the minimum percent specified at the job level or, if not there, at the company level.
How do projections work?
 Click [here](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections) for an overview on
 projections.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Insurance Code

Use
 this field to associate the job phase with an insurance code. Enter an insurance code or
 press F4 to select on from a list. Insurance codes are created and maintained using [HQ Insurance Codes ](/en/vista/vista/administration/headquarters/payroll-related-setup/about-the-hq-insurance-codes-form).
Although you can assign insurance codes to any job phase, you will typically only need to assign them to non-standard phases (e.g., when phase codes are unique by job).
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Active Phase

 Check
 this box if the phase as active and valid for posting estimates, projections, commitments,
 and costs.
By default this box is checked when a phase is added to the job.
Quickly change the status of several phases
Use the [JC Job Phase Status Change ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/change-the-status-of-phases-on-a-job) form to quickly change the active status of all phases, or a range of phases on the job. [More](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/change-the-status-of-phases-on-a-job)

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Cost Type

Enter a valid cost type (from JC Cost Types) for
 this phase. Initially defaults all cost types set up for the phase in JC Phases.
If you enter a cost type that does not exist
 for the phase in JC  Phases, it will be added for the job/phase here, but it will
 not be added to the phase in JC Phases.
To delete any unwanted cost types, just select the cost type and click the Delete button.
Note: If this is a hard- or soft- closed job, you can only add new cost types if you allow posting to hard- and/or soft-closed jobs (i.e. the 'allow posting to closed jobs' flags in JC Company Parameters are unchecked).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  U/M

 Specify the unit of measure for
 this phase/cost type. If you are not tracking units at this level, enter LS (lump sum).
 Regardless of what is entered here, units may be entered in Purchase Orders, Accounts
 Payable, Inventory, and other programs that will update the transaction detail associated
 with the phase/cost type. However, only units entered in those programs with a unit of
 measure that matches this unit of measure will update the actual or committed units at this
 level.
 Initially defaults the unit of measure
 assigned to the cost type in JC Phases. You may override/change this unit of measure as
 long as:

- the UM exists in HQUM (HQ Units of Measure).

- no change order detail exists in JCOD (Change Order Detail) where the source status equals ‘J’ (Job Cost) or ‘I’ (Interfaced).

- no change order detail exists in PMOL (Change Order Lines) where the source status equals ‘J’ (Job Cost) or ‘I’ (Interfaced).

- the TotalCmtdCost and RemainCmtdCost = 0.00 for every month in JCCP (Cost by Period).

 If this criteria is met, the change is allowed and will update JCCD (Cost Detail) as follows:

- If the JCCD UM is not equal to the JCCH UM, sets the estimated units to 0.00.

- Updates projections (PF) records, setting the projected and forecast units to 0.00 where the JCCD UM is not equal to the JCCH UM.

- Updates posted units equal to actual units and the posted UM to the JCCH UM where the posted UM is null and the JCTransType is not ‘PF’ or ‘OE’.

- Updates actual units to 0.00 and the JCCD UM to the JCCH UM for all transactions where the JCCD UM is not equal to the JCCH UM and the JCTransType is not 'PF' or 'OE'.

- Updates the actual units equal to the posted units where the posted UM is equal to the JCCH UM and the JCTransType is not ‘PF’ or ‘OE’.

Note: For labor, the unit of measure should not be HRS (hours) in most circumstances. Units are separate from hours, and actual units will not be updated with hours from Payroll. The UM should be the quantity to be completed. If you are not tracking the quantity (units), the UM may be set up as LS (lump sum).  
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Bill Flag

 Specify whether units and/or costs for this cost type on this phase are to be used in
 calculating progress complete for progress-type billings in Job Billing.

- Y-Units and Dollars – Both units and dollars posted to this cost type will be used to calculate progress complete.

- C-Only Dollars – Only dollars will be used in calculating percent complete for this phase/cost type.

- N-Neither – Neither units nor dollars posted to this cost type will be used when calculating progress complete. Phase cost types with this flag will also not be included in T & M billings.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Item Units

Check
 this box if this cost type on this phase will be used to accumulate units complete for the
 related contract item. When summarizing job costs, the costs are all totaled, but only the
 units posted to the specified phase/cost type are counted.
This flag is generally checked for only one cost type on one phase, and the phase selected would be the one most closely related to the contract item.
Leave this box unchecked if you are not using this cost type to accumulate units complete for the related contract item.
This flag is only used in reporting progress posting (JC Progress Entry) and projections (JC Cost Projections).
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Phase Unit

 Check
 this box if this cost type will be used to accumulate units complete for this phase. This
 flag is typically checked for the main cost type, and only units posted to that cost type
 for that phase would be accumulated.
 Leave this box unchecked if you are not using this cost type to accumulate units complete for this phase.
Note: This flag is only used in reporting projections (JC Cost Projections). JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

##  Buy Out

 Check
 this box if buy out is complete (total commitments have been made through subcontracts,
 purchase orders, and/or material orders) for this phase and cost type.
 Leave this box unchecked if buy out is not complete for this phase and cost type.
Note: This flag can be used in reporting and will be used in cost projections (JC Cost Projection and PM Cost Projections) if commitments are being included with actual costs (flag setting in JC Company Parameters). If buy out is complete for a phase/cost type (box checked), projected costs will be calculated as the actual cost plus total remaining committed cost.

Click the links below for more information.
[JC Job Phases Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
[PM Project Phases Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)

## Active

Check
 this box if costs, estimates, and commitments can be posted to the phase/cost type.
What if the phase is not Active?
If a phase is not active (Active Phase
 field), costs and estimates cannot be posted to any of the cost types for the selected
 phase regardless of the status defined for each cost type.
 Quickly change the status of several phases
Use the [JC Job Phase Status
 Change ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/change-the-status-of-phases-on-a-job) form (File > Phase Status
 Change) to quickly check or uncheck this box on several phases at once.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/change-the-status-of-phases-on-a-job)JC Job Phase Status Change
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Notes

Enter
 any notes on the job/project phase.
JC Job Phases and PM Project Phases
This field is on both the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) and [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) forms. When a change is made, both forms are updated.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/change-the-status-of-phases-on-a-job)JC Job Phase Status Change
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Role

Enter the role for this phase. Must be a role
 assigned to the job in JC Jobs.
You will only need to assign roles here if you want to filter job phases by role when entering progress and/or cost projections.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases

## Process

Select
 the process applicable to this role for this phase.

- C - Cost Projections — Select this option if this role will only be posting cost projections to this phase (in JC Cost Projections). Role will be unable to access this phase for progress posting.

- P - Progress Entry — Select this option if this role will only be posting progress to this phase (in JC Progress Entry). Role will be unable to access this phase for cost projections.

Note: If a role needs access to this phase in both cost projections and progress entry, you will need to set up an entry for each process. 
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form)JC Job Phases
JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)PM Project Phases
