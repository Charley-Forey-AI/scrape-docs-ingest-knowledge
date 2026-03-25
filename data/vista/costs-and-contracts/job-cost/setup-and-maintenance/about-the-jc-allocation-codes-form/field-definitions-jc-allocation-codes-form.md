---
title: "Field Definitions: JC Allocation Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form/field-definitions-jc-allocation-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form/field-definitions-jc-allocation-codes-form"
---

# Field Definitions: JC Allocation Codes Form

The following is a list of field descriptions for the JC
 Allocation Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Allocation Code

 Specify a number (0 to 255) that identifies this allocation code.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

##  Description

 Enter the description for this allocation code, up to 30 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Basis

Indicate which of the following methods will be used to calculate costs when processing cost allocations.

- Costs - Select this option to calculate costs based on the total dollars posted to the basis cost types. Basis cost types are defined on the Cost Types to Include tab.

- Hours - Select this option to calculate costs based on the total hours posted to the basis cost types. Basis cost types are defined on the Cost Types to Include tab.

- Revenue - Select this option to calculate costs based on a job’s total revenue dollars. If this option is selected, the Cost Types to Include tab is disabled.

Note: The accumulated dollars, hours, or revenue on which costs will be calculated (in JC Process Cost Allocations) are determined by the date option you specified (month or date range) for this allocation.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Date Options

- M-By Month – Select this option to calculate costs based on the total dollars, hours, or revenue for the month specified when running allocations (JC Cost Allocations).

- R-By Actual Date Range – Select this option to calculate allocations based on the total dollars, hours, or revenue for a specified range of ‘actual’ dates (invoice dates).

- P-By Posted Date Range – Select this option to calculate allocations based on the total dollars, hours, or revenue for a specified range of ‘posted’ dates (dates transactions entered).

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Jobs To Allocate

 Indicate which of the following job options to use when processing cost allocations.

- All Jobs - Select this option if this allocation will be based on and applied to all jobs.

- Assigned Jobs - Select this option if this allocation will be based on and applied to selected jobs (specified on the Jobs to Include tab).

- Prompt for Job - Select this option to prompt for the job when running allocations in JC Process Cost Allocations.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Departments To Allocate

Indicate which of the following department options to use when processing cost allocations.

- All Departments - Select this option if this allocation will be based on and applied to all departments.

- Assigned Departments - Select this option if this allocation will be based on and applied to selected departments (specified on the Departments to Include tab).

- Prompt for Department - Select this option to prompt for a department when running allocations in JC Process Cost Allocations.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Allocate Amount/Rate

- Amount - Select this option to allocate a fixed amount (specified below). If no fixed amount is specified below, you must specify the amount when processing allocations (in JC Process Cost Allocations).

- Rate - Select this option to calculate the allocation on a rate (specified below). If no rate is specified below, rate must be specified when processing allocation (in JC Process Cost Allocations).

Note: If the allocation basis is Hours, rate represents the dollar amount per hour.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

##  Amount to Allocate

 Enabled only if allocating a fixed amount.
 Enter the dollar amount for this allocation or enter 0.00 to enter the amount at the time you process this allocation (in JC Process Cost Allocations).
 Leave this field blank if you want the allocation amount to be specified on a per job basis using the Job Amount Column below.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Job Amount Column

Enabled only if allocating a fixed amount and the Amount To Allocate
 is null.
Using the predefined list (click on the arrow
 at the end of the field), indicate the custom (user-defined) field in JC Jobs from which to
 pull the allocation amount.
Note: In order to use this feature, you must have created a custom field (in VA Custom Fields Wizard) in which to designate the amount you wish to use.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

##  Allocation Rate

 Enabled only if allocating based on a rate.
 Enter the rate (percentage) for this allocation or enter 0.00 to enter the amount at the time you process this allocation (in JC Process Cost Allocations). If the allocation basis is Hours, this rate represents the dollar amount per hour.
 Leave this field blank if you want the allocation rate to be specified on a per job basis using the Job Rate Column below.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Job Rate Column

Enabled only if allocating a rate and the Allocation Rate is null.
Using the predefined list (click on the arrow
 at the end of the field), indicate the custom (user-defined) field in JC Jobs from which to
 pull the allocation rate.
Note: In order to use this feature, you must have created a custom field (in VA Custom Field Wizard) in which to designate the amount you wish to use.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Cost Type

Specify each of the cost types to include when processing this allocation (in JC Process Cost Allocations).
Note: Displays all cost types initialized via JC Allocations Initialize, if applicable.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Job

Specify each job to include when processing this allocation (in JC Process Cost Allocations).
Note: Displays all jobs initialized via JC Allocations Initialize, if applicable.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Department

Specify each department to include when processing this allocation (in JC Process Cost Allocations).
Note: Displays all departments initialized via JC Allocations Initialize, if applicable.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Post To: Phase

Required if the allocation basis is Revenue.
Enter the phase to which allocated costs will be posted on each job. If field is left blank (Costs or Hours basis only), allocated amounts will be posted to each phase used as the basis.
Note: When posting allocations, if the phase specified here
 does not exist for the job, it will be added automatically unless the job is ‘locked’. To
 add the phase to locked jobs, you will need to check the Add Allocation Phase Even
 if Job is Locked box in JC Process Cost Allocations.
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

## Post To: Cost Type

Required if the allocation basis is Revenue.
Enter the cost type to which allocated costs will be posted on each job. If this field is left blank (Costs or Hours basis only), allocated amounts will be posted to each of the basis cost types (defined in Cost Types to Include section).
Note: When posting allocations, if the cost type specified
 here does not exist for the job/phase, it will be added automatically unless the job is
 ‘locked’. To add the cost type to locked jobs, you will need to check the Add Allocation Phase Even
 if Job is Locked box in JC Process Cost Allocations.
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

##  GL Accounts: Debit

 Enter the override GL account to debit when
 posting allocations. Leave blank to use the GL account specified for the cost type in JC
 Departments.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes

##  GL Accounts: Credit

 Required.
 Specify the GL account to credit when posting allocations.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form)JC Allocation Codes
