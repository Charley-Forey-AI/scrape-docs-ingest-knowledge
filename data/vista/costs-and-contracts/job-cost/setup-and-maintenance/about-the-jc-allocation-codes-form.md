---
title: "About the JC Allocation Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocation-codes-form"
---

# About the JC Allocation Codes Form

Use this form to set up specifications for indirect costs that you incur and wish to allocate out among your active jobs.
The cost allocations feature allows you to allocate the costs automatically rather than making adjustment entries to each job individually. You can define up to 255 different allocations in this program.
For each allocation code you set up, you must define the calculation basis (cost, hours, or revenue), date option (month, actual date range, or posted date range), and allocation amounts or rates. If applicable, you can designate a specific phase and/or cost type to which allocations will be posted, as well as the GL accounts that will be debited/credited when costs are allocated. For allocations based on costs or hours, the ‘Cost Types to Include’ tab allows you to specify which cost types to include. Cost types can be entered manually or via initialization (Initialize Cost Types, File menu). If allocations are to apply to specific jobs and/or departments, the ‘Jobs to Include’ and ‘Departments to Include’ tabs allow you to specify which jobs and departments to include. Jobs and departments can be entered manually or via initialization (Initialize Jobs or Initialize Departments, File menu).  For more information about initializing cost types, jobs, and/or departments, see Related Topics below.
Once you have set up your allocation codes, cost allocations can then be performed using the JC Process Cost Allocations program. For example:
You have a monthly small tool expense that is to be distributed proportionately over all active jobs based on the total monthly cost of all labor posted to those jobs. You would set up the allocation as follows:
Allocation Code:
1

Basis:
Costs

Cost Types To Include :
1 (Labor)

Date Option:
M-By Month

Allocate Amount/Rate
Amount

Jobs To Allocate :
All

Departments To Allocate:
All

When you process allocations each month, the criteria you have defined here will display so that you know how that allocation will be applied. If you did not specify an amount, you will be prompted to do so before you can process the allocation.
Once an allocation has been processed, the ‘last run’ information is displayed in the lower right corner of the Info tab. Information includes the date the allocation was last run and the date range.

Related information

- [About Defining Allocation Amounts/Rates](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-defining-allocation-amountsrates)

- [About the JC Process Cost Allocations Form](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-process-cost-allocations-form)

- [About the JC Allocations Initialize Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-allocations-initialize-form)
