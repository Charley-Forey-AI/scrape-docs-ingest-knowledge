---
title: "Field Definitions: JC Original Estimates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form/field-definitions-jc-original-estimates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form/field-definitions-jc-original-estimates-form"
---

# Field Definitions: JC Original Estimates Form

The following is a list of field descriptions for the JC
 Original Estimates form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Job

 Specify the job for which you are entering estimate information. Once you have entered the job code, the job description displays to the right of this field.
 If you enter a soft- or hard-closed job and you allow posting to closed jobs (flags in JC Company Parameters), the job's status will display in red; however, entry is allowed. If you do not allow posting to closed jobs, a message displays indicating the job’s status and entry is not allowed.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

##  Phase

Enter a phase or press F4 to select
 a phase from a list.
Add a new phase to the job
Follow the steps below to add a new phase to the
 job. The new phase will automatically be assigned the cost types that were set up using
 the Cost Types tab on the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) form.

1. Enter or select a job in the
 Job field on the JC Original Estimates form.

1. Select a phase that isn't
 already associated with the job using the Phase field.

1. The JC Add New Phase form
 will open.

1. Enter the contract item that
 is associated with the new phase in the Item field. You cannot add a new
 contract item using this form.

1. Click the OK
 button.

1. The JC Add New Phase form
 will close.

1. The phase has been added to
 the job. You can see the new phase using the Phases tab on the [JC Jobs ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) form (or the [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) form).
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

## Cost Type

If this is an existing phase for this job,
 specify the cost type to review/modify.
 If you enter a cost type that does not already exist for the phase (in JC Job Phases), it will be added automatically.
Note: If the cost type is not set up for the phase in JC
 Phases, it will be added for phase in JC Job Phases, but it will not be added to the
 phase in JC Phases.
If this is a new phase for the job, you can
 add cost types either manually or by initializing them (using the Initialize Cost Types
 button). If initializing, all cost types defined for the phase in JC Phases will be added.
 You can then set up estimate information as necessary.

- Once you add a cost type manually, you cannot use the initialize feature. Remaining cost types must be entered manually.

- If this is a hard- or soft- closed job, you can only add new cost types if you allow posting to hard- and/or soft-closed jobs (i.e. the 'allow posting to closed jobs' flags in JC Company Parameters are unchecked).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

##  U/M

 Initially displays the unit of measure
 assigned to the cost type (in either JC Phases or in JC Job Phases). You may
 override/change this unit of measure as long as:

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

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

##  Hours

 Enabled only if you are tracking hours for this cost type (i.e. the Track Hours option checked in JC Cost Types).
 Specify the original estimated hours for this phase/cost type.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

##  Units

 Specify the original estimated units for this phase/cost type.
Lump Sum with one unit
Viewpoint does not typically allow the entry of units for LS (lump sum) unit of measure; however, if you plan to update progress in JC Progress Entry, it is recommended that estimates for LS items be entered with a unit of 1.000 so that you can enter a percent complete for progress on the job. Many Job Cost reports use this information for monitoring progress and projecting final costs.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

##  Unit Cost

Enter the original estimated unit cost for this phase/cost type. You can skip this field and enter total cost in the next field so the system calculates this unit cost for you.
 If the unit of measure is LS (Lump Sum), you must enter units in order to enter a unit cost. Otherwise, skip this field.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

##  Cost

 System automatically calculates the total estimated cost based on units multiplied by unit cost. If you change this total cost, the system recalculates the unit cost.
 If the unit of measure is LS (Lump Sum) and you did not enter units, enter the total cost.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates

## Bill

This field defaults to the bill flag setting
 assigned in JC Phases or JC Job Phases, but may be overridden here as needed. The bill flag
 determines if units and/or costs are to be used in calculating progress for progress-type
 billings in Job Billing.

- Y - Both units and dollars posted to this cost type will be used to calculate progress complete.

- C - Only dollars will be used in calculating percent complete for this phase/cost type.

- N - Neither units nor dollars posted to this cost type will be used when calculating progress complete.

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form)JC Original Estimates
