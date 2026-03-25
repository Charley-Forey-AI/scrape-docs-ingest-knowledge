---
title: "Field Definitions: JC Process Cost Allocations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form/field-definitions-jc-process-cost-allocations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form/field-definitions-jc-process-cost-allocations-form"
---

# Field Definitions: JC Process Cost Allocations Form

The following is a list of field descriptions for the JC
 Process Cost Allocations form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Allocation Date

 Enter the allocation date. This date will become the ‘actual date’ for all allocation transactions in this batch.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

## Reversal

Check this box if all transactions in this allocations batch should be set up for reversal in a future month. Reversal status will be set to ‘1’ (auto-reverse) for each transaction.
Leave this box unchecked if you do not want transactions in this batch set up for reversal in a future month. Reversal status will be set to ‘0’ (regular) for all transactions.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Allocation Code

 Specify the allocation code (from JC Allocation Codes) to process. Once entered, all specifications for the allocation code (including ‘last run’ details) are shown in the informational display below.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

## Job

Enabled only if the allocation’s Jobs to Allocation option is set to ‘Prompt for Job’ (in JC Allocation Codes).
Enter the job this allocation is based on and will be applied to.
Note: If you enter a soft- or hard-closed job and you do not allow posting to closed jobs, a message displays indicating the job’s status and entry is not allowed.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Dept

 Enabled only if the allocation’s Departments to Allocation option is set to ‘Prompt for Department’ (in JC Allocation Codes).
 Indicate the department this allocation is based on and will be applied to.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Amount to Allocate

 Displays only when Allocate Amount/Rate option is set to ‘Amount’ (in JC Allocation Codes).
 Enter the amount to allocate for this batch.
 Defaults the allocation amount specified for the allocation code in JC Allocation Codes or
 the amount specified in the custom field in JC Jobs (as designated in the Job Amount Column
 in JC Allocation Codes). May be overridden.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Rate to Allocate

 Displays only when Allocate Amount/Rate option is set to ‘Rate’ (in JC Allocation Codes).
 Enter the allocation rate for this batch.
 Defaults the allocation rate specified for the allocation code in JC Allocation Codes or
 the rate specified in the custom field in JC Jobs (as designated in the Job Rate Column in
 JC Allocation Codes). May be overridden.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Beginning Date

 Enabled only if the allocation’s Date option is set to ‘By Date Range’ (in JC Allocation Codes).
 Enter the beginning date in a range of dates for which to calculate the allocation basis.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Ending Date

 Enabled only if the allocation’s Date option is set to ‘By Date Range’ (in JC Allocation Codes).
 Enter the ending date in a range of dates for which to calculate the allocation basis.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

##  Add Allocation Phase Even if Job is Locked

 Specify how to handle allocation phases and cost types not already set up for ‘apply to’ jobs with locked phases.
 Check this box to override a job’s ‘locked phases’ status and add the allocation phase and cost type to JCJP (JC Job Phases) and JCCH (JC Cost Header).
 Leave this box unchecked if you do not want to add the allocation phase and cost type to jobs with locked phases. Batch entries will still be added to the JC Cost Adjustment batch, but batch validation will create an error message for any batch sequence where the phase/cost type does not exist (in Job Phases) for a job with locked phases.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations

## Include Soft Closed Jobs

Enabled only if the allocation applies to all jobs or a range of jobs.
Check this box to include 'soft-closed' jobs when processing this allocation. In addition to all open jobs, this allocation will be based on and applied to 'soft-closed' jobs. If checked and you do not allow posting to soft-closed jobs (flag in JC Company Parameters),  you will receive the following message:
Your company has chosen the option to not allow posting to soft-closed jobs. Do you want to override this option?
If you select Yes, the system allows you to continue the allocation process. Batch validation will allow allocation types (CA) for any job with a ‘soft-closed’ status. If you select No, the system automatically clears the ‘Include Soft Close Jobs’ checkbox. You can then continue with the allocation process.
Leave this box unchecked to exclude 'soft-closed' jobs when processing this allocation. Allocation will be based on and applied to jobs with an 'open' status only.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)JC Process Cost Allocations
