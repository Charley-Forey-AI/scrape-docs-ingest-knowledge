---
title: "About the JC Process Cost Allocations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form"
---

# About the JC Process Cost Allocations Form

Use this form to perform cost allocations based on an
 allocation code set up in the JC Allocations form.
This is not a required part of Job Cost processing, and should only be used if you need to post additional overhead costs to jobs.
When allocations are processed, adjusting entries are created for the specified jobs, phases, and cost types, and added to an open cost adjustments batch. The entries are flagged with a JC Type of ‘CA’, so that they are easily distinguished from other cost adjustments in the system. If needed, you can access the adjusting entries in JC Cost Adjustments and edit as necessary before posting and purging the batch.

## Adding an Allocation Phase Even if Job is Locked

If you use the 'lock phases' feature for your jobs (flag in JC
 Jobs), it is recommended that you check this option before running the allocation.
 If this option is not checked and the phase/cost type to which the allocation will
 be posted is not set up in JC Job Phases for a job to which the allocation is being
 posted, batch validation will return the following error:
Lock Phase XXXXX-XXX-  is not on job XXXXX--   . Job Phase Locked
In this case the batch cannot be processed until the situation is corrected by either manually adding the phase/cost type to the job in Job Phases, or by deleting the batch sequence to which the error message applies.

## Allocation Criteria / Last Run Info

When you specify the date and allocation code to process, the informational display shows how the allocation will be applied (e.g. applies to all jobs, selected departments, based on costs for cost types XXX, allocates a flat amount, etc.).
The information displayed depends on how you set up the allocation code (in JC Allocation Codes). Below the allocation specifications, 'last run' information is displayed, indicating the date on which the allocation was last run, as well as the month for which the allocation was run. If the allocation is using the 'By Date Range' date option (JC Allocation Codes), the date range for which the allocation was run will be included as well. For allocations that have not been successfully run, a message displays indicating that the allocation has never been run.

Click on the following link for more information about using this form.
[Before Running Allocations](/en/vista/vista/costs-and-contracts/job-cost/costs/before-running-allocations#concept-4392--en__concept-4392)

Related information

- [About the JC Allocation Codes Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)

- [Allocation Disbursement](/en/vista/vista/costs-and-contracts/job-cost/costs/allocation-disbursement)
